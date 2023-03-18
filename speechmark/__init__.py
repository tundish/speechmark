import datetime
import importlib.metadata

try:
    import tomllib
except ImportError:
    import tomli as tomllib


try:
    __version__ = importlib.metadata.version("nmskit")
except importlib.metadata.PackageNotFoundError:
    __version__ = datetime.date.today().strftime("%Y.%m.%d") + "+local_repository"

from .speechmark import SpeechMark
