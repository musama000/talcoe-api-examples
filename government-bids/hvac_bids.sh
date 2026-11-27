#!/usr/bin/env bash
# Open HVAC bids in Texas and Florida from SAM.gov and both state portals, as JSON.
# Needs APIFY_TOKEN in the environment.
curl -s -X POST "https://api.apify.com/v2/acts/talcoe~us-government-bids-rfps/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["hvac"], "states": ["TX", "FL"], "sources": ["sam", "texas", "florida"], "postedWithinDays": 14, "maxResults": 25}'
