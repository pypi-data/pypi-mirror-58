from typing import Optional, Union, List

from pydantic import BaseModel

from nidhoggr.utils.transformer import YggdrasilRequestTransformer, JSONResponseTransformer


class UserProperty(BaseModel):
    name: str
    value: str

    class Config:
        allow_mutation = False
        ignore_extra = False

    def __hash__(self):
        return hash((self.name, self.value))

    def verify(self, *, key: bytes):
        return True

    @property
    def unsigned(self):
        return self


class SignedUserProperty(UserProperty):
    signature: Optional[str] = None

    class Config:
        allow_mutation = False
        ignore_extra = False

    def __hash__(self):
        return hash((self.name, self.value, self.signature))

    def verify(self, *, key: bytes):
        from nidhoggr.utils.crypto import verify_property
        return verify_property(public_key=key, prop=self)

    @property
    def unsigned(self):
        return UserProperty(name=self.name, value=self.value)


class JoinRequest(BaseModel, YggdrasilRequestTransformer):
    accessToken: str
    selectedProfile: str
    serverId: str

    class Config:
        allow_mutation = False


class HasJoinedRequest(BaseModel, YggdrasilRequestTransformer):
    username: str
    serverId: str
    ip: str

    class Config:
        allow_mutation = False


class JoinedResponse(BaseModel, JSONResponseTransformer):
    id: str
    name: str
    properties: Union[List[UserProperty], List[SignedUserProperty]]

    class Config:
        allow_mutation = False


class ProfileRequest(BaseModel, YggdrasilRequestTransformer):
    id: str
    unsigned: bool = False

    class Config:
        allow_mutation = False
