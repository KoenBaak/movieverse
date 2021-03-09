# ------ Python standard library imports ---------------------------------------
from typing import Any, Optional, List, Dict
# ------ External imports ------------------------------------------------------
import pandas as pd
# ------ Imports from own package or module ------------------------------------
#-------------------------------------------------------------------------------


class MetaDataLibrary:

    def __init__(self):
        self._data = dict()
        self._directors = dict()
        self._genres = set()
        self.fields = ['title', 'year']

    def title(self, movie_id: Any) -> Optional[str]:
        return self._data.get(movie_id, {}).get('title', None)

    def year(self, movie_id: Any) -> Optional[int]:
        return self._data.get(movie_id, {}).get('year', None)

    def directors(self, movie_id: Any) -> Optional[List[Dict[str, Any]]]:
        return self._data.get(movie_id, {}).get('directors', None)

    def genres(self, movie_id: Any) -> Optional[List[str]]:
        return self._data.get(movie_id, {}).get('genres', None)

    def add_genre_dummies(self,
                          df: pd.DataFrame,
                          include: Optional[list] = None,
                          exclude: Optional[list] = None) -> pd.DataFrame:
        pass

    def add_genre_string(self,
                         df: pd.DataFrame,
                         sep: str = '|',
                         include: Optional[list] = None,
                         exclude: Optional[list] = None) -> pd.DataFrame:
        pass

    def add_directors(self,
                      df: pd.DataFrame,
                      n: int = 1) -> pd.DataFrame:
        pass

    def add_directors_string(self,
                             df: pd.DataFrame,
                             sep: str = '|',
                             n: int = -1) -> pd.DataFrame:
        pass

    def dataframe(self) -> pd.DataFrame:
        pass