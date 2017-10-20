Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ssh_pkt_switched_lsys from source-prefix-list ssh_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term snmp_pkt_switched_lsys from source-prefix-list snmp_addresses_client_list_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ntp_pkt_switched_lsys from source-prefix-list ntp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term tacacs_pkt_switched_lsys from source-prefix-list tacacs_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term bgp_pkt_switched_lsys from source-prefix-list bgp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from source-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from destination-address 224.0.0.2/32
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from source-address 10.223.255.176/29
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 172.16.0.0/12 except
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 10.0.0.0/8 except
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
set firewall family inet filter protect_re term ssh from source-prefix-list ssh_addresses
set firewall family inet filter protect_re term snmp from source-prefix-list snmp_addresses_client_list
set firewall family inet filter protect_re term ntp from source-prefix-list ntp_addresses
set firewall family inet filter protect_re term tacacs from source-prefix-list tacacs_addresses
set firewall family inet filter protect_re term bgp from source-prefix-list bgp_addresses
set firewall family inet filter protect_re term critical_app from source-address 0.0.0.0/0
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.2/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.22/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.5/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.6/32
Peers DOWN
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ssh_pkt_switched_lsys from source-prefix-list ssh_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term snmp_pkt_switched_lsys from source-prefix-list snmp_addresses_client_list_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ntp_pkt_switched_lsys from source-prefix-list ntp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term tacacs_pkt_switched_lsys from source-prefix-list tacacs_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term bgp_pkt_switched_lsys from source-prefix-list bgp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from source-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from destination-address 224.0.0.2/32
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from source-address 10.223.255.176/29
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 172.16.0.0/12 except
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 10.0.0.0/8 except
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32
set firewall family inet filter protect_re term ssh from source-prefix-list ssh_addresses
set firewall family inet filter protect_re term snmp from source-prefix-list snmp_addresses_client_list
set firewall family inet filter protect_re term ntp from source-prefix-list ntp_addresses
set firewall family inet filter protect_re term tacacs from source-prefix-list tacacs_addresses
set firewall family inet filter protect_re term bgp from source-prefix-list bgp_addresses
set firewall family inet filter protect_re term critical_app from source-address 0.0.0.0/0
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.2/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.22/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.5/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.6/32
Peers DOWN


###############################################################################
Total number of BGP Peerings checked: 148
All Peers that are down:

###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ssh_pkt_switched_lsys from source-prefix-list ssh_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term snmp_pkt_switched_lsys from source-prefix-list snmp_addresses_client_list_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ntp_pkt_switched_lsys from source-prefix-list ntp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term tacacs_pkt_switched_lsys from source-prefix-list tacacs_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term bgp_pkt_switched_lsys from source-prefix-list bgp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from source-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from destination-address 224.0.0.2/32
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from source-address 10.223.255.176/29
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 172.16.0.0/12 except
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 10.0.0.0/8 except
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
set firewall family inet filter protect_re term ssh from source-prefix-list ssh_addresses
set firewall family inet filter protect_re term snmp from source-prefix-list snmp_addresses_client_list
set firewall family inet filter protect_re term ntp from source-prefix-list ntp_addresses
set firewall family inet filter protect_re term tacacs from source-prefix-list tacacs_addresses
set firewall family inet filter protect_re term bgp from source-prefix-list bgp_addresses
set firewall family inet filter protect_re term critical_app from source-address 0.0.0.0/0
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.2/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.22/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.5/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.6/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
 | display set | match set groups   re0                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
 | display set | match set groups   re1                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ssh_pkt_switched_lsys from source-prefix-list ssh_addresses_pkt_switched_lsys
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term snmp_pkt_switched_lsys from source-prefix-list snmp_addresses_client_list_pkt_switched_lsys
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ntp_pkt_switched_lsys from source-prefix-list ntp_addresses_pkt_switched_lsys
 | display set | match set logical-systems   PACKET_SWITCHED                                                                                                    ^syntax error.mbatters@dn2e9203-re0> show configuration | match bgp | match 
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term tacacs_pkt_switched_lsys from source-prefix-list tacacs_addresses_pkt_switched_lsys
Traceback (most recent call last):
  File "C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py", line 89, in <module>
    bgpdesc(peeripdown)
  File "C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py", line 53, in bgpdesc
    madshow = ssh_conn.send_command_expect(command2)
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\site-packages\netmiko-1.4.2-py3.5.egg\netmiko\base_connection.py", line 819, in send_command_expect
    return self.send_command(*args, **kwargs)
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\site-packages\netmiko-1.4.2-py3.5.egg\netmiko\base_connection.py", line 807, in send_command
    time.sleep(delay_factor * .2)
