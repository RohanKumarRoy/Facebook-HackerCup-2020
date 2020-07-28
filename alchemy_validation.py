for cases in range(int(input())):
    size=int(input())
    s=input()
    freq_A=s.count('A')
    freq_B=s.count('B')
    
    if abs(freq_A-freq_B)==1:
        print("Case #"+str(cases+1)+": "+'Y')
    else:
        print("Case #"+str(cases+1)+": "+'N')
