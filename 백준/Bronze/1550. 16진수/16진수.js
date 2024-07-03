const fs = require('fs');
// const input = fs.readFileSync("example.txt").toString().trim();
const input = fs.readFileSync("/dev/stdin").toString().trim();

const output = parseInt(input, 16);

console.log(output);