import json
import requests

class connect_csp ():

    def __init__(self,clientid,secretid,tenatID) -> None:
        super().__init__()
        self.clientid=clientid
        self.secretid=secretid
        self.tenantID=tenatID
        self.loginurl="https://login.microsoftonline.com"
        self.grant_type= "client_credentials"
        self.result=""

    def login(self) -> str:

        """_summary_
            start login and get Bearer token
        Returns:
            str: Bearer token will be used in each requests.
        """
        
        headers={
        "Accept":"application/json",
        "return-client-request-id": "true",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Host": "login.microsoftonline.com",
        "Content-Length": "194",
        "Expect": "100-continue"
        }
        data={  "client_id": self.clientid, "client_secret": self.secretid, "grant_type": self.grant_type }
        url="{0}/{1}/oauth2/token".format(self.loginurl,self.tenantID)
        response= requests.post(url=url,headers=headers,data=data)
        self.result=response.json()
        return self.result

    def __del__(self) -> None:
        
        self.clientid=""
        self.secretid=""
        self.tenantID=""
        self.loginurl=""
        self.grant_type= ""
        self.result=""