from nltk import *
import clean_datas
import re
import nltk


def description():
    new_datas = clean_datas.limpa_query('video.csv')
    description_datas = [data for data in new_datas[6]]
    splited_data = [nltk.word_tokenize(i) for i in description_datas]
    # lower_data = [low.lower() for list_low in splited_data for low in list_low]
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
    stop = nltk.corpus.stopwords.words('portuguese')

    with open('stop_words.txt', 'w') as file:
        for i in stop:
            file.write(i)
            file.write('\n')
    return nltk.corpus.stopwords.words('portuguese')


def remove_stop_words():
    table = table_declaration()

    descriptions = description()
    for internal_list in range(1, len(descriptions)):
        for tokens in range(len(descriptions[internal_list])):
            descriptions[internal_list][tokens] = descriptions[internal_list][tokens].lower()
            if descriptions[internal_list][tokens] in table_declaration():
                descriptions[internal_list][tokens] = re.sub(descriptions[internal_list][tokens],
                                                             table_declaration()[descriptions[internal_list][tokens]],
                                                             descriptions[internal_list][tokens])
            if descriptions[internal_list][tokens] in stop_words():
                descriptions[internal_list][tokens] = re.sub(descriptions[internal_list][tokens], '',
                                                             descriptions[internal_list][tokens])

    print(descriptions)
    '''
    print(description())
        # print(description()[internal_list])
    for internal_list in descriptions:
        for tokens in internal_list:
            if tokens in table.keys():
                tokens = re.sub()
                # descriptions[nal_list[tokens]] = table
    print("****" * 5)
    print(stop_words())
    '''


remove_stop_words()
