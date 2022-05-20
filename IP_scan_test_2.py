#!/usr/bin/env python3

# ///////////////////////////////////////////////////////////////
#
# BY: TANATORN PRAVALPADD ,CHANAPAI CHUADCHUM
# V: 1.0.0
#
# ///////////////////////////////////////////////////////////////


# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////

import scapy.all as scapy
import socket
import sys

# HOST SCANNER
# ///////////////////////////////////////////////////////////////

print("run host_scanner_thread")
ip = socket.gethostbyname(
    socket.gethostname()).rsplit('.', 1)[0]+".1/24"
arp_req_frame = scapy.ARP(pdst=ip)
broadcast_ether_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame
answered_list = scapy.srp(
    broadcast_ether_arp_req_frame, timeout=1, verbose=False)[0]
for i in range(0, len(answered_list)):
    client_ip = str(answered_list[i][1].psrc)
    client_mac = str(answered_list[i][1].hwsrc)
    try:
        client_host = str(socket.gethostbyaddr(
            client_ip)).rsplit("'", 3)[0].rsplit("'", 1)[1]
    except:
        client_host = " - "

    print("ip: " + client_ip +"  mac: " + client_mac +"  host: " + client_host)