import http.client
import requests
import json

class Request:
    def __init__(self):
        self.conn = http.client.HTTPSConnection("omgvamp-hearthstone-v1.p.rapidapi.com")
        self.headers = {'X-RapidAPI-Host': "omgvamp-hearthstone-v1.p.rapidapi.com",
                        'X-RapidAPI-Key': "97167c7cc2mshbf62f83c1618b15p1d1cb2jsn097e721239cf"}

    def remove_bg(self,url) -> bytes:
        response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        data={
            'image_url': f'{url}',
            'size': 'auto'
        },
        headers={'X-Api-Key': 'DyNoGErN8hYLp7jpvtFKHcHi'},)
        if response.status_code == requests.codes.ok:
            return response.content
        print("Error:", response.status_code, response.text)
        return bytes([10])

    
    def get_attack_1(self) -> dict:
        self.conn.request("GET", "/cards?attack=1", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        a = json.loads(data.decode("utf-8"))
        return a
    
    def get_attack_2(self) -> dict:
        self.conn.request("GET", "/cards?attack=2", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        a = json.loads(data.decode("utf-8"))
        return a
    
    def get_attack_3(self) -> dict:
            self.conn.request("GET", "/cards?attack=3", headers=self.headers)
            res = self.conn.getresponse()
            data = res.read()
            a = json.loads(data.decode("utf-8"))
            return a
    
    def get_attack_4(self) -> dict:
        self.conn.request("GET", "/cards?attack=4", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        a = json.loads(data.decode("utf-8"))
        return a

    def get_attack_5(self) -> dict:
        self.conn.request("GET", "/cards?attack=5", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        a = json.loads(data.decode("utf-8"))
        return a
    
    def get_attack_6(self) -> dict:
        self.conn.request("GET", "/cards?attack=6", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        a = json.loads(data.decode("utf-8"))
        return a

    def get_attack_7(self) -> dict:
        self.conn.request("GET", "/cards?attack=7", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        a = json.loads(data.decode("utf-8"))
        return a
    
    def get_attack_8(self) -> dict:
        self.conn.request("GET", "/cards?attack=8", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        a = json.loads(data.decode("utf-8"))
        return a

    def get_attack_9(self) -> dict:
        self.conn.request("GET", "/cards?attack=9", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        a = json.loads(data.decode("utf-8"))
        return a
    
    def get_attack_10(self) -> dict:
        self.conn.request("GET", "/cards?attack=10", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        a = json.loads(data.decode("utf-8"))
        return a

    def get_attack_11(self) -> dict:
        self.conn.request("GET", "/cards?attack=11", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        a = json.loads(data.decode("utf-8"))
        return a
    
    def get_attack_12(self) -> dict:
        self.conn.request("GET", "/cards?attack=12", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        a = json.loads(data.decode("utf-8"))
        return a
