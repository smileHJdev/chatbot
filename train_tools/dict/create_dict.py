from utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

def read_corpus_data(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data

#말뭉치 데이터 나중에 교체할 데이터?
corpus_data = read_corpus_data('./corpus.txt')

#말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성
p = Preprocess()
dict = []
for c in corpus_data:
    pos = p.pos(c[1])
    for k in pos:
        dict.append(k[0])

#사전에 사용될 word2index 생성
#사전의 첫 번째 인덱스에는 OOV사용
tokenizer = preprocessing.text.Tokenizer(oov_token='OOV')
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index

#사건파일 생성
f= open("chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()