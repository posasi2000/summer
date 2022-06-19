m = 800
rate = 12.34
total = m*rate

print('타입 =', type(m))
print('주소 =', id(m))
print('타입 =', type(rate))
print('주소 =', id(rate))
print('총금액 =', (total))
print()  
# >오른쪽맞춤 의미
print('{:0>12,}'.format(total))   #000009,872.0
print('{:*>12,}'.format(total))   #*****9,872.0
print('{:,}'.format(total))	      #9,872.0

print()
msg=1234
print('|{}|'.format(msg))	   # |1234|
print('|{:^10}|'.format(msg))  # |   1234   |
print('|{:>10}|'.format(msg))  # |      1234|
print('|{:<10}|'.format(msg))  # |1234      |
print()