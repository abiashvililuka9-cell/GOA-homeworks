let sum = 0;
let i = 1;
do {
    sum += i;
    i++;
} while (i <= 5);
console.log(sum);



let count = 10;
do {
    console.log(count);
    count--;
} while (count >= 1);



let password;
do {
    password = prompt("Enter the password:");
} while (password !== "secret123");
console.log("Access granted!");



for (let index = 1; index <= 10; index++) {
    if (index === 6) {
        break;
    }
    console.log(index);
}



let numbers = [5, 12, 8, 130, 44];
for (let k = 0; k < numbers.length; k++) {
    if (numbers[k] > 100) {
        console.log(numbers[k]);
        break;
    }
}



let counter = 0;
while (true) {
    counter++;
    if (counter === 15) {
        break;
    }
}
console.log(counter);



let names = ["John", "Mary", "Jane", "STOP", "Patrick"];
for (let n = 0; n < names.length; n++) {
    if (names[n] === "STOP") {
        break;
    }
    console.log(names[n]);
}



let fruits = ["Apple", "Banana", "Mango", "Orange"];
fruits.forEach(fruit => {
    console.log(`My favorite fruit is ${fruit}`);
});


let numberList = [2, 4, 6, 8, 10];
let totalSum = 0;
numberList.forEach(num => {
    totalSum += num;
});
console.log(totalSum);


let prices = [10, 20, 30, 40];
prices.forEach((price, idx) => {
    console.log(`Index: ${idx}, Price: ${price}`);
});


let scores = [45, 80, 32, 95, 60, 50];
scores.forEach(score => {
    if (score >= 50) {
        console.log(score);
    }
});