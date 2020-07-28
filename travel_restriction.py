for cases in range(int(input())):
    country=int(input())
    entry=input()
    exit=input()
    dp=[["" for i in range(country)] for j in range(country)]
    for i in range(country):
        dp[i][i]='Y'
    for i in range(country-1):
        index=i
        for j in range(i+1,country):
            if (exit[index] == "Y" and entry[j] == 'Y') and dp[i][j - 1]== 'Y':
                dp[i][j]='Y'
            else:
                dp[i][j]='N'
            index+=1
    for i in range(country-1,0,-1):
        index=i
        for j in range(i-1,-1,-1):
            if (exit[index]=="Y" and entry[j]=="Y") and dp[i][j+1]=='Y':
                dp[i][j]='Y'
            else:
                dp[i][j]='N'
            index-=1
    print("Case #"+str(cases+1)+":")
    for x in dp:
        print("".join(x))