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