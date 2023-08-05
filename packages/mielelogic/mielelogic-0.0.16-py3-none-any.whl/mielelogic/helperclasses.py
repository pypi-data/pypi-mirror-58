from enum import Enum
from datetime import datetime
import requests

DATEFORMAT = "%Y-%m-%dT%H:%M:%S"
ALT_DATEFORMAT = "%Y-%m-%d %H:%M:%S"
ALT_DATEFORMAT_NO_SECONDS = "%Y-%m-%d %H:%M"

class WasherType(Enum):
    Washer = 0
    Dryer = 1
    Unknown = 2

class WasherState(Enum):
    Available = 1
    Reserved = 2

class Washer(object):
    def __init__(self, attrs):
        self.laundry = attrs["LaundryNumber"]
        self.group = attrs["GroupNumber"]
        self.machine_name = attrs["UnitName"]
        self.available = WasherState(attrs["MachineColor"])
        self.state = f'{attrs["Text1"]} {attrs["Text2"]}'
        self.type = WasherType(attrs["MachineSymbol"])
    
    def __repr__(self):
        return f"{self.machine_name}\n{self.available}\n{self.type}\n{self.state}\n"

class TimeSlot(object):
    def __init__(self, attrs, machine_id):
        self.start_time = (datetime.strptime(attrs["Start"], DATEFORMAT))
        self.end_time = (datetime.strptime(attrs["End"], DATEFORMAT))
        self.status = attrs["Status"]
        self.available = self.status == "Available"
        self.machine_id = machine_id
    
    def to_json(self, laundry):
        return {
            "MachineNumber":self.machine_id,
            "LaundryNumber":laundry,
            "Start":self.start_time.strftime(DATEFORMAT),
            "End":self.end_time.strftime(DATEFORMAT)
        }

    def __repr__(self):
        return f"{self.start_time.strftime(DATEFORMAT)}-{self.end_time.strftime(DATEFORMAT)}: {self.status}"

class TimeTable(object):
    def __init__(self, attrs):
        self.machine_id = attrs["MachineNumber"]
        self.machine_name = attrs["MachineName"]
        self.period_start = datetime.strptime(attrs["PeriodStart"], DATEFORMAT)
        self.period_end = datetime.strptime(attrs["PeriodEnd"], DATEFORMAT)
        self.time_table = [TimeSlot(x, self.machine_id) for x in attrs["TimeTable"]]
    
    def get_available_time_slots(self, start_time=None, end_time=None):
        if start_time and isinstance(start_time, str):
            if "T" in start_time.upper():
                start_time = datetime.strptime(start_time, DATEFORMAT)
            else:
                try:
                    start_time = datetime.strptime(start_time, ALT_DATEFORMAT)
                except ValueError:
                    start_time = datetime.strptime(start_time, ALT_DATEFORMAT_NO_SECONDS)                
        
        if end_time and isinstance(end_time, str):
            if "T" in end_time.upper():
                end_time = datetime.strptime(end_time, DATEFORMAT)
            else:
                try:
                    end_time = datetime.strptime(end_time, ALT_DATEFORMAT)
                except ValueError:
                    end_time = datetime.strptime(end_time, ALT_DATEFORMAT_NO_SECONDS)  

        if start_time is None and end_time is None:
            return [x for x in self.time_table if x.available]
        elif start_time is None:
            return [x for x in self.time_table if x.available and x.end_time <= end_time]
        elif end_time is None:
            return [x for x in self.time_table if x.available and x.start_time >= start_time]
        else:
            return [x for x in self.time_table if x.available and x.start_time >= start_time and x.end_time <= end_time]


    def __repr__(self):
        return f"{self.machine_name}:\n{self.time_table}"

class Reservation(object):
    def __init__(self, attrs):
        self.laundry = attrs["LaundryNumber"]
        self.machine_id = attrs["MachineNumber"]
        self.machine_name = attrs["MachineName"]
        self.start_time = (datetime.strptime(attrs["Start"], DATEFORMAT))
        self.end_time = (datetime.strptime(attrs["End"], DATEFORMAT))
    
    def to_json(self):
        return {
            "MachineNumber":self.machine_id,
            "LaundryNumber":self.laundry,
            "Start":self.start_time.strftime(DATEFORMAT),
            "End":self.end_time.strftime(DATEFORMAT)
        }

    def __repr__(self):
        return f"{self.machine_name}: {self.start_time.strftime(DATEFORMAT)}-{self.end_time.strftime(DATEFORMAT)}"