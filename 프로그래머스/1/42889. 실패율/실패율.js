function solution(N, stages) {
    var answer = []
    
    for (let i=1; i<=N; i++) {  
        const tried = stages.filter(x => x >= i).length
        const failed = stages.filter(x => x === i).length
        
        answer.push([failed/tried, i])
        }
    
    answer.sort((a, b)=>{
        return b[0] - a[0]
    })
    
    return answer.map(x => x[1]);
}