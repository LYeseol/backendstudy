var num = "20";
num = num.toString();
console.log(typeof num);

var number = 20;
console.log(typeof number);

number = number.toString();
console.log(number, typeof number);

var x = 2.5678;
//toFixed - 숫자를 고정 소수점 표기법으로 표기해 반환합니다. 
console.log(x.toFixed(1), typeof x.toFixed(1)); // 2.6 string
console.log(x.toFixed(2)); //2.57 srting

//toPrecision- 고정 소수점 또는 지수 표기법의 수를 정밀 유효 숫자로 반올림 한 문자열을 반환합니다. 
console.log(x.toPrecision(1), typeof x.toPrecision(1));  // 3 string
console.log(x.toPrecision(2)); //2.6

console.log(Number(true));
console.log(Number(false) );
console.log(Number("10"));
console.log(Number(" 10 "));
console.log(Number("10.25"));
// var text = prompt("Enter your name: ");
// document.write("Your name: "+text +"<br/>");

// var len = text.length;
// document.write("Number of  characters: "+ len+ " <br/>");

// document.write(text.charAt(2)+ "<br/>");

// // 모두 대문자, 소문자로 바꾸기
// document.write(text.toUpperCase()+ '<br/>');
// document.write(text.toLowerCase()+ '<br/>');

// var text1 = " hi ";
// var text2= "bye";
// var text3= text1.concat(text2);
// var text4 = text1+text2;
// document.write(text3+"<br/>");
// document.write(text4+"<br/>");

// var text5 = "hello";
// document.write("Original text5: "+ text5+ "<br/>")
// var result = text5.slice(1,3); // 0-1 index text
// document.write(result + "<br/>");

// var lName = "이";
// var fName = "예슬";

// var fullName= lName+fName;

// console.log(fullName);
// console.log("Today is"+ " a "+ "beautiful day");
// console.log("My name is "+ fullName);

// var num1 = 20;
// var num2 = 30;
// var sum = num1+num2;
// console.log(""+num1+num2);
// console.log(num1+ " + "+ num2 + " = "+ sum);



// var name= "이예슬";
// var age = 29;
// var cgpa = 4.3;
// var lineBreak="<br/>"

// document.write("이름: "+ name + lineBreak);
// document.write("나이: "+ age + lineBreak);
// document.write("학점: "+ cgpa + lineBreak);

// console.log(typeof 123);
// console.log(typeof 123.5);
// console.log(typeof "123");
// console.log(typeof true);
// console.log(typeof false);

// var car;
// console.log(car);
// var car ="";
// console.log(typeof car);
// var person ={firstName:"John", lastName:"Doe", age:50, eyeColor:'blue'};
// console.log(typeof person);
// person= null;

// console.log(typeof person);


// document.write("Hello world");
// document.write("<h1>Welcome to JS Program</h1>");
// document.write("<h2>Welcome to JS Program</h2>");

// console.log("Welcome JS Program");
// console.info( "Welcome JS Program");
// console.warn( "Welcome JS Program");
// console.error("Welcome JS Program");

// alert('Welcome JS Program');
// var a = prompt("Welcome JS Program");
// console.log(a);

