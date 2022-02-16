# flake8: noqa
#The MIT License (MIT)
#Copyright (c) 2021-present hawk_tomy
def s(t, l, r):
    t[l], t[r] = t[r], t[l]
def m(t_l, l, mid, r):
    l_s = l
    l_e = r_s = mid
    r_e = r
    m_l = []
    while l_s < l_e and r_s < r_e:
        if t_l[l_s] < t_l[r_s]:
            m_l.append(t_l[l_s])
            l_s += 1
        elif t_l[l_s] > t_l[r_s]:
            m_l.append(t_l[r_s])
            r_s += 1
    if l_s == l_e:
        m_l.extend(t_l[r_s:r_e])
    if r_s == r_e:
        m_l.extend(t_l[l_s:l_e])
    t_l[l:r] = m_l
def ms(t_l, l=0, r=None):
    if r is None: r = len(t_l) - 1
    if l == r or r - l == 1:
        if  t_l[l] > t_l[r]:
            return s(t=t_l, l=l, r=r)
    else:
        mid = (l + r) // 2
        ms(t_l=t_l, l=l, r=mid)
        ms(t_l=t_l, l=mid, r=r)
        m(t_l=t_l, l=l, mid=mid, r=r)
if __name__ == '__main__':
    from tester import tester
    tester(ms)