KeyboardInterrupt
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py 
Username: Mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ssh_pkt_switched_lsys from source-prefix-list ssh_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term snmp_pkt_switched_lsys from source-prefix-list snmp_addresses_client_list_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ntp_pkt_switched_lsys from source-prefix-list ntp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term tacacs_pkt_switched_lsys from source-prefix-list tacacs_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term bgp_pkt_switched_lsys from source-prefix-list bgp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from source-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from destination-address 224.0.0.2/32
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from source-address 10.223.255.176/29
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 172.16.0.0/12 except
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 10.0.0.0/8 except
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
set firewall family inet filter protect_re term ssh from source-prefix-list ssh_addresses
set firewall family inet filter protect_re term snmp from source-prefix-list snmp_addresses_client_list
set firewall family inet filter protect_re term ntp from source-prefix-list ntp_addresses
set firewall family inet filter protect_re term tacacs from source-prefix-list tacacs_addresses
set firewall family inet filter protect_re term bgp from source-prefix-list bgp_addresses
set firewall family inet filter protect_re term critical_app from source-address 0.0.0.0/0
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.2/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.22/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.5/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.6/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
No Description for this Peer configured on Router sorry!
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ssh_pkt_switched_lsys from source-prefix-list ssh_addresses_pkt_switched_lsys
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term snmp_pkt_switched_lsys from source-prefix-list snmp_addresses_client_list_pkt_switched_lsys
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ntp_pkt_switched_lsys from source-prefix-list ntp_addresses_pkt_switched_lsys
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term tacacs_pkt_switched_lsys from source-prefix-list tacacs_addresses_pkt_switched_lsys
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term bgp_pkt_switched_lsys from source-prefix-list bgp_addresses_pkt_switched_lsys
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from source-address 0.0.0.0/0
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from destination-address 224.0.0.2/32
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from source-address 10.223.255.176/29
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 0.0.0.0/0
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 172.16.0.0/12 except
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 10.0.0.0/8 except
No Description for this Peer configured on Router sorry!
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
No Description for this Peer configured on Router sorry!
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
No Description for this Peer configured on Router sorry!
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
No Description for this Peer configured on Router sorry!
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
No Description for this Peer configured on Router sorry!
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
No Description for this Peer configured on Router sorry!
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
No Description for this Peer configured on Router sorry!
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
No Description for this Peer configured on Router sorry!
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
No Description for this Peer configured on Router sorry!
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
No Description for this Peer configured on Router sorry!
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
No Description for this Peer configured on Router sorry!
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
No Description for this Peer configured on Router sorry!
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
No Description for this Peer configured on Router sorry!
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
No Description for this Peer configured on Router sorry!
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
No Description for this Peer configured on Router sorry!
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
No Description for this Peer configured on Router sorry!
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
No Description for this Peer configured on Router sorry!
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
No Description for this Peer configured on Router sorry!
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
No Description for this Peer configured on Router sorry!
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
No Description for this Peer configured on Router sorry!
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
No Description for this Peer configured on Router sorry!
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
No Description for this Peer configured on Router sorry!
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
No Description for this Peer configured on Router sorry!
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
No Description for this Peer configured on Router sorry!
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
No Description for this Peer configured on Router sorry!
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
No Description for this Peer configured on Router sorry!
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
No Description for this Peer configured on Router sorry!
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
No Description for this Peer configured on Router sorry!
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
No Description for this Peer configured on Router sorry!
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
No Description for this Peer configured on Router sorry!
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
No Description for this Peer configured on Router sorry!
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
No Description for this Peer configured on Router sorry!
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
No Description for this Peer configured on Router sorry!
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
No Description for this Peer configured on Router sorry!
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
No Description for this Peer configured on Router sorry!
set firewall family inet filter protect_re term ssh from source-prefix-list ssh_addresses
No Description for this Peer configured on Router sorry!
set firewall family inet filter protect_re term snmp from source-prefix-list snmp_addresses_client_list
No Description for this Peer configured on Router sorry!
set firewall family inet filter protect_re term ntp from source-prefix-list ntp_addresses
No Description for this Peer configured on Router sorry!
set firewall family inet filter protect_re term tacacs from source-prefix-list tacacs_addresses
No Description for this Peer configured on Router sorry!
set firewall family inet filter protect_re term bgp from source-prefix-list bgp_addresses
No Description for this Peer configured on Router sorry!
set firewall family inet filter protect_re term critical_app from source-address 0.0.0.0/0
No Description for this Peer configured on Router sorry!
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.2/32
No Description for this Peer configured on Router sorry!
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.22/32
No Description for this Peer configured on Router sorry!
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.5/32
No Description for this Peer configured on Router sorry!
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.6/32
No Description for this Peer configured on Router sorry!
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ssh_pkt_switched_lsys from source-prefix-list ssh_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term snmp_pkt_switched_lsys from source-prefix-list snmp_addresses_client_list_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ntp_pkt_switched_lsys from source-prefix-list ntp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term tacacs_pkt_switched_lsys from source-prefix-list tacacs_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term bgp_pkt_switched_lsys from source-prefix-list bgp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from source-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from destination-address 224.0.0.2/32
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from source-address 10.223.255.176/29
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 172.16.0.0/12 except
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 10.0.0.0/8 except
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32
set firewall family inet filter protect_re term ssh from source-prefix-list ssh_addresses
set firewall family inet filter protect_re term snmp from source-prefix-list snmp_addresses_client_list
set firewall family inet filter protect_re term ntp from source-prefix-list ntp_addresses
set firewall family inet filter protect_re term tacacs from source-prefix-list tacacs_addresses
set firewall family inet filter protect_re term bgp from source-prefix-list bgp_addresses
set firewall family inet filter protect_re term critical_app from source-address 0.0.0.0/0
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.2/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.22/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.5/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.6/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
No Description for this Peer configured on Router sorry!
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
No Description for this Peer configured on Router sorry!
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
Traceback (most recent call last):
  File "C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py", line 89, in <module>
    bgpdesc(peeripdown)
  File "C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py", line 53, in bgpdesc
    madshow = ssh_conn.send_command_expect(command2)
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\site-packages\netmiko-1.4.2-py3.5.egg\netmiko\base_connection.py", line 819, in send_command_expect
    return self.send_command(*args, **kwargs)
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\site-packages\netmiko-1.4.2-py3.5.egg\netmiko\base_connection.py", line 781, in send_command
    time.sleep(delay_factor * .2)
