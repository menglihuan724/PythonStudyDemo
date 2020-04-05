import scapy
from scapy.arch import show_interfaces, IFACES
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp

iface = list(IFACES.data.values())[1]
p = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst='192.168.0.106/24')
ans = srp(p, timeout=4, iface=iface)[0]
for snd, rcv in ans:
    mac = rcv.hwsrc
    print(mac)
