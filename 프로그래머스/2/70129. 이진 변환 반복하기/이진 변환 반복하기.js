function solution(s) {
    let zeroCnt = 0;
    let binaryCnt = 0;
    let sLst = s.split('');
    
    while (sLst.length > 1) {
        const tmpLst = [];
        sLst.forEach((ele) => {
            if (ele === '0') {
                zeroCnt++;
            } else {
                tmpLst.push('1')
            }
        });
        
        sLst = tmpLst;
        let sLstLen = sLst.length.toString(2);
        sLst = [...sLstLen];
        
        binaryCnt++;
    }
    
    return [binaryCnt, zeroCnt];
}