"""Every recent transcript from one YouTube channel, saved as one Markdown file and one SRT file per video.

Needs APIFY_TOKEN in the environment and `pip install requests`.
"""
import os, re, pathlib, requests
API = "https://api.apify.com/v2/acts/talcoe~youtube-transcripts/run-sync-get-dataset-items"
headers = {"Authorization": f"Bearer {os.environ['APIFY_TOKEN']}"}
body = {
    "sources": ["@Fireship"],
    "maxVideosPerSource": 5,
    "publishedAfter": "2026-11-01",
    "formats": ["text", "srt"],
    "language": "en",
}
resp = requests.post(API, headers=headers, json=body, timeout=300)
resp.raise_for_status()
items = resp.json()
out = pathlib.Path("fireship")
out.mkdir(exist_ok=True)
for v in items:
    slug = re.sub(r"[^a-z0-9]+", "-", v["title"].lower()).strip("-")[:60]
    page = f"# {v['title']}\n\nDate: {v['publishDate']}\nURL: {v['url']}\nWords: {v['wordCount']}\n\n{v['transcript']}\n"
    (out / f"{v['publishDate']}-{slug}.md").write_text(page, encoding="utf-8")
    print(v["publishDate"], v["videoId"], v["wordCount"], v["title"])
for v in items:
    (out / f"{v['videoId']}.srt").write_text(v["srt"], encoding="utf-8")
