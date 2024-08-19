function solution(n) {
    var answer = 0;
    
    let current;
    let prev1 = 1;
    let prev2 = 0;
    
    for (let i=2; i<=n; i++) {
        current = (prev1 + prev2) % 1234567;
        prev2 = prev1;
        prev1 = current;
    }
    
    return current;
}