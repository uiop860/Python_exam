import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import en_core_web_sm

def word_cloud(id,text):
    word_cloud = WordCloud(background_color='black', width=300, height=300, collocations = False)
    nlp = en_core_web_sm.load()
    
    # we only chose a subset of the training data to not crash our computers
    false_string = nlp(text)

    word_cloud_string = ""

    for token in false_string.ents:
        if token.label_ == 'PERSON':
            word_cloud_string += token.text.split(' ')[0] + " "
    false_text_cloud = word_cloud.generate(word_cloud_string)
    #plt.figure(figsize=(20,30))
    plt.imshow(false_text_cloud)
    plt.axis('off')
    plt.savefig(f"./images/{id}")
    return (f"{id}.png")
