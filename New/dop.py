import gensim.downloader as api
from gensim.models import Word2Vec
model = api.load("word2vec-ruscorpora-300")

var = list(model.key_to_index.items())[:10]

d= {k.split("_")[0]: k for k in model.key_to_index}

print(model.similarity(d["нога"], d["рука"]))


def get_most_similar_dict(word,topn):
    vals = model.most_similar(d[word], topn=topn)
    d={k.split("_")[0]: i+2 for i, (k,v) in enumerate(vals)}
    return d

print(get_most_similar_dict(word="нога", topn=1000))
