from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from transformers import BertTokenizer
import tensorflow as tf
import numpy as np
from collections import defaultdict
from ckonlpy.tag import Twitter
import pickle
from gensim.models import Word2Vec

# 키워드 추출용
class KeywordExtractor():
    def __init__(self) -> None:
        self.vectorizer = None
        # 미리 훈련된 tf-idf벡터화 모델을 로드
        with open('vectorizer.pyinstance', 'rb') as file:
            self.vectorizer = pickle.load(file)
        # 단어를 인덱스로 바꿔주기 위한 딕셔너리
        self.word2id = defaultdict(lambda : 0)
        for idx, feature in enumerate(self.vectorizer.get_feature_names_out()):  
            self.word2id[feature] = idx

        # 형태소 분석시 추가, 삭제할 단어들
        self.add_keyword = ('아이오아이',
        '방탄소년단',
        '비트코인',
        '유해란',
        '모모랜드',
        '현대캐피탈',
        '환승센터',
        '카카오게임',
        '행정복지센터',
        '소상공인',
        '촬영물',
        '남자친구',
        '여자친구'
        '현대로템',
        '롯데정밀화학',
        '네옴시티',
        '민주당',
        '더불어민주당',
        '알바트로스',
        '행안위원',
        '윤석열',
        '특별수사',
        '반부패수사부',
        '특수부')

        self.del_keyword = ('일단',
        '이면',
        '묵묵',
        '을지',
        '려면',
        '무엇',
        '매경닷컴',
        '매일경제',
        '가령',
        '살로',
        '넣기',
        '무릎',
        '마침내',
        '다른',
        '시어',
        '라며',
        '주로',
        '당시',
        '양쪽',)
        # Twitter 형태소 분석기에 사용자 키워드를 추가하고, 처음 형태소 분석시 지연이 발생하기에 의미없는 문장을 형태소 분석해 추후의 지연을 방지합니다.
        self.poser = Twitter()
        for i in range(len(self.add_keyword)):
            self.poser.add_dictionary(self.add_keyword[i], 'Noun')
        self.poser.pos('형태소 분석기의 첫번째 품사분석시 3초의 딜레이가 발생해 생성자에서 인위적으로 1번 해줍니다,')

    def __call__(self, article) -> tuple:
        """
        article
        """
        parsed_str = [self._pre_process(article), ]
        sp_matrix = self.vectorizer.transform(parsed_str)
        parsed_keywords = list(set([(token, sp_matrix[0, self.word2id[token]]) for token in parsed_str[0].split(' ')]))
        parsed_keywords.sort(key = lambda x: -x[1])
        keywords = []
        try:
            for keyword in parsed_keywords[:10]: keywords.append(keyword[0])
        except: pass
        return keywords

    def _pre_process(self, target:str) -> str:
        key_array = self.poser.pos(target)
        keyword_array = []
        for i in range(len(key_array)):
            if key_array[i][1] in('Noun', 'Hashtag') and len(key_array[i][0]) > 1 and key_array[i][0] not in self.del_keyword:
                keyword_array.append(key_array[i][0])
        keyword_array = " ".join(keyword_array)
        return keyword_array

# 카테고리 분류용
class Classifier():
    def __init__(self) -> None:
        self.tokenizer = BertTokenizer.from_pretrained("klue/bert-base")
        self.model = tf.saved_model.load('category_model//')
        self.category = ('IT', '경제', '과학', '국제', '문화', '사회', '스포츠', '연예', '정치')
        self.category_article_dict = {idx: cat for idx, cat in enumerate(self.category)}

    def _convert(self, article):
        encoding_result = self.tokenizer.encode_plus(article, truncation=True, padding='max_length')
        input_ids = encoding_result['input_ids']
        attention_masks = encoding_result['attention_mask']
        token_type_ids = encoding_result['token_type_ids']
            
        input_ids = np.array(input_ids, dtype=int)
        attention_masks = np.array(attention_masks, dtype=int)
        token_type_ids = np.array(token_type_ids, dtype=int)
        
        input_ids = np.expand_dims(input_ids, axis=0)
        attention_masks = np.expand_dims(attention_masks, axis=0)
        token_type_ids = np.expand_dims(token_type_ids, axis=0)

        return (input_ids, attention_masks, token_type_ids)

    def __call__(self, article) -> str:
        token = self._convert(article)
        logit = self.model(token)
        predicts = np.argmax(logit)
        probability = {cat: str(probability) for cat, probability in zip(self.category, np.squeeze(np.round(logit, 3)))}
        return (self.category_article_dict[predicts], probability)

# 단어 유사도 계산용
class TopRelation():
    def __init__(self) -> None:
        self.model = Word2Vec.load('word2vec.model')

    def __call__(self, word:str, top_n:int) -> list:
        sim = self.model.wv.most_similar(word, topn=int(top_n))
        results = []
        for word in sim:
            results.append(word[0])
        return results

# 서버 메모리에 항상 올라가 있도록 키워드 추출모델과 카테고리 분류모델을 생성
extractor = KeywordExtractor()
categoryClassifier = Classifier()
wordSim = TopRelation()

# 키워드 추출 요청용
class KeyWords(APIView):
    def _parse_request(self, request:Request) -> str:
        query_params = request.query_params
        article = query_params.get('article')
        return article

    def get(self, request:Request, *args, **kwargs):
        data = self._parse_request(request)
        keywords = extractor(data)
        result = {'keywords': keywords, 'len': len(keywords)}
        json_dumps_params = {'ensure_ascii':False}
        return JsonResponse(result, json_dumps_params=json_dumps_params)

# 카테고리 추출 요청용
class Category(APIView):
    def _parse_request(self, request:Request) -> str:
        query_params = request.query_params
        title = query_params.get('title')
        article = query_params.get('article')
        # 제목과 내용을 합쳐줌
        return title + ' ' + article

    def get(self, request:Request, *args, **kwargs):
        data = self._parse_request(request)
        result = categoryClassifier(data)
        result = {'category': str(result[0]), 'probability': result[1]}
        json_dumps_params = {'ensure_ascii':False}
        return JsonResponse(result, json_dumps_params=json_dumps_params)

# 유사도 높은 단어 추출 요청용
class WordRelation(APIView):

    def _parse_request(self, request:Request) -> str:
        query_params = request.query_params
        word = query_params.get('word')
        top_n = None
        try:
            top_n = query_params.get('top_n')
        except:
            top_n = 3
        return (word, top_n)

    def get(self, request:Request, *args, **kwargs):
        data = self._parse_request(request)
        result = wordSim(data[0], data[1])
        result = {'words': str(result)}
        json_dumps_params = {'ensure_ascii':False}
        return JsonResponse(result, json_dumps_params=json_dumps_params)