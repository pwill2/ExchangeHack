from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from TwitterAPI import TwitterAPI
from .models import User, Stock
import pyrebase
import json
import argparse
import sys
import re

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


def get_service():
    credentials = GoogleCredentials.get_application_default()
    scoped_credentials = credentials.create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    scoped_credentials.authorize(http)
    return discovery.build('language', 'v1beta1', http=http)

def analyze_sentiment(text):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        }
    }

    service = get_service()

    request = service.documents().analyzeSentiment(body=body)
    response = request.execute()

    return response

def index(request):
    #try:
    #except .DoesNotExist:
        #raise Http404("Page does not exist")
    return render(request, "smh2/index.html")

def startTrack(request):

    config = {
        "apiKey": "AIzaSyCYaZJlTQjeI-SsWTzW6xplKc7Ja7I-s8Q",
        "authDomain": "exchangehack-143922.firebaseapp.com",
        "databaseURL": "https://exchangehack-143922.firebaseio.com/",
        "storageBucket": "exchangehack-143922.appspot.com",
        "serviceAccount": "/Users/pwill2/Desktop/HTN/smh/smh2/static/smh2/EHKEY.json"
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    #TRACK_TERMS = ['walmart', 'apple', 'google', 'gopro']
    TRACK_TERMS = ['Walmart','Exxon Mobil','Apple','Berkshire Hathaway','McKesson','UnitedHealth Group','CVS Health','General Motors','Ford Motor','AT&T','General Electric','AmerisourceBergen','Verizon','Chevron','Costco','Fannie Mae','Kroger','Amazon.com','Amazon','Walgreens Boots Alliance','Walgreens','HP','Cardinal Health','Express Scripts Holding','J.P. Morgan Chase','Boeing','Microsoft','Bank of America Corp.','Wells Fargo','Home Depot','Citigroup','Phillips 66','IBM','Valero Energy','Anthem','Procter & Gamble','Alphabet','Comcast','Target','Johnson & Johnson','MetLife','Archer Daniels Midland','Marathon Petroleum','Freddie Mac','PepsiCo','United Technologies','Aetna',"Lowe’s",'UPS','AIG','Prudential Financial','Intel','Humana','Disney','Cisco Systems','Pfizer','Dow Chemical','Sysco','FedEx','Caterpillar','Lockheed Martin']
    CONSUMER_KEY = '0zvfK5MNq0dBg4Ymi1aZ3LgeJ'
    CONSUMER_SECRET = 'fXIYNVx5cjKR7dHz8QskYXCBQCNZR07Dsk0qf1TpnqXseVGN9m'
    ACCESS_TOKEN_KEY = '885756391-gy5jzaAGuIkSlVEMo38UTPAFIkYtUxPPDV6U5Xlt'
    ACCESS_TOKEN_SECRET = '1MAjzDlEipmz9NKq07JwJX8CXKoxmdwamBkn1wZvZVZZx'

    api = TwitterAPI(CONSUMER_KEY,
             CONSUMER_SECRET,
             ACCESS_TOKEN_KEY,
             ACCESS_TOKEN_SECRET)


    # walmart_pattern = re.compile('(@?[Ww][Aa][Ll][Mm][Aa][Rr][Tt])')
    # apple_pattern = re.compile('(@?[Aa][Pp][Pp][Ll][Ee])')
    # google_pattern = re.compile('(@?[Gg][Oo][Oo][Gg][Ll][Ee])')

    counter = db.child('counter').get().val()
    if counter is None:
        counter = 0
    r = api.request('statuses/filter', {'track': TRACK_TERMS})
    for item in r.get_iterator():
        try:
            google_sentiment = analyze_sentiment(item['text'])
        except:
            google_sentiment = ""
        data = {
            #'user_description': item['user']['description'],
            #'user_location': item['user']['location'],
            'text': item['text'],
            'coords': item['coordinates'],
            'geo': item['geo'],
            'screen_name': item['user']['screen_name'],
            'user_created': item['user']['created_at'],
            'followers': item['user']['followers_count'],
            'id_str': item['id_str'],
            'tweet_created_at': item['created_at'],
            'retweets': item['retweet_count'],
            'bg_color': item['user']['profile_background_color'],
            'google_sentiment': google_sentiment
        }
        # line = item['text']
        # if walmart_pattern.match(line):
        #     walmart_magnitude = walmart_magnitude = walmart_magnitude + google_sentiment['documentSentiment']['magnitude']
        #     walmart_polarity = walmart_polarity = walmart_polarity + google_sentiment['documentSentiment']['polarity']
        #     walmart_count = walmart_count + 1
        # elif apple_pattern.match(line):
        #     apple_magnitude = apple_magnitude + google_sentiment['documentSentiment']['magnitude']
        #     apple_polarity = apple_polarity + google_sentiment['documentSentiment']['polarity']
        #     apple_count = apple_count + 1
        # elif google_pattern.match(line):
        #     google_magnitude = google_magnitude + ['documentSentiment']['magnitude']
        #     google_polarity = google_polarity + google_sentiment['documentSentiment']['polarity']
        #     google_count = google_count + 1
        db.child('tweets').push(data)
        counter = counter + 1
        db.child('counter').set(counter)
        #print(counter)

def terms_conditions(request):
    return HttpResponse("Terms and conditions page.")

def privacy_policy(request):
    return HttpResponse("Privacy policy page.")
