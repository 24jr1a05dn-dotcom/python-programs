vowels="aeiouAEIOU"
word=input("enter a word: ")
flag=0
for char in word:
    if char in vowels:
        flag=1
        break
    if(flag==1):
       print('given string contains vowel')
    else:
        print('given string  not contains vowel')
    
