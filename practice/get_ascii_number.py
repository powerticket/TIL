def main(word):
    result = 0
    for w in word:
        result += ord(w)
    return result

# 테스트용 코드
if __name__ == '__main__':
    print(main('john'))