function solution(arr) {
    var answer = 0;
    
    let sum = 0
    
    for (let x of arr) {
        sum += x
    }
    
    answer = sum/arr.length
    
    return answer;
}