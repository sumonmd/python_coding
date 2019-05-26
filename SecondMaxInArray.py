'''
Second Maximum value in Array 
Here,
    max_in = 1st max value
    min_in = 2nd max value

'''

ar_list = [4, 6, 1, 4, 9, 2, 7]
max_in=-1000
min_in =-1000
length = len(ar_list)
for i in range(0,length):
    if(ar_list[i]>max_in):
        min_in = max_in
        max_in = ar_list[i]
    if(ar_list[i]>min_in and ar_list[i]<max_in):
        min_in = ar_list[i]
print min_in