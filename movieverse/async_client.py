# --- imports from python standard library -------------------------------------
from typing import Awaitable, Any, Callable
import asyncio
# --- external imports ---------------------------------------------------------
import aiohttp
# --- imports own packages and modules -----------------------------------------
# ------------------------------------------------------------------------------


def handle_session(func: Callable) -> Callable:

    async def result_func(obj: 'AsyncClient',
                          *args,
                          close_session: bool = False,
                          open_session: bool = False,
                          **kwargs) -> Awaitable:

        if close_session and obj.session is None:
            obj.session = aiohttp.ClientSession()

        result = await func(obj, *args, **kwargs)

        if close_session and obj.session is not None:
            await obj.async_close_session()

        return result

    return result_func


class AsyncClient:

    def __init__(self) -> None:
        self.session = None

    @staticmethod
    def run_coro(coro: Awaitable) -> Any:
        return asyncio.get_event_loop().run_until_complete(coro)

    @property
    def has_session(self) -> bool:
        return self.session is not None

    def get(self, url: str) -> Awaitable:
        if self.session is None:
            return aiohttp.get(url)
        return self.session.get(url)

    async def async_close_session(self):
        await self.session.close()
