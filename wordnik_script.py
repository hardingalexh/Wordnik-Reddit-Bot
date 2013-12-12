from wordnik import*
import praw
import pprint
# setting up wordnik API
apiUrl = 'http://api.wordnik.com/v4'
apiKey = '36e62c10651ad471c9e130213a707cd21c115dc40f4ce81e4'
client = swagger.ApiClient(apiKey, apiUrl)
wordApi = WordApi.WordApi(client)

#setting up reddit API
r = praw.Reddit (user_agent='Wordnik_Bot')
r.login('wordnik_bot', 'wordnik_bot')
subreddits = r.get_subreddit('test') # defines which subreddits to crawl
subreddits_comments = subreddits.get_comments() #s separates out flattened comments






def gather_definitions(word): # takes a string

    definition = wordApi.getDefinitions(word,useCanonical="True",)
    Y=0
    speech_used=[]
    
    # for loop that iterates list and parts of speech
    for x in range(len(definition)):
    	
        if Y < (len(definition)-1):
            if definition[Y].partOfSpeech not in speech_used:            
                speech_used.append(definition[Y].partOfSpeech)
                # this formats a string for reddit markdown and appends to a list
                definitions_list.append("**"+definition[Y].word+"**: *"+definition[Y].partOfSpeech+"* "+definition[Y].text)
            Y+=1



def word_remover(body):
    first_pass = body.split("define ",1)[1]
    word = first_pass.replace(".","")
    return word






def comment_formatter(word):
# not necessarily final
    gather_definitions(word)
    Z=0
    response=""
    # prints list, more for purposes of class display
    for W in range(len(definitions_list)):
    	if Z <= (len(definitions_list)-1):
    	    response += definitions_list[Z]
    	    Z += 1
    	else:
    	    break
    return response

cache=[]




for submission in subreddits_comments:


    if "wordnik_bot" in submission.body.lower():
    	body = submission.body
    	word = word_remover(body)
    	definitions_list=[]
    	response = comment_formatter(word)
    	submission.reply(response)


