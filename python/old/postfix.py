e,a,s=raw_input('? '),[0]*99,-1
for c in e:
    if c in '+*-/': exec('x=%s%s%s'%(a[s-1],c,a[s]));s-=1;a[s]=x
    else: s+=1;a[s]=c
print a[0]
