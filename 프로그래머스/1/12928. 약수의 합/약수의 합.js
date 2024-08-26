function solution(n) {
    var answer = 0;
    let x = 1;
    while (x<=n) {
        if (n%x==0) {
            answer+=x;
        }
        x++;
    }
    return answer;
}