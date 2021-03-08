# ------ Python standard library imports ---------------------------------------
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional
# ------ External imports ------------------------------------------------------
import pandas as pd
# ------ Imports from own package or module ------------------------------------
#-------------------------------------------------------------------------------


class MetaDataBase(ABC):

    def __init__(self):
        self.fields = ['title', 'year', 'directors', 'genres']

    @abstractmethod
    def title(self, movie_id : Any) -> Optional[str]:
        pass

    @abstractmethod
    def year(self, movie_id : Any) -> Optional[int]:
        pass

    @abstractmethod
    def directors(self, movie_id : Any) -> Optional[List[Dict[str, Any]]]:
        pass

    @abstractmethod
    def genres(self, movie_id : Any) -> Optional[List[str]]:
        pass

    @abstractmethod
    def dataframe(self, genre_dummies : bool = False) -> pd.DataFrame:
        pass