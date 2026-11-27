"""Run asynchronously, then read which videos had no captions in your language (NO_TRANSCRIPT)."""
import os, requests
BASE = "https://api.apify.com/v2"
headers = {"Authorization": f"Bearer {os.environ['APIFY_TOKEN']}"}
body = {
    "sources": ["Jatwf_XOncE", "NFvDHYMzj9U"],
    "language": "en",
    "fallbackToAnyLanguage": False,
    "formats": ["text"],
}
run = requests.post(
    f"{BASE}/acts/talcoe~youtube-transcripts/runs",
    params={"waitForFinish": 120},
    headers=headers,
    json=body,
    timeout=180,
).json()["data"]
print("run status:", run["status"])
rows = requests.get(f"{BASE}/datasets/{run['defaultDatasetId']}/items", headers=headers).json()
print("transcripts returned:", [r["videoId"] for r in rows])
store = run["defaultKeyValueStoreId"]
resp = requests.get(f"{BASE}/key-value-stores/{store}/records/NO_TRANSCRIPT", headers=headers)
for row in resp.json():
    print("skipped:", row["videoId"], row["reason"])
