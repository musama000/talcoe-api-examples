#!/usr/bin/env bash
# The same search saved as hvac_bids.csv with five columns.
# Needs APIFY_TOKEN in the environment.
curl -s -X POST "https://api.apify.com/v2/acts/talcoe~us-government-bids-rfps/run-sync-get-dataset-items?format=csv&fields=title,agency,state,dueDate,url" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["hvac"], "states": ["TX", "FL"], "sources": ["sam", "texas", "florida"], "postedWithinDays": 14, "maxResults": 25}' \
  -o hvac_bids.csv
