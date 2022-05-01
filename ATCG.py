S = input()
N = len(S)

#ACTG以外の文字列
alp = 'BDEFHIJKLMNOPQRSUVWXYZ'

cnt = []

for i in range(0, N):
    for j in range(i, N+1):
        tmp = S[i:j]
        flg = 1
        for a in alp:
             #ACTG以外の文字列の場合
            if a in tmp:
                flg = 0
        if flg:
            cnt.append(len(tmp))

print(max(cnt))
