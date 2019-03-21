import clean_datas
import nltk

def description():
    new_datas = clean_datas.limpa_query('video.csv')
    description_datas = [data for data in new_datas[6]]
    slited_data = [nltk.word_tokenize(i) for i in description_datas]



description()