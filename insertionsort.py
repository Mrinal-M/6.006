def InsertionSort(ar):
    for i in range(1,len(ar)):
        for j in range(i,0,-1):
            if ar[j]<ar[j-1]:
                temp=ar[j-1]
                ar[j-1]=ar[j]
                ar[j]=temp
            else:
                break    
    return ar


ar=[6,5,4,3,2,1]
sorted_ar=InsertionSort(ar)
print(sorted_ar)
