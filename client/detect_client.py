import json
import httplib
import ssl

service_host = 'yourcompanyhost'
service_port = 4273

class investigate():

    def __init__(self, host=None, port=None):
        if host == None:
            raise "Need host name!"
        if port == None:
            port = 443
        self.host = host
        self.port = port

    def start(self):
        headers = {'Content-type':'application/json'}
        url = "/certcheck/"+self.host
        ssl.get_server_certificate((self.domain, 443))
        conn = httplib.HTTPConnection(service_host,service_port, timeout=4)
        cert = ssl.get_server_certificate((self.host, self.port), ssl_version=ssl.PROTOCOL_TLSv1)
        payload = json.dumps({"host":self.host, "port":self.port, "cert":cert}, encoding="utf-8")
        conn.request("POST", url, json.dumps(payload), headers)
        return conn.getresponse().read()


