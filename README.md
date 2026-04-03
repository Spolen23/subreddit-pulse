# CommunityHelper Bot

A self-hosted Reddit bot that automatically responds to frequently asked questions with mod-approved wiki and FAQ links.

## What it does

CommunityHelper Bot reduces moderator workload and improves the new user experience by:

- **Monitoring new posts and comments** for configurable keyword/phrase triggers
- **Auto-replying** with relevant wiki pages, FAQ sections, or mod-approved responses
- **Respecting rate limits** and anti-spam protections (no duplicate replies, cooldown windows)
- **Logging all actions** for moderator review and transparency

Every reply includes a footer identifying itself as a bot with an opt-out option.

## How it works

1. Moderators configure trigger phrases and corresponding responses in `config.json`
2. The bot monitors the subreddit comment stream via Reddit API (OAuth2)
3. When a trigger is detected, it posts a helpful reply linking to the relevant resource
4. All actions are logged to `bot_activity.log` for mod review

## Tech Stack

- Python 3.11+
- PRAW (Python Reddit API Wrapper)
- SQLite for action logging
- Runs as a long-running background process on self-hosted infrastructure

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your Reddit API credentials to .env
cp config.example.json config.json
# Configure trigger phrases and responses
python main.py --subreddit <name>
```

## Configuration

Edit `config.json` to define triggers:

```json
{
  "triggers": [
    {
      "phrases": ["how do I start", "getting started", "new here"],
      "response": "Welcome! Check out our [Getting Started Guide]({wiki_url}/getting-started) for everything you need to know.",
      "cooldown_minutes": 60
    }
  ],
  "bot_footer": "\n\n---\n*I'm a bot. [Opt out](https://reddit.com/message/compose?to={bot_username}&subject=opt-out) | [Report issue](https://reddit.com/message/compose?to={mod_team})*"
}
```

## Target Subreddits

Designed for use in communities where recurring questions are common:
r/smallbusiness, r/Entrepreneur, r/SaaS, r/webdev, r/sysadmin, r/devops, r/automation, r/nocode, r/selfhosted, r/startups, r/microsaas, r/indiehackers

## Why not Devvit?

Devvit is scoped to interactive app surfaces within Reddit's UI. This bot needs to run continuously as a standalone background process on our own infrastructure, monitoring comment streams in real time and maintaining persistent configuration state outside of Reddit's platform.

## License

MIT
