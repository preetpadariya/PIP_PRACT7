"""Student Id = 20CE063
    Student name = Preet Padariya"""
#LAPINDROME
#GITHUB-LINK : https://github.com/preetpadariya/PIP_PRACT7.git

def Lapindrome(S):
    strlen = len(S)
    if(strlen%2==0):
        a = S[:(strlen//2)]
        b = S[(strlen//2):]
    else: 
        a = S[:(strlen//2)]
        b = S[(strlen//2)+1:]
    la = list(a)
    la.sort()
    lb = list(b)
    lb.sort()
    if (la==lb):
        print("YES")
    else:
        print("NO")

t = int(input())

for i in range(t):
    txt =  input()
    Lapindrome(txt)
