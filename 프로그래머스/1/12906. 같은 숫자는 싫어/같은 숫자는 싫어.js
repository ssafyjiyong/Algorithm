function solution(arr)
{
    const stack = [];
    
    for (e of arr) {
        if (stack.length<=0) {
            stack.push(e)
        } else {
            const tmp = stack.pop()
            if (tmp !== e) {
                stack.push(tmp)
                stack.push(e)
            } else {
                stack.push(tmp)
            }
        }
    }
    
    return stack;
}