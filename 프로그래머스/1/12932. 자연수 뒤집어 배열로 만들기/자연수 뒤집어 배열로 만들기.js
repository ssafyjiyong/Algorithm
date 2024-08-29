function solution(n) {
    var answer = [];
    const nStr = String(n);
    
    const nLst = [...nStr];
    
    nLst.reverse()
    for (let x of nLst) {
        answer.push(Number(x));
    }
    
    return answer;
}