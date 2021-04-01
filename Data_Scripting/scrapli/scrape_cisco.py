from scrapli.driver.core import IOSXEDriver
import re
import os

os.system("clear")

device = {
    "host":"ios-xe-mgmt-latest.cisco.com",
    "auth_username":"developer",
    "auth_password":"C1sco12345",
    "auth_strict_key":False
}

conn = IOSXEDriver(**device)
conn.open()
responses = conn.send_command("show version")
# print(responses.result)

# print(re.findall("Compiled.+", responses.result))

# responses = conn.send_commands(["show version", "show ip int brief"])

# for response in responses:
#    print(response.result)
# conn.close()

shver_parsed = responses.genie_parse_output()
# print(shver_parsed)

hostname = shver_parsed['version']['hostname']
platform = shver_parsed['version']['platform']
model = shver_parsed['version']['chassis']
version = shver_parsed['version']['version']
serial = shver_parsed['version']['chassis_sn']
noofint = shver_parsed['version']['number_of_intfs']

print(f'Switch {hostname} (Serial: {serial}) is a {model} running version {version} with {platform} platform and {noofint} Interfaces.')

