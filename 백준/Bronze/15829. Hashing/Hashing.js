const fs = require('fs');
// const [nString, [...input]] = fs.readFileSync("example.txt").toString().trim().split("\n");
const [nString, [...input]] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = parseInt(nString, 10)
let result = 0;

for (let i = 0; i < input.length; i++) {
    result += (input[i].charCodeAt()-96) * 31**i
}

console.log(result);