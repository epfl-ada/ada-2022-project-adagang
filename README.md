# Project ADA 2022-ADAGANG
Djian Post, Matteo Peduto, Victor Carles, Majdouline Ait Yahia

# Fame on YouTube: Does provocation make success?

Provocative content can gather a lot of attention by stimulating people's emotions and
catching their attention. But is it an effective way for YouTube channels to become famous?
Is provocation a good strategy?
The motivation behind this study is to determine, by analyzing the YouNiverse datasets, whether a channel should use provocative content to grow in popularity over time. To conduct this study, we will identify such provocative videos by the typography (capitalization, lots of exclamation marks, use of emojis), number of negative words and use sentiment analysis on the video’s title, description and tags. Therefore, we will find out if provocative videos increase the number of subscribers and views, on short or long term. We will also investigate whether provocative content is a more effective strategy in some fields (e.g. politics, science) than others (e.g. recipes), using video/channel tags.

## Research Questions

* What elements can make a video labelled as “provocative”?
    * How to determine a threshold that define a video as provocative?
* What is the proportion of provocative videos on YouTube?
    * Do successful channels use more those principles?
    * Is provocation more and more present on YouTube over time?
* How can we quantify the success of a video?
* How does provocative content generate success on a statistical point of view (number of likes, subscribers or views)?
    * What type of provocation makes more success (emojis, words, capital letters...)?
    * In which categories does it have the biggest impact?
    * Does provocative content help to get a trending video?
    * What is the proportion of provocative content in YouTube trends?
* How do provocative videos have an impact on the evolution of a channel (number of subscribers, ratio like/dislike, comments etc.)?
* Is it possible to perform a linear regression that determines the optimal way to use provocation to obtain the best success index?

## Additional Datasets
Two Datasets are used in this project, but they represent the same data at different moments in time.

The daily US YouTube trending videos are collected in those datasets. This [one](https://www.kaggle.com/datasets/datasnaek/youtube-new?select=USvideos.csv) collects the videos from 2017 to 2018 and this [other one](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset?select=US_youtube_trending_data.csv) collects videos from 2020 to 2022. The data has been collected using the YouTube API. The data was previously scrapped using the information available on this [site](https://github.com/mitchelljy/Trending-YouTube-Scraper/tree/master/output)

List of words are also used to determine the presence of style of the content.

The list of [negative words](https://ptrckprry.com/course/ssd/data/negative-words.txt) is used. The goal is to determine if content with a negative feeling induce more success.

The list of [positive words](https://ptrckprry.com/course/ssd/data/positive-words.txt) is used. This list is mainly necessary to determine if the negative impact really had a significant impact on the success.

## Folder structure

`data_processing.ipynb` Notebook that computes a relatively small parquet file (around 830 MB) that will be used as a basis for our analysis. It also computes features on the data (various counts and sentiment analysis).
It takes very long to run so we provide it without the cell outputs. The file produced can be downloaded from Google Docs (the link is in the file `data_exploration.ipynb`).

`data_exploration.ipynb` Notebook where we explore the data and the features we computed.


## Methods

### Step 1: Data loading, preprocessing and dataset construction
The first of the project was to be able to treat those huge datasets. In fact, a lot of time has been spent in optimization to be able to go through them in a reasonable computational time also using parallelism. The milestone 2 focus on one year only (2019), however, the whole dataset will be used for the analysis. Google Colab or swap functions will be used.
The data has been filtered with ASCII characters to reassure the fact of working with English videos. Finally, a data frame, linking the datasets Time Series Data and Video Metadata, has been constructed keeping record of important information about the content of the videos.

### Step 2: Initial plots, sentiment analysis
Plots about the found results on the title, description and tags are calculated. In fact, different graphics (e.g., histograms) giving information about the provocation in the content allowing to understand the portion of provocation on YouTube. In addition, a sentiment analysis is performed. The index returned is used to classify the videos for the next analysis.

### Step 3: Study of provocative videos and determination of success index
Plots will show how the different factors of provocation are linked with the success of the videos. We will check if a potential correlation between provocative content and interest in a video exists (likes, trending etc.). To do so the number of views or like in function of the content will be highlighted per example. This research must be normalized according to the importance of the respective channel. The categories will be analyzed separately to spot a potential difference. The criteria of success for such specific videos will be specified

### Step 4: Determination of the impact of provocative content on the evolution of a channel
The videos will be classified by provocation. The evolution of a channel depending to its most provocative content in comparison to its less provocative content can be plot through time. The average evolution between channels can be highlighted to determine if provocation induce a faster growth on short or long term. The videos of a channel must first be filtered. In fact, it is important to see the evolution of a channel because of a video, we have to be sure that that video is the only in a defined span.

### Step 5: Complementary analysis of the provocation on the channel
Maybe the impact of the provocative content won’t be that significant on the success of a channel. However, the effect could be sense on the discussion that it generates. The polarity of the likes/dislikes and the number of comments are then interesting. Another aspect to determine is whether a channel is sensitive to provocative videos. In fact, a channel used to this type of videos can be more robust to provocation than another one that hardly never use this pattern. People might get bored of provocative content.

### Step 6: Linear regression
Using the different factors that determine provocation content and the success index, the linear regression will try to show if it exists a way to combine those indicators that gives a statistically non-negligeable impact on the success of a video.

### Step 7: Github site building and Datastory redaction
The datastory will be write using a selection of the plots realized. The most interesting results will be reported.









## Timeline
### Step 1 and Step 2: Milestone 2

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
