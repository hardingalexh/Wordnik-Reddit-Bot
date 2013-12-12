import praw
import pprint
r = praw.Reddit (user_agent='Wordnik_Bot')
r.login('wordnik_bot', 'wordnik_bot')

subreddits = r.get_subreddit('test')
subreddits_comments = subreddits.get_comments()


def word_remover(body):
    first_pass = body.split("define ",1)[1]
    second_pass = first_pass.replace(".","")
    





for submission in subreddits_comments:
    if "wordnik_bot" in submission.body.lower():
    	body = submission.body
    	word_remover(body)