KeyboardInterrupt
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ssh_pkt_switched_lsys from source-prefix-list ssh_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term snmp_pkt_switched_lsys from source-prefix-list snmp_addresses_client_list_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ntp_pkt_switched_lsys from source-prefix-list ntp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term tacacs_pkt_switched_lsys from source-prefix-list tacacs_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term bgp_pkt_switched_lsys from source-prefix-list bgp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from source-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from destination-address 224.0.0.2/32
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from source-address 10.223.255.176/29
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 172.16.0.0/12 except
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 10.0.0.0/8 except
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
set firewall family inet filter protect_re term ssh from source-prefix-list ssh_addresses
set firewall family inet filter protect_re term snmp from source-prefix-list snmp_addresses_client_list
set firewall family inet filter protect_re term ntp from source-prefix-list ntp_addresses
set firewall family inet filter protect_re term tacacs from source-prefix-list tacacs_addresses
set firewall family inet filter protect_re term bgp from source-prefix-list bgp_addresses
set firewall family inet filter protect_re term critical_app from source-address 0.0.0.0/0
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.2/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.22/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.5/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.6/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ssh_pkt_switched_lsys from source-prefix-list ssh_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term snmp_pkt_switched_lsys from source-prefix-list snmp_addresses_client_list_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ntp_pkt_switched_lsys from source-prefix-list ntp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term tacacs_pkt_switched_lsys from source-prefix-list tacacs_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term bgp_pkt_switched_lsys from source-prefix-list bgp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from source-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from destination-address 224.0.0.2/32
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from source-address 10.223.255.176/29
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 172.16.0.0/12 except
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 10.0.0.0/8 except
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
set firewall family inet filter protect_re term ssh from source-prefix-list ssh_addresses
set firewall family inet filter protect_re term snmp from source-prefix-list snmp_addresses_client_list
set firewall family inet filter protect_re term ntp from source-prefix-list ntp_addresses
set firewall family inet filter protect_re term tacacs from source-prefix-list tacacs_addresses
set firewall family inet filter protect_re term bgp from source-prefix-list bgp_addresses
set firewall family inet filter protect_re term critical_app from source-address 0.0.0.0/0
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.2/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.22/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.5/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.6/32
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ssh_pkt_switched_lsys from source-prefix-list ssh_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term snmp_pkt_switched_lsys from source-prefix-list snmp_addresses_client_list_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ntp_pkt_switched_lsys from source-prefix-list ntp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term tacacs_pkt_switched_lsys from source-prefix-list tacacs_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term bgp_pkt_switched_lsys from source-prefix-list bgp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from source-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from destination-address 224.0.0.2/32
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from source-address 10.223.255.176/29
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 172.16.0.0/12 except
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 10.0.0.0/8 except
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32
set firewall family inet filter protect_re term ssh from source-prefix-list ssh_addresses
set firewall family inet filter protect_re term snmp from source-prefix-list snmp_addresses_client_list
set firewall family inet filter protect_re term ntp from source-prefix-list ntp_addresses
set firewall family inet filter protect_re term tacacs from source-prefix-list tacacs_addresses
set firewall family inet filter protect_re term bgp from source-prefix-list bgp_addresses
set firewall family inet filter protect_re term critical_app from source-address 0.0.0.0/0
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.2/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.22/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.5/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.6/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ssh_pkt_switched_lsys from source-prefix-list ssh_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term snmp_pkt_switched_lsys from source-prefix-list snmp_addresses_client_list_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term ntp_pkt_switched_lsys from source-prefix-list ntp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term tacacs_pkt_switched_lsys from source-prefix-list tacacs_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term bgp_pkt_switched_lsys from source-prefix-list bgp_addresses_pkt_switched_lsys
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from source-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter protect_re_pkt_switched_lsys term critical_app_pkt_switched_lsys from destination-address 224.0.0.2/32
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from source-address 10.223.255.176/29
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 0.0.0.0/0
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 172.16.0.0/12 except
set logical-systems PACKET_SWITCHED firewall family inet filter TESTAPN-CGTNAT-FBF term TEST-APN-SAE1 from destination-address 10.0.0.0/8 except
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32
set firewall family inet filter protect_re term ssh from source-prefix-list ssh_addresses
set firewall family inet filter protect_re term snmp from source-prefix-list snmp_addresses_client_list
set firewall family inet filter protect_re term ntp from source-prefix-list ntp_addresses
set firewall family inet filter protect_re term tacacs from source-prefix-list tacacs_addresses
set firewall family inet filter protect_re term bgp from source-prefix-list bgp_addresses
set firewall family inet filter protect_re term critical_app from source-address 0.0.0.0/0
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.2/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.22/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.5/32
set firewall family inet filter protect_re term critical_app from destination-address 224.0.0.6/32


###############################################################################
Total number of BGP Peerings checked: 296
All Peers that are down:
192.168.214.171/27 -*- 192.168.214.172/27 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- ssh_addresses_pkt_switched_lsys -*- snmp_addresses_client_list_pkt_switched_lsys -*- ntp_addresses_pkt_switched_lsys -*- tacacs_addresses_pkt_switched_lsys -*- bgp_addresses_pkt_switched_lsys -*- 0.0.0.0/0 -*- 224.0.0.2/32 -*- 10.223.255.176/29 -*- 0.0.0.0/0 -*- except -*- except -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*- ssh_addresses -*- snmp_addresses_client_list -*- ntp_addresses -*- tacacs_addresses -*- bgp_addresses -*- 0.0.0.0/0 -*- 224.0.0.2/32 -*- 224.0.0.22/32 -*- 224.0.0.5/32 -*- 224.0.0.6/32 -*- 192.168.214.174/27 -*- 192.168.214.175/27 -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- ssh_addresses_pkt_switched_lsys -*- snmp_addresses_client_list_pkt_switched_lsys -*- ntp_addresses_pkt_switched_lsys -*- tacacs_addresses_pkt_switched_lsys -*- bgp_addresses_pkt_switched_lsys -*- 0.0.0.0/0 -*- 224.0.0.2/32 -*- 10.223.255.176/29 -*- 0.0.0.0/0 -*- except -*- except -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*- ssh_addresses -*- snmp_addresses_client_list -*- ntp_addresses -*- tacacs_addresses -*- bgp_addresses -*- 0.0.0.0/0 -*- 224.0.0.2/32 -*- 224.0.0.22/32 -*- 224.0.0.5/32 -*- 224.0.0.6/32 -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32


###############################################################################
Total number of BGP Peerings checked: 212
All Peers that are down:
192.168.214.171/27 -*- 192.168.214.172/27 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*- 192.168.214.174/27 -*- 192.168.214.175/27 -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*- 
###############################################################################
>>> type peeripdown
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> 
>>> peeripdown
'172.16.5.83/32'
>>> type (peeripdown)
<class 'str'>
>>> 
>>> type (alldownpeer2)
<class 'str'>
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
Traceback (most recent call last):
  File "C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py", line 89, in <module>
    if peeripdown in alldownpeer:
