function solution(maps) {
    const col = maps[0].length
    const row = maps.length
    const directions = [[0,-1],[0,1],[-1,0],[1,0]];
    const visited = Array.from({length:row}, () => Array(col).fill(0));
    visited[0][0] = 1
    const needVisit = [[0,0,1]];
    
    while (needVisit.length > 0) {
        const [x, y, cnt] = needVisit.shift()
        
        if (x===row-1 && y===col-1) {
            return cnt
        }
        
        for (const [dx, dy] of directions) {
            const nx = x + dx
            const ny = y + dy
            if (nx>=0 && ny>=0 && nx<row && ny<col && maps[nx][ny]===1 && visited[nx][ny]===0) {
                visited[nx][ny] = 1
                needVisit.push([nx, ny, cnt+1])
            }
        }
    }
    
    return -1
}