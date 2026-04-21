import requests

def get_manufacturer(mac):
    
    try:
        # 1. extract the OUI (first 6 characters of MAC)
        oui = mac.replace(":", "")[:6].upper()
        
        # 2. call the free MAC lookup API
        url = f"https://api.maclookup.app/v2/macs/{oui}"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        # 3. return manufacturer name or Unknown
        if data.get("found"):
            return data.get("company", "Unknown")
        else:
            return "Unknown"
    
    # 4. if anything goes wrong return Unknown
    except:
        return "Unknown"
    

