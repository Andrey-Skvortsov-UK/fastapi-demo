from fastapi_sqlalchemy import db, DBSessionMiddleware
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import AllFeaturesMixin
from starlette.middleware.base import RequestResponseEndpoint
from starlette.requests import Request


Base = declarative_base(cls=AllFeaturesMixin)


class SQLAlchemySessionMiddleware(DBSessionMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        with db():
            Base.set_session(db.session)
        return await super().dispatch(request, call_next)
