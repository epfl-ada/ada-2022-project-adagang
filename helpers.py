from tqdm import tqdm
from nltk.sentiment import SentimentIntensityAnalyzer
import csv
import pandas as pd
from parallelbar import progress_imap


##=========================================Remove non-English words================================================

# Set of negative emojis
negative_emojis = {"\U0001F92E","\U0001F922","\U0001F623","\U0001F624","\U0001F621","\U0001F620","\U0001F92C","\U0001F608","\U0001F47F","\U0001F480","\U00002620","\U0001F4A9","\U0001F921","\U0001F479","\U0001F47A","\U0001F4A5","\U0001F4A2","\U0001F595","\U0001F44E","\U0001F52A","\U0001F9E8","\U0001FA93","\U0001F5E1","\U0001F51E","\U000026D4","\U00001F6AB","\U00002623","\U00002622","\U00002757","\U0000203C","\U00002049","\U0001F4DB"}

# After analyzing the videos, we detected the existence of weird characters in the titles and descriptions that could interfere with our
# study. We decided to code this function that will check if a given word is english, by checking if it has ascii characters, or negative
# emoji to fit in our study.
def isEnglish(w):
    return w.isascii() or w in negative_emojis

# This function checks for each word of the given text if it is english. We compute a percentage of english words in the text, that couls
# used as a threshold to filter our dataframe.
def english_or_emoji(text):
    words = set(text.split(' '))
    nb_en_words_or_emojis = sum(1 for w in words if isEnglish(w))
    nb_words = len(words)
    percentage = nb_en_words_or_emojis / nb_words
    return percentage
'''
f = open('yt_metadata_en.jsonl')
videos = ijson.items(f, '', multiple_values=True)

list_new_data = []

for video in tqdm(videos):    
    percentage_title = english_or_emoji(video['title'])
    percentage_des = english_or_emoji(video['description'])
    
    list_new_data.append({
        'percentage_title': percentage_title,
        'percentage_des': percentage_des
    })
        
print('Finished')  
f.close()

# Convert the list of dicts to a dataframe
w = pd.read_parquet('generated/videos_few_columns.parquet', engine='fastparquet')
newcols = pd.DataFrame.from_dict(list_new_data)
# Join the dataframe of videos with the newly copmuted columns
joined = w.join(newcols)
# Write the joined dataframe to a file
joined.to_parquet('generated/videos_CountNegWordsTitle.parquet', compression=None)

# When analysing on the title: keep titles where the percentage is above 60%
w = w[w['percentage_title'] > 0.6]

# When analysing on the descriptions: keep descriptions where the percentage is above 60%
w = w[w['percentage_title'] > 0.6]'''

##=========================================UPPERCASE AND EXCLAMATION================================================

# Helper function to count the number of capitalized words and exclamation marks in a text

def count_upper_and_excl(text, fieldname=''):
    words = set(text.split(' '))
    nb_upper_words = sum(map(str.isupper, words))
    nb_exc_marks = sum([w.count('!') for w in words])
    #nb_words = len(words)
    d = {
        f'count_upper_words_{fieldname}': nb_upper_words, 
        f'count_excl_marks_{fieldname}': nb_exc_marks
    }
    return d

'''
list_new_data = []

for video in tqdm(videos):    
    
    # Count upper words and exclamation marks in title
    count_upper_words_title, count_exc_marks_title, count_words_title = count_words(video['title'])
    count_upper_words_des, count_exc_marks_des, l = count_words(video['description'])
    
    list_new_data.append({
        'count_upper_words_title': count_upper_words_title,
        'count_exc_marks_title': count_exc_marks_title,
        'count_upper_words_des' : count_upper_words_des,
        'count_exc_marks_des': count_exc_marks_des
    })
    
print('Finished')  
f.close()'''

##======================================NEGATIVE EMOJIS==================================================

# function to count number of negative emojis in a text
def count_neg_emojis(text, fieldname=''):
    words = set(word for word in text.split(' '))
    nb_negative_emojis = len(words.intersection(negative_emojis))
    # No need to recompute total number of words since it's already computed ?
    d = {
        f'count_negative_emojis_{fieldname}': nb_negative_emojis
    }
    return d

