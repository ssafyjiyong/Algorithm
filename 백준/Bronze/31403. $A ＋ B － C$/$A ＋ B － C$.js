const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const aString = input[0]
const bString = input[1]

const a = parseInt(aString, 10)
const b = parseInt(bString, 10)

const plusString = aString + bString
const plus = parseInt(plusString, 10)

const c = parseInt(input[2], 10)

console.log(a + b - c)
console.log(plus - c)