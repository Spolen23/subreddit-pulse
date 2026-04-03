"""SubredditPulse — Subreddit analytics and community health dashboard."""
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="SubredditPulse - Subreddit Analytics")
    parser.add_argument("--subreddit", required=True, help="Subreddit to analyze")
    parser.add_argument("--days", type=int, default=30, help="Number of days to analyze")
    args = parser.parse_args()
    
    print(f"Analyzing r/{args.subreddit} for the last {args.days} days...")
    # TODO: Implement API connection and analysis

if __name__ == "__main__":
    main()
