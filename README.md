**YOUTUBE VIDEO ANALYZER USING 
SENTIMENT ANALYSIS**

**Abstract –** Sentiment analysis is a method 
used to ascertain the opinions and viewpoints 
of people regarding any service or product. 
With millions of views, YouTube is one of the 
most widely used sites for sharing videos. With 
the ever-increasing popularity of online videos 
and the exponential growth of user-generated 
content, understanding the quality and 
relevancy of content has become crucial for 
viewers by looking over the comments, number 
of views, and number of likes manually. The 
goal of this paper is to create a thorough 
methodology and a useful tool for assessing 
user sentiment on YouTube videos. The 
suggested method extracts text comments and 
transcripts from YouTube videos for 
examination using cutting-edge natural 
language processing algorithms and 
categorizes them into opinions that are neutral, 
positive, negative, relevant, and irrelevant
along with a transcript summary. Ultimately, 
this research endeavors to revolutionize the 
way YouTube videos are analyzed, facilitating 
informed decision-making and enhancing user 
experience on the platform.
Keywords: Sentiment analysis, Natural 
Language Processing, Opinion extraction,
Decision–making.

**1. INTRODUCTION**

YouTube is a useful tool for data 
collection because of its wide variety of usergenerated material. It offers a vast dataset for a 
variety of analytical and research applications 
because of its billions of videos and millions of 
users. Since social scientists use YouTube data 
to investigate cultural and social phenomena, 
and advertisers rely on it for targeted marketing, 
YouTube data is an invaluable resource for a 
wide range of academic fields. The platform's 
comments and debates provide a wealth of 
information that may be used to study public 
sentiment and opinion on a range of topics.
Furthermore, YouTube collects data for 
educational research, which aids academics and 
institutions in evaluating the efficacy of 
instructional tactics and online learning. 
YouTube's enormous content library, which 
includes everything from news and personal 
vlogs to entertainment and tutorials makes it a 
priceless tool for academics, companies, 
educators, and marketers wishing to leverage 
the wealth of data produced by users and their 
interactions with the platform.
As content creators and content are 
increasing rapidly there evolves an issue of data 
relevancy. Some people seek to watch long 
tutorials on various subjects and if the content 
is just slightly relevant or mostly irrelevant then 
the user’s time is wasted. To overcome such 
problems, we perform NLP-based sentiment 
analysis on real-time data collected from 
YouTube i.e., YouTube comments and 
transcript of the videos, then analyze and 
classify them using various libraries such as 
Textblob and Spacy, and finally generate the 
output in the form of graphs and summary. 
There are two graphs, one represents the 
classification of the comments into positive, 
negative, and neutral based on polarity values, 
and the other one into relevant and irrelevant. 
Transcript summarization is done using spacy
based on the normalized frequency of sentences 
under the condition of required parameters.
Based on the output, the user can decide 
whether to watch the video, just read the 
transcript, or proceed to the next one.

**2. PROPOSED SYSTEM**

The proposed system considers the 
sentiment of comments and transcript of the 
given video to provide relevancy classification 
and accurate results as per the user’s request. 
The main aim of this paper is to develop an 
innovative YouTube Video Analyzer that 
leverages the power of sentiment analysis to 
gain valuable insights into viewers’ emotions, 
opinions, and attitudes towards the video 
content through comments and provide a video 
summary using the transcript. The system 
utilizes natural language processing techniques
and machine learning algorithms i.e., Gaussian 
NB and Logistic Regression to assess the 
sentiment of comments on YouTube videos 
automatically. It classifies comments as 
positive, negative, neutral, relevant, and 
irrelevant based on polarity values. The system 
uses real-time data from comments and video 
transcripts to train its sentiment analysis model. 
The primary goal is focused on the user’s 
decision-making strategy within less range of 
time by providing the statistics of comments 
and ensuring accurate sentiment analysis 
irrespective of complex language expressions.
A simple web interface is created using Flask 
where the user can enter a valid YouTube video 
URL that needs to be analyzed. As soon as the 
user clicks on the analyze button, the 
application searches for comments and 
transcripts related to the video in the backend. 
Then, the comments related to the video are 
sent to the sentiment analysis model for 
classification and the result in graphical terms.
Simultaneously, the transcript of the video is 
sent to the summarization model which creates 
a pipeline to generate a summary and return it.
As a result, graphical representations of 
sentiment distribution of comments and 
transcript summary will be displayed to the 
user.

