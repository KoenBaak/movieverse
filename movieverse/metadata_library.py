# ------ Python standard library imports ---------------------------------------
from typing import Any, Optional, List, Dict
# ------ External imports ------------------------------------------------------
import pandas as pd
# ------ Imports from own package or module ------------------------------------
from movieverse.metadata_base import MetaDataBase
#-------------------------------------------------------------------------------


class MetaDataLibrary(MetaDataBase):

    def __init__(self):
        super().__init__()
        self._data = dict()

    def title(self, movie_id : Any) -> Optional[str]:
        return self._data.get(movie_id, {}).get('title', None)

    def year(self, movie_id : Any) -> Optional[int]:
        return self._data.get(movie_id, {}).get('year', None)

    def directors(self, movie_id : Any) -> Optional[List[Dict[str, Any]]]:
        return self._data.get(movie_id, {}).get('directors', None)

    def genres(self, movie_id : Any) -> Optional[List[str]]:
        return self._data.get(movie_id, {}).get('genres', None)

    def dataframe(self, genre_dummies : bool = False) -> pd.DataFrame:
