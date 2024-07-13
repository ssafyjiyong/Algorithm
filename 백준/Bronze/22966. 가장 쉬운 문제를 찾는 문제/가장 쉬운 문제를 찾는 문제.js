const fs = require('fs');
// const input = fs.readFileSync("example.txt").toString().trim().split("\n");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = parseInt(input[0], 10);
let minimum = 5;
var result = '';

for (let i = 1; i < n+1; i++) {
    if (input[i].split(" ")[1] < minimum) {
        minimum = input[i].split(" ")[1];
        result = input[i].split(" ")[0];
    }
}

console.log(result);