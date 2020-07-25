print('만들 파일의 갯수를 입력하세요: ')
T = int(input())
L = []
for _ in range(T):
    print('파일명을 입력하세요: ')
    L += [input()]
new_L = []
for l in L:
    new_l = []
    new_l = l.replace(' ', '-').lower()
    new_L += [new_l]
    


for l in new_L:    
    f = open(f'{l}.md', 'w')
    f.write(f'[TOC]\n\n***\n\n# {l}\n\n## About\n\n## Referencing websites')
    f.close()
    print(f'{l} 생성 완료')