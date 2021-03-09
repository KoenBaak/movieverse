# ------ Python standard library imports ---------------------------------------
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional
# ------ External imports ------------------------------------------------------
import pandas as pd
# ------ Imports from own package or module ------------------------------------
from movieverse.metadatalib import MetaDataLibrary
#-------------------------------------------------------------------------------


class MetaDataLibWithFallback(MetaDataLibrary, ABC):

    pass