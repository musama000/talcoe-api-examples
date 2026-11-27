#!/usr/bin/env bash
# Instant search over the nightly index of open bids (Government Bids Search API).
# Needs APIFY_TOKEN in the environment.
curl -s -H "Authorization: Bearer $APIFY_TOKEN" \
  "https://talcoe--government-bids-search-api.apify.actor/search?q=hvac&state=TX&limit=3"
