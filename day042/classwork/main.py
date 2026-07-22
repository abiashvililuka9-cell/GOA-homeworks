# 1) მომხმარებელს შეაყვანინეთ ორი რიცხვი
# • და სცადეთ მათი გაყოფა
# • დაიჭირეთ:
# • ValueError
# • ZeroDivisionError
# თითოეული Exception-ის შემთხვევაში განსხვავებული შეტყობინება დაბეჭდეთ.

# 2) მომხმარებელს შემოატანინეთ რიცხვი. 
# თუ ის ტექსტს შეიყვანს გაისროლეთ ValueError და დაბეჭდეთ:
# "Please Enter numbers only."





try:
    num1 = int(input('enter number: '))
    num2 = int(input('enter number 2: '))
    result = num1/num2
    print(f'result: {result}')
except ValueError:
    print('please enter numbers')
except ZeroDivisionError:
    print('dont use 0')









try:
    num = int(input('enter number: '))
    print('good boy')
except ValueError:
    print("Please Enter numbers only.")
