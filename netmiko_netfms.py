import os
from netmiko import ConnectHandler
from decouple import config
import json

dev_type = config('device_type')
host = config('host')
user = config('username')
passwd = config('passwd')
port = config('port')

cisco_881 = {
    'device_type': dev_type,
    'host':   host,
    'username': user,
    'password': passwd,
    'port' : port,          # optional, defaults to 22
    'secret': ''     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco_881)
net_connect.enable()
interfaces = net_connect.send_command('show ip int brief', use_textfsm=True)
noi = len(interfaces)
print("This device has " +str(noi) + " Interfaces")

for interface in interfaces:
    if interface['status'] == 'up':
        # config_command = ['int GigabitEthernet3', 'no shut']
        # output = net_connect.send_config_set(config_command)
        # print(output)
        print(interface['intf'] + " is Up")