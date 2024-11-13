'''
Use requests library to make basic API call to train delay API using API key 

write basic error handling for API responses (invalid key, bad requests, etc)

add unit tests for API calls

ensure data is in JSON

{
  "filter": {
    "min_delay": 100,
    "max_delay": 100,
    "route_id": [
      "Inland Emp.-Orange Co. Line"
    ],
    "stop_id": [
      "145"
    ],
    "stop_name": [
      "Orange Metrolink Station"
    ],
    "trip_id": [
      "200000030"
    ],
    "vehicle_id": [
      ""
    ],
    "vehicle_label": [
      ""
    ],
    "trip_direction_id": [
      0
    ],
    "trip_headsign": [
      "Laguna Niguel / Mission Viejo"
    ],
    "rail_environment": "",
    "rail_provider": ""
  }
}
'''
from dotenv import dotenv_values

config = dict(dotenv_values("../.env"))