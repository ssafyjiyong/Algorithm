function solution(n) {
    const nCnt = n.toString(2).split('1').length;
    
    let answer = n+1;
    while (1) {
        let nextCnt = answer.toString(2).split('1').length;
        if (nextCnt === nCnt) {
            return answer;
        }   
        answer++;
    }
}