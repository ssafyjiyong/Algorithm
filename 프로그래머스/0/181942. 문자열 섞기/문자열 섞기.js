function solution(str1, str2) {
    const answer = [];
    const lst1 = [...str1];
    const lst2 = [...str2];
    
    while(lst1.length > 0 && lst2.length > 0) {
        if (lst1.length > 0) {
            answer.push(lst1.shift());            
        };
        
        if (lst2.length > 0) {
            answer.push(lst2.shift());
        };
    }
    
    return answer.join('');
}