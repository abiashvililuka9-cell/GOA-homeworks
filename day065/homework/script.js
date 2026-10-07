let i = 1;
while (i <= 10) {
    console.log(i);
    i++;
}


let sum = 0;
let num = 1;
while (num <= 100) {
    sum += num;
    num++;
}
console.log(sum);


let targetNum = 7;
let multiplier = 1;
while (multiplier <= 10) {
    console.log(`${targetNum} x ${multiplier} = ${targetNum * multiplier}`);
    multiplier++;
}


let numbersList = [12, 7, 22, 15, 44, 9, 18];
let index = 0;
while (index < numbersList.length) {
    if (numbersList[index] % 2 === 0) {
        console.log(numbersList[index]);
    }
    index++;
}


let correctPassword = "mySecretPassword123";
let enteredPassword = "";

while (enteredPassword !== correctPassword) {
    enteredPassword = prompt("Enter your password:");
}
console.log("Access granted!");


let values = [2, 5, 8, 11, 14];
let idx = 0;
while (idx < values.length) {
    console.log(values[idx] * 2);
    idx++;
}


let numsArray = [10, 14, 21, 25, 30];
let k = 0;
while (k < numsArray.length) {
    console.log(numsArray[k] % 3);
    k++;
}


for (let row = 0; row < 5; row++) {
    let line = "";
    for (let col = 0; col < 5; col++) {
        line += "* ";
    }
    console.log(line);
}


for (let row = 1; row <= 10; row++) {
    let tableRow = "";
    for (let col = 1; col <= 10; col++) {
        tableRow += (row * col).toString().padStart(4, " ");
    }
    console.log(tableRow);
}


let array1 = [1, 3, 5, 7, 9, 11];
let array2 = [3, 6, 9, 12, 5];

for (let a = 0; a < array1.length; a++) {
    for (let b = 0; b < array2.length; b++) {
        if (array1[a] === array2[b]) {
            console.log(array1[a]);
        }
    }
}


let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
let matrixSum = 0;

for (let r = 0; r < matrix.length; r++) {
    for (let c = 0; c < matrix[r].length; c++) {
        matrixSum += matrix[r][c];
    }
}
console.log(matrixSum);