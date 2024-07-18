function solution(numbers) {
    let temp = [];
    numbers.sort((a,b) => a-b)
    for (let i = 0; i < numbers.length-1; i++) {
        for (let j = i+1; j < numbers.length; j++) {
            temp.push(numbers[i] + numbers[j]);
        }
    }
    const answer = [...new Set(temp)];
    answer.sort((a,b) => a-b)
    return answer;
}