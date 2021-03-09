# --- imports from python standard library -------------------------------------
from datetime import datetime
from typing import Callable, Any
import asyncio
# --- external imports ---------------------------------------------------------
from bs4 import BeautifulSoup
import aiohttp
# --- imports own packages and modules -----------------------------------------
from movieverse.async_client import AsyncClient, handle_session
# ------------------------------------------------------------------------------


class LetterboxdScraper(AsyncClient):

    base_url = 'https://letterboxd.com/'

    diary_data_holders = {
        'title' : 'data-film-name',
        'year' : 'data-film-year',
        'date' : 'data-viewing-date',
        'rating' : 'data-rating',
        'link' : 'data-film-link',
        'rewatch' : 'data-rewatch'
    }

    tmdb_id_holder = 'data-tmdb-id'

    def watched_url(self, username : str, pagenr : int = 1) -> str:
        return f'{self.base_url}{username}/films/page/{pagenr}'

    def diary_url(self, username : str, pagenr : int = 1) -> str:
        return f'{self.base_url}{username}/films/diary/page/{pagenr}'

    async def async_get_diary_page(self, username : str, pagenr : int = 1) -> dict:
        url = self.diary_url(username, pagenr)
        async with self.get(url) as response:
            soup = BeautifulSoup(await response.read(), 'lxml')

        entries = []
        entry_items = soup.find_all('tr', 'diary-entry-row')
        for item in entry_items:
            to_find = list(self.diary_data_holders.keys())
            info = dict()
            while to_find:
                search_key = to_find.pop(0)
                tag = item.find(lambda tag : self.diary_data_holders[search_key] in tag.attrs)
                info[search_key] = tag[self.diary_data_holders[search_key]]
                for target in to_find:
                    if self.diary_data_holders[target] in tag.attrs:
                        info[target] = tag[self.diary_data_holders[target]]
                        to_find.remove(target)

            info['rating'] = int(info['rating'])
            info['year'] = int(info['year'])
            info['link'] = info['link'].split('/')[-2]
            info['date'] = datetime.strptime(info['date'], '%Y-%m-%d')
            info['rewatch'] = info['rewatch'] == 'true'
            entries.append(info)
        return entries

    @handle_session
    async def async_get_pages_until_done(self, func : Callable,
                                         concurrent : int = 10,
                                         start_page : int = 1) -> Any:

        result = []
        i = 0
        while True:
            tasks = [
                func(n) for n in range(start_page+concurrent*i,
                                       start_page+concurrent*(i+1))
            ]
            i += 1
            results = await asyncio.gather(*tasks)
            for r in results:
                result.extend(r)
            if not results[-1]:
                break
        return result

    @handle_session
    async def async_get_diary(self, username : str,
                              concurrent_pages : int = 10) -> list:

        async def get_page(pagenr: int):
            return await self.async_get_diary_page(username, pagenr)

        return await self.async_get_pages_until_done(get_page,
                                                       concurrent=concurrent_pages)

    def get_diary(self, username : str, concurrent_pages : int = 10) -> list:
        return self.run_coro(
            self.async_get_diary(username, concurrent_pages=concurrent_pages,
                                 open_session=True, close_session=True)
        )