NameError: name 'alldownpeer' is not defined
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
***DUPLICATE***  192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
***DUPLICATE***  192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
***DUPLICATE***  172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
***DUPLICATE***  172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
***DUPLICATE***  10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
***DUPLICATE***  172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
***DUPLICATE***  172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
***DUPLICATE***  172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
***DUPLICATE***  172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
***DUPLICATE***  172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
***DUPLICATE***  172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
***DUPLICATE***  172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
***DUPLICATE***  172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
***DUPLICATE***  172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
***DUPLICATE***  172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
***DUPLICATE***  172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
***DUPLICATE***  172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
***DUPLICATE***  172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
***DUPLICATE***  172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
***DUPLICATE***  172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
***DUPLICATE***  172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
***DUPLICATE***  172.30.197.29/32
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
***DUPLICATE***  172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
***DUPLICATE***  172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
***DUPLICATE***  172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
***DUPLICATE***  172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
***DUPLICATE***  172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
***DUPLICATE***  172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
***DUPLICATE***  172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
***DUPLICATE***  172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
***DUPLICATE***  172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
***DUPLICATE***  172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
***DUPLICATE***  172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
***DUPLICATE***  172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
***DUPLICATE***  172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
***DUPLICATE***  172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
***DUPLICATE***  172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
***DUPLICATE***  172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
***DUPLICATE***  172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
***DUPLICATE***  172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
***DUPLICATE***  172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
***DUPLICATE***  172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
***DUPLICATE***  172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
***DUPLICATE***  172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
***DUPLICATE***  172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
***DUPLICATE***  172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
***DUPLICATE***  172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
***DUPLICATE***  172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
***DUPLICATE***  172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
***DUPLICATE***  172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
***DUPLICATE***  172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
***DUPLICATE***  172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
***DUPLICATE***  172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
***DUPLICATE***  172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
***DUPLICATE***  127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
***DUPLICATE***  172.16.5.82/32
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
***DUPLICATE***  192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
***DUPLICATE***  192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
***DUPLICATE***  172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
***DUPLICATE***  172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
***DUPLICATE***  172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
***DUPLICATE***  172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
***DUPLICATE***  172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
***DUPLICATE***  172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
***DUPLICATE***  172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
***DUPLICATE***  172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
***DUPLICATE***  172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
***DUPLICATE***  172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
***DUPLICATE***  172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
***DUPLICATE***  172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
***DUPLICATE***  172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
***DUPLICATE***  172.30.224.84/32
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
***DUPLICATE***  172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
***DUPLICATE***  172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
***DUPLICATE***  172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
***DUPLICATE***  172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
***DUPLICATE***  172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
***DUPLICATE***  172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
***DUPLICATE***  172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
***DUPLICATE***  172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
***DUPLICATE***  172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
***DUPLICATE***  172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
***DUPLICATE***  172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
***DUPLICATE***  172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
***DUPLICATE***  172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
***DUPLICATE***  172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
***DUPLICATE***  172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
***DUPLICATE***  172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
***DUPLICATE***  172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
***DUPLICATE***  172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
***DUPLICATE***  172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
***DUPLICATE***  172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
***DUPLICATE***  172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
***DUPLICATE***  172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
***DUPLICATE***  172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
***DUPLICATE***  172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
***DUPLICATE***  172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
***DUPLICATE***  172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
***DUPLICATE***  172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
***DUPLICATE***  172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
***DUPLICATE***  172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
***DUPLICATE***  172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
***DUPLICATE***  172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
***DUPLICATE***  172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
***DUPLICATE***  127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32
***DUPLICATE***  172.16.5.83/32


###############################################################################
Total number of BGP Peerings checked: 212
All Peers that are down:
192.168.214.171/27 -*- 192.168.214.172/27 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*- 192.168.214.174/27 -*- 192.168.214.175/27 -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
***DUPLICATE***  127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32


###############################################################################
Total number of BGP Peerings checked: 212
All Peers that are down:
192.168.214.171/27 -*- 192.168.214.172/27 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*- 192.168.214.174/27 -*- 192.168.214.175/27 -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
Output....
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
dn2e9204  ***DUPLICATE***  127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32


###############################################################################
Total number of BGP Peerings checked: 212
All Peers that are down:
192.168.214.171/27 -*- 192.168.214.172/27 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*- 192.168.214.174/27 -*- 192.168.214.175/27 -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Output....
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.171/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.172/27
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30
set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30
set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32
set interfaces ae0 unit 1116 family inet address 172.23.5.169/30
set interfaces ae0 unit 1121 family inet address 172.23.5.189/30
set interfaces ae0 unit 1125 family inet address 172.16.5.185/30
set interfaces ae0 unit 1160 family inet address 172.23.6.17/30
set interfaces ae0 unit 2638 family inet address 172.23.6.145/30
set interfaces ae0 unit 2640 family inet address 172.16.5.89/30
set interfaces ae1 unit 374 family inet address 172.16.5.178/30
set interfaces ae1 unit 860 family inet address 172.23.6.10/30
set interfaces ae3 unit 2445 family inet address 172.23.0.213/30
set interfaces ae3 unit 2460 family inet address 172.23.0.221/30
set interfaces ae3 unit 2462 family inet address 172.23.7.193/30
set interfaces ae3 unit 2464 family inet address 172.23.7.201/30
set interfaces ae3 unit 2466 family inet address 172.23.7.209/30
set interfaces ae3 unit 2468 family inet address 172.23.7.217/30
set interfaces ae3 unit 2470 family inet address 172.23.7.225/30
set interfaces ae3 unit 2472 family inet address 172.23.5.241/30
set interfaces ae4 unit 2555 family inet address 172.16.0.213/30
set interfaces ae4 unit 2560 family inet address 172.23.0.225/30
set interfaces ae4 unit 2562 family inet address 172.23.7.233/30
set interfaces ae4 unit 2564 family inet address 172.23.7.241/30
set interfaces ae4 unit 2566 family inet address 172.23.7.249/30
set interfaces ae4 unit 2568 family inet address 172.23.5.225/30
set interfaces ae4 unit 2570 family inet address 172.23.5.233/30
set interfaces ae4 unit 2572 family inet address 172.23.5.249/30
set interfaces ae6 unit 1124 family inet address 172.23.6.22/30
set interfaces ae6 unit 1125 family inet address 172.16.5.189/30
set interfaces ae6 unit 2636 family inet address 172.23.6.150/30
set interfaces ae6 unit 2640 family inet address 172.16.5.10/30
set interfaces ae7 unit 1117 family inet address 172.23.5.173/30
set interfaces ae7 unit 1122 family inet address 172.23.5.193/30
set interfaces ae17 unit 2605 family inet address 172.23.0.57/30
set interfaces ae18 unit 2705 family inet address 172.16.0.57/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.82/32
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Output....
Peers DOWN
set groups re0 interfaces fxp0 unit 0 family inet address 192.168.214.174/27
set groups re1 interfaces fxp0 unit 0 family inet address 192.168.214.175/27
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.18/30
set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.22/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 801 family inet address 172.23.5.5/30
set logical-systems PACKET_SWITCHED interfaces ae1 unit 803 family inet address 172.23.5.13/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2442 family inet address 172.23.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae3 unit 2443 family inet address 172.23.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2552 family inet address 172.16.0.197/30
set logical-systems PACKET_SWITCHED interfaces ae4 unit 2553 family inet address 172.16.0.133/30
set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.54/28
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2607 family inet address 172.23.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae17 unit 2609 family inet address 172.23.0.53/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2707 family inet address 172.16.0.45/30
set logical-systems PACKET_SWITCHED interfaces ae18 unit 2709 family inet address 172.16.0.53/30
set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.84/32
set interfaces ae0 unit 1116 family inet address 172.23.5.170/30
set interfaces ae0 unit 1121 family inet address 172.23.5.190/30
set interfaces ae0 unit 1125 family inet address 172.16.5.186/30
set interfaces ae0 unit 1160 family inet address 172.23.6.18/30
set interfaces ae0 unit 2638 family inet address 172.23.6.146/30
set interfaces ae0 unit 2640 family inet address 172.16.5.90/30
set interfaces ae1 unit 375 family inet address 172.16.5.182/30
set interfaces ae1 unit 861 family inet address 172.23.6.14/30
set interfaces ae3 unit 2446 family inet address 172.23.0.217/30
set interfaces ae3 unit 2461 family inet address 172.23.0.229/30
set interfaces ae3 unit 2463 family inet address 172.23.7.197/30
set interfaces ae3 unit 2465 family inet address 172.23.7.205/30
set interfaces ae3 unit 2467 family inet address 172.23.7.213/30
set interfaces ae3 unit 2469 family inet address 172.23.7.221/30
set interfaces ae3 unit 2471 family inet address 172.23.7.229/30
set interfaces ae3 unit 2473 family inet address 172.23.5.245/30
set interfaces ae4 unit 2556 family inet address 172.16.0.217/30
set interfaces ae4 unit 2561 family inet address 172.23.0.233/30
set interfaces ae4 unit 2563 family inet address 172.23.7.237/30
set interfaces ae4 unit 2565 family inet address 172.23.7.245/30
set interfaces ae4 unit 2567 family inet address 172.23.7.253/30
set interfaces ae4 unit 2569 family inet address 172.23.5.229/30
set interfaces ae4 unit 2571 family inet address 172.23.5.237/30
set interfaces ae4 unit 2573 family inet address 172.23.5.253/30
set interfaces ae6 unit 1125 family inet address 172.23.6.26/30
set interfaces ae6 unit 1126 family inet address 172.16.5.193/30
set interfaces ae6 unit 2637 family inet address 172.23.6.154/30
set interfaces ae6 unit 2640 family inet address 172.16.5.14/30
set interfaces ae7 unit 1118 family inet address 172.23.5.177/30
set interfaces ae7 unit 1123 family inet address 172.23.5.197/30
set interfaces ae17 unit 2611 family inet address 172.23.0.61/30
set interfaces ae18 unit 2711 family inet address 172.16.0.61/30
set interfaces lo0 unit 0 family inet address 127.0.0.1/32
dn2e9204  ***DUPLICATE***  127.0.0.1/32
set interfaces lo0 unit 145 family inet address 172.16.5.83/32


