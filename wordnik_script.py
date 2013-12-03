from wordnik import*
apiUrl = 'http://api.wordnik.com/v4'
apiKey = '36e62c10651ad471c9e130213a707cd21c115dc40f4ce81e4'
client = swagger.ApiClient(apiKey, apiUrl)

wordApi = WordApi.WordApi(client)

subject = raw_input('choose a word')


definition = wordApi.getDefinitions(subject)

example = wordApi.getExamples(subject)

related_words = wordApi.getRelatedWords(subject)

pronunciation = wordApi.getTextPronunciations(subject)

hyphenation = wordApi.getHyphenation(subject)

frequency = wordApi.getWordFrequency(subject)

phrases = wordApi.getPhrases(subject)

etymology = wordApi.getEtymologies(subject)

scrabble = wordApi.getScrabbleScore(subject)

print related_words

