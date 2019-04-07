import re
import string
import numpy as np
import clean_datas
import nltk


def stop_words():
    return nltk.corpus.stopwords.words('portuguese')


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


def clear_text(text):
    """
    Limpar os textos, eliminando pontuações e converter
    todo o texto com letras minusculas.
    """
    stopwords = str(stop_words())
    table = table_declaration()
    pattern = "[{}]".format(string.punctuation)
    text = [word.lower() for word in text]
    text = [[re.sub(pattern, "", word) for word in words.split()] for words in text]
    for words in text:
        for word in words:
            if len(word) > 1:
                print(word)
    text = [[word for word in words if len(word) > 1] for words in text]
    print(len(text))

    for words in range(0, len(text)):
        for word in range(len(text[words])):
            if text[words][word] in table:
                text[words][word] = re.sub(text[words][word], table[text[words][word]], text[words][word])

    text = [[word for word in words if word not in stopwords] for words in text ]
    print(len(text))

    text = [[word for word in words if len(word) > 1] for words in text]
    text = [' '.join(words) for words in text]
    return np.array(text)


new_datas = clean_datas.clean_query('video.csv')
corpus = np.array(new_datas[6])
corpus_clear = clear_text(corpus)


def popular_words(text):
    print(text)


# popular_words(corpus_clear)


def text_all(text):
    """
    Armazena em um vetor todas as palavras dos textos sem repetições.
    """
    text_set = set()
    for w in [words.split() for words in text]:
        text_set.update(w)
    return np.array(list(text_set))


vocabulary = text_all(corpus_clear)


def fit_transform(text, words=vocabulary):
    """
    Converte o texto em um vetor, onde compara se cada palavra obtida no vetor de
    todas as palavras contém ou não em cada texto.
    Insere 1 se sim e 0 se não.
    """
    # return [1 if word in text.split() else 0 for word in words]
    return [int(word in text.split()) for word in words]


features = np.array(list(map(fit_transform, corpus_clear)))


def cosine_similarity(v, w):
    # return np.dot(v, w) / np.sqrt(np.dot(v, v) * np.dot(w, w))
    return np.dot(v, w)/(np.linalg.norm(v)*np.linalg.norm(w))


def text_simillarities(id_text, features=features, text=corpus, n_text=3):
    """
    Dado o texto a ser analisado, a função retorna em ordem descrecente quais os demais textos são
    similares ao analisado. A função retorna matriz de 2 por n_text, onde a primeira e a segunda coluna
    refere-se ao texto analisado e a similaridade do texto analisado, respectivamente.
    """
    simillarity = [[cosine_similarity(features[id_text], feature), int(i)] for i, feature in enumerate(features)]
    simillarity = np.array(sorted(simillarity, key=lambda sim: sim[0], reverse=True))
    return [[text[y], simillarity[x, 0]] for x, y in enumerate(np.int0(simillarity[1:, 1]), 1)][:n_text]


print('Texto analisado -> ', corpus[3], '\n')
for t, s in text_simillarities(3):
    print('Texto: {} | Similaridade: {}'.format(t, round(s, 2)))
