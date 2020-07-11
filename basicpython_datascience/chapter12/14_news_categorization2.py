# News Categorization 2

# Data Set : 축구, 야구 선수들의 영문 기사 분류
# - 1, 2, 3, 4 : 야구
# - 5, 6, 7, 8 : 축구

# Process
# - 파일 불러오기
# - 파일을 읽어서 단어사전(corpus) 만들기
# - 단어별로 index 만들기
# - 만들어진 인덱스로 문서별 "Bag of Words" [Vector] 생성
# - 비교하고자 하는 문서 비교하기
# - 얼마나 맞는지 측정하기 


import os
import re
from collections import OrderedDict
import math
import operator


# 파일 명단 불러 오기
def get_file_list(dir_name):
    return os.listdir(dir_name)

# 파일별로 내용 읽기
def get_contents(file_list):
    y_class = []
    x_text = []
    class_dict = {1: '0', 2: '0', 3: '0', 4: '0', 5: '1', 6: '1', 7: '1', 8: '1'}
    for file_name in file_list:
        try:
            with open(file_name, 'r', encoding='utf8') as f:
                category = int(file_name.split(os.sep)[1].split('_')[0])
                y_class.append(class_dict[category])
                x_text.append(f.read())
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
    return x_text, y_class

# 단어 앞뒤 불필요한 부분 없애기 : import re => "Regular Expression(regex)"
def get_cleaned_text(text):
    text = re.sub('\n+', '', text.lower())
    return text

# Corpus 만들기, Dict(단어별 인덱스 사전) 만들기
def get_corpus_dict(text):
    text = [article.split() for article in text]
    cleaned_words = [get_cleaned_text(word) for article in text for word in article]
    corpus_dict = OrderedDict()
    for i, v in enumerate(set(cleaned_words)):
        corpus_dict[v] = i
    return corpus_dict

# 문서별로 Bag of Words Vector 생성 : *** 핵심!!! ***
def get_count_vector(text, corpus):
    text = [article.split() for article in text]
    word_index_list = [[corpus[get_cleaned_text(word)] for word in article] for article in text]
    x_vector = [[0 for _ in range(len(corpus))] for i in range(len(text))]
    for ind, text in enumerate(word_index_list):
        for i in text:
            x_vector[ind][i] += 1
    return x_vector

# 생성된 Vector들의 유사성 비교하기
"""Compute cosine similarity of v1 to v2:
    (v1 dot v2)/{||v1|| * ||v2||} """
def get_cosine_similarity(v1, v2):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

# 비교 결과 정리 하기
def get_similarity_score(x_vector, source):
    source_vector = x_vector[source]
    similarity_list =[]
    for target_vector in x_vector:
        similarity_list.append(get_cosine_similarity(source_vector, target_vector))
    return similarity_list

# 가장 유사한 상위 (몇개) 뉴스 선택
def get_top_n_similarity_news(similarity_score, n):
    x = {i: v for i, v in enumerate(similarity_score)}
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    return list(reversed(sorted_x))[1:n+1]


def main():
    dir_name = 'news_data'
    file_list = get_file_list(dir_name)
    file_list = [os.path.join(dir_name, file_name) for file_name in file_list]
    x_text, y_class = get_contents(file_list)
    corpus = get_corpus_dict(x_text)
    x_vector = get_count_vector(x_text, corpus)
    similarity_score = get_similarity_score(x_vector, 5)
    similar_news_top_10 = get_top_n_similarity_news(similarity_score, 10)
    print()
    print(similar_news_top_10)
    # 결론 : 내용적인 면에서 이대호 선수와의 관련성은 다소 약하나 10개 중 9개가 야구관련 기사이다.

if __name__ == '__main__':
    main()



