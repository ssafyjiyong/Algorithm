function solution(numbers) {
    var answer = 0;
    numbers.forEach(ele => answer+=ele);
    return answer/numbers.length;
}