from base64 import b64encode
from enum import Enum
from typing import Optional, Dict

from flask import request
from pydantic import BaseModel

from nidhoggr.models.session import UserProperty
from nidhoggr.utils.transformer import JSONResponseTransformer, JSONErrorTransformer, AbstractRequestTransformer

TextureMeta = Optional[Dict[str, str]]


class TextureType(Enum):
    SKIN = "SKIN"
    CAPE = "CAPE"
    ELYTRA = "ELYTRA"


class TextureItem(BaseModel):
    url: str
    metadata: TextureMeta = None

    class Config:
        allow_mutation = False


class TextureGetRequest(BaseModel, AbstractRequestTransformer):
    uuid: str

    class Config:
        allow_mutation = False

    @classmethod
    def transform(cls, *args, **kwargs):
        return cls(uuid=kwargs.get("uuid"))


class TextureSetRequest(BaseModel, AbstractRequestTransformer):
    uuid: str
    texture_type: TextureType
    payload: bytes
    metadata: TextureMeta = None
    access: Optional[str] = None

    class Config:
        allow_mutation = False

    @classmethod
    def transform(cls, *args, **kwargs):
        return cls(
            uuid=kwargs.get("uuid"),
            texture_type=kwargs.get("texture_type").upper(),
            payload=request.files["file"],
            metadata={
                name: value
                for name, value
                in request.form.items()
                if name != "file"
            },
            access=request.headers.get("Authorization")
        )


class TextureDeleteRequest(BaseModel, AbstractRequestTransformer):
    uuid: str
    texture_type: TextureType
    access: Optional[str] = None

    class Config:
        allow_mutation = False

    @classmethod
    def transform(cls, *args, **kwargs):
        return cls(
            uuid=kwargs.get("uuid"),
            texture_type=kwargs.get("texture_type").upper(),
            access=request.headers.get("Authorization")
        )


class TextureResponse(BaseModel, JSONResponseTransformer):
    timestamp: int
    profileId: str
    profileName: str
    textures: Dict[TextureType, TextureItem]

    class Config:
        allow_mutation = False
        use_enum_values = True

    def pack(self) -> UserProperty:
        return UserProperty(
            name="textures",
            value=b64encode(self.json().encode('ascii')).decode('ascii')
        )


class TextureToken(BaseModel):
    name: str
    ip: str
    server_id: str
    value: str

    class Config:
        allow_mutation = False


class TextureHandshakeFirstRequest(BaseModel, AbstractRequestTransformer):
    name: str
    ip: str

    class Config:
        allow_mutation = False

    @classmethod
    def transform(cls, *args, **kwargs):
        return cls(
            name=request.form.get("name"),
            ip=request.remote_addr,
        )


class TextureHandshakeFirstResponse(BaseModel, JSONErrorTransformer):
    offline: bool = False
    serverId: str
    verifyToken: str

    class Config:
        allow_mutation = False


class TextureHandshakeSecondRequest(BaseModel, AbstractRequestTransformer):
    name: str
    verifyToken: str

    class Config:
        allow_mutation = False

    @classmethod
    def transform(cls, *args, **kwargs):
        return cls(
            name=request.form.get("name"),
            ip=request.form.get("verifyToken"),
        )


class TextureHandshakeSecondResponse(BaseModel, JSONErrorTransformer):
    accessToken: str
    userId: str

    class Config:
        allow_mutation = False


class TextureStatusResponse(BaseModel, JSONErrorTransformer):
    message: str


TextureSuccess = TextureStatusResponse(message="OK")
