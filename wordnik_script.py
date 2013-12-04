# setting up the wordnik API
from wordnik import*
apiUrl = 'http://api.wordnik.com/v4'
apiKey = '36e62c10651ad471c9e130213a707cd21c115dc40f4ce81e4'
client = swagger.ApiClient(apiKey, apiUrl)
wordApi = WordApi.WordApi(client)
definitions_list=[]
# takes a string
def gather_definitions(word):

    # gets definitions and many other things... we're just using the definition and part of speech
    # useCanonical="True" tries to match a base word (ie: cats -> cat), if no luck ignores
    # this is a large list from many dictionaries... can be filtered down
    definition = wordApi.getDefinitions(word,useCanonical="True",)

    #setting up counters used for incrementing
    Y=0
    speech_used=[]
    
    # for loop that checks if the counter is still within the length of the list, and whether
    # or not the part of speech has been defined already... This essentially allows us to gather
    # each part of speech once in priority of first appearance 
    for x in range(len(definition)):
    	
        if Y < (len(definition)-1):
            if definition[Y].partOfSpeech not in speech_used:            
                speech_used.append(definition[Y].partOfSpeech)
                # this formats a string for reddit markdown and appends to a list
                definitions_list.append("**"+definition[Y].word+"**: *"+definition[Y].partOfSpeech+"* "+definition[Y].text)
            Y+=1


def comment_formatter(word):
# not necessarily final
    gather_definitions(word)
    Z=0
    # prints list, more for purposes of class display
    for W in range(len(definitions_list)):
    	if Z <= (len(definitions_list)-1):
    	    print definitions_list[Z]
    	    Z+=1
    	else:
    	    break

comment_formatter('lumber')