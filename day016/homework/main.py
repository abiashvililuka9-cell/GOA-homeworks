num1 = int(input('enter number: '))
num2 = int(input('enter number 2: '))
num3 = int(input('enter number 3: '))
num4 = int(input('enter number 4: '))
num5 = int(input('enter number 5: '))

numbers = [num1, num2, num3, num4, num5]
print(sum(numbers) / len(numbers))




sentence = input('enter your sentence: ')

print(len(sentence))




password = input('enter your password: ')

if password.find('1') == 1:
    print('password contains 1')
else:
    print('password doesnt contain 1')
არ შვება




fruits = ['apple', 'banana', 'orange', 'mango']

fruits.append('cherry')
fruits[3] = 'Blueberry'
print(fruits)




word = input('enter your word: ')

if word == word.capitalize():
    print('perfect')
else:
    print('Your word should be capitalized!')




name = input('enter your name: ')

print(name.upper())
print(name.lower())




myname = 'luka'
yourname = input('enter your name: ')

if myname.lower() == yourname.lower():
    print("Our names are similar!")
else:
    print("We have different names")




name = 'luka'

print(name.find('l'))




fruits = ['apple', 'banana', 'mango']
for i in range(len(fruits)):
    fruits[i] = fruits[i].upper()

print(fruits)




data_list = []

for i in range(3):
    item = input(f"Enter item {i+1}: ")
    data_list.append(item)

print(data_list)