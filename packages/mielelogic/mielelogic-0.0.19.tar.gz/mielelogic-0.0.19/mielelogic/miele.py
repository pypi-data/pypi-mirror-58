from urllib.parse import urlsplit, urlunsplit
from .helperclasses import *
import requests

class MieleLogic(object):
    def __init__(self, username, password, baseurl="https://mielelogic.com", countrycode="DA"):
        self.baseurl = baseurl
        self.username = username
        self.password = password
        self.countrycode = countrycode
        self.token = None
        self.laundry = None
        self.account_balance = None
        self.account_currency = None
        _uri = urlsplit(self.baseurl)
        self.sec_url = urlunsplit(_uri._replace(netloc=f'sec.{_uri.netloc}'))
        _uri = urlsplit(self.baseurl)
        self.api_url = urlunsplit(_uri._replace(netloc=f'api.{_uri.netloc}'))
        _uri = None
        self.Authenticate()
        self.Get_Details()

    def Authenticate(self):
        url = f"{self.sec_url}/v3/token"
        payload = f"grant_type=password&username={self.username}&password={self.password}&client_id=YV1ZAQ7BTE9IT2ZBZXLJ&scope={self.countrycode}"
        r = requests.post(url, data=payload)
        if not r.ok:
            print(r.text)
            r.raise_for_status()
        self.token = f"Bearer {r.json()['access_token']}"


    def Get_Details(self):
        url = f"{self.api_url}/v3/accounts/Details"
        headers = {
            "Authorization": self.token
        }
        r = requests.get(url, headers=headers)
        if r.status_code == 401:
            self.Authenticate()
            return self.Get_Details()
        if not r.ok:
            print(r.text)
            r.raise_for_status()
        jsonResponse = r.json()
        self.account_currency = jsonResponse["Cards"][0]["Currency"]
        self.account_balance = jsonResponse["Cards"][0]["AccountBallance"]
        self.laundry = jsonResponse["AccessibleLaundries"][0]["LaundryNumber"]
        

    def Get_Reservations(self):
        url = f"{self.api_url}/v3/reservations"
        headers = {
            "Authorization": self.token
        }
        params = {
            "laundry": self.laundry
        }
        r = requests.get(url, headers=headers, params=params)
        if r.status_code == 401:
            self.Authenticate()
            return self.Get_Reservations()
        if not r.ok:
            print(r.text)
            r.raise_for_status()
        return [Reservation(x) for x in r.json()["Reservations"]]
    
    def Get_Laundry_State(self):
        url = f"{self.api_url}/v3/Country/{self.countrycode}/Laundry/{self.laundry}/laundrystates?language=en"
        headers = {
            "Authorization": self.token
        }
        r = requests.get(url, headers=headers)
        if r.status_code == 401:
            self.Authenticate()
            return self.Get_Laundry_State()
        if not r.ok:
            print(r.text)
            r.raise_for_status()
        
        return [Washer(x) for x in r.json()["MachineStates"]]

    def Get_Time_Slots(self):
        url = f"{self.api_url}/v3/country/{self.countrycode}/laundry/{self.laundry}/timetable"
        headers = {
            "Authorization": self.token
        }
        r = requests.get(url, headers=headers)
        if r.status_code == 401:
            self.Authenticate()
            return self.Get_Time_Slots()
        if not r.ok:
            print(r.text)
            r.raise_for_status()
        return [TimeTable(v) for k, v in r.json()["MachineTimeTables"].items()]

    def reserve_time_slot(self, time_slot):
        if isinstance(time_slot, dict):
            time_slot = TimeSlot(time_slot)
        url = f"{self.api_url}/v3/reservations"
        headers = {
            "Authorization": self.token
        }
        payload = time_slot.to_json(self.laundry)
        print(payload)
        r = requests.put(url, headers=headers, json=payload)
        if r.status_code == 401:
            self.Authenticate()
            return self.reserve_time_slot(time_slot)
        if not r.ok:
            print(r.text)
            r.raise_for_status()
        print(r.text)
        return r.json()["ResultOK"]

    def delete_reservation(self, reservation):
        if isinstance(reservation, dict):
            reservation = Reservation(reservation)
        url = f"{self.api_url}/v3/reservations"
        headers = {
            "Authorization": self.token
        }
        params = reservation.to_json()
        r = requests.delete(url, headers=headers, params=params)
        if r.status_code == 401:
            self.delete_reservation()
            return self.reserve_time_slot(reservation)
        if not r.ok:
            print(r.text)
            r.raise_for_status()
        return r.json()["ResultOK"]
