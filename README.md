# Project ADA 2022-ADAGANG
Djian Post, Matteo Peduto, Victor Carles, Majdouline Ait Yahia

# Fame on YouTube: Does negativity make success?

It is often assumed that negative content gathers a lot of attention by stimulating people's emotions and catching their attention. But is it an effective way for YouTube channels to have success? The motivation behind this study is to determine, by analyzing the YouNiverse datasets, whether a channel should use negativity content to grow in popularity over time, and to obtain more attention. To conduct this study the video’s title, description and tags has been analyzed. Sentiment analysis, most used words and topic research have been performed in order to determine how emotions are linked to successful videos. The study is conduct on short and long term and investigates whether negative content is a more effective strategy in some fields (e.g. politics, science) than others (e.g. recipes). 

## Research Questions

* How to determine successful videos?
* Do most successful videos use more emotions in their title and descriptions? 
    * What kind of emotions?
* What is the impact of the negativity in the number of views or likes of a video?
    * Does positivity have a bigger impact?
    *	What are the most sensitive categories of videos to negative content?
* Is the use of negativity correlated to the success of a channel through time?
* What are the best negative topics to use to maximize the success?
* What are the most successful negative tags?

## Additional Datasets
Two Datasets are used in this project, but they represent the same data at different moments in time.

The daily US YouTube trending videos are collected in those datasets. This [one](https://www.kaggle.com/datasets/datasnaek/youtube-new?select=USvideos.csv) collects the videos from 2017 to 2018 and this [other one](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset?select=US_youtube_trending_data.csv) collects videos from 2020 to 2022. The data has been collected using the YouTube API. The data was previously scrapped using the information available on this [site](https://github.com/mitchelljy/Trending-YouTube-Scraper/tree/master/output)

List of words are also used to determine the presence of style of the content.

The list of [negative words](https://ptrckprry.com/course/ssd/data/negative-words.txt) is used. The goal is to determine if content with a negative feeling induce more success.

The list of [positive words](https://ptrckprry.com/course/ssd/data/positive-words.txt) is used. This list is mainly necessary to determine if the negative impact really had a significant impact on the success.

## Folder structure

`data_processing.ipynb` Notebook that computes a relatively small parquet file (around 830 MB) that will be used as a basis for our analysis. It also computes features on the data (various counts and sentiment analysis).
It takes very long to run so we provide it without the cell outputs. The file produced can be downloaded from Google Docs (the link is in the file `data_exploration.ipynb`).

`exploration.ipynb` Notebook where we explore the data and the features we computed, and do some light preprocessing.


## Methods

### Step 1: Data loading, preprocessing and dataset construction
The first task of the project was to be able to treat those huge datasets. In fact, a lot of time has been spent in optimization to be able to go through them in a reasonable computational time also using parallelism. For manageability reasons, the project will focus on one year only (2019). Google Colab is used. Finally, a data frame, linking the datasets Time Series Data and Video Metadata, has been constructed keeping record of important information about the content of the videos.

### Step 2: Initial plots, sentiment analysis
Plots about the found results on the title, description and tags are calculated. In fact, different graphics (e.g., histograms) giving information about the content allowing to understand what define successful videos. In addition, a sentiment analysis is performed using Vader. The index returned is used to classify the videos for the next analysis.

### Step 3: Determination of the use of emotions in successful videos
Plots will show how the negativity is linked with the success of the videos. The categories will be analyzed separately to spot a potential difference. 

### Step 4: Impact of the negativity on the views and likes
Through the sentiment analysis, the number of views and likes are studied with respect to the sentiment analysis score. Thanks to a linear regression, the goal is to determine if negativity or emotions in general generate more interest. The most sensitive categories to emotions are determined. It will also be determined whether a negative title or a negative description is more connected to the number of likes or views.

### Step 5: Evolution of a channel with respect to the sentiment analysis score
The study focused till here mostly on the videos. However, the evolution of a channel in term of subscribers, views or likes with respect to its mean sentiment analysis score is determined. The goal is to verify if a link can be found between the latter factors, synonyms of success for a channel, and its use of emotion’s trigger content. Is the impact of negativity so important that it is changing the evolution of a channel? Or is it only a way to maximize its potential?

### Step 6: Most frequent tags and topics for successful emotional videos 
First, some pre-processing is done to the most successful negative or positive videos filtered with the sentiment analysis score. In fact, the tags are plot in word clouds to determine the most frequent used ones. The descriptions are also clustered to identify the most used topics in emotional videos. The analysis is performed on different categories considered the most sensitive to emotions by the linear regression. 

### Step 7: Github site building and Datastory redaction
The datastory will be write using a selection of the plots realized. The most interesting results will be reported.









## Timeline
### Step 1 and Step 2:
Milestone 2

### Step 3:
*	START: 22 November 2022
*	END: 29 November 2022
### Step 4:
*	START: 30 November 2022
*	END: 6 December 2022

### Step 5:
*	START: 7 December 2022
*	END: 10 December 2022

### Step 6:
*	START: 10 December 2022
*	END: 15 December 2022

### Step 7:
*	START: 12 December 2022
*	END: 22 December 2022



## Organization in team
Step 3: teammate 1-2-3-4 <br />
Step 4: teammate 1-2 <br />
Step 5: teammate 3-4 <br />
Step 6: teammate 1-2 <br />
Step 7: teammate 3-4
