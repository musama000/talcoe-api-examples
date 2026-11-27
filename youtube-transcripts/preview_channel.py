"""List a channel's videos without transcripts (listOnly). Each listed video is one billed record."""
import os, requests
API = "https://api.apify.com/v2/acts/talcoe~youtube-transcripts/run-sync-get-dataset-items"
headers = {"Authorization": f"Bearer {os.environ['APIFY_TOKEN']}"}
body = {"sources": ["@Fireship"], "maxVideosPerSource": 10, "listOnly": True}
resp = requests.post(API, headers=headers, json=body, timeout=300)
resp.raise_for_status()
videos = resp.json()
for v in videos:
    print(v["publishDate"], v["durationSeconds"], v["videoId"], v["title"])
print(len(videos), "videos listed")
