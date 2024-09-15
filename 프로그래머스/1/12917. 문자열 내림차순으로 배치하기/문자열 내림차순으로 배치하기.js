function solution(s) {
    const sLst = [...s];
    sLst.sort((a, b) => {
        if(a < b) return 1
        if(a > b) return -1
    });
    return sLst.join('');
}
