
import getpass
import time
from instapy import InstaPy

# Set your target usernames
target_usernames = ['therock', 'sunnyleone', 'cristiano']

# Set the number of followers to get for each target user
followers_amount = 10

# Set the duration to follow each follower (in seconds)
follow_duration = 300

# Prompt the user to enter their Instagram username and password
username = input("Enter your Instagram username: ")
password = getpass.getpass("Enter your Instagram password: ")

# Create an InstaPy instance
bot = InstaPy()

# Login to Instagram account
bot.login(username=username, password=password)

# Get the followers of each target user
for target_username in target_usernames:
    print(f"Getting followers of {target_username}...")
    followers = bot.get_user_followers(target_username, amount=followers_amount, live_followers=True)
    print(f"Followers of {target_username}: {followers}")
    print("")

    # Perform follow and unfollow actions
    for follower in followers:
        print(f"Following {follower}...")
        bot.follow_user(follower)
        print(f"Followed {follower}")

        time.sleep(follow_duration)

        print(f"Unfollowing {follower}...")
        bot.unfollow_user(follower)
        print(f"Unfollowed {follower}")

        print("")
    print("")

# Logout from Instagram account
bot.logout()
