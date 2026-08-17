/*
const menu = ['Doro wat', 'tibs', 'Shiro'];
menu[0];
menu.lenght;
menu[menu.lenght -1];
menu.pop();
menu.push("firfir");
menu.includes("tibs");
menu.indexOf("Shiro");*/
/*
let a = 5;

function test() {
    console.log(a);

    let a = 10;

    console.log(a);
}

test();

const prices =  [120,130,400];
const withVat = prices.map(p => p * 1.15);
console.log(prices);
console.log(withVat);

const total = withVat.reduce((sum ,p) => sum + p, 0);
console.log(total)

const customer = {
    name: "aberach",
    phone:  "+251913126128",
    city:  "Addis ababa",
    member:  true ,
};
customer.name;
customer["phone"];
customer.member = false;
customer.email = "alza@34gmail.com";

Object.values
Object.keys

console.log(customer)

const account ={
    owner:"alazar",
    balance:5000,
    deposit(amount){
        this.balance += amount;
        return this.balance;
        
    },
};
account.deposit(0);
console.log(account);

const order = {
    id: 1043,
    customer:"tigist mideksa",
    items: [
        {name:"tibs", qty:2, price:322,},
        {name:"shiro", qty:2, price:120},
    ]
};
console.log (order.items[0].name);
console.log(order.items.length);
console.log(order.items
  .reduce((s,i) => s + i.qty * i.price, 0));
console.log(order)

const price = {tibs: 200, shiro:120};
for(const dish of Object.keys(price)) {
    console.log(dish);
}

//Key and value together
for (const [dish ,price] of 
    Object.entries(price)){
        console.log(`${dish}: ${price} ETB`);
    }

const user = { name: "Hanna", city: "Bole" };
// pull keys into variables by name
const { name, city } = user;
name; // "Hanna" city; // "Bole"
// rename + default
const { name: who, member = false } = user;
// arrays destructure by POSITION
const [first, second] = ["Tibs", "Shiro"];

console.log(user)

const menu = ["Tibs","Shiro"];
const copy = [...menu];

const full = [...menu,"firfir","buna"];
console.log(full);

const user = {name: "eyob" , city: "addis ababa"};
const updated = {...user , city:"kasanchis"};
console.log(updated);

const order = {
    id: 1043,
    customer:"tigist mideksa",
    items: [
        {name:"tibs", qty:2, price:322,},
        {name:"shiro", qty:2, price:120},
    ]

};
const { id, ...rest } = order;
console.log(order)
*/
export const vat = 0.15;
export const withVat = n => n *(1 + vat);

export default function format(n){
    return `${n.toFixed(2)} ETB`;
}

import format,{withVat,vat}
from "./appp.js";
format(withVat(489));