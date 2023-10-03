def findMissing(arr,n):
    difffrount=arr[0]-arr[1]
    differend=arr[-1]-arr[-2]

    if difffrount==differend:
        diff=differend
    else:
        diff=min(difffrount,differend)

    A=diff
    for i in range(n-1):
        if arr[i]-arr[i+1]!=diff:
            return arr[i]+abs(diff)
    else:
        return "Equal"
    



n=int(input())
arr=list(map(int,input().split()))
print(findMissing(arr,n))