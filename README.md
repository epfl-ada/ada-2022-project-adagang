# Controversy and Fame: Does provocation make success?

Provocative content can gather a lot of attention by stimulating people's emotions and
catching their attention. But is it an effective way for YouTube channels to become famous? 
Is provocation a good strategy? 

The motivation behind this study is to determine, by analyzing the YouNiverse datasets, whether or not a channel should use provocative content to grow in popularity over time. To conduct this study, we will identify such provocative videos by the number of dislikes and comments, the typography of the title (capitalization, lots of exclamation marks), and use sentiment analysis on the video description and tags. Therefore, we will find out if provocative videos increase the number of subscribers and views, on short or long term. We will also investigate whether provocative content is a more effective strategy in some fields (e.g. politics, science) than others (e.g. recipes), using video/channel tags.
# Research Questions

- What elements can make a video labelled as "provocative" ?
- How much more provocative videos are there compared to non-provocative ones in the datasets ?
- What type of provocation makes more succes (emojis, words, capital letters...) ?
- Do provocative videos gather more success than non-provocative ones in general ? Is it statistically significant ?
- How can we quantify the fame of a channel ? 
- Have provocative videos become more and more present on Youtube over time ?
- Is provocation a more efficient strategy in some fields than others?
- What aspects of the channel a provocative content impacts the most (number of subscribers, ratio like/dislike, comments etc) ?

# Datasets 

Our study will use the following datasets from YouNiverse:
- df_channels_en.tsv
- df_timeseries_en.csv
- yt_metadata_en.jsonl

# Methods

def json_to_df(json_file):
    converts a json file to pandas dataframe

def filter_videos_by_controversy(df_metadata):
    returns a filtered version of the metadata dataframe containing only the videos that are labelled as "controversial", grouped by channel id

def join_controversial_channel(df_filtered_metadata,df_channel):
    returns a dataframe that is an inner join of df_filtered_metadata and df_channel by channel id (unecessary columns are removed)    

def plot_fame_per_period(df, period):
    Visualize the effect of uploading a controversial video to a channel by plotting the number of views, subscribers, likes, dislikes, number of comments over the given period of time (for all videos, for all channels)

def compare_fame_per_period(channel_controversial, channel_uncontroversial, period):
    return the stats difference between channel_controversial and channel_uncontroversial over the same period of time

def compare(df_controversial, df_uncontroversial):
    return the stats difference between df_controversial and df_uncontroversial. For each channel in the dfs, we'll use a lambda that applies the compare_fame_per_period method.

# Timeline

## General examination of the datasets

This part in examination.ipynb loads the datasets and convert them into dataframes, conduct some basic analyses and data handling pipelines. we plot the various feature distributions, and pre-process useless columns and rows that might congest our computations.

## How to identify provocative/controversial content ? 

In this first step, we clearly define the elements that make us consider a video as "provocative" controversial. This would include words for the tags, title and description, typography, like/dislike ratio as well as number of comments.
Then, we create a dictionaries containing these elements.

## Filter videos dataset

Now, we can use the dictionaries we have created to filter the yt_metadata dataframe to contain only controversial videos. We can show the difference in numbers between the yt_metadata dataframe and the filtered yt_metadata dataframe.

## How to quantify fame ?

Now, we do the exact same reflection as for controversy, but for fame, by creating dictionaries that contain the elements that can make us quantify the fame of a channel.

## Statistic analysis on videos over time

We regroup all the channels that use controversial videos, and for each of these videos posted, we study the impact it had on the channel over time. We can then compare all these channels together. And finally, the controversial videos compared to the non-controversial ones. Then, we use a t-test to see if the difference is statistically significant. We can plot all the results and draw conclusions. We will test over different period of time to see if our null hypothesis is rejected, accepted or failed to reject. 

## Further analysis

We can extend our research.

# Milestones

