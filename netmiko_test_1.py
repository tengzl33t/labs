import os
from netmiko import ConnectHandler
from decouple import config

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
output = net_connect.send_command('show ip int brief')
print(output)