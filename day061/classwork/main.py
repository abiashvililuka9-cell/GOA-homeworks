# 1) შექმენით Cat კლასი, რომელსაც ექნება ატრიუტები: Breed და Color. მას ასევე დაუმატეთ make_sound მეთოდი, 
# რომელიც გამოძახებისას დაბეჭდავს 'Meow'ს. შექმენით მინიმუმ ორი ინსტანცია და ყველა ატრიბუტი/მეთოდი გამოიძახეთ ტერმინალში.



# 2) შექმენით კლასი iphone, რომელსაც ექნება ატრიუტები: model, price და color. მას ასევე დაუმატეთ pay მეთოდი, 
# რომელიც გამოძახებისას დაბეჭდავს 'Succesfully paid {price} dollars to buy {model}' price და 
# მოდელის მაგივრად ჩასვით ატრიბუტები საჭირო სინტაქსით. შექმენით მინიმუმ ორი ინსტანცია და ყველა ატრიბუტი/მეთოდი გამოიძახეთ ტერმინალში.




class Cat:
    def __init__(self, Breed, Color):
        self.Breed = Breed
        self.Color = Color

    def Meow():
        print('Meow')


cat1 = Cat('egvipturi', 'lurji')
print(cat1.Breed)
print(cat1.Color)
Cat.Meow()
cat2 = Cat('quchis', 'mwvane')
print(cat2.Breed)
print(cat2.Color)
Cat.Meow()







    





class Iphone:
    def __init__(self, model, price, color):
        self.model = model
        self.price = price
        self.color = color

    def Pay(self):
        print(f'Succesfully paid {self.price} dollars to buy {self.model} price')

iphone1 = Iphone('11', '1234', 'yellow')
print(iphone1.model)
print(iphone1.price)
print(iphone1.color)
iphone1.Pay()


