import json
import requests

class connect_csp ():

    #def __init__(self,clientid,secretid,tenatID) -> None:
    #    super().__init__()
    #    self.clientid=clientid.strip()
    #    self.secretid=secretid.strip()
    #    self.tenantID=tenatID.strip()
    #    self.loginurl="https://login.microsoftonline.com"
    #    self.grant_type= "client_credentials"
    #    self.result=""
    
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
        #headers={
        # "Accept": "*/*",
        #"Content-Type": "application/x-www-form-urlencoded"
        #}
        #data={  "resource": "https%3A%2F%2Fgraph.windows.net","client_id": self.clientid, "client_secret": self.secretid, "grant_type": self.grant_type }
        #data="resource=https%3A%2F%2Fgraph.windows.net&client_id=42a9418c-a829-4852-b943-bcfd7f07a836&client_secret=4RJwgFymMpNL7o1%2BXY6%2BpHGdBJSOocWF2/W5V5B/K3w=&grant_type=client_credentials"
        #data="resource=https%3A%2F%2Fgraph.windows.net&client_id=" + self.clientid + "&client_secret=" + self.secretid + "&grant_type=client_credentials"
        #print(self.data)
        
        url="{0}/{1}/oauth2/token".format(self.loginurl,self.tenantID)
        response= requests.post(url=url,headers=headers,data=self.data)
        #print(response.json)
        #self.result=response.json()
        return response

    def __del__(self) -> None:
        
        self.clientid=""
        self.secretid=""
        self.tenantID=""
        self.loginurl=""
        self.grant_type= ""
        self.result=""