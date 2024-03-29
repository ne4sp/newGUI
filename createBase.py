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

def tclean(db, t1=None, t2=None):
    t1 = float(t1)
    t2 = float(t2)

    for line in db.copy():
        num = float(line.t)
        if ((num < t2) and (num > t1)) is False:
            db.remove(line)
    return db


def rvclean(db, rv=None, rv2=None):
    rv = float(rv)
    rv2 = float(rv2)

    for line in db.copy():
        num = float(line.t)
        if ((num < rv2) and (num > rv)) is False:
            db.remove(line)
    return db


def st(path):
    a = ''
    with open(path, 'r') as f:
        for line in f:
            a = (re.findall(r'\d{4}/\d\d/\d\d|\d\d:\d\d:\d\d', line))[1]
            print(a)
            break
    y4 = int(a[:4])
    m2=  int(a[5:7])
    d2 = int(a[-2:])
    m = [y4, m2, d2]
    return m


def dateclean(db, d1=None, d2=None):
    flag = False
    s = '/'
    date_oplimit = d1[6:10] + s + d1[3:5] + s + d1[:2]
    print(date_oplimit)
    date_cllimit = d2[6:10] + s + d2[3:5] + s + d2[:2]
    print(date_cllimit)
    time_oplimit = d1[-5:].strip()
    # if time_oplimit[0] == '0':
    #     time_oplimit = '0' + time_oplimit
    time_cllimit = d2[-5:].strip()
    # if time_cllimit[0] == '0':
    #     time_cllimit = '0' + time_cllimit
    mm_ol = int(date_oplimit[5:7])
    mm_cl = int(date_cllimit[5:7])
    dd1_ol = int(date_oplimit[8:])
    dd1_cl = int(date_cllimit[8:])
    hh1_ol = int(time_oplimit[:2])
    hh1_cl = int(time_cllimit[:2])
    m1_ol = int(time_oplimit[3:])
    m1_cl = int(time_cllimit[3:])
    for line in db.copy():
        time = line.date[1]
        date = line.date[0]
        m = int(time[3:5])
        hh = int(time[:2])
        mm = int(date[5:7])
        dd = int(date[8:])

        if (mm == mm_ol) and (dd == dd1_ol):
            if hh1_ol == hh:
                if m < m1_ol:
                    flag = True
        if (mm == mm_cl) and (dd == dd1_cl):
            if hh1_cl == hh:
                if m < m1_cl:
                    flag = False
        if flag == False:
            db.remove(line)
    return db

