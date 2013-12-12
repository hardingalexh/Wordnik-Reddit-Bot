import praw
import pprint
r = praw.Reddit (user_agent='Wordnik_Bot')
r.login('wordnik_bot', 'wordnik_bot')

subreddits = r.get_subreddit('test')
subreddits_comments = subreddits.get_comments()




for submission in subreddits_comments:
    if "wordnik_bot" in submission.body.lower():
    	print submission.body