def PeakFinder1D(ar):
    n=len(ar)//2
    if(len(ar)==1):
        return ar[0]
    if(len(ar)==2):
        if(ar[0]>=ar[1]):
            return ar[0]
        else:
            return ar[1]
    if (ar[n+1]>ar[n]):
        return(PeakFinder1D(ar[n+1:]))
    elif (ar[n-1]>ar[n]):
        return(PeakFinder1D(ar[:n]))
    else:
        return(ar[n])

#def PeakFinder2D(ar):

ar=[1,5,3,6,4,3,6,10]
#p=PeakFinder1D(ar)
print(PeakFinder1D(ar))

