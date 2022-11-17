##=========================================UPPERCASE AND EXCLAMATION================================================

# Helper function to count the number of capitalized words and exclamation marks in a text

def count_words(text):
    words = set(text.split(' '))
    nb_upper_words = sum(map(str.isupper, words))
    nb_exc_marks = sum([w.count('!') for w in words])
    nb_words = len(words)
    return nb_upper_words, nb_exc_marks, nb_words

# Count the upper words and exclamation marks in titles and descriptions 
f = open('yt_metadata_en.jsonl')
videos = ijson.items(f, '', multiple_values=True)

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
f.close()

##======================================NEGATIVE EMOJIS==================================================
# Set of negative emojis
neg_emojis = set(["\U0001F52B","\U0001F92E","\U0001F922","\U0001F623","\U0001F624","\U0001F621","\U0001F620","\U0001F92C","\U0001F608","\U0001F47F","\U0001F480","\U00002620","\U0001F4A9","\U0001F921","\U0001F479","\U0001F47A","\U0001F4A5","\U0001F4A2","\U0001F595","\U0001F44E","\U0001F52A","\U0001F9E8","\U0001FA93","\U0001F5E1","\U0001F51E","\U000026D4","\U0001F6AB","\U00002623","\U00002622","\U00002757","\U0000203C","\U00002049","\U0001F4DB"])


# function to count number of negative emojis in a text
def count_neg_emojis(text):
    words = set(word for word in text.split(' '))
    nb_negative = len(words.intersection(neg_emojis))
    # No need to recompute total number of words since it's already computed ?
    return nb_negative

# Loop to count total number of emojis for all videos
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
print("finished") #takes 40 min approx