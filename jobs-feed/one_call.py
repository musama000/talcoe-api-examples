"""Remote data engineer jobs from every system in one call, printed one line per job.

Needs APIFY_TOKEN in the environment and `pip install requests`.
"""
import os
import requests

url = "https://api.apify.com/v2/acts/talcoe~ats-careers-multi/run-sync-get-dataset-items"
headers = {"Authorization": "Bearer " + os.environ["APIFY_TOKEN"]}
body = dict(searchQueries=["data engineer"], remoteOnly=True, postedWithinDays=14, maxResults=10)
jobs = requests.post(url, headers=headers, json=body, timeout=300).json()
print(len(jobs), "jobs")
for job in jobs[:10]:
    print(job["ats"], "|", job["company"], "|", job["title"], "|", job["matchScore"], "|", job["seniority"], "|", job["salaryMin"], job["salaryMax"], job["salaryCurrency"])
