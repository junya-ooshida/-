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

"""
問題文
英大文字からなる文字列 S が与えられます。S の部分文字列 (注記を参照) であるような最も長い ACGT 文字列 の長さを求めてください。

ここで、ACGT 文字列とは A, C, G, T 以外の文字を含まない文字列です。

注記
文字列 T の部分文字列とは、T の先頭と末尾から 0 文字以上を取り去って得られる文字列です。

例えば、ATCODER の部分文字列には TCO, AT, CODER, ATCODER, (空文字列) が含まれ、AC は含まれません。

制約
S は長さ 1 以上 10 以下の文字列である。
S の各文字は英大文字である。

入力：
ATCODER

出力：
3
"""
