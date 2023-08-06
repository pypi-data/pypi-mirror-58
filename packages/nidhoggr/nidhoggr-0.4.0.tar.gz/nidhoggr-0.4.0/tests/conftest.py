import json
from functools import wraps
from itertools import product
from pathlib import Path
from typing import Optional, Dict, Any, Union, Callable, TypeVar

import pytest
from flask import url_for, Response, Flask

from nidhoggr.application import create_app
from nidhoggr.bl import BaseUserRepo, User, BLConfig, BaseTextureRepo
from nidhoggr.errors.common import YggdrasilError
from nidhoggr.models.auth import AuthenticationResponse, RefreshResponse
from nidhoggr.models.session import JoinedResponse
from nidhoggr.models.texture import TextureType, TextureItem, TextureResponse
from nidhoggr.utils.crypto import KeyPair


class TestUser(User):
    # NOTE: Still needed for testing purposes
    password: str


USERS = list(map(
    TestUser.parse_obj,
    json.loads((Path(__file__).parent / "data/users.json").read_text())
))

EndpointCallable = Callable[[Dict[str, Any]], Response]
TEST_KEY_PAIR = KeyPair.generate()

YggdrasilResponse = Union[
    AuthenticationResponse,
    RefreshResponse,
    JoinedResponse,
    TextureResponse,
]


def accessor(func):
    @wraps(func)
    def wrapper(client, data):
        return client.post(
            url_for(func.__name__),
            data=json.dumps(data),
            content_type='application/json'
        )

    return wrapper


T = TypeVar("T")


class cast:
    def __getitem__(self, other) -> Callable[[T], Union[YggdrasilError, YggdrasilResponse]]:
        if isinstance(other, YggdrasilError):
            return lambda res: self[YggdrasilError](res) == other
        elif issubclass(other, YggdrasilError):
            return lambda res: other(status=res.status_code, **res.json)
        elif other in YggdrasilResponse.__args__:
            return lambda res: other(**res.json)
        else:
            return lambda res: None


cast = cast()


class TestUserRepo(BaseUserRepo):
    __users: Dict[int, TestUser]

    def __init__(self, *, users):
        self.__users = {user.uuid: user.copy() for user in users}

    def get_user(self, **kw: Dict[str, str]) -> Optional[TestUser]:
        res = [
            u
            for u
            in self.__users.values()
            if any(getattr(u, k) == v for k, v in kw.items())
        ]
        return (res or [None])[0]

    def save_user(self, *, user: TestUser):
        self.__users[user.uuid] = user

    def check_password(self, *, clean: str, uuid: str) -> bool:
        user = self.get_user(uuid=uuid)
        return user and user.password == clean


class TestTextureRepo(BaseTextureRepo):
    def get(self, *, uuid: str) -> Dict[TextureType, TextureItem]:
        return {}


@pytest.fixture(params=list(product((False, True), (False, True))))
def config(request) -> BLConfig:
    strict, simple_login, *_ = request.param
    return BLConfig(
        key_pair=TEST_KEY_PAIR,
        strict=strict,
        simple_login=simple_login,
    )


@pytest.fixture
def users() -> TestUserRepo:
    return TestUserRepo(users=USERS)


@pytest.fixture
def textures() -> TestTextureRepo:
    return TestTextureRepo()


@pytest.fixture(autouse=True)
def skip_bl(request, config):
    if request.node.get_marker("skip_bl_on"):
        marker = request.node.get_marker("skip_bl_on")
        if any(
            marker.kwargs.get(name, ...) == value
            for name, value
            in config._asdict().items()
        ):
            pytest.skip(f"Skipped on {config}")


@pytest.fixture
def user(users) -> User:
    return users.get_user(uuid="1")


@pytest.fixture
def old_user(users) -> User:
    return users.get_user(uuid="2")


@pytest.fixture
def new_user(users) -> User:
    return users.get_user(uuid="3")


@pytest.fixture
def app(
    users,
    config: BLConfig,
    textures: BaseTextureRepo
) -> Flask:
    return create_app(
        users=users,
        config=config,
        textures=textures,
    )
