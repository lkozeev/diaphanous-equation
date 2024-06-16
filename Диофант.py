def g(a, b):
    a,b,k=max(a,b),min(a,b),[]
    print('--АЛГОРИТМ-ЕВКЛИДА------')
    while b!=0:
        print('',a,'=',b,'*',a//b,'+',a%b)
        k.append([a,b,a//b,a%b]);a,b=b,a%b
    print('--ВЫРАЖЕНИЕ-ОСТАТКОВ----');return k
def nod(m, n):
    return m if n==0 else nod(n,m%n)
try:
    print('Формат ввода "a b c", в Диофантовом ур-ии ax+by=c')
    print('Н-р 1999 201 12')
    xna,yna,fin=[int(i) for i in input().split()]
    x,y=abs(xna),abs(yna)
    if fin%nod(x,y):print("Impossible")
    else:
        g=g(x,y)
        g.pop()
        for i in g:print('',i[3],'=',i[0],'-',i[1],'*',i[2])
        for i in g:i[0],i[1],i[2],i[3]=i[3],i[0],i[1],i[2]
        g.reverse()
        for i in g:
            if g.index(i)==0: print('--ВЫРАЖЕНИЕ-ЕДИНИЦЫ-----'); continue
            if g.index(i)>=2: break
            j=g[g.index(i)-1]
            print('',j[0],'=',i[2],'*',i[3]*j[3]+1,'-',i[1],'*',j[3])
            v=[i[2],i[3]*j[3]+1,i[1],j[3]]
        for i in range(2,len(g)):
            k=g[i]
            if v.index(k[0])==0:
                v=[k[1],v[1],v[2],v[1]*k[3]+v[3]]
                print(' 1 =',v[0],'*',v[1],'-',v[2],'*',v[3])
            elif v.index(k[0])==2:
                v=[v[0],v[1]+v[3]*k[3],k[1],v[3]]
                print(' 1 =',v[0],'*',v[1],'-',v[2],'*',v[3])
        print('--ФИНАЛЬНОЕ-ДОМНОЖЕНИЕ--\n',fin,'=',v[0],'*',v[1]*fin,'-',v[2],'*',v[3]*fin)
        input()
except Exception: print('Не дурак, сам решишь!');input()
