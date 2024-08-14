function solution(s) {
    var answer = '';
    
    const sLst = s.split(' ');
    
    let min = Number(sLst[0]);
    let max = Number(sLst[0]);
    
    for (let x of sLst) {
        let numX = Number(x)
        if(numX<min){min=numX}
        if(numX>max){max=numX}
    }
    
    answer += min
    answer += ' '
    answer += max

    return answer;
}