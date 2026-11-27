"""Feed mode: each run appends only jobs it has not returned before to jobs.csv. Schedule it daily."""
import csv
import os
import requests

URL = "https://api.apify.com/v2/acts/talcoe~ats-careers-multi/run-sync-get-dataset-items"
HEADERS = {"Authorization": "Bearer " + os.environ["APIFY_TOKEN"]}
BODY = dict(searchQueries=["site reliability engineer"], remoteOnly=True, postedWithinDays=30, newSinceLastRun=True, maxResults=200)
FIELDS = ["postedAt", "company", "title", "location", "salaryMin", "salaryMax", "applyUrl"]
jobs = requests.post(URL, headers=HEADERS, json=BODY, timeout=300).json()
new_file = not os.path.exists("jobs.csv")
with open("jobs.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
    new_file and writer.writeheader()
    writer.writerows(jobs)
print("new jobs this run:", len(jobs))
