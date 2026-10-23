from importlib import metadata

try:
    __version__ = metadata.version(__name__)
except pkg_resources.DistributionNotFound:
    __version__ = 'unknown'
