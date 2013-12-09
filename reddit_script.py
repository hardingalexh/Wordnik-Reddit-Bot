import praw
r = praw.Reddit (user_agent='Wordnik_Bot')
r.login('wordnik_bot', 'wordnik_bot')

while True:
    subreddit = r.get_subreddit('test')
    for submission in subreddit.get_hot(limit=10):