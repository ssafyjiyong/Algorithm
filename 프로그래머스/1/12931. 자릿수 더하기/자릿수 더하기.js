function solution(n)
{
    var answer = 0;

    const nStr = String(n);
    const nLst = [...nStr];
    
    for (let x of nLst) {
        answer += Number(x);
    }

    return answer;
}