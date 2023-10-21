def search(mylist,itme)->int|None:
    low = 0
    high = len(mylist)-1
    while low <= high:
        mid = (low+high)//2
        value = mylist[mid]
        if value == itme:
            return mid
        if value > itme:
            high = mid-1
        else:
            low = mid+1
    return None

mylist = [10,48,1,4,2,8,37]
mylist.sort()
print(f"mylist={mylist},result:{search(mylist,itme=10)}")
