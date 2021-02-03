# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
from ast import literal_eval


def search(book_name):
    client_id = "QjR83GfN10eigg4vKf7j"
    client_secret = "UlbTDATSHY"
    encText = urllib.parse.quote(book_name)
    url = "https://openapi.naver.com/v1/search/book.json?query=" + encText # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

book_names = "Python" # input("책 이름을 검색하세요: ").split(',')
search(book_names)
# for book_name in book_names:
#     search(book_name)