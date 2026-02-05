import configparser
import os
config=configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "..", "config", "config.ini"))


BASEURL=config.get("env","baseurl")
USERNAME=config.get("credentials","username")
PASSWORD=config.get("credentials","password")
LEVEL=config.get("logs","level")





