function solution(s) {
    const stack = [];
    
    for (let L of s) {
        if (stack.length === 0) {
            stack.push(L)
        } else {
            let tmpPop = stack.pop()
            if (tmpPop === L) {
                continue;
            } else {
                stack.push(tmpPop)
                stack.push(L)
            }
        }
    }

    return stack.length === 0? 1:0;
}
