from nltk.twitter import Twitter
from nltk.twitter import Query
from nltk.twitter import Streamer
from nltk.twitter import TweetViewer
from nltk.twitter import TweetWriter
from nltk.twitter import credsfromfile

oauth = credfromfile()
client = Streamer(**oauth)
client.register(TweetViewer(limit=10))
client.filter(track='walmart, apple')
