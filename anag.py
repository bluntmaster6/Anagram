from itertools import permutations
def main():
    llist=[]
    srting=''
    size= int(input())
    for i in range(0,size):
        #llist.append(input())
        srting+=input()
    file = open("collin.txt",'r')
    wlist = file.readlines()
    t=0
    while t<len(wlist):
        wlist[t]=wlist[t].strip("\n").lower()
        if len(wlist[t])<3:
            wlist.remove(wlist[t])
        t+=1
    print(wlist)
    perms = []
    mlist=[]
    for i in range(1, len(srting)+1):
        for c in permutations(srting, i):
            perms.append("".join(c))
    print(len(perms))
    for c in perms:
        if c in wlist:
            mlist.append(c)
            if len(c)>5:
                print(c)
    smlist = sorted(mlist, key=len)
    print(smlist)


main()
