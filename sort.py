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
    if A[i] > A[l]

def merge_sort(A,left,right):
    pass

print(rand)
merge_sort(rand,0,len(rand)-1)
