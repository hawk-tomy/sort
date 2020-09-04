import random
rand = []
while 1:
    rand_ = random.randint(1,100)
    if not rand_ in rand:
        rand.append(rand_)
    if len(rand) = 100:
        break

#merge sort
def merge(A,left,mid,right):
    #mid 右側リストのスタート
    i = left
    l = mid
    i_e = mid-1
    l_e = right
    B = []
    while i <= i_e and 
    if A[i] > A[l]:
        B += A[l]
        l += 1
    elif A[l] > A[i]:
        B += A[i]
        i += 1


def merge_sort(A,left,right):
    #mid is right list start point
    if left+1 == right or left == right:
        if A[left] > A[right]:
            A[left],A[right] = A[right],A[left]
            return A
        else:
            return A
    else:
        mid = (left+right)//2
        merge_sort(A,left,mid-1)
        merge_sort(A,mid,right)
        merge(A,left,mid,right)
        return A

print(rand)
merge_sort(rand,0,len(rand)-1)
