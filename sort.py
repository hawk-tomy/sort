#import pandas as pd
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from PIL import Image,ImageDraw
import os
import random

print('rand start')
rand = [x+1 for x in range(0,10000000)]
random.shuffle(rand)
print('start : ' + str(len(rand)))
#g = 0
#df = pd.DataFrame(rand)
#df.plot(kind='bar')
#plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
#plt.savefig('data/'+str(g).zfill(3)+'.png')
#g+=1
#plt.close('all')

#merge sort
def merge(A,left,mid,right):
#    global g
    #mid 右側リストのスタート
    i = left
    l = mid
    i_e = mid-1
    l_e = right
    B = []
    while i <= i_e and l <= l_e:
        if A[i] > A[l]:
            B.append(A[l])
            l += 1
        elif A[l] > A[i]:
            B.append(A[i])
            i += 1
    if i > i_e:
        while l <= l_e:
            B.append(A[l])
            l += 1
    elif l > l_e:
        while i <= i_e:
            B.append(A[i])
            i += 1
#    print('A:' + str(A[left:right+1]))
#    print('B:' + str(B))
#    print('')
    A[left:right+1] = B
#    plt.figure()
#    df = pd.DataFrame(rand)
#    df.plot(kind='bar')
#    plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
#    plt.savefig('data/'+str(g).zfill(3)+'.png')
#    g+=1
#    plt.close('all')
    return A

def merge_sort(A,left,right):
#    global g
    #mid is right list start point1
    if left == right or left+1 == right:
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

merge_sort(rand,0,len(rand)-1)

#df = pd.DataFrame(rand)
#df.plot(kind='bar')
#plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False)
#plt.savefig('data/'+str(g).zfill(3)+'.png')
#plt.show()
print('ended')
#path = './data'
#files = os.listdir(path)
#ims = [f for f in files if os.path.isfile(os.path.join(path, f))]
#images = []
#for i in ims:
#    images.append(Image.open('data/' + i).resize((320,240)))
#images[0].save('data/sort.gif',save_all=True, append_images=images[1:], optimize=False, duration=50, loop=0)
print('save gif')
