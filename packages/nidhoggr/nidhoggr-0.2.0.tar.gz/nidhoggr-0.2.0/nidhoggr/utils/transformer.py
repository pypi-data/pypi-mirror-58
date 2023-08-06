from abc import ABCMeta, abstractmethod

from flask import request, Response
from pydantic import BaseModel

MIME_TYPE = 'application/json'


class AbstractRequestTransformer(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def transform(cls, *args, **kwargs) -> BaseModel:
        pass


class AbstractResponseTransformer(metaclass=ABCMeta):
    @abstractmethod
    def transform(self, *args, **kwargs) -> Response:
        pass


class YggdrasilRequestTransformer(AbstractRequestTransformer):
    @classmethod
    def transform(cls, *args, **kwargs):
        # noinspection PyArgumentList
        return cls(**(request.json or {}))


class JSONResponseTransformer(AbstractResponseTransformer):
    def transform(self: BaseModel, *args, **kwargs):
        return Response(
            mimetype=MIME_TYPE,
            content_type=MIME_TYPE,
            response=self.json()
        )


class JSONErrorTransformer(AbstractResponseTransformer):
    def transform(self: BaseModel, *args, **kwargs):
        return Response(
            status=self.status,
            mimetype=MIME_TYPE,
            content_type=MIME_TYPE,
            response=self.copy(exclude={'status'}).json()
        )
