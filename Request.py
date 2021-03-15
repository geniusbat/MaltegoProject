import string
from collections import namedtuple
import json
import requests


class Request:
    """
    This class is used for making requests
    """
    resCode: int #The code of the request
    res: string #The json string returned from the request

    def __init__(self, url):
        obj = requests.get(url)
        self.resCode = obj.status_code
        self.res = obj.text

    # When called, it returns a list of arrays, each one being a certificate
    def getCertificatesFromText(self):
        certList = []
        # Block the function if the result code is wrong and return an empty list
        if self.resCode != 200:
            print(self.resCode)
            return certList
        # Load the Json
        jsonObject = json.loads(self.res)
        # For issuer name I did that splitting as I didn't really know which was the name, can be corrected very quickly
        for element in jsonObject:
            certList.append((element["id"], element["name_value"],
                             element["issuer_name"].split(",")[1].strip().split("=")[1], element["issuer_ca_id"],
                             element["not_after"]))
        return certList


#obj = Request("https://crt.sh/?CN=maltego.com&output=json")
#print(obj.getCertificatesFromText()[0][0])
