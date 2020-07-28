for case in range(1,int(input())):
    location={}
    n=int(input())
    for _ in range(n):
        pos, height= map(int,input().split())
        location[pos]=height
    location=sorted(location.items(), key=lambda x:x[0])
    dp={}
    ans=0
    for i in range(n):
        pos=location[i][0]
        height=location[i][1]
        if pos not in dp:
            dp[pos]=0
        if pos+height not in dp:
            dp[pos+height]=0
        if pos-height not in dp:
            dp[pos-height]=0
        dp[pos+height]=max(dp[pos+height], dp[pos]+height)
        dp[pos]=max(dp[pos],dp[pos-height]+height)
        ans=max(ans, dp[pos], dp[pos+height])
    print("Case #"+str(case)+": "+str(ans))
'''
I/P --->
8
2
0 5
5 4
2
0 5
9 4
3
0 5
9 3
2 6
5
3 2
2 8
-4 5
8 5
1 4
6
-15 15
-9 9
-3 3
5 5
9 9
18 18
8
10 20
20 20
30 20
40 20
50 20
60 20
70 20
80 20
12
13 8
-14 5
2 19
33 10
-31 9
15 21
5 3
-22 16
-6 11
25 12
-40 24
21 18
2
-500000000 500000000
500000000 500000000
'''
'''
O/P --->
Case #1: 9
Case #2: 9
Case #3: 6
Case #4: 12
Case #5: 33
Case #6: 80
Case #7: 56
Case #8: 1000000000
'''
