# News Categorization 1
# 컴퓨터는 사람의 문자를 이해하지 못한다.
# 숫자로 표현했을 때 "가깝다" == "유사하다"
# 문자 => 숫자 => Vector


# One-hot Encoding : 문자를 Vector로 
# "하나의 단어"를 Vector의 Index로 인식, 단어 존재시 1, 없으면 0.
#
#    index  0  1  2  3  4  5  ...  
#           R  P  I  F        ... word V
# Rome   = [1, 0, 0, 0, 0, 0, ..., 0]
# Paris  = [0, 1, 0, 0, 0, 0, ..., 0]
# Italy  = [0, 0, 1, 0, 0, 0, ..., 0]
# France = [0, 0, 0, 1, 0, 0, ..., 0]
#   :


# Bags of Words : 문장(문서)을 Vector로
# 단어별로 인덱스를 부여해서 한 문장(또는 문서)의 단어의 개수를 Vector로 표현
#
# the dog  is on  the table
# 
#  0   0   1   1   0    1    1    1    binary type(있다, 없다)             
#  0   0   1   1   0    1    1    2    count type(몇번 나온다)
# are cat dog  is now  on  table the 
#  0   1   2   3   4    5    6    7    index


# 그렇다면 유사성 측정을 어떻게 할 것인가?
# Distance Measure
# 1. Cosine Similarity : 두 점 사이의 각도
# 2. Euclidean Distance : 피타고라스 정리, 두 점 사이의 직선 거리
# 3. Manhattan Distnace 

# Why Cosine Similarity? : Count(Euclidean) < Direction(Cosine)
# 어떤 문장에서 '러브'와 '헤이트' 두단어를 측정하여 본 결과가 아래와 같다면 c에서 어느 점이 더 가까운가?
# Love(x),Hate(y) : a(1, 0), b(5, 4), c(5, 0)
# 일단 빈도성(유클리드 거리)으로는 a, b 둘다 같다.
# 얼핏 보기에 c 만큼이나 'love'라는 단어를 사용한 b가 유사한 것처럼 보인다.
# 하지만 b는 'hate'라는 단어를 'love' 못지않게 4번이나 사용한 반면에,
# a는 'love'라는 단어를 비록 1번 밖에 사용하지 않았지만, 
# 'hate'라는 단어를 c와 마찬가지로 단 한번도 사용하지 않았다.
# 다시말해, 방향성(코사인 유사성)이 a와 c가 동일하여 유사하다고 할 수 있다.

# 결론적으로 빈도(코사인 유사성)와 방향(유클리드 거리) 모두 고려해야 하지만, 
# *** 방향(코사인 유사성) ***이 더 중요하다!!!