function solution(n) {
    var answer = 0;
    let x = 2;
    while (true) {
        if (n % x == 1) return x;
        x++;
    }
    return answer;
}