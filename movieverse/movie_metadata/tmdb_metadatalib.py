# --- imports from python standard library -------------------------------------
# --- external imports ---------------------------------------------------------
# --- imports own packages and modules -----------------------------------------
from .abc_metadata_manager import MetaDataManager
from movieverse.async_client import AsyncClient
# ------------------------------------------------------------------------------

class TMDBMetaDataLib(AsyncClient, MetaDataManager):
    def __init__(self) -> None:
        # TODO:
        pass
