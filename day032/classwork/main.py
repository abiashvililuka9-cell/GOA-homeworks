# 1) შექმენი Tuple,  რომელიც შეიცავს 5 შენს საყვარელ ფილმს. დაბეჭდე  Tuple-ის ყველა ელემენტი ცალცალკე ამ ელემენტის მონაცემის ტიპთან ერთად. (მაგ. 'Interstellar', <class 'str>)

# 2) ჩამოწერეთ რა მსგავსება და განსხვავებაა List-ებსა და Tuple-ბს შორის.

# 3) ახსენით რას აკეთებს Asterisk ოპერატორი და მოიყვანეთ მინიმუმ 2 მაგალითი.

# 4) შექმენით Tuple, სადაც შეინახავთ 7 ელემენტს. გამოიყენეთ Tuple Unpacking იმისთვის, რომ 4 სხვადასხვა ცვლადში გადაანაწილოთ Tuple-ის ელემენტები. ოთხივე ცვლადი დაბეჭდეთ ტერმინალში.



tuple1 = ('interstelar', 'gori', 'gia suramelashvilis pilmi', 'kide rame', 'da ramec')
for i in tuple1:
    print(tuple1, type(tuple1))



# tuple ში ვერ შევცვლით ანუ immutable არის და list ში შევცვლით რადგან mutable ა.
# მსგავსება არის ის რომ ორივე მიმდევრობითია



# Asterisk ოპერატორი ანუ * unpacking ისთვის
nums = (1, 2, 3, 4, 5)
a, b, *rest = nums
print(a)
print(b)





