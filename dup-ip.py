#!/usr/bin/python
#
#dup-ip.py
#Script to return Duplicate IP interface allocations within Juniper config.
#Duplicate IP's are not ususally an issue if within different VRF's/LS's
#However Juniper devices can object to duplicate IP's existing in different logical containers
#when upgrading Junos versions.

import os.path
import re, getpass, netmiko
from netmiko import ConnectHandler

#Define pointers
totalpeer=0
alldownpeer2=""
alldups=""
dothis = "show configuration | display set | match \"inet address\" | except vrrp | except fxp"
device_type="juniper"
j_routers = []

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'device-list.txt')
hostfile=open(filename)

ssh_exceptions = (netmiko.ssh_exception.NetMikoAuthenticationException,
                  netmiko.ssh_exception.NetMikoTimeoutException, netmiko.NetMikoTimeoutException,
                  netmiko.NetMikoAuthenticationException, netmiko.NetmikoTimeoutError, netmiko.NetmikoAuthError,
                  netmiko.ssh_exception.SSHException, netmiko.ssh_exception.AuthenticationException)

un = input('Username: ')
pw = getpass.getpass()
my_file_object = open("device-list.txt", "r")

#Read from hostfile
for line in hostfile:
    if "#" not in line:
        j_routers.append(line.strip())

hostfile.close()

#Below there be dragons

def devicetype():
    madshow = ssh_conn.send_command_expect("show version")
    if "cisco" in madshow.lower():
        return "CISCO"
    elif "junos" in madshow.lower():
        return "JUNIPER"
    else:
        return None

print ("Here we go:")

for j_rtr in j_routers:
    try:
        print ("#"*79)
        print ("Connecting to:",j_rtr)
        ssh_conn = ConnectHandler(ip=j_rtr, device_type=device_type, username=un, password=pw)
        output = ssh_conn.send_command_expect(dothis)
        print (devicetype())
        lineoutput = output.splitlines()

        print ("Connected to:",j_rtr)
        
        for line in lineoutput: #Extract IP address from command and print if dupicate within this device.
            line = line.replace('{master}','') #Clean up junk lines
            totalpeer += 1
            prefix = line.split(" ")[-1]
            if prefix in alldownpeer2:
                print (j_rtr," ***DUPLICATE***",prefix)
                alldups += prefix + (",")
            alldownpeer2 += prefix + (" -*- ")

                
        ssh_conn.disconnect()
    except ssh_exceptions:
        print ("Could not connect to device:",j_rtr)

print ("#"*79)    
print ("IP's checked:",totalpeer)
print ("#"*79)
print ("All Duplicates:")
print (alldups)

