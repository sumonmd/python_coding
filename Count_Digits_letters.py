str = input("Enter the string:")
count_d = 0
count_l = 0
count_s = 0
for i in str:
    if(i.isdigit()):
        count_d+=1
    elif (i.isspace()):
        count_s+=1
    else:
        count_l+=1
print ("total digits of the string: ",count_d)
print("total number of letters in string: ",count_l)
print("total number of letters in string: ",count_s)
