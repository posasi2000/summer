import time


data = [33,'bc',77,'book']
print(data[-4], end=' ')
print(data[-3], end=' ')
print(data[-2], end=' ')
print(data[-1], end=' ')
print()
print('- ' * 30)
#문제 data리스트를 for반복문으로 출력 
for a in range(4):
    print(data[a], end=' ')

print()
print('- ' * 30)
for b in data:
    print(b,  end=' ')

print()
print(data)  #[  ]

print( ' test  test ') 


