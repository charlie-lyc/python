# 공개된 API(Twitter)로 부터 데이터 가져오기
# - 트위터에서 제공하는 Developer API를 사용하여 트위터 데이터 수집
# - 수집되는 데이터 형태는 JSON 형태로 제공함
# - https://dev.twitter.com/ 사이트와 Oauth 인증으로 데이터를 주고 받을 수 있음
# - 다양한 기능을 이해하기 위해 API 문서의 공부는 필수!!!
#   https://dev.twitter.com/overview/api


# https://dev.twitter.com/에서 개발자 신분으로 회원가입하여 
# API Key, Access Token 등 반드시 기억
#
# 일종의 API 개발 과정이므로 가상환경을 설치하고 
# requests, requests-oauthlib 모듈도 설치
#
# pip install requests
# pip install requests-oauthlib


# Coding
# - oauth 접속권한 받기

import requests
from requests_oauthlib import OAuth1

cosumer_key = '확인한 cosumer_key'
consumer_secret = '확인한 consumer_secret'
access_token = '확인한 access_token'
access_token_secret = '확인한 access_token_secret'

oauth = OAuth1(client_key=consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)

# 'naver_d2'라는 트위터 계정의 정보를 가져오기 위한 url 설정
url = 'https:api.twitter.com/1.1/statuses/user_timeline.json?screen_name={0}'.format('naver_d2')
r = requests.get(url=url, auth=oauth)
statuses = r.json()

# 트윗된 내용과 작성된 날짜시간 정보 출력
for status in statuses:
    print(status['text'], status['created_at'])


