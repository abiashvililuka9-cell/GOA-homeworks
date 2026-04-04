# შედარების ოპერატორები

# > - მეტია
# < - ნაკლებია
# >= - მეტია ან ტოლია
# <= - ნაკლებია ან ტოლია
# == - უდრის (ამოწმებს როგორც მონაცემს, ასეევე მონაცემების ტიპს)
# != - არ უდრის (ამოწმებს როგორც მონაცემს, ასეევე მონაცემების ტიპს)


# ლოგიკური ოპერატორები

# and - და, არის მკაცრი ოპერატორი, თუ მაგალითად ორი მოქმედებიდან ერთი მაინც არის false მაშინ ტერმინალშიც გამოიტანს false_ს
# or - ან, არის შედარებით არამკაცრი ოპერატორი, თუ ორი მოქმედებიდან ერთი მაინც იქნება true მაშინ ის ტერმინალშიც გამოიტანს true_ს




userheight = int(input())
print(bool(180 <= userheight))



num1 = "21"
num2 = 21
print(num1 == num2)  #გამოიტანს False რადგან num1 ცვლადი არის სტრინგი(str) ხოლო num2 ცვლადი არის ინტეჯერი, და თუ ჩვენ ამ ორს ერთმანეთს გავუტოლებთ მაშინ გამოიტანს False რადგან სტრინგი ინტეჯერის ტოლი არარის




name = 'luka'
user_name = input('enter your name:')
print(name == user_name)




print(False or True and True and False) #გამოიტანს False რადგამ False or True არის True,  True or True არის True და True and False არის False

print(True and False or False or True) #გამოიტანს True რადგან True and False არის False,  False or False არის False და False or True არის True

print(True or True and False or True or False and True or False) #გამოიტანს True რადგან True or True არის True,  True and False არის false,  False or True არის True,  True or False არის True,  True or True არის True და True or False არის False




temperature = int(input('enter temperature:'))
print((30 < temperature))





