import os
import yaml

from cryptowatch import errors


def read_api_key_from_config():
    user_home_dir = os.environ.get("HOME")
    filepath = "{}/.cw/credentials.yml".format(user_home_dir)
    api_key = None
    try:
        with open(filepath, "r") as config_file:
            config = yaml.safe_load(config_file)
            if not config.get("apikey"):
                log("No API key seen in credential file", is_debug=True)
            else:
                api_key = config.get("apikey")
    except FileNotFoundError as ex:
        log("No credential file found", is_debug=True)
    except yaml.YAMLError as ex:
        log("Credential is not a valid YAML file", is_error=True)
        raise error.CredentialsFileError(
            "Your Cryptowatch credentials file at "
            "{} is not properly formatted.".format(filepath)
        )
    except Exception as ex:
        log("Credential is not a valid YAML file", is_error=True)
    finally:
        return api_key
