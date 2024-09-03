sorted_lists = [4,7,8,12,45,99]
n = 4


low = 0
high = len(sorted_lists)-1
found = False

while (low <= high):
    mid = (low+high)//2
    if (sorted_lists[mid] == n):
        print(f"Found at position {mid+1}")
        found = True
        break
    elif (sorted_lists[mid]<n):
        low = mid+1 #search right part
    else:
        high = mid-1

if not found:
    print("Not found")