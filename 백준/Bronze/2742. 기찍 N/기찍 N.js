const fs = require("fs");
const nString = fs.readFileSync("dev/stdin").toString().trim();
// const nString = fs.readFileSync("example.txt").toString().trim();

const n = parseInt(nString, 10);
let result = [];

for (let i = n; i > 0; i--) {
  result.push(i);
}

console.log(result.join("\n"));