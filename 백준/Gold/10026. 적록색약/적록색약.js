const fs = require('fs');
const [nString, ...tmpLst] = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

const n = parseInt(nString);
const lst = tmpLst.map(ele => ele.trim().split(''));

const otherLst = lst.map(line => {
    return line.map(ele => {
        if (ele === 'G') {
            return 'R'
        } else {
            return ele;
        }
    })
})

const direction = [[1,0],[-1,0],[0,-1],[0,1]]

function bfs(x, y, lst, visited) {
    const queue = [[x,y]];
    visited[x][y] = true;
    const color = lst[x][y];

    while (queue.length>0) {
        const [curX, curY] = queue.shift();

        for (let [dx, dy] of direction) {
            const newX = curX + dx
            const newY = curY + dy
    
            if (newX >= 0 && newX < n && newY >= 0 && newY < n && !visited[newX][newY] && lst[newX][newY] === color) {
                queue.push([newX, newY]);
                visited[newX][newY] = true;
            }
        }
    }
}

const visited = Array.from({length:n}, () => Array(n).fill(false));
const otherVisited = Array.from({length:n}, () => Array(n).fill(false));

let count = 0;
let otherCnt = 0;

for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        if (!visited[i][j]) {
            bfs(i, j, lst, visited);
            count++;
        }
    }
}

for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
        if (!otherVisited[i][j]) {
            bfs(i, j, otherLst, otherVisited);
            otherCnt++;
        }
    }
}

console.log(count, otherCnt);