**3. METHODOLOGY**

The project mainly consists of three submodules. These three modules are as follows:
a) YouTube Video Comment Classification
b) YouTube Video Transcript Summary 
Generation
c) Integration and User Interface

**3.1 YouTube Video Comment Classification**

User comments related to the YouTube 
video provided by the user are collected by 
making use of the YouTube Data API v3 which 
allows developers to access video statistics by 
making REST and XML-RPC calls using its 
URL. These scraped comments are stored in a 
response object and are processed to extract 
only comments text ignoring other metadata,
and stored in a list to create a data frame of 
comments.
The collected comments in the data 
frame undergo preprocessing, including 
lowercasing, tokenization using 
WordNetLemmatizer, and removal of special 
characters, new line characters, punctuations, 
multiple spaces, references, hashtags, and 
stopwords using the substitute method of 
regular expressions package.
Later, Sentiment analysis is 
implemented on these preprocessed comments. 
Polarity is calculated for each comment in the 
data frame using the TextBlob library and 
transformed the polarity values into a set of -1, 
0, and 1. Comments with polarity values greater 
than 0 are labeled as positive, those with values 
less than 0 as negative, and those with values 
equal to 0 as neutral. A classification machine 
learning model i.e., a Logistic Regression 
classifier is trained with the labeled sentiment 
data and predicts the results for test data.
In parallel with sentiment analysis, 
comments are classified as relevant or 
irrelevant to the video's content based on the 
same polarity values. The comments whose 
polarity value is greater than 0.5 or less than -
0.5 are labeled as relevant, and those are in 
between the range of -0.5 to +0.5 labeled as 
irrelevant. GaussianNB classifier is trained with 
the labeled sentiment data and predicts the 
results for test data.
Finally, the module outputs sentiment 
analysis results, relevance classification for 
each comment, and classification reports. These 
results can be visualized using bar graphs 
plotted using the Matplotlib library, allowing 
users to understand the overall sentiment and 
relevance distribution.

**3.2 YouTube Video Transcript Summary 
Generation**

Initially, the transcript of the YouTube 
video is obtained through a third-party youtube
– transcript – api by passing the corresponding 
video ID as a parameter to it. The extracted 
transcript undergoes preprocessing, including 
lowercasing, tokenization, and removal of 
special characters, new line characters, 
punctuations, multiple spaces, references, 
hashtags, and stopwords imported from the 
spacy library. This step ensures the transcript is 
free from noisy text.
After preprocessing the video’s 
transcript, a word frequency table is created in 
which the frequency of each word i.e., the 
number of times each word has appeared in the 
transcript is recorded as a key–value pair. 
Thereafter, the frequency of each word in the 
word frequency table is normalized by dividing 
it by the maximum frequency obtained from the 
word frequency table. The frequency of each 
transcript sentence is measured by adding the 
normalized frequency of each word in that 
particular sentence. This step ensures the 
transcript is ready for summarization.
As a result, the summary of the video is 
generated using the nlargest method of the 
heapq library by providing it with the 
preprocessed transcript, calculated sentence 
scores for each sentence of the transcript, and 
maximum length or maximum percentage of 
summary to be generated. Depending upon 
these parameters, the function will ignore the 
sentences with the least frequency and include 
those with the highest frequency to generate the 
summary. This summary is designed to provide 
users with a quick overview of the video's 
content.

**3.3 Integration and User Interface**

The outputs of both modules above are 
integrated into a single interface using Flask, a 
web framework of Python. The user interface 
comprises input fields for the video URL and 
buttons to initiate analysis. Users can input a 
YouTube video URL, and the system processes 
its comments and transcript to provide 
sentiment distribution graphs, relevance 
classification, and the generated video 
summary in an intuitive manner.

**4. RESULTS**

The required comments and transcript 
of a video are fetched successfully and trained 
classification models with that data resulting in 
an accuracy of 90%. Sentiment and relevancy 
distribution graphs along with the summarized 
transcript of the provided video URL are 
displayed. This output showcases the relevancy 
of the YouTube video to a respected user and 
they can decide whether to watch the video or 
proceed with the next one by saving their time.
