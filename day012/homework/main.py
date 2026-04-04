num = int(input('enter number: '))

if num % 2 == 1:
    print('kenti')
else:
    print('luwi')


temp = int(input('enter temperature: '))

if temp > 30:
    print('its hot')
elif temp > 15 and temp <30:
    print('its warm')
else:
    print('its cold')


num = int(input('enter number: '))

if num > 0:
    if num % 2 == 0:
        print('positive even')
    else:
        print('positive odd')
else:
    print('negative')


num = int(input('enter number: '))

for i in range(0, num+1):
    if i % 2 == 0:
        print('even')
    else:
        print('odd')


pos = 0
neg = 0
zero = 0

for i in range(10):
    num = int(input('enter number: '))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print('positive is: ', pos, 'negative is: ', neg, 'zero is: ', zero)


fruits = ["apple", "banana", "orange", "grape"]
fruits[1] = 'kiwi'
print(fruits)

nums = [4, 8, 12, 16, 20]
result = nums[0] + nums[-1]
print(result)

num = [1, 2, 3, 4, 5]
for i in num:
    print(i)


num = [1, 2, 3, 4, 5]
for i in num:
    if i % 2 == 0:
        print(i)



num = [1, 2, 3, 4, 5]

for i in num:
    if i % 2 == 0:
        i += 0
    print(i)



nums = [3, 4, 5, 6, 7, 8, 9]

for i in nums:
    if i > 6:
        print(i)



name = ('luka')
print(name[0])
print(name[1])
print(name[2])
print(name[3])


nums = [1, 2, 3, 4, 5]
print(nums[0], nums[1], nums[2])




