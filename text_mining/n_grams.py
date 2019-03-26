from nltk import *
import clean_datas
import re
import nltk


def description():
    new_datas = clean_datas.clean_query('video.csv')
    description_datas = [data for data in new_datas[6]]
    splited_data = [nltk.word_tokenize(i) for i in description_datas]
    return splited_data


def table_declaration():
    _table = {
        "á": "a", "à": "a", "â": "a", "ä": "a", "ã": "a", "å": "a",
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "í": "i", "ì": "i", "î": "i", "ï": "i",
        "ó": "o", "ò": "o", "ô": "o", "ö": "o", "õ": "o", "ø": "o",
        "ú": "u", "ù": "u", "û": "u", "ü": "u",
        "ñ": "n", "ç": "c",
        "Á": "A", "À": "A", "Â": "A", "Ä": "A", "Ã": "A", "Å": "A",
        "É": "E", "È": "E", "Ê": "E", "Ë": "E",
        "Í": "I", "Ì": "I", "Î": "I", "Ï": "I",
        "Ó": "O", "Ò": "O", "Ô": "O", "Ö": "O", "Õ": "O", "Ø": "O",
        "Ú": "U", "Ù": "U", "Û": "U", "Ü": "U",
        "Ñ": "N", "Ç": "C",
        "ß": "ss", "Þ": "d", "æ": "ae"
    }
    return _table


def replace(s, _table):
    for original, plain in _table.items():
        s = [i.replace(original, plain) for j in s for i in j]
    return s


def stop_words():
    return nltk.corpus.stopwords.words('portuguese')


def remove_stop_words():
    stop = stop_words()
    descriptions = description()
    for internal_list in range(1, len(descriptions)):
        for tokens in range(len(descriptions[internal_list])):
            descriptions[internal_list][tokens] = descriptions[internal_list][tokens].lower()
            if descriptions[internal_list][tokens] in table_declaration():
                descriptions[internal_list][tokens] = re.sub(descriptions[internal_list][tokens],
                                                             table_declaration()[descriptions[internal_list][tokens]],
                                                             descriptions[internal_list][tokens])

    final_text = [descriptions[i][j] for i in range(1, len(descriptions)) for j in range(len(descriptions[i])) if
                  descriptions[i][j] not in stop]
    # print(stop)
    # print(final_text)

    return final_text


def count_frequency(text):
    fdist = nltk.FreqDist(text)
    most_frequent = [(word, frequency) for word, frequency in fdist.most_common(120)]
    print(most_frequent)
    return most_frequent


# :TODO computar a frquência de cada termo
stop = remove_stop_words()
count_frequency(stop)
# print(stop)
