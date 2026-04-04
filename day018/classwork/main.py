# 1) შექმენით ფუნქცია რომელიც იღებს პარამეტრად სახელს და აბრუნებს "Hello <name>"
# 2) შექმენით ფუნქცია, რომელიც პარამეტრად მიიღებს ორ რიცხვს და დააბრუნებს მათ ჯამს
# 3) შექმენით ფუნქცია, რომელიც იღებს პარამეტრად რიცხვს და ამოწმებს რიცხვი ლუწია თუ კენტი
# 4) შექმენით ფუნქცია რომელიც პარამეტრად იღებს ორ რიცხვს და აბრუნებს ერთი რიცხვი აყვანილი მეორეს ხარისხში
# 5) შექმენით ფუნქცია რომელიც პარამეტრად იღებს ნებისმიერ string-ს და აბრუნებს მის სიგრძეს
# 6) შექმენით ფუნქცია რომელიც პარამეტრად იღებს სიტყვას და აბრუნებს მის შებრუნებულ ვერსიას
# 7) შექმენით ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ამ სიის რიცხვების ჯამს
# 8) შექმენით ფუნქცია რომელიც პარამეტრად იღებს სახელს და ასაკს, თუ სრულწლოვანია აბრუნებს "<name> is adult" სხვა შემთხვევაში "<name> is not adult"



def pers_greet(name):
    return f'Hello {name}'

print(pers_greet('luka'))




def nums(x, y):
    return x + y

print(nums(5, 5))





def even_or_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
print(even_or_odd(5))





def nums(x, y):
    return x ** y

print(nums(5, 2))





def string_lenght(string):
    return len(string)

print(string_lenght('luka'))






def string_rev(string):
    return string[::-1]

print(string_rev('luka'))





def lists(list):
    return sum(list)

print(lists([1, 2, 3, 4]))
