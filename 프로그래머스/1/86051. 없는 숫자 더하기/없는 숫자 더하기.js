function solution(numbers) {
    var answer = 0;
    const nums = [0,1,2,3,4,5,6,7,8,9];

    nums.forEach((ele) => {
        if (!numbers.includes(ele)) {
            answer += ele;
        }
    })
    return answer;
}