'''# Loop to count total number of emojis for all videos
f = open("data/yt_metadata_en.jsonl")
videos = ijson.items(f, '', multiple_values=True)
list_count_neg_emojis = []

for video in tqdm.tqdm(videos):
    count_neg_emojis_desc = count_neg_emojis(video['description'])
    count_neg_emojis_title = count_neg_emojis(video['title'])
    list_count_neg_emojis.append({
        'count_neg_emojis_desc': count_neg_emojis_desc,
        'count_neg_emojis_title': count_neg_emojis_title
    })
f.close()    
print("finished") #takes 40 min approx'''



##=================================NEGATIVE WORDS==================================

# Load the dataset of negative words
neg_words = set(open('negative-words.txt', mode='r', encoding='iso-8859-1').read().strip().split("\n"))

def count_neg_words(text, fieldname=''):
    ''' Count the number of words and the number of negative words in the text
    
        :param text: a string
        :param field: the name of the field
        
        :return: dictionary of features (nb_words, nb_negative_words)
    '''
    words = set(word.lower() for word in text.split(' '))
    nb_negative = len(words.intersection(neg_words))
    nb_words = len(words)
    d =  {
        f'count_words_{fieldname}': nb_words,
        f'count_negative_words_{fieldname}': nb_negative
    }
    return d


##=================================SENTIMENT ANALYSIS=================================

# Load VADER from nltk
sia = SentimentIntensityAnalyzer()

def sentiment(text, fieldname=''):
    ''' Perform sentiment analysis
    
        :param text: a string
        :param field: the name of the field
        
        :return: dictionary of features (negative, neutral, positive, compound)
    '''
    
    negative, neutral, positive, compound = sia.polarity_scores(text).values()
    d = {
        f'sia_negative_{fieldname}': negative,
        f'sia_neutral_{fieldname}': neutral,
        f'sia_positive_{fieldname}': positive,
        f'sia_compound_{fieldname}': compound
    }
    return d


##=================================FEATURE EXTRACTION==================================


def extract_features_mp(text_to_features, year, field, nb_cores=1):
    ''' Extract the video features according to a specified function, on a given year, on a given field.
        With multiprocessing. It is not always faster, use it with caution!
        
        :param text_to_features: function that maps a string to a list of features. The prototype must be
            text_to_features(text, fieldname) -> dict of features.
        :param year: string of the year
        :param field: name of the video field to analyse (string)
        :param nb_cores: number of cores to use for the multiprocessing
        
        :return: DataFrame with the features (each row corresponds to a video, the features are columns)
    '''
    
    print(f'[1/3] Extracting the fields `{field}`...')
    list_text = []
    with open(f'generated/{year}/{year}_videos.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for video in tqdm(reader):
            list_text.append(video[field])
    print('...done.')
    
    print(f'[2/3] Computing features (using {nb_cores} CPU cores)')
    features_list = [] # list of dicts (one for each video)
    chunksize = len(list_text) // nb_cores
    features_list = progress_imap(text_to_features, list_text, n_cpu=nb_cores, chunk_size=chunksize)
    print('...done.')

    print('[3/3] Converting features to dataframe...')
    features_list = pd.DataFrame.from_dict(features_list)
    print('...done.')
    
    return features_list



def extract_features(text_to_features, year, field):
    ''' Extract the video features according to a specified function, on a given year, on a given field. 
        Without multiprocessing.
        
        :param text_to_features: function that maps a string to a list of features. The prototype must be
            text_to_features(text, fieldname) -> dict of features.
        :param year: string of the year
        :param field: name of the video field to analyse (string)
        
        :return: DataFrame with the features (each row corresponds to a video, the features are columns)
    '''
    
    print('Computing features')
    features_list = [] # list of dicts (one for each video)
    with open(f'generated/{year}/{year}_videos.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for video in tqdm(reader):
            features_video = text_to_features(video[field], fieldname=field)
            features_video
            features_list.append(features_video)
    print('...done.')

    print('Converting features to dataframe...')
    features_list = pd.DataFrame.from_dict(features_list)
    print('...done.')
    
    return features_list