# Talcoe data API examples

Runnable examples for the data APIs Talcoe publishes on [Apify](https://apify.com/talcoe). Each API is a hosted actor that you call over HTTPS with an Apify token, and each one bills per result, so a test run costs cents.

| API | What it returns | Price |
|---|---|---|
| [US Government Bids & RFPs](https://apify.com/talcoe/us-government-bids-rfps) | Open bids from SAM.gov, 29 state portals, BidNet Direct, Bonfire, PlanetBids, OpenGov, Public Purchase, CivicPlus and three city portals, in one record shape | $0.006 a bid |
| [Government Bids Search API](https://apify.com/talcoe/government-bids-search-api) | Instant search over a nightly index of the same open bids, one GET request | $0.008 a bid returned |
| [YouTube Transcript API](https://apify.com/talcoe/youtube-transcripts) | Transcripts for videos, whole channels and playlists as text, timestamped segments, SRT or VTT | $0.005 a transcript, less on higher Apify plans |
| [Jobs Feed API](https://apify.com/talcoe/ats-careers-multi) | New jobs from 10,716 Greenhouse, Lever, Ashby and Workday boards plus Workable and SmartRecruiters search, with a mode that returns only new jobs | $0.005 a job |
| [Public Meeting Agendas](https://apify.com/talcoe/public-meeting-agendas) | City council, county and school board agenda items from Legistar, BoardDocs, CivicClerk, eSCRIBE, NovusAGENDA and BoardBook | $0.005 an item |
| [US Business Entity Search](https://apify.com/talcoe/us-business-entity-search) | Registered businesses in Colorado, New York, Oregon and Connecticut, newest first | $0.004 a record |

Each run also has a small start fee ($0.001 to $0.005, shown on each Store page).

## Setup

1. Create an Apify account and copy your API token from Apify Console, under Settings, then API & Integrations.
2. Put it in your shell as `APIFY_TOKEN`, for example `export APIFY_TOKEN=...`.
3. For the Python scripts, install `requests` with `pip install requests`.

## Examples

### Government bids

- [`government-bids/hvac_bids.sh`](government-bids/hvac_bids.sh) returns open HVAC bids in Texas and Florida from SAM.gov and both state portals as JSON.
- [`government-bids/hvac_bids_csv.sh`](government-bids/hvac_bids_csv.sh) saves the same search as a CSV file with five columns.
- [`government-bids/bids_to_csv.py`](government-bids/bids_to_csv.py) searches every source for janitorial work in New York and New Jersey and writes the bids to a CSV sorted by due date.
- [`government-bids/daily_monitor_input.json`](government-bids/daily_monitor_input.json) is an input for a daily schedule that returns only bids you have not received before.
- [`government-bids/search_api.sh`](government-bids/search_api.sh) queries the nightly index and gets JSON back in seconds.

### YouTube transcripts

- [`youtube-transcripts/channel_to_markdown.py`](youtube-transcripts/channel_to_markdown.py) downloads the recent transcripts of a channel and saves one Markdown file and one SRT file per video.
- [`youtube-transcripts/preview_channel.py`](youtube-transcripts/preview_channel.py) lists a channel's videos without fetching transcripts, so you can check the range first.
- [`youtube-transcripts/skipped_videos.py`](youtube-transcripts/skipped_videos.py) runs asynchronously and reads which videos had no captions in your language. Those videos are not charged.

## Use them from Claude, Cursor or another MCP client

Every API here also works as an MCP tool through Apify's MCP server. Seven ready made server listings, with setup steps and example prompts, live in [musama000/talcoe-mcp-servers](https://github.com/musama000/talcoe-mcp-servers) and in the official MCP Registry under `io.github.musama000`.

## Tutorials

- [Fixing RequestBlocked in youtube-transcript-api on a cloud server](https://dev.to/mohammed_usama_d2c2854d70/fixing-requestblocked-in-youtube-transcript-api-on-a-cloud-server-1jlg)
- More walkthroughs for each API are on [Dev.to](https://dev.to/mohammed_usama_d2c2854d70).

## Bids by email

If you would rather not write code, [Talcoe Bid Alerts](https://talcoe.com/bids) emails the new bids for your trades and states every morning. It costs $49 a month after a 14 day trial that needs no card.

## License

The code here is MIT licensed. The examples call paid APIs, so each run is billed to the Apify account whose token you use.
