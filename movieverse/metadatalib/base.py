# --- imports from python standard library -------------------------------------
from abc import ABC, abstractmethod
from typing import Any, Generator, List
# --- external imports ---------------------------------------------------------
import pandas as pd
# --- imports own packages and modules -----------------------------------------
# ------------------------------------------------------------------------------


REQUIRED_FIELDS = [
    "title", "year"
]

class MetaDataLibraryBase(ABC):

    @abstractmethod
    def _get_data(self, movie_id: Any, field: str) -> Any:
        pass

    @abstractmethod
    def _set_data(self, movie_id: Any, field: str, value: Any) -> None:
        pass

    @abstractmethod
    def add_movie(self, movie_id: Any, title: str, year: int, **fields) -> None:
        pass

    @abstractmethod
    def delete_movie(self, movie_id: Any) -> None:
        pass

    @abstractmethod
    def iter_ids(self) -> Generator[Any, None, None]:
        pass

    @abstractmethod
    def nmovies(self) -> int:
        pass

    @property
    def fields(self) -> List[str]:
        return REQUIRED_FIELDS.copy()

    def get_data(self, movie_id: Any, field: str) -> Any:
        if field not in self.fields:
            raise ValueError(f"{self} has no field {field}")
        return self._get_data(movie_id, field)

    def set_data(self, movie_id: Any, field: str) -> Any:
        if field not in self.fields:
            raise ValueError(f"{self} has no field {field}")
        return self._set_data(movie_id, field)

    def title(self, movie_id: Any) -> str:
        return self._get_data(movie_id, "title")

    def year(self, movie_id: Any) -> int:
        return self._get_data(movie_id, "year")

    def to_pandas(self):
        data = {
            field: [self._get_data(mid, field) for mid in self.iter_ids()]
            for field in self.fields
        }
        index = pd.Index(list(self.iter_ids), name='movie_id')
        return pd.DataFrame(data=data, index=index)

    def __repr__(self):
        return "<Movie Metadata Library>"
