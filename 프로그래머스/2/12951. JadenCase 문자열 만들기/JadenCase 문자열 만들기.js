function solution(s) {
    let sLst = s.toLowerCase().split(' ');
    
    for (let i=0; i<sLst.length; i++) {       
        if (sLst[i].length > 0) {            
            sLst[i] = sLst[i][0].toUpperCase() + sLst[i].slice(1);
        }
    }
    
    const answer = sLst.join(' ')
    
    return answer;
}