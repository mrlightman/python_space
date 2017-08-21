
a = {7:2,5:4,4:5,1:20}
li = [7,5,4,1]
rl = []
def func(r,li):
    k = li[0]
    i = a[k]
#    print(r,li,i,k)
    while i >= 0:
        m = r + i*k
        i -= 1
        if m == 20:
            j = i + 1
            while j > 0:
                rl.append(k)
                j -= 1
            print("succ",rl)
            j = i + 1
            while j > 0:
                rl.pop()
                j -= 1
            continue
        elif m > 20:
            continue
        else:
#            print("func",li)
            j = i + 1
            while j > 0:
                rl.append(k)
                j -= 1
            if len(li) > 1:
                tli = li[1:]
#                print("func",m,tli)
                func(m,tli)
                j = i + 1
                while j > 0:
                    rl.pop()
                    j -= 1
            else:
                j = i + 1
                while j > 0:
                    rl.pop()
                    j -= 1
                continue

func(0,li)
