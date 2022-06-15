print('- ' * 50 )

money = 800
rate = 12.34 
total = money * rate
print('총금액 =', total)
print('총금액 = {:,}'.format(total))	      #9,872.0
print('총금액 = {:*>12,}'.format(total))      #*****9,872.0
print()

# print('총금액 = {,}'.format(total))	         #9,872.0
# print('총금액 = {*>12,}'.format(total))      #*****9,872.0


#문제 천단위 , 표시
#문제 *****9,872.0천단위 