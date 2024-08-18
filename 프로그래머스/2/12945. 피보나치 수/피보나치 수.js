function solution(n) {
    let prev1 = 1;
    let prev2 = 0;
    
    for (let i = 2; i <= n; i++) {
        const current = (prev1 + prev2) % 1234567;
        prev2 = prev1;
        prev1 = current;
    }
    
    return prev1;
}
