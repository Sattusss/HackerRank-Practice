def calc_pal(line):

    list = [x for x in line]
    
    orig = list[:]
    rev = list[:]
    rev.reverse()
    
    if orig == rev:
            return -1
       
    for i in range(len(orig)):
        if not orig[i] == rev[i]:
            cpy = orig[:]
            del cpy[i]
            cpyRev = rev[:]
            del cpyRev[len(orig) - i - 1]
            if cpy == cpyRev:
                return i
            else:
                return len(orig) - i - 1

m = int(input().strip())

lines = []
for i in range(m):
    lines.append(input())
    
for line in lines:
    print(calc_pal(line))