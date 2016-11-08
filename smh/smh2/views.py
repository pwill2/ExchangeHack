from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from TwitterAPI import TwitterAPI
from .models import Stock, Tweet
from textblob import TextBlob
from django.contrib.auth.models import User

from django.conf import settings
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.decorators import login_required

import pyrebase
import json
import argparse
import json
import sys
import re
import sys

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

def index(request):
    #try:
    #except .DoesNotExist:
        #raise Http404("Page does not exist")
    return render(request, "smh2/index.html")

def signup(request):
    #validate the form
    form = SignupForm();
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            u = User()
            u.username = form.cleaned_data.get('username')
            print(form.cleaned_data.get('email'))
            u.email = form.cleaned_data.get('email')
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.set_password(form.cleaned_data.get('password'))
            u.save()

            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))

            login(request, user)

            return HttpResponseRedirect('/startTrack')

    template_vars = {
        'form': form,
    }

    return render(request, 'account/signup.html', template_vars)

class SignupForm(forms.Form):
    username = forms.CharField(label='Username', required=True, max_length=100)
    email = forms.CharField(label='Email', required=True, max_length=100)
    first_name = forms.CharField(label='First Name:', required=True, max_length=100)
    last_name = forms.CharField(label='Last Name:', required=True, max_length=100)
    password = forms.CharField(label='Password:', required=True, max_length=100, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password:', required=True, max_length=100, widget=forms.PasswordInput())

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords do not match')
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
		# check uniqueness of the username
        if User.objects.filter(username=username).count() > 0:
            raise forms.ValidationError('This username is already taken. Please try another.')
        return username


def textblobSentimentAnalysis(text):
    sentiment = TextBlob(text)
    return sentiment

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

    TRACK_TERMS = ['walmart', 'apple', 'google', 'gopro']
    #TRACK_TERMS = ['Walmart','Exxon Mobil','Apple','Berkshire Hathaway','McKesson','UnitedHealth Group','CVS Health','General Motors','Ford Motor','AT&T','General Electric','AmerisourceBergen','Verizon','Chevron','Costco','Fannie Mae','Kroger','Amazon.com','Amazon','Walgreens Boots Alliance','Walgreens','HP','Cardinal Health','Express Scripts Holding','J.P. Morgan Chase','Boeing','Microsoft','Bank of America Corp.','Wells Fargo','Home Depot','Citigroup','Phillips 66','IBM','Valero Energy','Anthem','Procter & Gamble','Alphabet','Comcast','Target','Johnson & Johnson','MetLife','Archer Daniels Midland','Marathon Petroleum','Freddie Mac','PepsiCo','United Technologies','Aetna',"Lowe’s",'UPS','AIG','Prudential Financial','Intel','Humana','Disney','Cisco Systems','Pfizer','Dow Chemical','Sysco','FedEx','Caterpillar','Lockheed Martin']
    CONSUMER_KEY = '0zvfK5MNq0dBg4Ymi1aZ3LgeJ'
    CONSUMER_SECRET = 'fXIYNVx5cjKR7dHz8QskYXCBQCNZR07Dsk0qf1TpnqXseVGN9m'
    ACCESS_TOKEN_KEY = '885756391-gy5jzaAGuIkSlVEMo38UTPAFIkYtUxPPDV6U5Xlt'
    ACCESS_TOKEN_SECRET = '1MAjzDlEipmz9NKq07JwJX8CXKoxmdwamBkn1wZvZVZZx'

    api = TwitterAPI(CONSUMER_KEY,
             CONSUMER_SECRET,
             ACCESS_TOKEN_KEY,
             ACCESS_TOKEN_SECRET)

    counter = db.child('counter').get().val()
    if counter is None:
        counter = 0
    r = api.request('statuses/filter', {'track': TRACK_TERMS})
    for item in r.get_iterator():
        data = {
            'lang': item['user']['lang'],
            'location': item['user']['location'],
            'name': item['user']['name'],
            'screen_name': item['user']['screen_name'],
            'text': item['text'],
            'time_zone': item['user']['time_zone'],
            'user_followers': item['user']['followers_count'],
            'user_is_following': item['user']['friends_count'],
            'user_tweets': item['user']['statuses_count'],
            'user_total_likes': item['user']['favourites_count'],
            'verified': item['user']['verified'],
        }
        #The polarity score is a float within the range [-1.0, 1.0].
        #The subjectivity is a float within the range [0.0, 1.0]
            #0.0 is very objective
            #1.0 is very subjective
        textblob_sentiment = textblobSentimentAnalysis(data['text'])
        data['text_polarity'] = textblob_sentiment.sentiment.polarity
        data['text_subjectivity'] = textblob_sentiment.sentiment.subjectivity

        if data['lang'] == 'en':
            db.child('tweets').push(data)
            counter = counter + 1
            db.child('counter').set(counter)


def terms_conditions(request):
    return HttpResponse("Terms and conditions page.")

def privacy_policy(request):
    return HttpResponse("Privacy policy page.")
