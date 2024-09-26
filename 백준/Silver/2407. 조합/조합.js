const fs = require("fs");
const [nString, mString] = fs.readFileSync("dev/stdin").toString().trim().split(' ');
// const [nString, mString] = fs.readFileSync("example.txt").toString().trim().split(' ');

const n = parseInt(nString, 10);
const m = parseInt(mString, 10);

function factorial(n) {
  let result = BigInt(1);
  for (let i = 2; i <= n; i++) {
    result *= BigInt(i);
  }
  return result;
}

function combination(n, m) {
  return factorial(n) / (factorial(m) * factorial(n - m));
}

console.log(combination(n, m).toString());