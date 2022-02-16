import sys

sys.setrecursionlimit(10000)

ms=lambda a:(m:=lambda a,b:[((a.pop()if b[-1]>a[-1]else b.pop())if b else a.pop())if a else b.pop() for _ in range(len(a+b))][::-1])and(s:=lambda a:m(s(a[:(b:=(len(a)+1)//2)]),s(a[b:])))(a)

if __name__ == '__main__':
    from tester import tester
    tester(ms)
