function solution(num) {
    var answer = 0;
    let x = num
    while(x!==1) {
        if (answer>=500) {
            answer = -1;
            break;
        }
        if (x%2===0) {
            x=x/2
            answer+=1
        } else {
            x=x*3+1
            answer+=1
        }
    }
    return answer;
}