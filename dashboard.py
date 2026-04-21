from flask import Flask
from app import get_all_devices

app = Flask(__name__)
#put your network range exemple: NETWORK_RANGE = "192.168.1.0/24"
NETWORK_RANGE = ""

@app.route("/")
def dashboard():
    
    # 1. get all devices
    devices = get_all_devices(NETWORK_RANGE)
    
    # 2. count known and suspicious devices
    total       = len(devices)
    known       = len([d for d in devices if d["status"] == "known"])
    suspicious  = len([d for d in devices if d["status"] == "suspicious"])
    
    # 3. build table rows
    rows = ""
    for device in devices:
        color = "#2ecc71" if device["status"] == "known" else "#e74c3c"
        label = "Known"   if device["status"] == "known" else "⚠ Suspicious"
        rows += f"""
        <tr>
            <td>{device["ip"]}</td>
            <td>{device["mac"]}</td>
            <td>{device["manufacturer"]}</td>
            <td style="color:{color}; font-weight:bold;">{label}</td>
        </tr>
        """
    
    # 4. return the full dashboard page
    return f"""
    <html>
    <head>
        <title>Network Scanner Dashboard</title>
        <style>
            body      {{ font-family: Arial; margin: 40px; background: #1a1a2e; color: white; }}
            h1        {{ color: #00d4ff; }}
            .stats    {{ display: flex; gap: 20px; margin: 20px 0; }}
            .card     {{ padding: 20px 40px; border-radius: 8px; text-align: center; }}
            .card h2  {{ margin: 0; font-size: 36px; }}
            .card p   {{ margin: 5px 0 0; }}
            .total    {{ background: #16213e; }}
            .known    {{ background: #1a472a; }}
            .danger   {{ background: #7b1c1c; }}
            table     {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th        {{ background: #16213e; padding: 12px; text-align: left; color: #00d4ff; }}
            td        {{ padding: 12px; border-bottom: 1px solid #333; }}
            tr:hover  {{ background: #16213e; }}
            .refresh  {{ margin-top: 20px; padding: 10px 24px; background: #00d4ff; 
                         color: #1a1a2e; border: none; border-radius: 6px; 
                         cursor: pointer; font-size: 15px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>Network Scanner Dashboard</h1>
        <p style="color:#aaa;">Network range: {NETWORK_RANGE}</p>

        <div class="stats">
            <div class="card total">
                <h2>{total}</h2>
                <p>Total Devices</p>
            </div>
            <div class="card known">
                <h2>{known}</h2>
                <p>Known Devices</p>
            </div>
            <div class="card danger">
                <h2>{suspicious}</h2>
                <p>Suspicious Devices</p>
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>IP Address</th>
                    <th>MAC Address</th>
                    <th>Manufacturer</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>

        <button class="refresh" onclick="location.reload()">Refresh Scan</button>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
