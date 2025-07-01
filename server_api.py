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

def get_data_from_ip(ips: str, save: bool = True) -> list:
    url = "https://api.smartserver.vn/api/server/list"
    
    # Convert to comma-separated string
    ip_list = [ip.strip() for ip in ips.strip().splitlines() if ip.strip()]
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
        
        data = []
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
            data.append(filtered)

        if save:
            # 💾 Save to JSON file
            with open("data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("✅ Data saved to data.json")
        return data
    else:
        print("❌ Request failed:", response.status_code)
        return None
    
def change_note(sid: str, note: str) -> int:
    url = "https://api.smartserver.vn/api/server/info/note"
    
    response = requests.put(url, headers=headers, json={"sid": sid, "note": note})
    print(f"{sid} '{note}' -> {response.status_code}")
    return response.status_code

def change_notes(sids: str, note: str):
    url = "https://api.smartserver.vn/api/server/info/note"
    
    sid_list = [sid.strip() for sid in sids.strip().splitlines() if sid.strip()]
    
    data_list = [
        {"sid": sid, "note": note} for sid in sid_list
    ]
    
    for data in data_list:
        response = requests.put(url, headers=headers, json=data)
        print(f"Sent for {data['sid']} -> {response.status_code}")
        time.sleep(0.5)  # optional: delay to avoid hitting rate limits
    
def reinstall(sid: str, custom_info: str = None, type: str = "proxy_https") -> str:
    url = "https://api.smartserver.vn/api/server/reinstall"

    list_info = custom_info.split(":")
    if custom_info is not None:
        data =  {
            "random_remote_port": "",
            "remote_port": list_info[1],
            "random_username": "",
            "username": list_info[2],
            "random_password": "",
            "password": list_info[3],
            "type": type,
            "sid": sid
        }
    else:
        data =  {
            "random_remote_port": "on",
            "remote_port": "",
            "random_username": "on",
            "username": "",
            "random_password": "on",
            "password": "",
            "type": type,
            "sid": sid
        }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        raw_data = response.json()
        print(raw_data)
        proxy_info = f"{raw_data['ip']}:{raw_data['remote_port']}:{raw_data['username']}:{raw_data['password']}"
        print(proxy_info)
        return proxy_info
    else:
        print(f"❌{data['sid']}")
        return None

if __name__ == "__main__":
    pass
    # reinstall(sid = "564340", custom_info="103.16.224.43:46287:yzjo1765:YFXfjw7609")
    # ips = pyperclip.paste()
    # get_data_from_ip(ips)
    # change_notes(ips, "2906 tung1-chung2")
    # change_note("563352", "1307 huy2 chung2")