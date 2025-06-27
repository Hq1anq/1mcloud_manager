import requests, time, json, pyperclip, os
from dotenv import load_dotenv

load_dotenv()

headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,vi;q=0.8",
        "authorization": f"Bearer {os.getenv("API_KEY")}",
        "content-type": "application/json",
        "origin": "https://manage.1mcloud.vn",
        "referer": "https://manage.1mcloud.vn/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    }

def get_data_from_ip():
    url = "https://api.smartserver.vn/api/server/list"

    ips_text = pyperclip.paste()
    
    # Convert to comma-separated string
    ip_list = [ip.strip() for ip in ips_text.strip().splitlines() if ip.strip()]
    ip_string = ",".join(ip_list)
    params = {
        "page": 1,
        "limit": 200,
        "by_status": "",
        "by_time": "using",
        "by_created": "",
        "keyword": "",
        "ips": ip_string,
        "proxy": "true"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        raw_data: dict = response.json()
        servers: list[dict] = raw_data.get("servers", [])
        
        filtered_servers = []
        for server in servers:
            filtered = {
                "server_id": server.get("server_id"),
                "ip_port": server.get("ip_port"),
                "country": server.get("country"),
                "plan_number": server.get("plan_number"),
                "ngay_mua": server.get("ngay_mua"),
                "het_han": server.get("het_han"),
                "changed_ip": server.get("change_ip_time"),
                "trang_thai": server.get("trang_thai"),
                "note": server.get("note")
            }
            filtered_servers.append(filtered)

        result = {"servers": filtered_servers}

        # 💾 Save to JSON file
        with open("servers_filtered.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

        print("✅ Data saved to servers_filtered.json")
    else:
        print("❌ Request failed:", response.status_code)

def change_note(note: str):
    url = "https://api.smartserver.vn/api/server/info/note"
    
    sid_text = pyperclip.paste()
    
    sid_list = [sid.strip() for sid in sid_text.strip().splitlines() if sid.strip()]
    
    data_list = [
        {"sid": sid, "note": note} for sid in sid_list
    ]
    
    for data in data_list:
        response = requests.put(url, headers=headers, json=data)
        print(f"Sent for {data['sid']} -> {response.status_code}")
        time.sleep(0.5)  # optional: delay to avoid hitting rate limits

# get_data_from_ip()
change_note("1107 hue2-chung2")