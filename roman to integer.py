# roman to integer 
s='XVII'
num=0
d={'I':1,'IV':4,'V':5,'IX':9,'X':10,'L':50,'C':100,'D':500,'M':1000}# to store roman numerals with integer value
i=0
for i in range(0,len(s)):
    if i+1!=len(s) and d[s[i]]<d[s[i+1]]:# to check current value of symbol is less than next  symbol
         num-=d[s[i]] # if yes decrement the value from num
    else:
        num+=d[s[i]] # increment the num with the value 

print(num)
# integer to roman
num=45
list=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
str=['I','IV','V','IX','X','XL','L', 'XC','C','CD', 'D','CM','M']
i=12 # no.of roman numerals
while num:
    div=num//list[i]
    num=num%list[i]
    while div:
        print(str[i],end='')
        div-=1
    i-=1





        
        






    
