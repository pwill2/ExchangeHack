##1. Word and Sentence tokenizing
    #from nltk.tokenize import sent_tokenize, word_tokenize

    #example_text = "Hello there, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."
    #print(sent_tokenize(example_text))
    #print(word_tokenize(example_text))

##2. Stop Words Filtering
    # from nltk.corpus import stopwords
    # from nltk.tokenize import word_tokenize
    # example_sentence = "This is an example showing off stop word filtration."
    #
    # stop_words = set(stopwords.words("english"))
    # words = word_tokenize(example_sentence)
    #
    # filtered_sentence = []
    #
    # for w in words:
    #     if w not in stop_words:
    #         filtered_sentence.append(w)
    #
    # # One line of code that does the above 4 lines
    # # filtered_sentence = [w for w in words if not w in stop_words]
    # print(filtered_sentence)

##3. Stemming
    # from nltk.stem import PorterStemmer
    # from nltk.tokenize import word_tokenize
    #
    # ps = PorterStemmer()
    # example_words = ['python', 'pythoner', 'pythoning', 'pythoned', 'pythonly']
    #
    # for w in example_words:
    #     print(ps.stem(w))
    #
    # new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
    #
    # words = word_tokenize(new_text)
    # for w in words:
    #     print(ps.stem(w))

##4. Part of Speech Tagging

    # POS tag list:
    #     CC	coordinating conjunction
    #     CD	cardinal digit
    #     DT	determiner
    #     EX	existential there (like: "there is" ... think of it like "there exists")
    #     FW	foreign word
    #     IN	preposition/subordinating conjunction
    #     JJ	adjective	'big'
    #     JJR	adjective, comparative	'bigger'
    #     JJS	adjective, superlative	'biggest'
    #     LS	list marker	1)
    #     MD	modal	could, will
    #     NN	noun, singular 'desk'
    #     NNS	noun plural	'desks'
    #     NNP	proper noun, singular	'Harrison'
    #     NNPS	proper noun, plural	'Americans'
    #     PDT	predeterminer	'all the kids'
    #     POS	possessive ending	parent's
    #     PRP	personal pronoun	I, he, she
    #     PRP$	possessive pronoun	my, his, hers
    #     RB	adverb	very, silently,
    #     RBR	adverb, comparative	better
    #     RBS	adverb, superlative	best
    #     RP	particle	give up
    #     TO	to	go 'to' the store.
    #     UH	interjection	errrrrrrrm
    #     VB	verb, base form	take
    #     VBD	verb, past tense	took
    #     VBG	verb, gerund/present participle	taking
    #     VBN	verb, past participle	taken
    #     VBP	verb, sing. present, non-3d	take
    #     VBZ	verb, 3rd person sing. present	takes
    #     WDT	wh-determiner	which
    #     WP	wh-pronoun	who, what
    #     WP$	possessive wh-pronoun	whose
    #     WRB	wh-abverb	where, when

    # import nltk
    # from nltk.corpus import state_union
    # from nltk.tokenize import PunktSentenceTokenizer
    #
    # train_text = state_union.raw("2005-GWBush.txt")
    # sample_text = state_union.raw("2006-GWBush.txt")
    #
    # custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    #
    # tokenized = custom_sent_tokenizer.tokenize(sample_text)
    #
    # def process_content():
    #     try:
    #         for i in tokenized:
    #             words = nltk.word_tokenize(i)
    #             tagged = nltk.pos_tag(words)
    #             print(tagged)
    #
    #     except Exception as e:
    #         print(str(e))
    #
    # process_content()

##5. Chunking
    # import nltk
    # from nltk.corpus import state_union
    # from nltk.tokenize import PunktSentenceTokenizer
    # train_text = state_union.raw("2005-GWBush.txt")
    # sample_text = state_union.raw("2006-GWBush.txt")
    #
    # custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    #
    # tokenized = custom_sent_tokenizer.tokenize(sample_text)
    #
    # def process_content():
    #     try:
    #         for i in tokenized:
    #             words = nltk.word_tokenize(i)
    #             tagged = nltk.pos_tag(words)
    #
    #             chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""
    #             chunkParser = nltk.RegexpParser(chunkGram)
    #             chunked = chunkParser.parse(tagged)
    #
    #             #chunked.draw()
    #             print(chunked)
    #
    #     except Exception as e:
    #         print(str(e))
    #
    # process_content()

##6. Chinking (You chink from a chunk, *removing something)
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<.*>+}
                }<VB.?|IN|DT|TO>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            #chunked.draw()
            print(chunked)

    except Exception as e:
        print(str(e))

process_content()
