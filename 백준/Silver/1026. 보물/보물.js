const fs = require('fs');
// const [nString, arrAString, arrBString] = fs.readFileSync("example.txt").toString().trim().split("\n");
const [nString, arrAString, arrBString] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = parseInt(nString, 10);

const arrA = arrAString.split(" ").map(Number);
const arrB = arrBString.split(" ").map(Number);

arrA.sort((a, b) => a - b);
arrB.sort((a, b) => b - a);

let result = 0;

for (let i = 0; i < n; i++) {
    result += arrA[i] * arrB[i]
};

console.log(result);