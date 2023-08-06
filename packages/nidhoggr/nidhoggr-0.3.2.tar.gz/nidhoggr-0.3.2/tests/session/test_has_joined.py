from nidhoggr.errors.auth import InvalidProfile
from nidhoggr.errors.common import BadPayload
from nidhoggr.errors.session import InvalidServer
from nidhoggr.models.session import JoinedResponse
from nidhoggr.utils.crypto import generate_uuid
from ..conftest import cast


def test_empty_credentials(user, has_joined):
    assert cast[BadPayload](has_joined({}))
    assert cast[BadPayload](has_joined({"username": user.login}))
    assert cast[BadPayload](has_joined({"ip": "127.0.0.1"}))
    assert cast[BadPayload](has_joined({"serverId": generate_uuid()}))
    assert cast[BadPayload](has_joined({"username": user.login, "ip": "127.0.0.1"}))
    assert cast[BadPayload](has_joined({"username": user.login, "serverId": generate_uuid()}))
    assert cast[BadPayload](has_joined({"ip": "127.0.0.1", "serverId": generate_uuid()}))


def test_invalid_server(user, join, has_joined):
    join({
        "accessToken": user.access,
        "selectedProfile": user.uuid,
        "serverId": generate_uuid()
    })
    has_joined_response = has_joined({
        "username": user.login,
        "serverId": "anything",
        "ip": "127.0.0.1",
    })

    assert cast[InvalidServer](has_joined_response)


def test_nonexistent_user(has_joined):
    response = has_joined({
        "username": "anything",
        "serverId": "anything",
        "ip": "127.0.0.1",
    })

    assert cast[InvalidProfile](response)


def test_has_joined(user, join, has_joined):
    server_id = generate_uuid()
    join({
        "accessToken": user.access,
        "selectedProfile": user.uuid,
        "serverId": server_id
    })
    has_joined_response = has_joined({
        "username": user.login,
        "serverId": server_id,
        "ip": "127.0.0.2",
    })
    result = cast[JoinedResponse](has_joined_response)
    assert result is not None
    assert result.id == user.uuid
    assert result.name == user.login
