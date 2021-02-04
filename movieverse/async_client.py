# --- imports from python standard library -------------------------------------
from typing import Awaitable, Any
import asyncio
# --- external imports ---------------------------------------------------------
import aiohttp
# --- imports own packages and modules -----------------------------------------
# ------------------------------------------------------------------------------

class AsyncClient:

    def __init__(self) -> None:
        self.session = None

    @staticmethod
    def run_coro(coro):
        return asyncio.get_event_loop().run_until_complete(coro)

    @property
    def has_session(self):
        return self.session is not None

    def get(self, url):
        if self.session is None:
            return aiohttp.get(url)
        return self.session.get(url)

    async def async_close_session(self):
        await self.session.close()

    def close_session(self):
        self.run_coro(self.async_close_session())
