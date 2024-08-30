function solution(n) {
    const nStr = String(n);
    const nLst = [...nStr];
    nLst.sort((a,b) => b-a);
    return Number(nLst.join(''))
}