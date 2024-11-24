const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().trim().split("\n");

function solve(input) {
    const t = parseInt(input[0]);
    const results = [];

    for (let i = 1; i <= t; i++) {
        const n = parseInt(input[i]);
        let sum = 0;

        // 홀수 합
        for (let j = 1; j <= n; j += 2) {
            sum += j;
        }

        results.push(sum);
    }

    console.log(results.join("\n"));
}

solve(input);
