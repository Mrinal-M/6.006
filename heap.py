def maxheapify(ar,index):
    size=len(ar)
    left=2*index+1
    right=2*index+2
    if(left<size-1):
        if ar[left]>=ar[right]:
            temp=ar[left]
            ar[left]=ar[index]
            ar[index]=temp
            maxheapify(ar,left)
        else:
            temp=ar[right]
            ar[right]=ar[index]
            ar[index]=temp
            maxheapify(ar,right)
    elif(left==size-1):
        temp=ar[left]
        ar[left]=ar[index]
        ar[index]=temp

def build_max_heap(ar):
    size=len(ar)
    for i in range(size//2,-1,-1):
        left=2*i+1
        right=left+1
        if left<size-1:
            if ar[i]<ar[left] or ar[i]<ar[right]:
                maxheapify(ar,i)
        elif left==size-1:
            if ar[i]<ar[left]:
                maxheapify(ar,i)

def extract_max(ar):
    size=len(ar)
    curr_max=ar[0]
    ar[0]=ar[size-1]
    ar[size-1]=-1
    maxheapify(ar,0)
    return curr_max

def heap_sort(ar):
    sorted_ar=[]
    for i in range(len(ar)):
        sorted_ar.append(extract_max(ar))
    return sorted_ar

ar=[8,3,15,1,7,21,17,9,100,95,64,36]
build_max_heap(ar)
new=heap_sort(ar)
print(new)