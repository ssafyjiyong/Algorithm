function solution(seoul) {
    const location = seoul.findIndex(x => x==='Kim');
    var answer = `김서방은 ${location}에 있다`;
    return answer;
}