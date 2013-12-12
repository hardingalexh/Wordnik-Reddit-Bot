Wordnik-Reddit-Bot
==================

A python project using the Wordnik API and the Reddit PRAW API to respond to calls with multiple word definitions and parts of speech.

## Setup
This program requires the installation of the Wordnik library. This is easily set up using `pip install Wordnik`. This program also requires the use of an API key, [freely available from Wordnik.](http://developer.wordnik.com)

## Documentation
This program uses the [Wordnik Python API](https://github.com/wordnik/wordnik-python) to access Wordnik json files ([sample](http://developer.wordnik.com/docs.html)). The plan is to feed these Wordnik definitions and other word metadata into a [Reddit](http://www.reddit.com) bot using [PRAW](https://praw.readthedocs.org/en/latest/).

## Contributor Guidelines
At this point in time, this project is being undertaken as part of a final assignment for a programming course at the University of North Carolina, Chapel Hill. Upon completion of that project, a full set of contributor guidelines will be opened to allow for further expansion on the bot re: using the vast amount of wordnik metadata to offer services other than simple word definitions.

# Milestones

- [X] *Wordnik*
- [X] Connect to API
- [X] Pull appropriate data from word definition
- [X] Parse Data
- [X] Display Data
- [X] *Reddit*
- [X] find comments by name
- [X] pull word from comment
- [X] embed wordnik script
- [X] reply to comment
