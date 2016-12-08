from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms

# Create your views here.
def tweet(request):
	form = TweetForm();

	if request.method == 'POST':
		form = TweetForm(request.POST)
		if form.is_valid():
			return HttpResponse('This is working')

	template_vars = {
		'form': form,
	}

	return render(request, 'analysis/tweet.html', template_vars)

class TweetForm(forms.Form):
	tweet = forms.CharField(label='Enter tweet text', required=True, max_length=150)

def results(request):
    return render(request, "analysis/results.html")

def dashboard(request):
    return render(request, "analysis/dashboard.html")