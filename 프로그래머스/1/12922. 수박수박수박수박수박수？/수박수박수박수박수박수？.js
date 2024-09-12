function solution(n) {
    var answer = '';
    let letter
    for (let i=0; i<n; i++) {
        if (i%2 == 0) {
            letter = '수'
        } else {
            letter = '박'
        }
        answer += letter;
    }
    return answer;
}