###############################################################################
Total number of BGP Peerings checked: 212
All Peers that are down:
192.168.214.171/27 -*- 192.168.214.172/27 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*- 192.168.214.174/27 -*- 192.168.214.175/27 -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE***  
dn2e9203  ***DUPLICATE***  
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Checking for Duplicates
dn2e9204  ***DUPLICATE***  
dn2e9204  ***DUPLICATE***  127.0.0.1/32
dn2e9204  ***DUPLICATE***  
dn2e9204  ***DUPLICATE***  {master}


###############################################################################
IP's checked: 112
All Peers that are down:
 -*- 192.168.214.171/27 -*- 192.168.214.172/27 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*-  -*- {master} -*-  -*- 192.168.214.174/27 -*- 192.168.214.175/27 -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*-  -*- {master} -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
Traceback (most recent call last):
  File "C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py", line 83, in <module>
    print (j_rtr," ***DUPLICATE*** ",peeripdown)
NameError: name 'peeripdown' is not defined
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE***  
dn2e9203  ***DUPLICATE***  250
dn2e9203  ***DUPLICATE***  preempt
dn2e9203  ***DUPLICATE***  accept-data
dn2e9203  ***DUPLICATE***  md5
dn2e9203  ***DUPLICATE***  */
dn2e9203  ***DUPLICATE***  250
dn2e9203  ***DUPLICATE***  preempt
dn2e9203  ***DUPLICATE***  accept-data
dn2e9203  ***DUPLICATE***  md5
dn2e9203  ***DUPLICATE***  */
dn2e9203  ***DUPLICATE***  preempt
dn2e9203  ***DUPLICATE***  accept-data
dn2e9203  ***DUPLICATE***  md5
dn2e9203  ***DUPLICATE***  */
dn2e9203  ***DUPLICATE***  172.23.7.1
dn2e9203  ***DUPLICATE***  200
dn2e9203  ***DUPLICATE***  preempt
dn2e9203  ***DUPLICATE***  accept-data
dn2e9203  ***DUPLICATE***  md5
dn2e9203  ***DUPLICATE***  */
dn2e9203  ***DUPLICATE***  150
dn2e9203  ***DUPLICATE***  200
dn2e9203  ***DUPLICATE***  preempt
dn2e9203  ***DUPLICATE***  accept-data
dn2e9203  ***DUPLICATE***  md5
dn2e9203  ***DUPLICATE***  */
dn2e9203  ***DUPLICATE***  200
dn2e9203  ***DUPLICATE***  preempt
dn2e9203  ***DUPLICATE***  accept-data
dn2e9203  ***DUPLICATE***  md5
dn2e9203  ***DUPLICATE***  */
dn2e9203  ***DUPLICATE***  200
dn2e9203  ***DUPLICATE***  preempt
dn2e9203  ***DUPLICATE***  accept-data
dn2e9203  ***DUPLICATE***  md5
dn2e9203  ***DUPLICATE***  */
dn2e9203  ***DUPLICATE***  200
dn2e9203  ***DUPLICATE***  preempt
dn2e9203  ***DUPLICATE***  accept-data
dn2e9203  ***DUPLICATE***  md5
dn2e9203  ***DUPLICATE***  */
dn2e9203  ***DUPLICATE***  150
dn2e9203  ***DUPLICATE***  
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Checking for Duplicates
dn2e9204  ***DUPLICATE***  
dn2e9204  ***DUPLICATE***  172.30.196.27
dn2e9204  ***DUPLICATE***  accept-data
dn2e9204  ***DUPLICATE***  md5
dn2e9204  ***DUPLICATE***  */
dn2e9204  ***DUPLICATE***  172.30.196.155
dn2e9204  ***DUPLICATE***  230
dn2e9204  ***DUPLICATE***  accept-data
dn2e9204  ***DUPLICATE***  md5
dn2e9204  ***DUPLICATE***  */
dn2e9204  ***DUPLICATE***  172.30.196.62
dn2e9204  ***DUPLICATE***  230
dn2e9204  ***DUPLICATE***  accept-data
dn2e9204  ***DUPLICATE***  md5
dn2e9204  ***DUPLICATE***  */
dn2e9204  ***DUPLICATE***  172.16.4.1
dn2e9204  ***DUPLICATE***  150
dn2e9204  ***DUPLICATE***  preempt
dn2e9204  ***DUPLICATE***  accept-data
dn2e9204  ***DUPLICATE***  md5
dn2e9204  ***DUPLICATE***  */
dn2e9204  ***DUPLICATE***  172.23.7.1
dn2e9204  ***DUPLICATE***  150
dn2e9204  ***DUPLICATE***  preempt
dn2e9204  ***DUPLICATE***  accept-data
dn2e9204  ***DUPLICATE***  md5
dn2e9204  ***DUPLICATE***  */
dn2e9204  ***DUPLICATE***  172.23.7.145
dn2e9204  ***DUPLICATE***  150
dn2e9204  ***DUPLICATE***  preempt
dn2e9204  ***DUPLICATE***  accept-data
dn2e9204  ***DUPLICATE***  md5
dn2e9204  ***DUPLICATE***  */
dn2e9204  ***DUPLICATE***  172.16.4.161
dn2e9204  ***DUPLICATE***  150
dn2e9204  ***DUPLICATE***  preempt
dn2e9204  ***DUPLICATE***  accept-data
dn2e9204  ***DUPLICATE***  md5
dn2e9204  ***DUPLICATE***  */
dn2e9204  ***DUPLICATE***  172.23.6.193
dn2e9204  ***DUPLICATE***  150
dn2e9204  ***DUPLICATE***  preempt
dn2e9204  ***DUPLICATE***  accept-data
dn2e9204  ***DUPLICATE***  md5
dn2e9204  ***DUPLICATE***  */
dn2e9204  ***DUPLICATE***  172.23.6.161
dn2e9204  ***DUPLICATE***  150
dn2e9204  ***DUPLICATE***  preempt
dn2e9204  ***DUPLICATE***  accept-data
dn2e9204  ***DUPLICATE***  md5
dn2e9204  ***DUPLICATE***  */
dn2e9204  ***DUPLICATE***  127.0.0.1/32
dn2e9204  ***DUPLICATE***  
dn2e9204  ***DUPLICATE***  {master}


