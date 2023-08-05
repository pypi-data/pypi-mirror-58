from abc import ABC, abstractmethod
from logging import getLogger
from typing import Mapping, Optional

from .utils import Con, create_db_pool, fetch, fetchval, fetchrow

logger = getLogger(__name__)


class DBRequest(ABC):
    pool: Con

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.pool = instance.pool
        return self

    @abstractmethod
    async def __call__(self, *args, **kwargs):
        pass


class DBApi:
    def __init__(self, pool: Con):
        self.pool = pool

    @classmethod
    async def create(cls, dsn, endpoints: Optional[Mapping[str, DBRequest]] = None, **kwargs):
        pool = await create_db_pool(dsn, **kwargs)
        res = cls(pool)
        if endpoints:
            res.set_req_methods(endpoints)
        return res

    async def close(self):
        await self.pool.close()

    def set_req_methods(self, endpoints: Mapping[str, DBRequest]):
        for endpoint_name, endpoint in endpoints.items() or []:
            endpoint.pool = self.pool
            setattr(self, endpoint_name, endpoint)


class SearchRequest(DBRequest):
    _query: str = None
    _count_query: str = None
    default_limit = 10

    @property
    def fetch_result(self):
        @fetch(limit=self.default_limit, offset=0)
        def q():
            return self._query

        return q

    @property
    def fetch_pagination(self):
        @fetchval(limit=self.default_limit, offset=0)
        def q():
            return self._count_query

        return q

    async def __call__(self, **kwargs):
        res = {'result': await self.fetch_result(self.pool, **kwargs)}
        if self._count_query:
            res['pagination'] = await self.fetch_pagination(self.pool, **kwargs)
        return res


class MutationRequest(DBRequest):
    _query: str = None

    async def __call__(self, **kwargs):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                res = await self.fetch_result(conn, **kwargs)
        return {'result': res}

    @property
    def fetch_result(self):
        @fetchrow()
        def q():
            return self._query

        return q


def get_request_class(query: str, count_query: Optional[str] = None,
                      request_type: Optional[str] = 'search', **kwargs):
    inherit_cls = SearchRequest if request_type == 'search' else MutationRequest

    class Request(inherit_cls):
        _query = query
        _count_query = count_query

    return Request()
