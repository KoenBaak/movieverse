# ------ Python standard library imports ---------------------------------------
from abc import ABC, abstractmethod
from typing import Any, Iterable, Optional
# ------ External imports ------------------------------------------------------
import pandas as pd
# ------ Imports from own package or module ------------------------------------
#-------------------------------------------------------------------------------

METADATA_FIELDS = [
    'title',
    'original_title',
    'year',
    'genres',
    'directors'
]


class MetaDataLibraryBase(ABC):

    __slots__ = ['base_fields', 'other_fields']

    def __init__(self, fields: Optional[list] = None) -> None:
        self.base_fields = ['title', 'year']
        given_fields = fields or []
        self.other_fields = [f for f in given_fields if f not in self.base_fields]

    @property
    def fields(self) -> list:
        return self.base_fields + self.other_fields

    @abstractmethod
    def get_data(self, field: str, movie_id: Any) -> Any:
        pass

    @abstractmethod
    def available_ids(self) -> list:
        pass

    def title(self, movie_id: Any) -> str:
        return self.get_data('title', movie_id)

    def year(self, movie_id) -> int:
        return self.get_data('year', movie_id)

    def get_optional_data(self, field: str, movie_id: Any) -> Any:
        if field not in self.fields:
            raise ValueError(f'{self} does not support field {field}')
        return self.get_data(field, movie_id)

    def original_title(self, movie_id: Any) -> str:
        return self.get_optional_data('original_title', movie_id)

    def genres(self, movie_id: Any) -> list:
        return self.get_optional_data('genres', movie_id)

    def directors(self, movie_id: Any) -> list:
        return self.get_optional_data('directors', movie_id)

    def dataframe(self,
                  movie_ids: Optional[Iterable] = None,
                  fields: Optional[list] = None) -> pd.DataFrame:

        fields = fields or self.base_fields
        movie_ids = movie_ids or self.available_ids()
        data = {
            field : [self.get_data(field, id_) for id_ in movie_ids]
            for field in fields
        }
        df = pd.DataFrame(data, index=movie_ids)
        df.index.name = 'movie_id'
        return df

    def add_genre_dummies(self,
                          df: pd.DataFrame,
                          include: Optional[list],
                          exclude: Optional[list]) -> pd.DataFrame:

        if 'genres' not in self.fields:
            raise ValueError(f'{self} does not support genres')

        raise NotImplemented

    def __repr__(self) -> str:
        return f'<MetaDataLibrary with fields {self.fields}>'