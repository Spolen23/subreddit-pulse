# SubredditPulse

A subreddit analytics and community health dashboard built with Python.

## What it does

SubredditPulse helps moderators and community managers understand their subreddit's health by tracking:

- **Post trends** — Volume, types, and engagement patterns over time
- **Community sentiment** — General mood and topic distribution
- **Engagement metrics** — Comment rates, upvote ratios, response times
- **Growth tracking** — Subscriber trends and active user patterns

## Tech Stack

- Python 3.11+
- Reddit API (PRAW)
- SQLite for local data storage
- Matplotlib/Plotly for visualizations

## Status

🚧 Early development — core API integration in progress.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your Reddit API credentials to .env
python main.py --subreddit <name>
```

## License

MIT
