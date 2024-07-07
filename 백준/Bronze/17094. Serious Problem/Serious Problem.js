const fs = require('fs');
const [nString, input] = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(nString, 10);

const spell = input.split('').filter(char => char === 'e').length;

const num = n - spell;

if (spell > num) {
    console.log('e');
} else if (spell < num) {
    console.log('2');
} else {
    console.log('yee');
}
