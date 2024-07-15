const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const numbers = input.map(number => number.split(' ').map(Number));

const scale = Math.max(...numbers.flat())

let arr = new Array(scale);

for (let i = 0; i < arr.length; i++) {
    arr[i] = new Array(scale).fill(0);
}

for (let i = 0; i < 4; i++) {
    const [x1, y1, x2, y2] = numbers[i];

    for (let x = x1; x < x2; x++) {
        for (let y = y1; y < y2; y++) {
            arr[x][y] = 1;
        }
    }
}

let result = 0
arr.flat().forEach(x => {
    result += x
});

console.log(result);