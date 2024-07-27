function solution(s) {
    const stack = [];

    for (let L of s) {
        if (stack.length > 0 && stack[stack.length - 1] === L) {
            stack.pop();
        } else {
            stack.push(L);
        }
    }

    return stack.length === 0 ? 1 : 0;
}
