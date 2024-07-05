const fs = require("fs");
const arr = fs.readFileSync("dev/stdin").toString().trim().split("\n");
// const arr = fs.readFileSync("example.txt").toString().trim().split("\n");

const nString = arr.shift();
const n = parseInt(nString, 10);

arr.map((item, idx) => {
  const [name, scoreString] = item.split(" ")
  const score = parseInt(scoreString, 10);
  let grade;
  if (97<=score && score<=100){
    grade = "A+";
  } else if (90<=score && score<=96){
    grade = "A";
  } else if (87<=score && score<=89){
    grade = "B+";
  } else if (80<=score && score<=86){
    grade = "B";
  } else if (77<=score && score<=79){
    grade = "C+";
  } else if (70<=score && score<=76){
    grade = "C";
  } else if (67<=score && score<=69){
    grade = "D+";
  } else if (60<=score && score<=66){
    grade = "D";
  } else {
    grade = "F";
  }
  console.log(name + " " + grade)
})