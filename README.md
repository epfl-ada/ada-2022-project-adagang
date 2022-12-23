# Project ADA 2022-ADAGANG
Djian Post, Matteo Peduto, Victor Carles, Majdouline Ait Yahia

# Fame on YouTube: Does negativity make success?

It is often assumed that negative content gathers a lot of attention by stimulating people's emotions and catching their attention. But is it an effective way for YouTube channels to have success? The motivation behind this study is to determine, by analyzing the YouNiverse datasets, whether a channel should use negativity content to grow in popularity over time, and to obtain more attention. To conduct this study the video’s title, description and tags has been analyzed. Sentiment analysis, most used words and topic research have been performed in order to determine how emotions are linked to successful videos. The study is conduct on short and long term and investigates whether negative content is a more effective strategy in some fields (e.g. politics, science) than others (e.g. recipes). 

## Datastory

https://djianpost.github.io/youtube-negativity/

## Research Questions

* How to determine successful videos?
* Do most successful videos use more emotions in their title and descriptions? 
* What is the impact of the negativity in the number of views or likes of a video?
    * Does positivity have a bigger impact?
    *	What are the most sensitive categories of videos to negative content?
* Is the use of negativity correlated to the success of a channel through time?
* What are the best negative topics to use to maximize the success?
* What are the most successful negative titles?

## Additional Datasets

We use a daily US YouTube trending videos [dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new?select=USvideos.csv), from 2017 to 2018. The data has been collected using the YouTube API. The data was previously scrapped using the information available on this [site](https://github.com/mitchelljy/Trending-YouTube-Scraper/tree/master/output)


## Folder structure

`data_processing.ipynb` Notebook that computes a relatively small parquet file (around 830 MB) that will be used as a basis for our analysis. It also computes features on the data (various counts and sentiment analysis).
It takes very long to run so we provide it without the cell outputs. The file produced can be downloaded from Google Docs (the link is in the file `main.ipynb`).

`main.ipynb` Main notebook where all the results are computed. The order of the results is the same than what can be found on the website.

`helpers.py`Python file where all the functions used to process the title and description can be found. The functions are used in the notebook `data_processing.ipynb`. The idea of the project has largely been changed since the milestone 2. A lot of the functions present in the file do not end in results foundable in the data story. The function sentiment however, basis of our project, is defined in this file.


## Methods

### Step 1: Data loading, preprocessing and dataset construction
The first task of the project was to be able to treat those huge datasets. In fact, a lot of time has been spent in optimization to be able to go through them in a reasonable computational time. For manageability reasons, the project will focus on one year only (2019). We create a smaller dataframe that contains the video metadata but not the heaviest fields ("title", "description" and "tags") plus the sentiment analysis done in step 2.

### Step 2: Initial plots, sentiment analysis
Plots about the found results on the title, description and tags are calculated. Different graphics (e.g., histograms) giving information about the content allowing to understand what define successful videos. In addition, a sentiment analysis is performed using Vader. The values returned are used to classify the videos for the next analysis.

### Step 3: Determination of the use of emotions in successful videos
This is a preliminary analysis performed to determine if successful videos use more negativity title and description. The success of a video is determined with the trending dataset. The number of views and likes of the videos of this dataset are used to determine tresholds to filter successful videos from the created dataset. Likes and views are indeed an important factor of the YouTube trending algorithm. This step justify the rest of the project. 

### Step 4: Impact of the negativity on the views and likes
Through the sentiment analysis, the number of views and likes are studied with respect to the sentiment analysis score. Thanks to a linear regression, the goal is to determine if negativity (or emotions in general) generate more interest. The most sensitive categories to emotions are determined. It will also be determined whether a negative title or a negative description (predictor) is more connected to the number of likes or views (outcome).

### Step 5: Evolution of a channel with respect to the sentiment analysis score
The study focused until here mostly on the videos. Now we look at the evolution of a channel in term of number of subscribers, views or likes with respect to its mean sentiment analysis score. The goal is to verify if a link can be found between the latter factors, synonyms of success for a channel, and its use of emotion triggering content. Is the impact of negativity so important that it is changing the evolution of a channel? Or is it only a way to maximize its potential?

### Step 6: Most frequent words and topics for successful emotional videos 
First, some pre-processing is done to the most successful negative videos filtered with the sentiment analysis score. Then the words in the titles of the videos are plotted in wordclouds to determine the most frequent ones. The descriptions are also clustered to identify the most used topics in emotional videos. The analysis is performed on different categories considered the most sensitive to emotions by the linear regression. 

### Step 7: Github site building and Datastory redaction
The datastory will be write using a selection of the plots realized. The most interesting results will be reported.

## Authors contributions
Teammate 1: Djian Post <br>
Teammate 2: Matteo Peduto <br>
Teammate 3: Victor Carles <br>
Teammate 4: Majdouline Ait Yahia <br>

Conception: 1, 2, 3 and 4 <br>
Data Preprocessing: 1, 2, 3 and 4 <br>
Sentiment analysis: 1 <br>
Trending dataset and first analysis: 2 <br>
Topic research, wordclouds: 4 <br>
Evolution channels through time: 3 <br>
Linear regression: 1 <br>
Data Story construction: 1, 2, 3 and 4 <br>