###############################################################################
IP's checked: 220
Set of all IP's checked:
 -*- 192.168.214.171/27 -*- 192.168.214.172/27 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.196.62 -*- 250 -*- preempt -*- accept-data -*- md5 -*- */ -*- 172.30.196.27 -*- 250 -*- preempt -*- accept-data -*- md5 -*- */ -*- 172.30.196.155 -*- 250 -*- preempt -*- accept-data -*- md5 -*- */ -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 172.16.4.1 -*- 200 -*- preempt -*- accept-data -*- md5 -*- */ -*- 100 -*- 172.23.7.1 -*- 200 -*- preempt -*- accept-data -*- md5 -*- */ -*- 150 -*- 172.23.7.145 -*- 200 -*- preempt -*- accept-data -*- md5 -*- */ -*- 172.16.4.161 -*- 200 -*- preempt -*- accept-data -*- md5 -*- */ -*- 172.23.6.193 -*- 200 -*- preempt -*- accept-data -*- md5 -*- */ -*- 172.23.6.161 -*- 200 -*- preempt -*- accept-data -*- md5 -*- */ -*- 150 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*-  -*- {master} -*-  -*- 192.168.214.174/27 -*- 192.168.214.175/27 -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.30.196.27 -*- 230 -*- accept-data -*- md5 -*- */ -*- 172.30.196.155 -*- 230 -*- accept-data -*- md5 -*- */ -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.196.62 -*- 230 -*- accept-data -*- md5 -*- */ -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 172.16.4.1 -*- 150 -*- preempt -*- accept-data -*- md5 -*- */ -*- 172.23.7.1 -*- 150 -*- preempt -*- accept-data -*- md5 -*- */ -*- 172.23.7.145 -*- 150 -*- preempt -*- accept-data -*- md5 -*- */ -*- 172.16.4.161 -*- 150 -*- preempt -*- accept-data -*- md5 -*- */ -*- 172.23.6.193 -*- 150 -*- preempt -*- accept-data -*- md5 -*- */ -*- 172.23.6.161 -*- 150 -*- preempt -*- accept-data -*- md5 -*- */ -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*-  -*- {master} -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE***  
dn2e9203  ***DUPLICATE***  
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Checking for Duplicates
dn2e9204  ***DUPLICATE***  
dn2e9204  ***DUPLICATE***  127.0.0.1/32
dn2e9204  ***DUPLICATE***  
dn2e9204  ***DUPLICATE***  {master}


###############################################################################
IP's checked: 112
Set of all IP's checked:
 -*- 192.168.214.171/27 -*- 192.168.214.172/27 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*-  -*- {master} -*-  -*- 192.168.214.174/27 -*- 192.168.214.175/27 -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*-  -*- {master} -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE***  
dn2e9203  ***DUPLICATE***  
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Checking for Duplicates
dn2e9204  ***DUPLICATE***  
dn2e9204  ***DUPLICATE***  127.0.0.1/32
dn2e9204  ***DUPLICATE***  
dn2e9204  ***DUPLICATE***  {master}


###############################################################################
IP's checked: 108
Set of all IP's checked:
 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*-  -*- {master} -*-  -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*-  -*- {master} -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE***  
Derived from:  
dn2e9203  ***DUPLICATE***  
Derived from:  
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Checking for Duplicates
dn2e9204  ***DUPLICATE***  
Derived from:  
dn2e9204  ***DUPLICATE***  127.0.0.1/32
Derived from:  set interfaces lo0 unit 0 family inet address 127.0.0.1/32
dn2e9204  ***DUPLICATE***  
Derived from:  
dn2e9204  ***DUPLICATE***  {master}
Derived from:  {master}


###############################################################################
IP's checked: 108
Set of all IP's checked:
 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*-  -*- {master} -*-  -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*-  -*- {master} -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE***  2
Derived from:  2
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Checking for Duplicates
dn2e9204  ***DUPLICATE***  

Derived from:  



###############################################################################
IP's checked: 10
Set of all IP's checked:
d -*- n -*- 2 -*- e -*- 9 -*- 2 -*- 0 -*- 4 -*- 
 -*- 
 -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE***  
Derived from:  
dn2e9203  ***DUPLICATE***  
Derived from:  
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Checking for Duplicates
dn2e9204  ***DUPLICATE***  
Derived from:  
dn2e9204  ***DUPLICATE***  127.0.0.1/32
Derived from:  set interfaces lo0 unit 0 family inet address 127.0.0.1/32
dn2e9204  ***DUPLICATE***  
Derived from:  
dn2e9204  ***DUPLICATE***  {master}
Derived from:  {master}


