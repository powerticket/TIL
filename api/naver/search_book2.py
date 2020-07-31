import requests


def search():
    client_id = "QjR83GfN10eigg4vKf7j"
    client_secret = "UlbTDATSHY"
    headers = {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret' : client_secret
    }
    encText = "python" # input()
    url = "https://openapi.naver.com/v1/search/book.json?query=" + encText
    r = requests.get(url, headers=headers)
    # f = open('book.json', 'w')
    # f.write(r.json())
    # f.close()
    print(r.json())

search()


# book_names = input("책 이름을 검색하세요: ").split(',')
# for book_name in book_names:
#     search(book_name)