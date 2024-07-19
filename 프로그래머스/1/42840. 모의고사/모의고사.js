function solution(answers) {
    var answer = [];
    
    const first = [1,2,3,4,5];
    const second = [2,1,2,3,2,4,2,5];
    const third = [3,3,1,1,2,2,4,4,5,5];
    
    for (let i = 0; i < answers.length; i++) {
        first.push(first[i % first.length])
        second.push(second[i % second.length])
        third.push(third[i % third.length])
    };
    
    let a = 0
    let b = 0
    let c = 0
    
    answers.forEach((ans, idx) => {
        if (ans === first[idx]) {
            a++
        }; 
        if (ans === second[idx]) {
            b++
        };
        if (ans === third[idx]) {
            c++
        };
    });
    
    let max = Math.max(a, b, c)
    
    if (a === max) answer.push(1)
    if (b === max) answer.push(2)
    if (c === max) answer.push(3)
    
    return answer;
}