import argparse
from discord_bot import run_bot
from email_crawler import fetch_unread_emails

def main():
    parser = argparse.ArgumentParser(description="Newsletter Digest Service Runner")
    parser.add_argument('--bot', action='store_true', help='Run the Discord bot')
    parser.add_argument('--crawl', action='store_true', help='Run the email crawler')
    
    args = parser.parse_args()
    
    if args.bot:
        print("Starting Discord bot...")
        run_bot()
    elif args.crawl:
        print("Starting email crawler...")
        fetch_unread_emails()
    else:
        print("Please specify a service to run: --bot or --crawl")

if __name__ == "__main__":
    main()
