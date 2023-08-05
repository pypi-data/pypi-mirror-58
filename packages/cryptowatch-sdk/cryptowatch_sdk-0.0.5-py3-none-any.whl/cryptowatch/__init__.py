from cryptowatch.utils import log
from cryptowatch.auth import read_api_key_from_config
from cryptowatch.requestor import Requestor
from cryptowatch.resources.assets import Assets
from cryptowatch.resources.instruments import Instruments
from cryptowatch.resources.exchanges import Exchanges
from cryptowatch.resources.markets import Markets


# Package version
__version__ = "0.0.4"


# SDK constants
api_endpoint = "https://api.cryptowat.ch"
sdk_version = __version__


# HTTP client default settings
verify_ssl = True
connect_timeout = 4  # in seconds
read_timeout = 10  # in seconds
max_retries = 10  # number of time we'll retry a failing request
_user_agent = (
    "Mozilla/5.0 (compatible; Cryptowatch-Official-Python-SDK"
    "/v{} +https://cryptowat.ch/)".format(sdk_version)
)


# Try to read and set the API key from credential file
api_key = read_api_key_from_config()


def is_authenticated():
    return api_key is not None


# Get an instance of the HTTP client
requestor = Requestor(api_endpoint, _user_agent, locals())


# Serialize resources to namespace
assets = Assets(requestor)
instruments = Instruments(requestor)
exchanges = Exchanges(requestor)
markets = Markets(requestor)
