// 1) ახსენით რა არის ES6 და EcmaScript კომენტარების სახით
// 2) შექმენი ცვლადი name რომელიც იქნება falsy - ს ტოლი და nickname 
// რომელსაც მნიშნველობა არ ექნება მინიჭებული, შემდეგ if - else - ის გამოყენებით შეამოწმე, თუ name იქნება truthy, nickname გახდეს nameს ტოლი, სხვა შემთხვევაში "stranger"

// 3) შექმენი ცვლადი day = 5; Switch - ის გამოყენებით:
// თუ day იქნება 1 - ის ტოლი --> Monday
// თუ day იქნება 2 - ის ტოლი --> Tuesday
// და ასე შემდეგ



// ES6 არის javascript_ის მნიშვნელოვანი დამატება სადაც დაემატა ბევრი შესაძლებლობები(let, const და ა.შ)
// EcmaScript კი განსაზღვრავს javascript_ის ენის მტავარ წესებს






let name1 = "";
let nickname;

if (name1) {
    nickname = name;
} else {
    nickname = "stranger"
}





let day = 5;

switch (day) {
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("Tuesday")
        break;
    case 3:
        console.log("Wednesday");
        break;
    case 4:
        console.log("Thursday")
        break;
    case 5:
        console.log("Friday")
        break;
    case 6:
        console.log("Saturday");
        break;
    case 7:
        console.log("Sunday");
        break
    default:
        console.log("Invalid number")
}

