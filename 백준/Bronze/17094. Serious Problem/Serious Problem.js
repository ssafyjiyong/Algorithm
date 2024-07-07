const fs = require('fs');
const [nString, input] = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(nString, 10);

let num = 0;
let spell = 0;   
for (let i = 0; i < n; i++) {
    if (input[i] === 'e') {
        spell ++;
    } else {
        num ++;
    }
}

if (spell > num) {
    console.log('e');
} else if (spell < num) {
    console.log('2');
} else {
    console.log('yee');
}