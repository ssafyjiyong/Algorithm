const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0], 10);
const tShirtsArr = input[1].split(' ').map(Number);
const countArr = input[2].split(' ').map(Number);

const T = countArr[0];
const P = countArr[1];

let tResult = 0;

tShirtsArr.forEach(item => {
    tResult += Math.ceil(item/T);
});

console.log(tResult);
console.log(Math.floor(n / P), n % P);