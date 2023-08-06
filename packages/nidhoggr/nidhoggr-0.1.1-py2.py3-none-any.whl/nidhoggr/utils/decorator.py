from functools import wraps
from typing import Callable

from flask import current_app, Response
from pydantic import ValidationError

from nidhoggr.errors.common import BadPayload
from nidhoggr.utils.transformer import AbstractRequestTransformer, AbstractResponseTransformer


def _transform_request(cls, *view_args, **view_kwargs):
    if issubclass(cls, AbstractRequestTransformer):
        return cls.transform(*view_args, **view_kwargs)
    else:
        return current_app.bl.get(cls)


def _transform_response(instance):
    if isinstance(instance, AbstractResponseTransformer):
        return instance.transform()
    elif instance is None:
        return Response(response="", status=204)
    else:
        raise NotImplementedError()


def as_response(func):
    @wraps(func)
    def wrapper(error):
        return _transform_response(func(error))

    return wrapper


def typed(func: Callable):
    @wraps(func)
    def wrapper(*view_args, **view_kwargs) -> Response:
        try:
            # noinspection PyUnresolvedReferences
            args = [
                _transform_request(arg_cls, *view_args, **view_kwargs)
                for arg_name, arg_cls
                in func.__annotations__.items()
                if arg_name != "return"
            ]
        except ValidationError:
            response = BadPayload
        else:
            response = func(*args)
        return _transform_response(response)

    return wrapper
