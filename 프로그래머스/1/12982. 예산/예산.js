function solution(d, budget) {
    var answer = 0;
    let sum = 0;
    d.sort((a, b) => a-b);
    d.forEach((ele) => {
        if (budget >= sum+ele) {
            sum += ele;
            answer++;
        }
    })
    return answer;
}