#25
a=input().split()
b=list(map(int,input().split()))
date=dict(zip(a,b))

del date['alpha']
del date['delta']
print(date)

#26
park={'korean':94, 'english':91, 'mathematics':89, 'science':83}
print(park['english'])
print(park['science'])

#27
kim={'korean':94, 'english':91, 'mathematics':89, 'science':83}
kim.update(korean=100, englis=100,mathematics=100, science=100)
print(kim)

#28
lee={'korean':94, 'english':91, 'mathematics':89, 'science':83}
if 'english' in lee:
    del lee['english']
    print('삭제')
else:
    print('english가없음')

print(lee)
    
#29
lim={'korean':94, 'english':91, 'mathematics':89, 'science':83}
print(lim.items())

#30
choi={'korean':94, 'english':91, 'mathematics':89, 'science':83}
x={key:value for key, value in choi.items() if value>=90}
print(x.keys())

#31
yoo={'korean':94, 'english':91, 'mathematics':89, 'science':83}
scores=yoo.values()
total=sum(scores)
count=len(scores)
average=total/count

print(average)