

// 1) შექმენით ორი სხვადასხვა ცვლადი let-ის გამოყენებით: word1, word2.
// ორივეში შეინახეთ სხვადასხვა სტრინგი და გამოიტანეთ კონსოლში. გამოიყენეთ შესაბამისი მეთოდები,
// რომ გადაიყვანოთ პირველი სტრინგი დიდ ასოებად, ხოლო მეორე პატარა ასოებად და შეინახეთ ისინი ახალ ცვლადებში (შემდეგ ისევ გამოიტანეთ კონსოლში).

// 2) გამოიყენეთ დღეს ნასწავლი მეთოდი, რომ ამ სტრინგს მოაშოროთ ცარიელი სფეისები:
// const variable = '     Group 71      '

// 3) კომენტარის სახით ახსენით რას აკეთებს - Math.random() და Math.floor()

// 4) დააგენერირეთ რენდომ რიცხვი 0-დან 96-მდე და გამოიტანეთ კონსოლში. ეს რიცხვი აუცილებლად უნდა იყოს მთელი.





let world1 = 'rame'
let world2 = 'RAIME'

console.log(world1)
console.log(world2)


world1 = world1.toUpperCase()
world2 = world2.toLowerCase()

console.log(world1)
console.log(world2)








const variable = '     Group 71      '

console.log(variable.trim())










// Math.random()_ს გამოაქვს რენდომ რიცხვი 0_დან 1_მდე
// Math.floor()_ს გამოაქვს წილადის მთელი რიცხვი(დაბალი)









console.log(Math.floor(Math.random() * 96))


