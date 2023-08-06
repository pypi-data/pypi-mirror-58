from functools import partial

import pytest
from flask.testing import FlaskClient

from nidhoggr.views import session
from ..conftest import accessor, EndpointCallable


@pytest.fixture
def join(client: FlaskClient) -> EndpointCallable:
    return partial(accessor(session.join), client)


@pytest.fixture
def has_joined(client: FlaskClient) -> EndpointCallable:
    return partial(accessor(session.has_joined), client)


@pytest.fixture
def profile(client: FlaskClient) -> EndpointCallable:
    return partial(accessor(session.profile), client)
