from youtube_transcript_api import YouTubeTranscriptApi
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

# text = '''Logistic regression is one of the most popular Machine Learning algorithms, which comes under the Supervised Learning technique. It is used for predicting the categorical dependent variable using a given set of independent variables.
# Logistic regression predicts the output of a categorical dependent variable. Therefore the outcome must be a categorical or discrete value. It can be either Yes or No, 0 or 1, true or False, etc. but instead of giving the exact value as 0 and 1, it gives the probabilistic values which lie between 0 and 1.
# Logistic Regression is much similar to the Linear Regression except that how they are used. Linear Regression is used for solving Regression problems, whereas Logistic regression is used for solving the classification problems.
# In Logistic regression, instead of fitting a regression line, we fit an "S" shaped logistic function, which predicts two maximum values (0 or 1).
# The curve from the logistic function indicates the likelihood of something such as whether the cells are cancerous or not, a mouse is obese or not based on its weight, etc.
# Logistic Regression is a significant machine learning algorithm because it has the ability to provide probabilities and classify new data using continuous and discrete datasets.
# Logistic Regression can be used to classify the observations using different types of data and can easily determine the most effective variables used for the classification.'''

# youtube_video_url = input("Enter the video url: ")
# if '=' in youtube_video_url:
#     video_id = youtube_video_url.split("=")[1]
# else:
#     video_id = youtube_video_url[-11:]
# print(video_id)

def get_video_summary(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    # print(transcript)

    result = ""
    for i in transcript:
        result += ' '+i['text']
    print(result)
    print("Length of Original text: ",len(result.split(" ")))

    stopwords = list(STOP_WORDS)
    # print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(result)
    # print(doc)
    tokens = [token.text for token in doc]
    #print(tokens)
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
    # print(word_freq)
    max_freq = max(word_freq.values())
    # print(max_freq)
    #normalized frequency of each word in doc
    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq
    # print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    # print(sent_tokens)
    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]
    # print(sent_scores)

    select_len = int(len(sent_tokens)*0.2)
    #print(select_len)

    summary = nlargest(select_len, sent_scores, key=sent_scores.get)
    # print(summary)
    final_summary = [word.text for word in summary]
    summary = " ".join(final_summary)
    # print(summary)
    # print("Length of summary text: ",len(summary.split(" ")))
    return summary