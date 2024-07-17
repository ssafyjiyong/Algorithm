const fs = require('fs');
// const [nString, ...wordslst] = fs.readFileSync("example.txt").toString().trim().split("\n");
const [nString, ...wordslst] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = parseInt(nString);
const words = Array.from(new Set(wordslst));

words.sort((a, b)=> {
    if (a.length !== b.length) {
        return a.length - b.length;
    } else {
        return a.localeCompare(b);
    }
});

words.forEach(word => {
    console.log(word);
});