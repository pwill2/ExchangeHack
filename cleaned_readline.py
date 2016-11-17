# Special Thanks To:
# Shivam Bansal shivam5992@gmail.com
# James R. A. Davenport jrad@astro.washington.edu
# Taylor Funk theefunk@gmail.com

import json
import codecs
import csv
import sys
import time
import datetime
import httplib2
import re
import string
import requests
#from google.cloud import language
from textstat.textstat import textstat
from textblob import TextBlob
from timeit import default_timer as timer
from nltk.corpus import stopwords
from apostrophe import APPOSTROPHES
from slang import SLANGS

#client = language.Client.from_service_account_json('/Users/pwill2/Desktop/ExchangeHack/smh/smh2/static/smh2/exchangehack1-1504793b8e5e.json')
start = time.time()
time_counter = timer()
print("Read by line timer: ", start)

file_path = "/Users/pwill2/Desktop/ExchangeHack/nuvi_data/BYU_AWS_dump.json"
lineCount = 0
tweetCount = 0
time_tweetCount = 0
tweetCount_Counter = 0

# Caching stopwords Part I
cached_stop_words = stopwords.words("english")
exclude = set(string.punctuation)
reader = codecs.getreader("utf-8")

with open(file_path) as f:
    with open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanLines_1to100000.csv", "w") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(
            [
                '_id',
                'TimeMs',
                'HourMs',
                'DayMs',
                'AggregatedMs',
                'Text',
                'Mentions',
                'Author',
                'Lang',
                'IsReshare',
                'Reach',
                'Spread',
                'TopicReach',
                'TopicSpread',
                'RetweetCount',
                'Likes',
                'Text Word Count',
                'Text Character Count',
                'Klout',
                'Nuvi Sentiment',
                'Textblob Senitment Polarity',
                'Textblob Senitment Subjectivity',
                'Amazon Twinword Sentiment Type', #ats_type
                'Amazon Twinword Sentiment Score', #ats_score
                'Amazon Twinword Sentiment Ratio', #ats_ratio
                'Amazon Twinword Sentiment Keywords', #ats_keywords
                #'Google Sentitment Polarity',
                #'Google Sentiment Magnitude',
                #'Google Message',
                #'Google Entities',
                'Flesch Kincaid',
                'Coleman Liau Index',
                'Linsear Write',
                'Flesch Reading Ease',
                'SMOG',
                'Gunning Fog',
                'Automated Readability Index',
                'Standard Text Score',
                'Network',
                'SourceName',
                'Latitude',
                'Longitude',
                'Country',
                'State',
                'County',
                'City',
                'DisplayName',
                'UserId',
                'Gender'
            ]
        )

        for line in f:
            if lineCount < 100001:
                if tweetCount <= 400000:
                    if time_tweetCount == 999:
                        time_counter_end = timer()
                        time_diff =  time_counter_end - time_counter
                        if time_diff < 100:
                            sleep_time = (100 - time_diff) + 3
                        elif time_diff == 100:
                            sleep_time = 3
                        else:
                            sleep_time = 0
                        time_tweetCount = 0
                        tweetCount_Counter +=1
                        print("Time Diff: ", time_diff)
                        print("Tweet Count Counter: ", tweetCount_Counter)
                        print("Sleep Time: ", sleep_time)
                        time.sleep(sleep_time)
                        time_counter = timer()

                    try:
                        item = json.loads(line)
                    except ValueError:
                        print("ValueError error: ", sys.exc_info()[0], " Line: ", lineCount)
                        end = time.time()
                        print(end - start)
                        break

                    if "_id" in item:
                        network = str(item['Network'].encode('ascii', 'ignore'), 'UTF8')
                        if network == "Twitter":
                            _id = str(item["_id"].encode('ascii', 'ignore'), 'UTF8')

                            # Format Datetime Stamps
                            timems = datetime.datetime.fromtimestamp(float(item['TimeMs']['$numberLong']) / 1e3)
                            hourms = datetime.datetime.fromtimestamp(float(item['HourMs']['$numberLong']) / 1e3)
                            dayms = datetime.datetime.fromtimestamp(float(item['DayMs']['$numberLong']) / 1e3)
                            aggregatedms = datetime.datetime.fromtimestamp(float(item['AggregatedMs']['$numberLong']) / 1e3)
                        ## Start Text Cleaning
                            text = str(item["Text"].encode('ascii', 'ignore'), 'UTF8')
                            text = text.replace(',', '')
                            text = text.replace('"', '')
                            text = text.replace("''", '')
                            if text.startswith('"') and text.endswith('"'):
                                text = text[1:-1]

                            # Apostrophe Lookup
                            new_text_1 = []
                            for word in text.split():
                                word_lower = word.lower()
                                #print("word lower: ", word_lower)
                                if word_lower in APPOSTROPHES:
                                    new_text_1.append(APPOSTROPHES[word_lower])
                                    #print("new text: ", new_text_1)
                                else:
                                    new_text_1.append(word)
                            text_1 = " ".join(new_text_1)
                            #print("text 1: ", text_1)

                            # Caching Stop-Words Part II
                            #text_2 = " ".join([word for word in text_1.split() if word not in cached_stop_words])
                            new_text_2 = []
                            for word in text_1.split():
                                if word not in cached_stop_words:
                                    new_text_2.append(word)
                            text_2 = " ".join(new_text_2)

                            # Remove URLs
                            new_text_3 = []
                            for word in text_2.split():
                                if not word.startswith("http") or word.startswith("www"):
                                    new_text_3.append(word)
                            text_3 = " ".join(new_text_3)
                            # print('remove urls:', text_3)

                            # Remove RT @name
                            new_text_4 = []
                            for word in text_3.split():
                                word = re.sub('RT', '', word)
                                word = re.sub('@\w+:', '', word)
                                word = re.sub('@\w+', '', word)
                                # print('word from rt: ', word)
                                new_text_4.append(word)
                            text_4 = " ".join(new_text_4)
                            # print('remove rt: ',text_4)

                            # Remove Unnecessary Punctuations
                            # for punc in exclude:
                            #     text = text.replace(punc, " ")

                            # Split Attached Words
                            # text_5 = " ".join(re.findall('[A-Z][^A-Z]*', text_4))
                            # print('split word: ', text)

                            # Slangs Lookup
                            new_text_5 = []
                            for word in text_4.split():
                                word_lower = word.lower()
                                if word_lower in SLANGS:
                                    new_text_5.append(SLANGS[word_lower])
                                else:
                                    new_text_5.append(word)
                            text_5 = " ".join(new_text_5)
                            # print('slangs:', text_5)

                            # Standardizing Words
                            # text = " ".join(" ".join(s)[:2] for _, s in itertools.groupby(text))
                        ## End Text Cleaning

                            # Document For Google NLP API
                            # document = client.document_from_text(text_5)

                            mentions = str(item['Mentions'])

                            author = str(item['Author'].encode('ascii', 'ignore'), 'UTF8')

                            lang = ""
                            try:
                                if item['Lang'] is not None and item['Lang']:
                                    lang = str(item['Lang'])
                                elif item['Lang'] is None:
                                    lang = lang
                            except IndexError:
                                print("IndexError: ", sys.exc_info()[0], " Line: ", lineCount)
                                print(item['Lang'])
                                break

                            reach = ""
                            if "Reach" in item['Stats']:
                                reach = item['Stats']['Reach']

                            spread = ""
                            if "Spread" in item['Stats']:
                                spread = item['Stats']['Spread']

                            topicreach = ""
                            if "TopicReach" in item['Stats']:
                                topicreach = item['Stats']['TopicReach']

                            topicspread = ""
                            if "TopicSpread" in item['Stats']:
                                topicspread = item['Stats']['TopicSpread']

                            retweet = ""
                            if "RetweetCount" in item['Stats']:
                                retweet = item['Stats']['RetweetCount']

                            likes = ""
                            if "Likes" in item['Stats']:
                                likes = item['Stats']['Likes']

                            # Count of words in text
                            word_count = len(text_5.split())

                            # Character Count
                            text_character_count = 0
                            for word in text_5.split():
                                characters = len(word)
                                text_character_count = text_character_count + characters
                            # print("text character count: ", text_character_count)

                            # Scored 1-100, higher more influence
                            klout = ""
                            if "Klout" in item['Stats']:
                                klout = item['Stats']['Klout']

                            # Scored from -
                            nuvi_sentiment = ""
                            if "Sentiment" in item['Stats']:
                                nuvi_sentiment = item['Stats']['Sentiment']

                        ## Start TextBlob Sentiment Analysis
                            textblob_hold_sentiment = TextBlob(text_5)
                            # Polarity = how negative(-1.0), neutral(0), positive(1.0)
                            textblob_senitment_polarity = textblob_hold_sentiment.sentiment.polarity
                            # Subjectivity = very objective(0.0), very subjective(1.0)
                            textblob_senitment_subjectivity = textblob_hold_sentiment.sentiment.subjectivity
                        ## End TextBlob Sentiment Analysis

                        ## Start Amazon Sentiment Analysis
                            # Using Twinword API through Mashape
                            r = requests.post("https://twinword-sentiment-analysis.p.mashape.com/analyze/",
                                headers = {
                                    "X-Mashape-Key": "nHuvksHMcHmshf4F6YhtiLVt14x1p11qBu1jsnBTbuQyX03l3j",
                                    "Content-Type": "application/x-www-form-urlencoded",
                                    "Accept": "application/json"
                                },
                                params = {
                                    "text": text_5
                                }
                            )
                            response_data = json.loads(r.content.decode('utf-8'))
                            ats_type = response_data['type']
                            ats_score = response_data['score']
                            ats_ratio = response_data['ratio']
                            ats_keywords = response_data['keywords']
                            #print("amazon response: ", response_data)
                        ## End Amazon Sentiment Analysis

                        # ## Start Google Analytics - Message, Sentiment, Entities
                        #     google_annotations = document.annotate_text()
                        #     google_message = []
                        #     for token in google_annotations.tokens:
                        #         google_message.append(dict([('Part of Speech', token.part_of_speech), ('Text Content', token.text_content)]))
                        #
                        #     google_sentitment_polarity = 0#google_annotations.sentiment.polarity
                        #     google_sentiment_magnitude = 0#google_annotations.sentiment.magnitude
                        #
                        #     google_entities = []
                        #     for entity in google_annotations.entities:
                        #         google_entities.append(dict([('Name', entity.name), ('Type', entity.entity_type), ('Salience', entity.salience)]))
                        # ## End Google Analytics

                        ## Start Readability Analytics
                            # Returns grade level using Lisear Write Formula
                            linsear_write = textstat.linsear_write_formula(text_5)
                            # Returns grade level based on 3,000 most commonly used english words
                            dale_chall = textstat.dale_chall_readability_score(text_5)
                            # Returns SMOG index score, MAY NOT BE VALID
                            smog = textstat.smog_index(text_5)
                            # Returns Gunning Fog index score
                            # 17: College Graduate, 16: College Senior, 15: College Junior, 14: College Sophomore,
                            # 13: College Freshman, 12: Highschool Senior, 11: Highschool Junior, 10: Highschool Sophomore,
                            # 9: Highschool Freshman, 8: Eighth Grade, 7: Seventh Grade, 6: Sixth Grade
                            fog = textstat.gunning_fog(text_5)
                            # Approximate grade level needed to comprehend text
                            ari = textstat.automated_readability_index(text_5)
                            # print("length of word count: ", word_count)
                            if word_count > 2:
                                # Returns grade level using Flesch-Kincaid Grade Forumla
                                flesch_kincaid = textstat.flesch_kincaid_grade(text_5)
                                # Returns grade level using Coleman-Liau Formula
                                coleman_liau_index = textstat.coleman_liau_index(text_5)
                                # Returns Flesch Reading Ease Score
                                # 90-100 : Very Easy, 80-89 : Easy, 70-79 : Fairly Easy, 60-69 : Standard,
                                # 50-59 : Fairly Difficult, 30-49 : Difficult, 0-29 : Very Confusing
                                flesch_reading_ease = textstat.flesch_reading_ease(text_5)
                                # Based on all above tests, returns best grade level which text belongs to
                                standard = textstat.text_standard(text_5)
                            else:
                                flesch_kincaid = None
                                coleman_liau_index = None
                                flesch_reading_ease = None
                                standard = None
                        ## End Readability Analytics

                            sourcename = str(item['SourceName'].encode('ascii', 'ignore'), 'UTF8')

                            latitude = ""
                            longitude = ""
                            # need to check size
                            try:
                                if item['Loc'] is not None and item['Loc']:
                                    if item['Loc'][0] is not 0:
                                        latitude=float(item['Loc'][0])
                                    if item['Loc'][1] is not 0:
                                        longitude=float(item['Loc'][1])
                            except IndexError:
                                print("IndexError: ", sys.exc_info()[0], " Line: ", lineCount)
                                print(item['Loc'])
                                break

                            country = ""
                            if "Country" in item['LocationAttributes']:
                                country = str(item['LocationAttributes']['Country'].encode('ascii', 'ignore'), 'UTF8')

                            state = ""
                            if "State" in item['LocationAttributes']:
                                state = str(item['LocationAttributes']['State'].encode('ascii', 'ignore'), 'UTF8')

                            county = ""
                            if "County" in item['LocationAttributes']:
                                county = str(item['LocationAttributes']['County'].encode('ascii', 'ignore'), 'UTF8')

                            city = ""
                            if "City" in item['OtherLocationAttributes']:
                                city = str(item['OtherLocationAttributes']['City'].encode('ascii', 'ignore'), 'UTF8')

                            displayname = ""
                            if "DisplayName" in item['UserAttributes']:
                                displayname = str(item['UserAttributes']['DisplayName'].encode('ascii', 'ignore'), 'UTF8')

                            userid = ""
                            if "UserId" in item['UserAttributes']:
                                userid = str(item['UserAttributes']['UserId'].encode('ascii', 'ignore'), 'UTF8')

                            gender = ""
                            if "Gender" in item['UserAttributes']:
                                gender = str(item['UserAttributes']['Gender'].encode('ascii', 'ignore'), 'UTF8')

                            # Twitter Data
                            try:
                                csv_file.writerow(
                                    [
                                        _id,
                                        timems,
                                        hourms,
                                        dayms,
                                        aggregatedms,
                                        text_5,
                                        mentions,
                                        author,
                                        lang,
                                        item['IsReshare'],
                                        reach,
                                        spread,
                                        topicreach,
                                        topicspread,
                                        retweet,
                                        likes,
                                        word_count,
                                        text_character_count,
                                        klout,
                                        nuvi_sentiment,
                                        textblob_senitment_polarity,
                                        textblob_senitment_subjectivity,
                                        ats_type,
                                        ats_score,
                                        ats_ratio,
                                        ats_keywords,
                                        #google_sentitment_polarity,
                                        #google_sentiment_magnitude,
                                        #google_message,
                                        #google_entities,
                                        flesch_kincaid,
                                        coleman_liau_index,
                                        linsear_write,
                                        flesch_reading_ease,
                                        smog,
                                        fog,
                                        ari,
                                        standard,
                                        network,
                                        sourcename,
                                        latitude,
                                        longitude,
                                        country,
                                        state,
                                        county,
                                        city,
                                        displayname,
                                        userid,
                                        gender
                                    ]
                                )

                            except (UnicodeEncodeError, AttributeError,IndexError):
                                print("error caught: ", sys.exc_info()[0], " Line: ", lineCount)
                                print(_id, timems, hourms, dayms, aggregatedms, text_5, mentions, author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, word_count, text_character_count, klout, nuvi_sentiment, textblob_senitment_polarity, textblob_senitment_subjectivity, ats_type, ats_score, ats_ratio, ats_keywords, flesch_kincaid, coleman_liau_index, linsear_write, flesch_reading_ease, smog, fog, ari, standard, network, sourcename, latitude, longitude, country, state, county, city, displayname, userid, gender)
                                #google_sentitment_polarity, google_sentiment_magnitude, google_message, google_entities,
                                break

                            except Exception:
                                print("Unexpected error: ", sys.exc_info()[0], " Line: ", lineCount)
                                print(_id, timems, hourms, dayms, aggregatedms, text_5, mentions, author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, word_count, text_character_count, klout, nuvi_sentiment, textblob_senitment_polarity, textblob_senitment_subjectivity, ats_type, ats_score, ats_ratio, ats_keywords, flesch_kincaid, coleman_liau_index, linsear_write, flesch_reading_ease, smog, fog, ari, standard, network, sourcename, latitude, longitude, country, state, county, city, displayname, userid, gender)
                                #google_sentitment_polarity, google_sentiment_magnitude, google_message, google_entities,
                                end = time.time()
                                print(end - start)
                                raise
                            # Increment tweetCounter
                            tweetCount +=1
                            print("Tweet Count: ", tweetCount)
                            # Increment time_tweetCount
                            time_tweetCount +=1
                            print("Time Tweet Count: ", time_tweetCount)
                    # Increment lineCounter
                lineCount +=1
                print("Line Num: ", lineCount)
            else:
                sys.exit("Reached Line Limit Condition. Script Done Running.")

end = time.time()
print("Total time: ", end - start)
print("~~~~~~~~Count Report~~~~~~~~")
print("Line Number: ", lineCount)
print("Twitter: ", tweetCount)
print("Tweet % of Total: ", tweetCount/lineCount )
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
