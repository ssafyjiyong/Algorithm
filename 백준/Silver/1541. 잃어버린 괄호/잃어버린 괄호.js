const fs = require('fs');
const string = fs.readFileSync("/dev/stdin").toString().trim();

const lst = [...string];

const ansLst = [];
let numTest = ''

for (let x of lst) {
    if (x == '+' || x == '-') {
        ansLst.push(Number(numTest));
        numTest = '';
        ansLst.push(x);
    } else {
        numTest += x;
    }
}

ansLst.push(Number(numTest));

let flag = 0
let answer1 = 0
let answer2 = 0

for (let x of ansLst) {
    if (typeof x === 'number') {
        if (flag === 0) {
            answer1 += x;
        } else {
            answer2 += x;
        }
    } else {
        if (x === '-') {
            flag = 1;
        }
    }
}

if (answer1===0 || answer2===0) {
    console.log(answer1+answer2);
} else {
        console.log(answer1-answer2);
}