###############################################################################
IP's checked: 108
Set of all IP's checked:
 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*-  -*- {master} -*-  -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*-  -*- {master} -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Traceback (most recent call last):
  File "C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py", line 73, in <module>
    lineoutput = lineoutput.replace('/n','')
AttributeError: 'list' object has no attribute 'replace'
>>> 
>>> type (lineoutput)
<class 'list'>
>>> lineoutput
['', 'set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1114 family inet address 172.23.5.161/30', 'set logical-systems PACKET_SWITCHED interfaces ge-2/0/7 unit 1115 family inet address 172.23.5.165/30', 'set logical-systems PACKET_SWITCHED interfaces gr-2/1/0 unit 0 family inet address 10.0.0.22/24', 'set logical-systems PACKET_SWITCHED interfaces ae0 unit 1304 family inet address 172.23.5.17/30', 'set logical-systems PACKET_SWITCHED interfaces ae0 unit 1305 family inet address 172.23.5.21/30', 'set logical-systems PACKET_SWITCHED interfaces ae1 unit 800 family inet address 172.23.5.1/30', 'set logical-systems PACKET_SWITCHED interfaces ae1 unit 802 family inet address 172.23.5.9/30', 'set logical-systems PACKET_SWITCHED interfaces ae1 unit 806 family inet address 172.23.5.154/30', 'set logical-systems PACKET_SWITCHED interfaces ae3 unit 2440 family inet address 172.23.0.193/30', 'set logical-systems PACKET_SWITCHED interfaces ae3 unit 2441 family inet address 172.23.0.129/30', 'set logical-systems PACKET_SWITCHED interfaces ae3 unit 2444 family inet address 172.23.0.201/30', 'set logical-systems PACKET_SWITCHED interfaces ae4 unit 2550 family inet address 172.16.0.193/30', 'set logical-systems PACKET_SWITCHED interfaces ae4 unit 2551 family inet address 172.16.0.129/30', 'set logical-systems PACKET_SWITCHED interfaces ae12 unit 0 family inet address 172.30.199.53/28', 'set logical-systems PACKET_SWITCHED interfaces ae17 unit 2601 family inet address 172.23.0.41/30', 'set logical-systems PACKET_SWITCHED interfaces ae17 unit 2603 family inet address 172.23.0.49/30', 'set logical-systems PACKET_SWITCHED interfaces ae18 unit 2701 family inet address 172.16.0.41/30', 'set logical-systems PACKET_SWITCHED interfaces ae18 unit 2703 family inet address 172.16.0.49/30', 'set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.224.83/32', 'set logical-systems PACKET_SWITCHED interfaces lo0 unit 1 family inet address 172.30.197.29/32', 'set interfaces ae0 unit 1116 family inet address 172.23.5.169/30', 'set interfaces ae0 unit 1121 family inet address 172.23.5.189/30', 'set interfaces ae0 unit 1125 family inet address 172.16.5.185/30', 'set interfaces ae0 unit 1160 family inet address 172.23.6.17/30', 'set interfaces ae0 unit 2638 family inet address 172.23.6.145/30', 'set interfaces ae0 unit 2640 family inet address 172.16.5.89/30', 'set interfaces ae1 unit 374 family inet address 172.16.5.178/30', 'set interfaces ae1 unit 860 family inet address 172.23.6.10/30', 'set interfaces ae3 unit 2445 family inet address 172.23.0.213/30', 'set interfaces ae3 unit 2460 family inet address 172.23.0.221/30', 'set interfaces ae3 unit 2462 family inet address 172.23.7.193/30', 'set interfaces ae3 unit 2464 family inet address 172.23.7.201/30', 'set interfaces ae3 unit 2466 family inet address 172.23.7.209/30', 'set interfaces ae3 unit 2468 family inet address 172.23.7.217/30', 'set interfaces ae3 unit 2470 family inet address 172.23.7.225/30', 'set interfaces ae3 unit 2472 family inet address 172.23.5.241/30', 'set interfaces ae4 unit 2555 family inet address 172.16.0.213/30', 'set interfaces ae4 unit 2560 family inet address 172.23.0.225/30', 'set interfaces ae4 unit 2562 family inet address 172.23.7.233/30', 'set interfaces ae4 unit 2564 family inet address 172.23.7.241/30', 'set interfaces ae4 unit 2566 family inet address 172.23.7.249/30', 'set interfaces ae4 unit 2568 family inet address 172.23.5.225/30', 'set interfaces ae4 unit 2570 family inet address 172.23.5.233/30', 'set interfaces ae4 unit 2572 family inet address 172.23.5.249/30', 'set interfaces ae6 unit 1124 family inet address 172.23.6.22/30', 'set interfaces ae6 unit 1125 family inet address 172.16.5.189/30', 'set interfaces ae6 unit 2636 family inet address 172.23.6.150/30', 'set interfaces ae6 unit 2640 family inet address 172.16.5.10/30', 'set interfaces ae7 unit 1117 family inet address 172.23.5.173/30', 'set interfaces ae7 unit 1122 family inet address 172.23.5.193/30', 'set interfaces ae17 unit 2605 family inet address 172.23.0.57/30', 'set interfaces ae18 unit 2705 family inet address 172.16.0.57/30', 'set interfaces lo0 unit 0 family inet address 127.0.0.1/32', 'set interfaces lo0 unit 145 family inet address 172.16.5.82/32', '', '{master}']
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE***  
Derived from:  
dn2e9203  ***DUPLICATE***  
Derived from:  
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Checking for Duplicates
dn2e9204  ***DUPLICATE***  
Derived from:  
dn2e9204  ***DUPLICATE***  127.0.0.1/32
Derived from:  set interfaces lo0 unit 0 family inet address 127.0.0.1/32
dn2e9204  ***DUPLICATE***  
Derived from:  
dn2e9204  ***DUPLICATE***  {master}
Derived from:  {master}


###############################################################################
IP's checked: 108
Set of all IP's checked:
 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*-  -*- {master} -*-  -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*-  -*- {master} -*- 
###############################################################################
>>> -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*-  -*- {master} -*-  -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*-  -*- {master} -*-
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> type (line)
<class 'str'>
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE***  
dn2e9203  ***DUPLICATE***  
dn2e9203  ***DUPLICATE***  
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Checking for Duplicates
dn2e9204  ***DUPLICATE***  
dn2e9204  ***DUPLICATE***  127.0.0.1/32
dn2e9204  ***DUPLICATE***  
dn2e9204  ***DUPLICATE***  


