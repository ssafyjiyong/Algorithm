function solution(dirs) {
    const answer = new Set();
    
    let x=0, y=0;
    
    for (let dir of dirs) {
        if (dir === "U" && y < 5) {
            let tmpX = x, tmpY = y;
            y++
            answer.add(`${x},${y},${tmpX},${tmpY}`)
            answer.add(`${tmpX},${tmpY},${x},${y}`)
        } else if (dir === "D" && y > -5) {
            let tmpX = x, tmpY = y;
            y--
            answer.add(`${x},${y},${tmpX},${tmpY}`)
            answer.add(`${tmpX},${tmpY},${x},${y}`)
        } else if (dir === "R" && x < 5) {
            let tmpX = x, tmpY = y;
            x++
            answer.add(`${x},${y},${tmpX},${tmpY}`)
            answer.add(`${tmpX},${tmpY},${x},${y}`)
        } else if (dir === "L" && x > -5) {
            let tmpX = x, tmpY = y;
            x--
            answer.add(`${x},${y},${tmpX},${tmpY}`)
            answer.add(`${tmpX},${tmpY},${x},${y}`)
        }
    }
    
    return answer.size/2;
}