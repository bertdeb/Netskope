"""
Retrieve CSV file of the list of Netskope CCI related application details based on the connector tag
"""

import requests
import json
import pandas as pd

resource = "services/cci/app"

parameters = {
    "connector": 1,
    "offset": 0,
    "limit": 3000
}

headers = {
    "Accept":"application/json",
    "Netskope-Api-Token":"0df0ebd17c6022556822afb3b513d0f7"
}

response = requests.get("https://forcesgcsndbx.goskope.com/api/v2/"+resource, params=parameters, headers=headers)

df = pd.DataFrame(data=response.json()['data'])

df.to_csv("output.csv", index=False)
