// შექმენით ორი მასივი: languageA, languageB. სადაც 5-5 ელემენტს მოათავსებთ. თქვენი დავალებაა გამოიყენოთ forLoop-ი, 
// რომ დაადგინოთ ამ ორ მასივს შორის არის თუ არა საერთო ელემენტები. თუ აღმოაჩენთ - კონსოლში დალოგეთ 'found mutual language: {...}'



// let languageA = ['inglisuri', 'qartuli', 'franguli', 'rusuli', 'romauli']
// let languageB = ['inglisuri', 'italiuri', 'qartuli', 'rusuli', 'iaponuri']


// for (let i = 0; i <= languageA.length; i++){
//     for (let j = 0; j <= languageB.length; j++){
//         if (languageA[i] == languageB[j]){
//             console.log(`found mutual language: ${languageA[i]}`)
//         }
//     }
// }











// 2) შექმენით fruits მასივი: ['apple', 'cherry', 'melon']
// დაწერეთ while loop-ის პროგრამა, math.random-ის საშუალებით currentFruit-ში ყოველ ჯერზე რენდომული მნიშვნელობა ჩაიწერება, სანამ 'cherry' მნიშვნელობა არ ჩაჯდება currentFruit-ში, იქამდე გააგრძელეთ ძებნა.




let fruits = ['apple', 'cherry', 'melon']

let currentFruit = ''

while (currentFruit !== 'cherry'){
    let rendomindex = Math.floor(Math.random() * fruits.length - 1)
    currentFruit = fruits[rendomindex]
    console.log(currentFruit)
}
