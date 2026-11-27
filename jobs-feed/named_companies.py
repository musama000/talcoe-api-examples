"""Read only the boards of the companies you name."""
import collections
import os
import requests

url = "https://api.apify.com/v2/acts/talcoe~ats-careers-multi/run-sync-get-dataset-items"
headers = {"Authorization": "Bearer " + os.environ["APIFY_TOKEN"]}
body = dict(companies=["Stripe", "Plaid"], searchQueries=["data engineer"], maxResults=20)
jobs = requests.post(url, headers=headers, json=body, timeout=300).json()
print(collections.Counter(job["company"] for job in jobs).most_common())
for job in jobs[:4]:
    print(job["company"], "|", job["ats"], "|", job["title"], "|", job["location"], "|", job["postedAt"][:10])
