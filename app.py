from scanner import scan
from lookup import get_manufacturer

def get_all_devices(network_range):
    
    # 1. scan the network
    devices = scan(network_range)
    
    # 2. for each device look up the manufacturer
    for device in devices:
        manufacturer = get_manufacturer(device["mac"])
        device["manufacturer"] = manufacturer
        
        # 3. flag unknown devices
        if manufacturer == "Unknown":
            device["status"] = "suspicious"
        else:
            device["status"] = "known"
    
    return devices

if __name__ == "__main__":
    #put your network range exemple: network_range = "192.168.1.0/24"
    network_range = ""
    devices = get_all_devices(network_range)
    
    print(f"\n[+] Found {len(devices)} devices\n")
    for device in devices:
        flag = "WARNING" if device["status"] == "suspicious" else "OK"
        print(f"[{flag}] IP: {device['ip']}  |  MAC: {device['mac']}  |  {device['manufacturer']}")
