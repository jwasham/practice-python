import random
import re
import sys

tweet = {
    "user": "jwasham",
    "text": "Data Science is Cool",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience"]
}

tweet_keys = tweet.keys()  # list of keys
tweet_values = tweet.values()  # list of values
tweet_items = tweet.items()  # list of (key, value) tuples

print(tweet_items)
print(sys.version)

up_to_ten = list(range(10))
random.shuffle(up_to_ten)
print(up_to_ten)

lottery_numbers = list(range(60))
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)

print(random.choice(range(10)))

print("=================")

print(re.match("a", "cat"))
print(re.match("ca", "cat"))
print(re.search('mo', 'remote'))
print(re.split('[0-9]', 'R5D4'))
print(re.sub('[0-9]', 'x', 'R2D2'))
