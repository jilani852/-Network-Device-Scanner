from scapy.all import ARP,Ether,srp

def scan (network_range):

    # 1.create an ARP request packet 
    arp_request = ARP(pdst=network_range)

    # 2.create an Ethernet broacast frame
    brodcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    # 3. combine them together
    packet = brodcast / arp_request

    # 4. send the packet and capture responses
    answerd,unanswered  = srp(packet,timeout=2,verbose=False)

    # 5.extract IP and MAC from responses
    devices = []
    for sent,received in answerd:
        devices.append({
            "ip" : received.psrc,
            "mac" : received.hwsrc
        })
    
    return devices

if __name__ == "__main__":
    network_range = "192.168.1.0/24"
    devices = scan(network_range)
    
    print(f"[+] Found {len(devices)} devices\n")
    for device in devices:
        print(f"IP: {device['ip']}  |  MAC: {device['mac']}")