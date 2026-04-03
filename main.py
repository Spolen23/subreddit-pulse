"""CommunityHelper Bot — Auto-respond to FAQ with mod-approved wiki/FAQ links."""
import argparse
import json
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    filename="bot_activity.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def load_config(path="config.json"):
    with open(path) as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="CommunityHelper Bot")
    parser.add_argument("--subreddit", required=True, help="Subreddit to monitor")
    parser.add_argument("--dry-run", action="store_true", help="Log matches without posting")
    args = parser.parse_args()

    config = load_config()
    print(f"Monitoring r/{args.subreddit} for {len(config.get('triggers', []))} trigger patterns...")
    logging.info(f"Bot started for r/{args.subreddit} (dry_run={args.dry_run})")

    # TODO: Connect to Reddit API via PRAW and monitor comment stream
    # TODO: Match incoming comments against trigger phrases
    # TODO: Post replies with cooldown enforcement
    # TODO: Log all actions for mod review

if __name__ == "__main__":
    main()
