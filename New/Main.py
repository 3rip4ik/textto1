import time
import pickle
import gensim
from gensim.models import KeyedVectors
from gensim.models import Word2Vec
from clean import get_max_count

data = []
for i in range(1, get_max_count()+1):
    with open(f'data/chunk_{i}.pickle', "rb") as f:
        data+=pickle.load(f)

data = [i for i in data if len(i) >0]
print(f'Найдено {len(data)}, не пустых предл.')

start_time = time.time()

model = Word2Vec(sentences=data,
                 sg=1,
                 vector_size=100,
                 workers=8)

print(f'Времени занялл{(time.time() - start_time)/60:.2f} mins')

model.wv.most_similar('Нога')

model.wv.save_word2vec_format('custom_embedding.txt')

w2v = KeyedVectors.load_word2vec_format('custom_embedding.txt')

w2v.similarity('Нога','рука')

def get_most_similar(word, topn):
    vals = model.wv.most_similar(word, topn=topn)
    d={k:i+2 for i,(k,v) in enumerate(vals)}
    return d

get_most_simmilar_dict('нога', 10000)