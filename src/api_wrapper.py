'''
Use requests library to make basic API call to train delay API using API key 

write basic error handling for API responses (invalid key, bad requests, etc)

add unit tests for API calls

ensure data is in JSON
'''
from dotenv import dotenv_values

config = dict(dotenv_values("../.env"))