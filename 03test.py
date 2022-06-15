def  pyData(*param):
    print(type(param)) #타입 tuple
    total = 0
    for k in param:
        total = total + k
    return total


def display(**pm):
    print(type(pm)) #타입 dict
    for k,j in pm.items():
        print(k , ':', j)

print()
a = pyData(1,2,3,4,5)
print('총합계 =',a)

print('- ' * 50)
#db = { 'dbName':'guest', 'userid':'red', 'userpwd':1234, 'flag':False }
#display(db)
display(dbName='board', userid='sky', userpwd=1234, flag=True)

#3시 30분에 시작합니다 