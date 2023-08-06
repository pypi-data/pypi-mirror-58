import os
import sys
import time 
import datetime
import calendar
import socket





def getTimestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

def getMachine_serial():
    """ Find OS and run appropriate read mobo serial num command"""
    os_type = sys.platform.lower()
 
    if "win" in os_type:
        command = "wmic bios get serialnumber"
 
    elif "linux" in os_type:
        command="sudo dmidecode -s system-serial-number"
 
    elif "darwin" in os_type:
        command = "ioreg -l | grep IOPlatformSerialNumber"
    return os.popen(command).read().replace("\n", "").replace("  ", "").replace(" ", "")

def getXray_asset_tracking_id():
    return str(getMachine_serial())+str(calendar.timegm(time.gmtime()))


def getMachine_registration_id():
    return 'Xray0051'

def getMachine_mac_address():
        MAC_ADDRESS = os.popen('ifconfig `route | grep default | awk \'{print $8}\' | head -n1` | grep -Po \'HWaddr \K.*$\'').read()
        return MAC_ADDRESS.strip('\n')

def serialize(obj):
    if isinstance(obj, datetime.date):
        serial = obj.isoformat()
        return serial

    return obj.__dict__

def getHost_name_ip(): 
    try:  
        return socket.gethostbyname(socket.gethostname()) 
    except: 
        print("Unable to get Hostname and IP") 