const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0], 10);
const arr = input[1].split(' ').map(Number);

arr.sort((a, b) => a-b)

const resultarr = [];

for (let i = 0; i < n; i++) {
    const temp = arr.pop() + arr.shift()
    resultarr.push(temp);
}

console.log(Math.min(...resultarr));