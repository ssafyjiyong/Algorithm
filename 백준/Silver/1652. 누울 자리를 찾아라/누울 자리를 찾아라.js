const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().trim().split("\n");
// const input = fs.readFileSync("example.txt").toString().trim().split("\n");

function findLyingSpots(input) {
    const n = parseInt(input[0]); // 방의 크기
    const room = input.slice(1); // 방의 상태 (배열)

    let horizontal = 0; // 가로로 누울 자리 개수
    let vertical = 0; // 세로로 누울 자리 개수

    // 가로 방향 검사
    for (let i = 0; i < n; i++) {
        let count = 0;
        for (let j = 0; j < n; j++) {
            if (room[i][j] === '.') {
                count++;
            } else {
                if (count >= 2) horizontal++;
                count = 0;
            }
        }
        if (count >= 2) horizontal++; // 줄 끝까지 빈 공간이 이어질 경우 처리
    }

    // 세로 방향 검사
    for (let j = 0; j < n; j++) {
        let count = 0;
        for (let i = 0; i < n; i++) {
            if (room[i][j] === '.') {
                count++;
            } else {
                if (count >= 2) vertical++;
                count = 0;
            }
        }
        if (count >= 2) vertical++; // 열 끝까지 빈 공간이 이어질 경우 처리
    }

    console.log(`${horizontal} ${vertical}`);
}

findLyingSpots(input);
