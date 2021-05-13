# ------ Python standard library imports ---------------------------------------
from typing import Any, Union
# ------ External imports ------------------------------------------------------
# ------ Imports from own package or module ------------------------------------
from movieverse.metadatalib.base import MetaDataLibraryBase
from movieverse.movie import Movie
from movieverse.viewer import Viewer
#-------------------------------------------------------------------------------


class Movieverse:

    def __init__(self,
                 metadatalib: MetaDataLibraryBase,
                 name: str = 'U',
                 viewer_lookup: str = 'id') -> None:

        self.name = name
        self.metadatalib = metadatalib
        if self.viewer_lookup not in ['id', 'name']:
            raise ValueError('Viewer lookup must be "name" or "id"')
        self.viewer_lookup = viewer_lookup
        self.movies = dict()
        self.viewers = dict()

    def get_movie(self, movie_id: Any) -> Movie:
        return self.movies.get(movie_id, None)

    def get_viewer_by_name(self, name: str,
                           first: bool = False) -> Union[Viewer, list]:
        if self.viewer_lookup == 'name':
            return self.viewers.get(name, None)
        result = []
        for viewer in self.viewers.values():
            if viewer.name == name:
                if first:
                    return viewer
                result.append(viewer)
        return result

    def get_viewer_by_id(self, viewer_id: int) -> Viewer:
        if self.viewer_lookup == 'id':
            return self.viewers.get(viewer_id, None)
        for viewer in self.viewers:
            if viewer.id == viewer_id:
                return viewer
        return None

    @property
    def nviewers(self) -> int:
        return len(self.viewers)

    @property
    def nmovies(self) -> int:
        return len(self.movies)

    def __repr__(self) -> str:
        return f'<Movieverse {self.name}>'
