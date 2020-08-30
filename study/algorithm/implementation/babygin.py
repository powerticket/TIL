baby = [2, 3, 5, 4, 6, 7]
idx = [0] * 10
for b in baby:
    idx[b] += 1
cnt = 0

for _ in range(2):
    for i in range(len(idx)):
        if idx[i] >= 3:
            idx[i] -= 3
            cnt += 1
for _ in range(2):
    for i in range(len(idx)-2):
        if idx[i] and idx[i+1] and idx[i+2]:
            idx[i] -= 1
            idx[i+1] -= 1
            idx[i+2] -= 1
            cnt += 1

if cnt == 2:
    print('baby-gin!')
else:
    print('no gin!')