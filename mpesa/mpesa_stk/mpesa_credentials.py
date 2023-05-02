import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64




class MpesaC2bCredentials:
    consumer_key='au4Xlvi60wH7Dtna0lnMxdbaiNxdz1tV'
    consumer_secret='LA88qpcJfO1QRZKA'
    api_url ='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

class MpesaAccessToken:
    r = requests.get(MpesaC2bCredentials.api_url,
                     auth=HTTPBasicAuth(MpesaC2bCredentials.consumer_key,MpesaC2bCredentials.consumer_secret))
    mpesa_access_token=json.loads(r.text)
    validated_mpesa_mpesa_token = mpesa_access_token['access_token']
                                        