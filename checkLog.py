import linecache


def createtemp(path):
    flag = False
    f2 = open('temp1.txt', 'w+')
    with open(path, 'r') as f:
        for line in f:
            if 'Date: ' in line:
                f2.write(line)
            if flag is True:
                f2.write(line)
                flag = False
            if 'Light values' in line:
                flag = True
            if ' T = ' in line:
                f2.write(line)
            if ' result_value = ' in line:
                f2.write(line)
    f2.close()

    i = 0
    finfile = open('temp2.txt', 'w+')
    with open('temp1.txt', 'r') as f:
        for lines in f:
            i += 1
            line = linecache.getline('temp1.txt', i)
            line2 = linecache.getline('temp1.txt', i + 1)
            line3 = linecache.getline('temp1.txt', i + 2)
            line4 = linecache.getline('temp1.txt', i + 3)
            if ('Date: ' in lines) and (' result_value = ' in line3) and (' T = ' in line4):
                finfile.write(line)
                finfile.write(line2)
                finfile.write(line3)
                finfile.write(line4)
                finfile.write('\n')


