import csv
import os
import requests
URL = "https://api.apify.com/v2/acts/talcoe~us-government-bids-rfps/run-sync-get-dataset-items"
query = {
    "keywords": ["janitorial", "custodial"],
    "states": ["NY", "NJ"],
    "postedWithinDays": 14,
    "maxResults": 100,
}
resp = requests.post(URL, json=query, headers={"Authorization": f"Bearer {os.environ['APIFY_TOKEN']}"}, timeout=600)
resp.raise_for_status()
bids = sorted(resp.json(), key=lambda b: b.get("dueDate") or "")
with open("bids.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["due", "state", "agency", "title", "url"])
    for b in bids:
        w.writerow([(b.get("dueDate") or "")[:10], b.get("state"), b.get("agency"), b.get("title"), b.get("url")])
print(f"{len(bids)} bids saved to bids.csv")
