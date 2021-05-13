# --- imports from python standard library -------------------------------------
# --- external imports ---------------------------------------------------------
# --- imports own packages and modules -----------------------------------------
from metadalib.base import MetaDataLibraryBase
from movieverse.async_client import AsyncClient
# ------------------------------------------------------------------------------

class TMDBMetaDataLib(MetaDataLibraryBase, AsyncClient):
    def __init__(self) -> None:
        # TODO:
        pass
