const fs = require("fs");
const lst = fs.readFileSync("dev/stdin").toString().trim().split(/\r?\n/);
// const lst = fs.readFileSync("example.txt").toString().trim().split(/\r?\n/);

const n = parseInt(lst.shift(), 10);
const answer = [];

while (1) {
  if (lst[0] === "KBS1" && lst[1] === "KBS2") {
    break;
  }

  if (lst[0] === "KBS1") {
    for (let i = 0; i < lst.length; i++) {
      if (lst[i] === "KBS2") {
        for (let j = 0; j < i; j++) {
            answer.push(4);
            [lst[i-j], lst[i-j - 1]] = [lst[i-j - 1], lst[i-j]];
        };       
        break;
      } else {
        answer.push(1);
      }
    }
  } else {
    for (let i = 0; i < lst.length; i++) {
      if (lst[i] === "KBS1") {
        for (let j = 0; j < i; j++) {
            answer.push(4);
            [lst[i-j], lst[i-j - 1]] = [lst[i-j - 1], lst[i-j]];
        };
        break;
      } else {
        answer.push(1);
      }
    }
  }
}

console.log(answer.join(""));