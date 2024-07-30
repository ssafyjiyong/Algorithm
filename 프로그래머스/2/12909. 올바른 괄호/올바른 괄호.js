function solution(s){
    var answer = true;
    const stack = [];
    
    for (let x of s) {
        if (x==="(") {
            stack.push(x)
        } else if (x===")") {
            if (stack.length === 0) {
                answer = false;
            } else {
                stack.pop()
            }
        }
    }
    
    if (stack.length > 0) {
        answer = false;
    }
    
    return answer;
}