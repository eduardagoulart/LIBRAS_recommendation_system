from nltk import *
import clean_datas
import nltk


def description():
    new_datas = clean_datas.limpa_query('video.csv')
    description_datas = [data for data in new_datas[6]]
    slited_data = [nltk.word_tokenize(i.lower()) for i in description_datas]
    return slited_data


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
    st = RSLPStemmer()
    tokens = [token for _list in description() for token in _list if token not in stop_words()]
    tokens = [st.stem(replace(token, table_declaration())) for token in tokens if token.isalpha()]
    return tokens

remove_stop_words()