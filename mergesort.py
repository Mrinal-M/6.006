def merge(left,right):
    l=len(left)
    r=len(right)
    a=[]
    i=0
    j=0
    while(i<l and j<r):
        if left[i]<right[j]:
            a.append(left[i])
            i+=1
        else:
            a.append(right[j])
            j+=1
    if(i<l):
        while(i<l):
            a.append(left[i])
            i+=1
    else:
        while(j<r):
            a.append(right[j])
            j+=1
    return a

def MS(ar):
    n=len(ar)//2
    if len(ar)==1:
        return ([ar[0]])
    else:
        left = MS(ar[:n])
        right = MS(ar[n:])
        return merge(left,right)

ar=[9,8,7,6,5,4,3,2,1]
sorted_ar=MS(ar)
print(sorted_ar)

