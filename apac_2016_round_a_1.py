t=int(raw_input())
for _ in range(0,t):
	n=int(raw_input())
	ans_c=0
	ans=''
	for __ in range(0,n):
		count=0
		l=[0]*26
		s=raw_input()
		for i in s:
			if (ord(i)>=65 and ord(i)<=90):#(ord(i)>=97 and ord(i)<=122) or 
				l[ord(i)-65]=1
		count = l.count(1)
		if count>ans_c:
			ans_c=count
			ans = s
		if count==ans_c:
			ans = min(ans,s)
	print 'Case #'+str(_+1)+': '+str(ans)