beeminderpy
===========

python wrapper for beeminder api

Instructions:
-------------

* Create a copy of settings.py.readme and call it settings.py. The settings are not used for beeminder.
* To access the API, call Beeminder(), your API token will be automatically pulled from settings.py. Store the new object in a variable.
* To read the API values, use the (JSON decoder)[http://docs.python.org/2/library/json.html]