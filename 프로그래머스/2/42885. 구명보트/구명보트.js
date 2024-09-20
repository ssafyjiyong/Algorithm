function solution(people, limit) {
    var answer = 0;
    
    people.sort((a,b) => a-b)
    
    let light = 0;
    let heavy = people.length - 1;
    
    while (light <= heavy) {
        if (people[light] + people[heavy] <= limit) {
            answer++;
            light++;
            heavy--;
        } else {
            answer++;
            heavy--;
        }
    }
    
    return answer;
}