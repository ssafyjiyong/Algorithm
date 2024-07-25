const fs = require('fs');
// const [nString, ...input] = fs.readFileSync("example.txt").toString().trim().split("\n");
const [nString, ...input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [rowString, colString] = nString.split(" ");
const row = parseInt(rowString);
const col = parseInt(colString);

function paintCount (chessBoard, startColor) {
    const line = startColor === 'B' ? ['B','W'] : ['W','B'];
    let count = 0;

    for (let i = 0; i < 8; i++) {
        for (let j = 0; j < 8; j++) {
            if (chessBoard[i][j] !== line[(i + j) % 2]) {
                count++;
            }
        }
    }

    return count;
}

let minCount = 99999;

for (let i = 0; i <= row - 8; i++) {
    for (let j = 0; j <= col - 8; j++) {
        const boardForCheck = new Array(8).fill().map(() => new Array(8).fill(0))
        for (let k = 0; k < 8; k++) {
            for (let l = 0; l < 8; l++) {
                boardForCheck[k][l] = input[i + k][j + l];
            }
        }
        const result1 = paintCount(boardForCheck, 'B');
        const result2 = paintCount(boardForCheck, 'W');
        minCount = Math.min(minCount, result1, result2);
    }   
}

console.log(minCount);