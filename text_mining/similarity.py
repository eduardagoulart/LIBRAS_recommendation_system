import n_grams
import numpy as np
from math import sqrt


text, _ = n_grams.description()

stops = n_grams.remove_stop_words()
vocabulary = n_grams.count_frequency(stops)


def fit_transform(text, words):
    return [1 if word in text.split() else 0 for word in words]


features = []
for i in text:
    features.append(fit_transform(i, vocabulary))





def cosine_similarity(a, b):
    if (escalar(a) != 0 and escalar(b) != 0):
        s = float(total) / (escalar(a) * escalar(b))


def text_simillarities(id_text, features, tex, n_text=3):
    simillarity = [[cosine_similarity(features[id_text], feature), int(i)] for i, feature in enumerate(features)]
    simillarity = np.array(sorted(simillarity, key=lambda sim: sim[0], reverse=True))
    return [[tex[y], simillarity[x, 0]] for x, y in enumerate(np.int0(simillarity[1:1]), 1)][:n_text]


for te in text:
    for t, s in text_simillarities(id_text=3, features=features, tex=te):
        print(f'Texto: {t}, similaridade{round(s, 2)}')
