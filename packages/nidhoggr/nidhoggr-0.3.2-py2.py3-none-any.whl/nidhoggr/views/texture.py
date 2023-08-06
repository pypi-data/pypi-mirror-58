from datetime import datetime
from typing import Union

from nidhoggr.bl import BaseUserRepo, BaseTextureRepo, BLConfig
from nidhoggr.errors import texture as err
from nidhoggr.models import texture as tex
from nidhoggr.models.session import HasJoinedRequest, JoinedResponse
from nidhoggr.utils.crypto import generate_uuid
from nidhoggr.utils.decorator import typed
from nidhoggr.utils.texture import check_texture, optimize_texture
from nidhoggr.views import session


@typed
def get(
    req: tex.TextureGetRequest,
    users: BaseUserRepo,
    textures: BaseTextureRepo
) -> Union[tex.TextureResponse, err.TextureError]:
    user = users.get_user(uuid=req.id)

    if user is None:
        return err.UnknownUser

    result = textures.get(uuid=req.id)

    return tex.TextureResponse(
        timestamp=int(datetime.now().timestamp() * 1000),
        profileId=user.uuid,
        profileName=user.login,
        textures=result
    )


@typed
def save(
    req: tex.TextureSetRequest,
    users: BaseUserRepo,
    textures: BaseTextureRepo,
    config: BLConfig
) -> Union[tex.TextureStatusResponse, err.TextureError]:
    user = users.get_user(uuid=req.id)

    if user is None:
        return err.UnknownUser

    if req.access is None:
        return err.MissingToken

    if req.access != user.access:
        return err.InvalidToken

    texture_error = check_texture(data=req.payload)
    if texture_error is not None:
        return texture_error

    if config.optimize_textures:
        payload = optimize_texture(data=req.payload)
    else:
        payload = req.payload

    result = textures.save(
        uuid=req.uuid,
        texture_type=req.texture_type,
        payload=payload,
        metadata=req.metadata
    )

    return result and tex.TextureSuccess or err.StorageError


@typed
def delete(
    req: tex.TextureDeleteRequest,
    users: BaseUserRepo,
    textures: BaseTextureRepo
) -> Union[tex.TextureStatusResponse, err.TextureError]:
    user = users.get_user(uuid=req.id)

    if user is None:
        return err.UnknownUser

    if req.access is None:
        return err.MissingToken

    if req.access != user.access:
        return err.InvalidToken

    result = textures.get(uuid=req.id)

    if req.texture_type not in result:
        return err.EmptySkinType

    textures.delete(uuid=user.uuid, texture_type=req.texture_type)

    return tex.TextureSuccess


@typed
def handshake_first_stage(
    req: tex.TextureHandshakeFirstRequest,
    textures: BaseTextureRepo
) -> tex.TextureHandshakeFirstResponse:
    server_id = generate_uuid()

    generated_token = textures.save_token(
        name=req.name,
        ip=req.ip,
        server_id=server_id
    )

    return tex.TextureHandshakeFirstResponse(
        serverId=generate_uuid(),
        verifyToken=generated_token.value
    )


@typed
def handshake_second_stage(
    req: tex.TextureHandshakeSecondRequest,
    textures: BaseTextureRepo,
    users: BaseUserRepo
) -> Union[tex.TextureHandshakeSecondResponse, err.TextureError]:
    token = textures.get_token(value=req.verifyToken)

    if token is None:
        return err.MissingToken

    if token.name != req.name:
        return err.InvalidName

    if token.ip != req.ip:
        return err.InvalidIP

    join_request = HasJoinedRequest(username=req.name, serverId=token.server_id, ip=token.ip)
    join_result = session.has_joined.__wrapped__(join_request, users)

    if not isinstance(join_result, JoinedResponse):
        return err.NotJoined

    user = users.get_user(uuid=join_result.id)

    return tex.TextureHandshakeSecondResponse(
        accessToken=user.access,
        userId=user.uuid
    )
