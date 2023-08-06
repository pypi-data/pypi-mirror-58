from pydantic import BaseModel

from nidhoggr.utils.transformer import JSONErrorTransformer


class TextureError(BaseModel, JSONErrorTransformer):
    status: int
    message: str


EmptySkinType = TextureError(message="Requested type is empty", status=400)

StorageError = TextureError(message="Can't save texture", status=500)

UnknownUser = TextureError(message="Unknown user", status=404)

UnsupportedFormat = TextureError(message="Unsupported format", status=400)

UnsupportedSize = TextureError(message="Unsupported size", status=400)

MissingToken = TextureError(message="Authorization token not provided or it has expired", status=401)

InvalidToken = TextureError(message="Invalid authorization token", status=403)

InvalidName = TextureError(message="Wrong name", status=403)

InvalidIP = TextureError(message="IP does not match", status=403)

NotJoined = TextureError(message="User has not joined yet", status=403)
