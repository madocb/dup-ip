# dup-ip

## What does this do:
dup-ip uses Nekmiko (https://github.com/ktbyers/netmiko) which in turn utilises Paramiko SSH connections
to connect to Juniper and Cisco routers, issue a command, analyse output and run additional commands and collate findings.<br>
This script return a list of duplicate interface IP addresses accociated with hosts defined in `device-list.txt` 

## In short what does this do:
Output a list of duplicate interface IP addresses.

## What use is this to me:
- Duplicate IP's are not ususally an issue on Junos devices if within different VRF's/Logical Systems
- However Juniper devices can object to duplicate IP's existing in different logical containers when upgrading Junos.
- This allows you to identigy duplicate IP's before an upgrade so you can change/upgrade/change back to avoid a commit fail.

## How do I use dup-ip:
- Enter your device hostnames or IP addresses into `device-list.txt`
- Run the script: `python dup-ip.py`
- Enter your common username and password.
- Observe output with duplicate IP list.