###############################################################################
IP's checked: 108
Set of all IP's checked:
 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*-  -*-  -*-  -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*-  -*-  -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE***#  #
dn2e9203  ***DUPLICATE***#  #
dn2e9203  ***DUPLICATE***#  #
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Checking for Duplicates
dn2e9204  ***DUPLICATE***#  #
dn2e9204  ***DUPLICATE***# 127.0.0.1/32 #
dn2e9204  ***DUPLICATE***#  #
dn2e9204  ***DUPLICATE***#  #


###############################################################################
IP's checked: 108
Set of all IP's checked:
 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*-  -*-  -*-  -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*-  -*-  -*- 
###############################################################################
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE*** 
Traceback (most recent call last):
  File "C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py", line 91, in <module>
    alldups += prefix + (",")
NameError: name 'alldups' is not defined
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Traceback (most recent call last):
  File "C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py", line 16, in <module>
    alldups-""
NameError: name 'alldups' is not defined
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
All Juniper Switches/Routers:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
Checking for Duplicates
dn2e9203  ***DUPLICATE*** 
dn2e9203  ***DUPLICATE*** 
dn2e9203  ***DUPLICATE*** 
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
Checking for Duplicates
dn2e9204  ***DUPLICATE*** 
dn2e9204  ***DUPLICATE*** 127.0.0.1/32
dn2e9204  ***DUPLICATE*** 
dn2e9204  ***DUPLICATE*** 


###############################################################################
IP's checked: 108
Set of all IP's checked:
 -*- 172.23.5.161/30 -*- 172.23.5.165/30 -*- 10.0.0.22/24 -*- 172.23.5.17/30 -*- 172.23.5.21/30 -*- 172.23.5.1/30 -*- 172.23.5.9/30 -*- 172.23.5.154/30 -*- 172.23.0.193/30 -*- 172.23.0.129/30 -*- 172.23.0.201/30 -*- 172.16.0.193/30 -*- 172.16.0.129/30 -*- 172.30.199.53/28 -*- 172.23.0.41/30 -*- 172.23.0.49/30 -*- 172.16.0.41/30 -*- 172.16.0.49/30 -*- 172.30.224.83/32 -*- 172.30.197.29/32 -*- 172.23.5.169/30 -*- 172.23.5.189/30 -*- 172.16.5.185/30 -*- 172.23.6.17/30 -*- 172.23.6.145/30 -*- 172.16.5.89/30 -*- 172.16.5.178/30 -*- 172.23.6.10/30 -*- 172.23.0.213/30 -*- 172.23.0.221/30 -*- 172.23.7.193/30 -*- 172.23.7.201/30 -*- 172.23.7.209/30 -*- 172.23.7.217/30 -*- 172.23.7.225/30 -*- 172.23.5.241/30 -*- 172.16.0.213/30 -*- 172.23.0.225/30 -*- 172.23.7.233/30 -*- 172.23.7.241/30 -*- 172.23.7.249/30 -*- 172.23.5.225/30 -*- 172.23.5.233/30 -*- 172.23.5.249/30 -*- 172.23.6.22/30 -*- 172.16.5.189/30 -*- 172.23.6.150/30 -*- 172.16.5.10/30 -*- 172.23.5.173/30 -*- 172.23.5.193/30 -*- 172.23.0.57/30 -*- 172.16.0.57/30 -*- 127.0.0.1/32 -*- 172.16.5.82/32 -*-  -*-  -*-  -*- 172.23.5.18/30 -*- 172.23.5.22/30 -*- 172.23.5.5/30 -*- 172.23.5.13/30 -*- 172.23.0.197/30 -*- 172.23.0.133/30 -*- 172.16.0.197/30 -*- 172.16.0.133/30 -*- 172.30.199.54/28 -*- 172.23.0.45/30 -*- 172.23.0.53/30 -*- 172.16.0.45/30 -*- 172.16.0.53/30 -*- 172.30.224.84/32 -*- 172.23.5.170/30 -*- 172.23.5.190/30 -*- 172.16.5.186/30 -*- 172.23.6.18/30 -*- 172.23.6.146/30 -*- 172.16.5.90/30 -*- 172.16.5.182/30 -*- 172.23.6.14/30 -*- 172.23.0.217/30 -*- 172.23.0.229/30 -*- 172.23.7.197/30 -*- 172.23.7.205/30 -*- 172.23.7.213/30 -*- 172.23.7.221/30 -*- 172.23.7.229/30 -*- 172.23.5.245/30 -*- 172.16.0.217/30 -*- 172.23.0.233/30 -*- 172.23.7.237/30 -*- 172.23.7.245/30 -*- 172.23.7.253/30 -*- 172.23.5.229/30 -*- 172.23.5.237/30 -*- 172.23.5.253/30 -*- 172.23.6.26/30 -*- 172.16.5.193/30 -*- 172.23.6.154/30 -*- 172.16.5.14/30 -*- 172.23.5.177/30 -*- 172.23.5.197/30 -*- 172.23.0.61/30 -*- 172.16.0.61/30 -*- 127.0.0.1/32 -*- 172.16.5.83/32 -*-  -*-  -*- 
###############################################################################
All Duplicates:
,,,,127.0.0.1/32,,,
>>> 
 RESTART: C:/Users/MBatters/AppData/Local/Programs/Python/Python35-32/dup-ip-v01.py 
Username: mbatters

Warning (from warnings module):
  File "C:\Users\MBatters\AppData\Local\Programs\Python\Python35-32\lib\getpass.py", line 101
    return fallback_getpass(prompt, stream)
GetPassWarning: Can not control echo on the terminal.
Warning: Password input may be echoed.
Password: Welcome123
Here we go:
###############################################################################
Connecting to: dn2e9203
JUNIPER
Connected to: dn2e9203
dn2e9203  ***DUPLICATE*** 
dn2e9203  ***DUPLICATE*** 
dn2e9203  ***DUPLICATE*** 
###############################################################################
Connecting to: dn2e9204
JUNIPER
Connected to: dn2e9204
dn2e9204  ***DUPLICATE*** 
dn2e9204  ***DUPLICATE*** 127.0.0.1/32
dn2e9204  ***DUPLICATE*** 
dn2e9204  ***DUPLICATE*** 
###############################################################################
IP's checked: 108
###############################################################################
All Duplicates:
,,,,127.0.0.1/32,,,
>>> 
