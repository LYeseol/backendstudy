
//모음자음 구분하기
var letter = prompt("Enter a letter: ");

letter =letter.toLowerCase();

if(letter == 'a'|| letter=='e' || letter=='i'|| letter =='o'|| letter =='u'){
    console.log('Vowel');
}else{
    console.log('Consonant');
}



// var num1 = parseInt(prompt("첫번째 숫자 입력: "));
// var num2 = parseInt(prompt("두번째 숫자 입력: "));

// if(num1 > num2){
//     console.log("큰 수는 num1 :"+ num1);
// }
// if(num1<num2){
//     console.log("큰 수는 num2: "+ num2);
// }

// if(num1 == num2){
//     console.log("같은 수 : "+ num1);
// }

// if(num1>num2){
//     console.log("큰 수 num1: "+ num1 );
// }else if(num1<num2){
//     console.log("큰 수 num2: "+ num2);
// }else{
//     console.log("같은 수");
// }


// //비교연산자
// var num1 = 20;
// var num2 = 10;
// var num3 = "10";
// var num4 = 20;
// var num5 = 15;

// console.log("일반 크기 비교");
// console.log(num1>num2, num1,'>', num2);
// console.log(num1>=num2, num1, '>=', num2);
// console.log(num1<num2, num1, '<', num2);
// console.log(num1<=num2, num1, '<=', num2);

// console.log("같은지 여부 확인");
// console.log(num1==num4, num1, '==', num4);
// console.log(num1!=num4, num1, '!=', num4);

// console.log("===");
// console.log(num1===num3, num1, '===', num3);

// console.log(num2===num3, num2, '===', num3);
// console.log(num2==num3, num1, '==', num3);

// // 논리연산자
// console.log("논리 연산자");
// console.log('num1>num2 && num1< num5', num1>num2 && !(num1< num5));
// console.log('num1>num2 || num1> num5', num1>num2 || num1> num5);



// var cels = parseFloat(prompt("Enter cels: "));
// var farn = cels *( 9/5 )+32;

// document.write("화씨: "+ farn);


// var base = parseFloat(prompt(" Enter 밑변: "));
// var height = parseFloat(prompt(" Enter 높이: "));

// var area = 0.5*base*height;

// document.write("Triangle Area: "+ area+ "<br/>")



// //input으로 두 숫자 받기
// var num1 = parseInt(prompt("Enter first number: "));
// var num2 = parseInt(prompt("Enter second number: "));
// var lineBreak = "<br/>"
// //덧셈
// var result = num1+num2;
// document.write("The sum is: "+ result+ lineBreak);
// //뺄셈
// var result = num1-num2;
// document.write("The sub is: "+ result+ lineBreak);
// //곱셈
// var result = num1*num2;
// document.write("The mult is: "+ result+ lineBreak);
// //나누기
// var result = num1 / num2;
// document.write("The division is: "+ result.toPrecision(3)+ lineBreak);
// //나머지
// var result = num1 %num2;
// document.write("The remainder is: "+ result+ lineBreak);



// var num = "20";
// num = num.toString();
// console.log(typeof num);

// var number = 20;
// console.log(typeof number);

// number = number.toString();
// console.log(number, typeof number);

// var x = 2.5678;
// //toFixed - 숫자를 고정 소수점 표기법으로 표기해 반환합니다. 
// console.log(x.toFixed(1), typeof x.toFixed(1)); // 2.6 string
// console.log(x.toFixed(2)); //2.57 srting

// //toPrecision- 고정 소수점 또는 지수 표기법의 수를 정밀 유효 숫자로 반올림 한 문자열을 반환합니다. 
// console.log(x.toPrecision(1), typeof x.toPrecision(1));  // 3 string
// console.log(x.toPrecision(2)); //2.6

// console.log(Number(true));
// console.log(Number(false) );
// console.log(Number("10"));
// console.log(Number(" 10 "));
// console.log(Number("10.25"));
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

// console.debug("Welcome JS Program");
// console.log("Welcome JS Program");
// console.info( "Welcome JS Program");
// console.warn( "Welcome JS Program");
// console.error("Welcome JS Program");

// alert('Welcome JS Program');
// var a = prompt("Welcome JS Program");
// console.log(a);

