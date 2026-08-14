/*
let inner = myfun();
inner();
*/
/*function makeQueue()
{
    let number = 0 ;

 return{
    next(){ number++; return number;},
    current() {return number ;},
 };
 const bank = makeQueue();
    bank.next();
    banc.next();
    bank.current();
}
console.log(makeQueue);
*/
/*unction sum(a,b){
    return a+b;
}
function subtract(a,b){
    return a-b;
}
function divid(a,b){
    return a-b
}
function adder(num1,num2,fun){
    return fun(num1,num2)
} 
console.log(adder(1,2 ,sum))
console.log(adder(45,10,subtract))
console.log(adder(45,10,divid))
*/
/*
function makeRecriptMaker(){
    let orderNo=0;
    const mamberOff = discountBy(0.1)
    return function
}
*/
/*declaration
function multiply(x,y)
{
    return x*y;
}
/*exprassion
const multiply = function(x,y){
   return x*y 
};

/*expreasion the function has itsown name
const multiply  = function funName(x,y){
  return x*y4
}

//arrow function
const multiply = (x,y) => x*y;
*/
//normal expression
/*const vat = function (n) {
    return n * 0.15; };
//arrow - same thing, shorter
const vat = n => { return n * 0.15;}
//one expression  implicit return
const vat = n => n * 0.15;

vat(429)
*/

function makeGreater(city) {
  //inner function "closes over" city
  return function (name) {
    return `selam ${name}, from ${city}`;
  };
}
const addis = makeGreater("Addis ababa");
addis("Almaz");

function makeQueue(){
    let number = 0;
return{
    next(){ number++; return number},
    Current(){return number;},
};
}
const bank = makeQueue(); //CBE counter
console.log (bank.next());
console.log (bank.next());
console.log (bank.Current());

function onec(fn){
    let called = false;  //pvt flag
 return function (...args){
    if (called) return;
    called = true;
    return (fn(...args));
 };
}





// "do something to each item"
function forEachPrice(prices, action) {
for (const p of prices) {
action(p); // call what we got
}
}
forEachPrice([120, 200, 160], price => {
console.log(`${price} ETB`);
});

let fruit = "apple"; 

if (fruit !== "banana") {
    let fruit = "banana";
    console.log(fruit);   
}
console.log(fruit);

function forEachPrice(price,action) {
    
}

