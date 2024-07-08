const fs = require('fs');
// const [nString, ...arrString] = fs.readFileSync("example.txt").toString().trim().split("\n");
const [nString, ...arrString] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const n = parseInt(nString, 10);

arrString.forEach((item, idx) => {
    const [ateString, needString] = item.split(" ");
    const ate = parseInt(ateString, 10);
    const need = parseInt(needString, 10);

    if (ate >= need) {
        console.log("MMM BRAINS");
    } else {
        console.log("NO BRAINS");
    }
});