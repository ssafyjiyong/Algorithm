function solution(N, stages) {
    const tried = new Array(N).fill(0);
    const failed = new Array(N).fill(0);
    
    stages.forEach(item => {
        for (let i=0; i<N; i++) {
            if (item >= i+1) {
                tried[i]++
            }
        }
    });
    
    stages.forEach(item => {
        if (item <= N) {
            failed[item-1]++
        }
    });
    
    const answer = [];
    for (let i=0; i<N; i++) {
        if (failed[i] === 0) {
            answer.push([0,i+1])
        } else {            
            answer.push([failed[i]/tried[i],i+1])
        }
    }
    
    answer.sort((a, b)=> {
        if(a[0] !== b[0]) {
            return b[0] - a[0]
        } else {
            return a[1] - b[1]
        }
    })
    
    return answer.map(item => item[1]);
}