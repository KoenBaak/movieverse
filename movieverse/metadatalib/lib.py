# --- imports from python standard library -------------------------------------
from typing import List, Dict, Iterable, Any, Optional, Generator
# --- external imports ---------------------------------------------------------
import pandas as pd
# --- imports own packages and modules -----------------------------------------
from .base import MetaDataLibraryBase, REQUIRED_FIELDS
# ------------------------------------------------------------------------------

class MetaDataLib(MetaDataLibraryBase):

    def __init__(self, data: Optional[Dict[str, Iterable]] = None,
                 ids: Optional[Iterable[Any]] = None,
                 fields: Optional[Iterable[str]] = None) -> None:

        data = data or dict()
        ids = ids or []
        self._fields = REQUIRED_FIELDS.copy()
        for field in fields or []:
            if field not in REQUIRED_FIELDS:
                self._fields.append(field)

        detected_fields = list(data.keys())
        if not all(field in self._fields for field in detected_fields):
            raise ValueError(f"Given value of fields parameter does not agree with given data")

        self._data = {}
        self._ids = {
            movie_id: i for i, movie_id in enumerate(ids)
        }

        for field, values in data.items():
            if len(values) != len(self._ids):
                raise ValueError(f"length of data in field {field} does not equal nr of movie ids")
            self._data[field] = list(values)

        for field in self._fields:
            if field not in self._data:
                self._data[field] = [None for _ in range(len(self._ids))]

    def _get_data(self, movie_id: Any, field: str) -> Any:
        return self._data[field][self._ids[movie_id]]

    def _set_data(self, movie_id: Any, field: str, value: Any) -> None:
        current_value = self._get_data(movie_id, field)
        if isinstance(current_value, list):
            current_value.append(value)
        else:
            self._data[field][self._ids[movie_id]] = value

    def add_movie(self, movie_id: Any, title: str, year: int, **fields) -> None:
        self._ids[movie_id] = len(self._ids)
        self._data["title"].append(title)
        self._data["year"].append(year)
        for field in filter(lambda f: f not in ['title', 'year'], self._fields):
            self._data[field].append(fields.get(field, None))

    def delete_movie(self, movie_id: Any) -> None:
        index = self._ids[movie_id]
        for movie_id, old_index in self._ids.items():
            if old_index > index:
                self._ids[movie_id] = old_index - 1
        del self._ids[movie_id]
        for field, values in self._data.items():
            values.pop(index)

    def iter_ids(self) -> Generator[Any, None, None]:
        for movie_id in self._ids:
            yield movie_id

    def nmovies(self) -> int:
        return len(self._ids)

    @property
    def fields(self) -> List[str]:
        return self._fields.copy()

    def to_pandas(self):
        index = pd.Index(list(self._ids.keys()), name="movie_id")
        return pd.DataFrame(data=self._data, index=index)
