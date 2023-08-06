from abc import ABCMeta, abstractmethod
from typing import Optional, List, Dict, NamedTuple

from pydantic import BaseModel

from nidhoggr.models.session import UserProperty
from nidhoggr.models.texture import TextureType, TextureItem, TextureMeta, TextureToken
from nidhoggr.utils.crypto import KeyPair


class User(BaseModel):
    uuid: str
    login: str
    email: str
    password: str
    access: Optional[str] = None
    client: Optional[str] = None
    server: Optional[str] = None
    properties: List[UserProperty] = []

    class Config:
        allow_mutation = False


class BLConfig(NamedTuple):
    key_pair: KeyPair
    strict: bool = False
    simple_login: bool = True
    optimize_textures: bool = True


class BaseUserRepo(metaclass=ABCMeta):

    @abstractmethod
    def get_user(self, **kw: Dict[str, str]) -> Optional[User]:
        pass

    @abstractmethod
    def check_password(self, *, clean: str, hashed: str) -> bool:
        pass

    @abstractmethod
    def save_user(self, *, user: User) -> bool:
        pass


class BaseTextureRepo(metaclass=ABCMeta):
    @abstractmethod
    def get(self, *, uuid: str) -> Dict[TextureType, TextureItem]:
        pass

    @abstractmethod
    def save(self, uuid: str, texture_type: TextureType, payload: bytes, metadata: TextureMeta) -> bool:
        pass

    @abstractmethod
    def delete(self, *, uuid: str, texture_type: TextureType):
        pass

    @abstractmethod
    def fetch_remote(self, *, url: str) -> bytes:
        pass

    @abstractmethod
    def save_token(self, *, name: str, ip: str, server_id: str) -> TextureToken:
        pass

    @abstractmethod
    def get_token(self, *, value: str) -> TextureToken:
        pass
