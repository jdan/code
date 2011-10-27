h,s='.;*&8#',''
for q in range(801):
 if q%40==0:print s;s=''
 i,k=0,0
 while(abs(k)<2*(i<15)):k,i=k**2+complex(q%40*.075-2,q/40*-.1+1),i+1
 s+=h[i/3]