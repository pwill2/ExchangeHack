from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms

import re
from textblob import TextBlob
from .textstat import textstatistics
# Create your views here.
def tweet(request):
	form = TweetForm();

	if request.method == 'POST':
		form = TweetForm(request.POST)
		if form.is_valid():
			tweet = form.cleaned_data.get('tweet')
    	## Start TextBlob Sentiment Analysis
			textblob_hold_sentiment = TextBlob(tweet)
            # Polarity = how negative(-1.0), neutral(0), positive(1.0)
			textblob_senitment_polarity = textblob_hold_sentiment.sentiment.polarity
			# Subjectivity = very objective(0.0), very subjective(1.0)
			textblob_senitment_subjectivity = textblob_hold_sentiment.sentiment.subjectivity
        ## End TextBlob Sentiment Analysis

	        ## Start Readability Analytics
			if re.search('[a-zA-Z]', tweet):
				txtstats = textstat.textstatistics()
                # Returns grade level using Lisear Write Formula
				linsear_write = txtstats.linsear_write_formula(tweet)
				# Returns grade level based on 3,000 most commonly used english words
				dale_chall = txtstats.dale_chall_readability_score(tweet)
				# Returns SMOG index score, MAY NOT BE VALID
				smog = txtstats.smog_index(tweet)
				# Returns Gunning Fog index score
                # 17: College Graduate, 16: College Senior, 15: College Junior, 14: College Sophomore,
                # 13: College Freshman, 12: Highschool Senior, 11: Highschool Junior, 10: Highschool Sophomore,
                # 9: Highschool Freshman, 8: Eighth Grade, 7: Seventh Grade, 6: Sixth Grade
				fog = txtstats.gunning_fog(tweet)
                # Approximate grade level needed to comprehend text
				ari = txtstats.automated_readability_index(tweet)
                # print("length of word count: ", word_count)
                #if word_count > 2:
                # Returns grade level using Flesch-Kincaid Grade Forumla
				flesch_kincaid = txtstats.flesch_kincaid_grade(tweet)
                # Returns grade level using Coleman-Liau Formula
				coleman_liau_index = txtstats.coleman_liau_index(tweet)
                # Returns Flesch Reading Ease Score
                # 90-100 : Very Easy, 80-89 : Easy, 70-79 : Fairly Easy, 60-69 : Standard,
                # 50-59 : Fairly Difficult, 30-49 : Difficult, 0-29 : Very Confusing
				flesch_reading_ease = txtstats.flesch_reading_ease(tweet)
                # Based on all above tests, returns best grade level which text belongs to
				standard = txtstats.text_standard(tweet)
                # else:
                #     flesch_kincaid = None
                #     coleman_liau_index = None
                #     flesch_reading_ease = None
                #     standard = None
	        ## End Readability Analytics

			return HttpResponse('Some test values' + textblob_hold_sentiment)

	template_vars = {
		'form': form,
	}

	return render(request, 'analysis/tweet.html', template_vars)

class TweetForm(forms.Form):
	tweet = forms.CharField(label='Enter tweet text', required=True, max_length=150, widget=forms.Textarea)
