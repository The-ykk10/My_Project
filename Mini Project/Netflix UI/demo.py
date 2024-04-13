num = int(input ('Enter The number:'))
digit=len(str(num))
sum=0
temp=num
while(num>0)
    rem=num%10
    sum=(rem**digit)+sum
    num=num//10
if(sum==temp)
    print("It is Armstrong")
else:
    print("Not Armstrong")