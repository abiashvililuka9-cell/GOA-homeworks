let fruits = ["Apple", "Banana", "Orange", "Mango"];
console.log(`There are ${fruits.length} items in the array`);





let todoList = [];
todoList.push("learn");
todoList.push("workout");
todoList.push("rest");
console.log(todoList);






let numbers = [10, 20, 30, 40, 50];
let removedNumber = numbers.pop();
console.log(numbers);
console.log(removedNumber);





let colors = ["Red", "Green", "Blue", "Yellow", "Purple"];
console.log(colors.at(0));
console.log(colors.at(-1));






let queue = ["Giorgi", "Ana", "Nika", "Mariam"];
queue.shift();
console.log(queue);






let frontEnd = ["HTML", "CSS", "JS"];
let backEnd = ["Node.js", "Python"];
let fullStack = frontEnd.concat(backEnd);
console.log(fullStack);







let animals = ["Dog", "Cat", "Bear", "Wolf"];
console.log(animals.indexOf("Cat"));
console.log(animals.indexOf("lion"));









let days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
let workDays = days.slice(0, 5);
console.log(workDays);









let randomMovies = ["Inception", "Interstellar"];
randomMovies.unshift("The Dark Knight");
console.log(randomMovies);








let scores = [50, 65, 78, 92, 45, 88, 99];
let topScores = scores.slice(-3);
console.log(topScores);








let searchHistory = [];
searchHistory.push("google.com", "github.com", "youtube.com");
searchHistory.pop();
searchHistory.push("stackoverflow.com");
console.log(searchHistory.length);
console.log(searchHistory.at(-1));








let shoppingList = ["bread", "milk", "cheese", "eg"];
console.log(shoppingList.indexOf("cheese"));