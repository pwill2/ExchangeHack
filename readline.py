import json
import csv
import sys
import time
import datetime

#author: Taylor Funk, edited by Parker Williams
#major: Information Systems

start = time.time()
print("Read by line timer: ", start)

file_path = "/Users/pwill2/Desktop/ExchangeHack/BYU_AWS_dump.json"
lineCount = 0
badenCount = 0
blogCount = 0
bloggerCount = 0
californiaCount = 0
googleCount = 0
instagramCount = 0
franceCount = 0
southwalesCount = 0
redditCount = 0
rssCount = 0
tamilCount = 0
tkyCount = 0
tumblrCount = 0
tweetCount = 0
usCount = 0
wordpressCount = 0
youtubeCount = 0
blanksCount = 0

with open(file_path) as f:
    with open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_test2.csv", "w") as file:
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
                'Klout',
                'Sentiment',
                'Network',
                'SourceName',
                'Latitude',
                'Longitude',
                'Country',
                'Region',
                'State',
                'County',
                'City',
                'DisplayName',
                'UserId',
                'Gender'
            ]
        )

        # csv_file_baden = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_blog.csv", "w"))
        # csv_file_baden.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_blog = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_blog.csv", "w"))
        # csv_file_blog.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_blogger = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_blogger.csv", "w"))
        # csv_file_blogger.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_california = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_california.csv", "w"))
        # csv_file_california.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_google = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_california.csv", "w"))
        # csv_file_google.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_instagram = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_instagram.csv", "w"))
        # csv_file_instagram.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_le_de_france = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_le-de-france.csv", "w"))
        # csv_file_le_de_france.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_new_south_wales = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_new-south-wales.csv", "w"))
        # csv_file_new_south_wales.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_reddit = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_reddit.csv", "w"))
        # csv_file_reddit.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_rss = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_rss.csv", "w"))
        # csv_file_rss.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_tamil_ndu = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_tamil-ndu.csv", "w"))
        # csv_file_tamil_ndu.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_tky = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_tky.csv", "w"))
        # csv_file_tky.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_tumblr = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_tumblr.csv", "w"))
        # csv_file_tumblr.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_twitter = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_twitter.csv", "w"))
        # csv_file_twitter.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_unitedstates = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_unitdestates.csv", "w"))
        # csv_file_unitedstates.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_wordpress = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_wordpress.csv", "w"))
        # csv_file_wordpress.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_youtube = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_youtube.csv", "w"))
        # csv_file_youtube.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])
        #
        # csv_file_blanks = csv.writer(open("/Users/pwill2/Desktop/ExchangeHack/nuvi_data/cleanedNuvi_blanks.csv", "w"))
        # csv_file_blanks.writerow(['_id', 'TimeMs', 'HourMs', 'DayMs', 'AggregatedMs','Text', 'Mentions', 'Author', 'Lang', 'IsReshare', 'Reach','Spread', 'TopicReach', 'TopicSpread', 'RetweetCount', 'Likes', 'Klout', 'Sentiment', 'Network','SourceName','Latitude', 'Longitude', 'Country', 'Region', 'State', 'County', 'City', 'DisplayName', 'UserId', 'Gender'])


        for line in f:
            try:
                item = json.loads(line)
                print("lineCount: ", lineCount, "item: ", item)

            except ValueError:
                print("ValueError error: ", sys.exc_info()[0], " Line: ", lineCount)
                end = time.time()
                print(end - start)
                break

            if "_id" in item:
                _id = str(item["_id"].encode('ascii', 'ignore'), 'UTF8')

                #timems = (item['TimeMs']['$numberLong'].encode('ascii', 'ignore'), 'UTF8'
                timems = datetime.datetime.fromtimestamp(float(item['TimeMs']['$numberLong']) / 1e3)

                #hourms = (item['HourMs']['$numberLong'].encode('ascii', 'ignore'), 'UTF8'
                hourms = datetime.datetime.fromtimestamp(float(item['HourMs']['$numberLong']) / 1e3)

                #dayms = (item['DayMs']['$numberLong'].encode('ascii', 'ignore'), 'UTF8'
                dayms = datetime.datetime.fromtimestamp(float(item['DayMs']['$numberLong']) / 1e3)

                #aggregatedms = (item['AggregatedMs']['$numberLong'].encode('ascii', 'ignore'), 'UTF8'
                aggregatedms = datetime.datetime.fromtimestamp(float(item['AggregatedMs']['$numberLong']) / 1e3)

                text = str(item["Text"].encode('ascii', 'ignore'), 'UTF8')
                text = text.replace(',', '')
                text = text.replace('"', '')
                text = text.replace("''", '')
                if text.startswith('"') and text.endswith('"'):
                    text = text[1:-1]

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

                klout = ""
                if "Klout" in item['Stats']:
                    klout = item['Stats']['Klout']

                sentiment = ""
                if "Sentiment" in item['Stats']:
                    sentiment = item['Stats']['Sentiment']

                network = str(item['Network'].encode('ascii', 'ignore'), 'UTF8')

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

                region = ""
                if "Region" in item['LocationAttributes']:
                    region = str(item['LocationAttributes']['Region'].encode('ascii', 'ignore'), 'UTF8')

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

            #######ALL DATA
                try:
                    csv_file.writerow(
                        [
                            _id,
                            timems,
                            hourms,
                            dayms,
                            aggregatedms,
                            text,
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
                            klout,
                            sentiment,
                            network,
                            sourcename,
                            latitude,
                            longitude,
                            country,
                            region,
                            state,
                            county,
                            city,
                            displayname,
                            userid,
                            gender
                        ]
                                        )

                    #Increment Network Counters
                    if network == "Baden-Wrttemberg Region":
                        #csv_file_baden.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        badenCount +=1
                    if network == "Blog":
                        #csv_file_blog.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        blogCount +=1
                    if network == "Blogger":
                        #csv_file_blogger.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        bloggerCount +=1
                    if network == "California":
                        #csv_file_california.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        californiaCount +=1
                    if network == "Google":
                        #csv_file_google.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        googleCount +=1
                    if network == "Instagram":
                        #csv_file_instagram.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        instagramCount +=1
                    if network == "le-de-France":
                        #csv_file_le_de_france.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        franceCount +=1
                    if network == "New South Wales":
                        #csv_file_new_south_wales.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        southwalesCount +=1
                    if network == "Reddit":
                        #csv_file_reddit.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        redditCount +=1
                    if network == "RSS":
                        #csv_file_rss.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        rssCount +=1
                    if network == "Tamil Ndu":
                        #csv_file_tamil_ndu.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        tamilCount +=1
                    if network == "Tky":
                        #csv_file_tky.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        tkyCount +=1
                    if network == "Tumblr":
                        #csv_file_tumblr.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        tumblrCount +=1
                    if network == "Twitter":
                        #csv_file_twitter.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        tweetCount +=1
                    if network == "United States":
                        #csv_file_unitedstates.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        usCount +=1
                    if network == "WordPress":
                        #csv_file_wordpress.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        wordpressCount +=1
                    if network == "YouTube":
                        #csv_file_youtube.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        youtubeCount +=1
                    if network =="(Blanks)":
                        #csv_file_blanks.writerow([_id, timems, hourms, dayms, aggregatedms, text, mentions,  author, lang, item['IsReshare'], reach, spread, topicreach, topicspread, retweet, likes, klout, sentiment, network, sourcename, latitude, longitude, country, region, state, county, city, displayname, userid, gender])
                        blanksCount +=1

                except (UnicodeEncodeError, AttributeError,IndexError):
                    print("error caught: ", sys.exc_info()[0], " Line: ", lineCount)
                    print([item['_id'], item['TimeMs']['$numberLong'], item['HourMs']['$numberLong'],item['DayMs']['$numberLong'],item['AggregatedMs']['$numberLong'], text, item['Author'], item['ProfileUrl'],item['PostUrl'], item['Lang'], item['IsReshare'],reach, spread,topicreach,topicspread,retweet,likes,klout,sentiment,item['Network'],item['SourceName'],item['SourceUri'],item['Loc'],country,state,statecode,city,bio,displayname,userid,gender])
                    break

                except Exception:
                    print("Unexpected error: ", sys.exc_info()[0], " Line: ", lineCount)
                    print([item['_id'], item['TimeMs']['$numberLong'], item['HourMs']['$numberLong'],item['DayMs']['$numberLong'],item['AggregatedMs']['$numberLong'], text,item['Mentions'], item['Author'], item['ProfileUrl'],item['PostUrl'], item['Lang'], item['IsReshare'],reach, spread,topicreach,topicspread,retweet,likes,klout,sentiment,item['Network'],item['SourceName'],item['SourceUri'],item['Loc'],country,state,city,displayname,userid,gender])
                    end = time.time()
                    print(end - start)
                    raise

            #Increment Line Counter
            lineCount +=1
            print("Line Count: ", lineCount)
            #if lineCount ==  1571635: #1571634one before error
                #break
                ######Twitter Data
                # if network == "Twitter":
                #     try:
                #         csv_file.writerow(
                #             [
                #                 _id,
                #                 timems,
                #                 hourms,
                #                 dayms,
                #                 aggregatedms,
                #                 text,
                #                 mentions,
                #                 author,
                #                 lang,
                #                 item['IsReshare'],
                #                 reach,
                #                 spread,
                #                 topicreach,
                #                 topicspread,
                #                 retweet,
                #                 likes,
                #                 klout,
                #                 sentiment,
                #                 network,
                #                 sourcename,
                #                 latitude,
                #                 longitude,
                #                 country,
                #                 region,
                #                 state,
                #                 county,
                #                 city,
                #                 displayname,
                #                 userid,
                #                 gender
                #             ]
                #         )
                #
                #     except (UnicodeEncodeError, AttributeError,IndexError):
                #         print("error caught: ", sys.exc_info()[0], " Line: ", lineCount)
                #         print([item['_id'], item['TimeMs']['$numberLong'], item['HourMs']['$numberLong'],item['DayMs']['$numberLong'],item['AggregatedMs']['$numberLong'], text, item['Author'], item['ProfileUrl'],item['PostUrl'], item['Lang'], item['IsReshare'],reach, spread,topicreach,topicspread,retweet,likes,klout,sentiment,item['Network'],item['SourceName'],item['SourceUri'],item['Loc'],country,state,statecode,city,bio,displayname,userid,gender])
                #         break
                #
                #     except Exception:
                #         print("Unexpected error: ", sys.exc_info()[0], " Line: ", lineCount)
                #         print([item['_id'], item['TimeMs']['$numberLong'], item['HourMs']['$numberLong'],item['DayMs']['$numberLong'],item['AggregatedMs']['$numberLong'], text,item['Mentions'], item['Author'], item['ProfileUrl'],item['PostUrl'], item['Lang'], item['IsReshare'],reach, spread,topicreach,topicspread,retweet,likes,klout,sentiment,item['Network'],item['SourceName'],item['SourceUri'],item['Loc'],country,state,city,displayname,userid,gender])
                #         end = time.time()
                #         print(end - start)
                #         raise
                #     #Increment Tweet Counter
                #     tweetCount +=1
                #     print("Tweet Count: ", tweetCount)
                # #Increment Line Counter
                # lineCount +=1
                # print("Line Num: ", lineCount)

end = time.time()
print("Total time: ", end - start)
print("~~~~~~~~Count Report~~~~~~~~")
print("Line Number: ", lineCount)
print("Network Sum: ", badenCount + blogCount + bloggerCount + californiaCount + googleCount + instagramCount + franceCount + southwalesCount + redditCount + rssCount + tamilCount + tkyCount + tumblrCount + tweetCount + usCount + wordpressCount + youtubeCount + blanksCount)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Baden-Wrttemberg Region: ", badenCount)
print("Blog: ", blogCount)
print("Blogger: ", bloggerCount)
print("California: ", californiaCount)
print("Google: ", googleCount)
print("Instagram: ", instagramCount)
print("le-de-France: ", franceCount)
print("New South Wales: ", southwalesCount)
print("Reddit: ", redditCount)
print("RSS: ", rssCount)
print("Tamil Ndu: ", tamilCount)
print("Tky: ", tkyCount)
print("Tumblr: ", tumblrCount)
print("Twitter: ", tweetCount)
print("United States: ", usCount)
print("WordPress: ", wordpressCount)
print("YouTube: ", youtubeCount)
print("(Blanks): ", blanksCount)
