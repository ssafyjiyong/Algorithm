function isCorrect(lst) {
    const stack = [];
    for (const e of lst) {
        if (e === '[' || e === '(' || e === '{') {
            stack.push(e)
        } else {
            if (stack.length === 0) return 0
            const tmp = stack.pop();
            if ((tmp === '[' && e !== ']') ||
                (tmp === '{' && e !== '}') ||
                (tmp === '(' && e !== ')')) {
                return 0;
            }
        }
    }
    return stack.length === 0 ? 1:0
}

function solution(s) {
    var answer = 0;
    const sLst = [...s];
    for (let i=0; i<sLst.length;i++) {
        const checkLst = sLst.slice(i,sLst.length).concat(sLst.slice(0,i))
        if(isCorrect(checkLst)) {
            answer++
        }
    }
    return answer;
}