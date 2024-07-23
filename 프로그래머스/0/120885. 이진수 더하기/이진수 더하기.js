function solution(bin1, bin2) {
    var answer = [];
    
    let tmp = 0
    
    const binLst1 = [...bin1]
    const binLst2 = [...bin2]
    
    while (binLst1.length > 0 || binLst2.length > 0) {
        let c1 = binLst1.length > 0 ? Number(binLst1.pop()) : 0;
        let c2 = binLst2.length > 0 ? Number(binLst2.pop()) : 0;
        
        if (c1 + c2 + tmp < 2) {            
            answer.push(c1 + c2 + tmp)
            tmp = 0
        } else {
            answer.push(c1 + c2 + tmp - 2)
            tmp = 1
        }
    }
    
    if (tmp > 0) {
        answer.push(tmp);
    }
    
    return answer.reverse().join('');
}