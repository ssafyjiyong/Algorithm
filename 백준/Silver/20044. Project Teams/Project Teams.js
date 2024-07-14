const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0], 10);
const arr = input[1].split(' ').map(Number);

const ordinaryarr = arr.slice().sort((a, b) => a - b);
const reversearr = arr.slice().sort((a, b) => b - a);

const resultarr = [];

for (let i = 0; i < n; i++) {
    const temp = ordinaryarr[i] + reversearr[i];
    resultarr.push(temp);
}

console.log(Math.min(...resultarr));