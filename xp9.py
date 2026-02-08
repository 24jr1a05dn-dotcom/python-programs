st1=str(input("enter string1"))
st2=str(input("enter string2"))
if len(st1)==len(st2):
    print("strings with same length")
    for i in range(len(st1)):
        print(st1[i],end=" ")
        print(st2[i],end=" ")
else:
    print("strings with different length")
