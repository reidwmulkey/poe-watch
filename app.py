import requests
from requests.auth import HTTPDigestAuth
import json
import Config
import StashResponses

print(Config)
config = Config.Config()

print(config.GET_PUBLIC_STASH_TABS)
response = requests.get(config.GET_PUBLIC_STASH_TABS)
#print(response.json())
print(response.json().keys())
print(response.json()['next_change_id'])
stashResponses = StashResponses.StashResponses(response.json())
