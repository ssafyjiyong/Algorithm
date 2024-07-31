const fs = require('fs');
const [nString, [...input]] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = parseInt(nString, 10)
let result = 0;
let value = 1;
const MOD = 1234567891;

for (let i = 0; i < input.length; i++) {
    result = result + ((input[i].charCodeAt()-96) * value) % MOD;
    value = (value * 31) % MOD;
}

if (result > MOD) {
    result %= MOD;
}

console.log(result);