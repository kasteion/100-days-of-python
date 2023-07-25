from speedtest_twitter_bot import SpeedTestTwitterBot
import os

TWITTER_USER = os.environ.get("TWITTER_USER")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")

bot = SpeedTestTwitterBot(TWITTER_USER, TWITTER_PASSWORD)

speed = bot.get_internet_speed()
print(speed)
bot.twitter_login_flow()
bot.tweet_internet_speed(f"My speed test report for today is: "
                         f"{speed.get('download_speed')} Mbps download and {speed.get('upload_speed')} Mbps upload")
