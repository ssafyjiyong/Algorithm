process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    
    const answer = [];
    for (let j=0; j<b; j++) {
        const tmp = [];
        for (let i=0; i<a; i++) {
            tmp.push('*');
        }
        answer.push(tmp.join(''))
    }
    answer.forEach(ele=>{
        console.log(ele);
    })
});