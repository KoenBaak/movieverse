# ------ Python standard library imports ---------------------------------------
from typing import Any, Optional, Iterable
# ------ External imports ------------------------------------------------------
import pandas as pd
# ------ Imports from own package or module ------------------------------------
from movieverse.metadatalib_base import MetaDataLibraryBase, METADATA_FIELDS
#-------------------------------------------------------------------------------


class MetaDataLibrary(MetaDataLibraryBase):

    def __init__(self, fields: Optional[list] = None) -> None:
        super().__init__(fields)
        self._index = {}
        self._data = {
            field : [] for field in self.fields
        }
        self._counter = 0

    def add_data(self,
                 movie_id: Any,
                 title: str,
                 year: int,
                 **other_fields) -> None:

        index = self._counter
        self._counter += 1
        self._index[movie_id] = index
        self._data['title'].append(title)
        self._data['year'].append(year)
        for f in self.other_fields:
            self._data[f].append(other_fields.get(f, None))

    def set_data(self,
                 movie_id: Any,
                 **fields) -> None:

        if movie_id not in self._index:
            return self.add_data(movie_id, **fields)

        index = self._index[movie_id]
        for f in fields:
            self._data[f][index] = fields[f]

    def get_data(self, field: str, movie_id: Any) -> Any:
        index = self._index.get(movie_id, None)
        if index is None:
            raise ValueError(f'Movie with ID {movie_id} not known')
        return self._data[field][index]

    def available_ids(self) -> list:
        return list(self._index.keys())

    def dataframe(self,
                  movie_ids: Optional[Iterable] = None,
                  fields: Optional[list] = None) -> pd.DataFrame:

        if movie_ids is None:
            fields = fields or self.base_fields
            data = {field : self._data[field] for field in fields}
            df = pd.DataFrame(data, index=self.available_ids())
            df.index.name = 'movie_id'
            return df

        return super().dataframe(movie_ids, fields)
