function solution(arr, divisor) {
    var answer = [];
    arr.forEach((ele)=>{
        if (ele%divisor===0) {
            answer.push(ele);
        }
    })
    if (answer.length===0) {
        answer.push(-1);
    }
    answer.sort((a,b)=>a-b)
    return answer;
}