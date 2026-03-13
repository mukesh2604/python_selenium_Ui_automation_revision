import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "..", "config", "config.ini"))

# Optional API-specific config file (keeps API keys separate from general config)
api_config = configparser.ConfigParser()
api_config_path = os.path.join(os.path.dirname(__file__), "..", "config", "api_config.ini")
if os.path.exists(api_config_path):
    api_config.read(api_config_path)

# Core config values
BASEURL = config.get("env", "baseurl")
USERNAME = config.get("credentials", "username")
PASSWORD = config.get("credentials", "password")
LEVEL = config.get("logs", "level")

API_BASEURL=config.get("api", "api_base_url")