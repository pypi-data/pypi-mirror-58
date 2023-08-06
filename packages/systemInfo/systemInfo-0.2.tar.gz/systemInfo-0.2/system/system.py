import os
import sys
import time 
import datetime
import calendar
import socket
import uuid


def getTimestamp():
    try:
        return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        raise e

def getMachine_serial():
    try:
        """ Find OS and run appropriate read mobo serial num command"""
        os_type = sys.platform.lower()
    
        if "win" in os_type:
            command = "wmic bios get serialnumber"
    
        elif "linux" in os_type:
            command="sudo dmidecode -s system-serial-number"
    
        elif "darwin" in os_type:
            command = "ioreg -l | grep IOPlatformSerialNumber"
        return os.popen(command).read().replace("\n", "").replace("  ", "").replace(" ", "")
    except Exception as e:
        raise e

def getXray_asset_tracking_id():
    try:
        return str(getMachine_serial())+str(calendar.timegm(time.gmtime()))
    except Exception as e:
        raise e

def getMachine_registration_id():
    try:
        return getMachine_serial()+str(getMachine_mac_address(False))
    except Exception as e:
        raise e

def getMachine_mac_address(is_hex):
    try:
        if is_hex == True:
            return hex(uuid.getnode())
        return uuid.getnode() 
    except Exception as e:
        raise e
def serialize(obj):
    try:
        if isinstance(obj, datetime.date):
            serial = obj.isoformat()
            return serial

        return obj.__dict__
    except Exception as e:
        raise e
def getHost_name_ip(): 
    try:  
        return socket.gethostbyname(socket.gethostname()) 
    except: 
        raise e

def getPublic_ip():
    try:
        return json.loads(urllib.urlopen("http://ip.jsontest.com/").read())
    except Exception as e:
        raise e



