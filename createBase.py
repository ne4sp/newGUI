from objects import Meta
import re


def buildbd(path):
    REGXPs = [r'\d\d\d\d.\d\d\d\d\d|\d\d\d\d.\d\d',
              r'\d{4}/\d\d/\d\d|\d\d:\d\d:\d\d',
              r' T = \d{1,2}.\d{1,2}',
              r'\d{1,2}\.\d{1,5}|\d\d',
              r'result_value = (\d{1,5}\.\d{1,5}|\d\d)'
              ]
    i = 1
    k = 1
    bd = []
    with open(path, 'r') as f:
        for line in f:
            if i == 1:
                a = (re.findall(REGXPs[1], line))
            if i == 2:
                c = (re.findall(REGXPs[0], line))[1:]
                c = [float(x) for x in c]
            if i == 3:
                d = (re.findall(REGXPs[4], line))
                d = (re.findall(REGXPs[3], d[0]))[0]
            if i == 4:
                b = (re.findall(REGXPs[2], line))
                b = re.findall(REGXPs[3], b[0])[0]
                bd.append(Meta(a[:2], c, b, d))
                bd[(k//4)-1].upd_date(a[1:])
                bd[(k//4)-1].upd_lv(c)
                bd[(k//4)-1].upd_t(b)
                bd[(k//4)-1].upd_rv(d)
                k -= 1
                i = -1
            i += 1
            k += 1
    return bd


