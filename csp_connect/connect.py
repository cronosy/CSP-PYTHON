import json
import requests

class connect_csp ():

    
    def __init__(self,tenantID,data) -> None:
        super().__init__()
        self.loginurl="https://login.microsoftonline.com"
        self.grant_type= "client_credentials"
        self.data=data
        self.result=""
        self.tenantID=tenantID

    def login(self) -> str:

        """_summary_
            start login and get Bearer token
        Returns:
            str: Bearer token will be used in each requests.
        """
        
        headers={
        "Accept":"application/json",
        "return-client-request-id": "true",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "login.microsoftonline.com",
        "Content-Length": "194",
        "Expect": "100-continue"
        }
 
        
        url="{0}/{1}/oauth2/token".format(self.loginurl,self.tenantID)
        response= requests.post(url=url,headers=headers,data=self.data)
        return response

    def __del__(self) -> None:
        
        self.clientid=""
        self.secretid=""
        self.tenantID=""
        self.loginurl=""
        self.grant_type= ""
        self.result=""