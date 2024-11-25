function solution(cards) {
    const n = cards.length;
    const visited = Array(n).fill(0);
    const sizes = [];

    function dfs(start) {
        let size = 0;
        let current = start;

        while (!visited[current]) {
            visited[current] = true;
            size++;
            current = cards[current] - 1;
        }

        return size;
    }

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            const groupSize = dfs(i);
            sizes.push(groupSize);
        }
    }

    sizes.sort((a, b) => b - a);

    if (sizes.length <= 1) {
        return 0;
    }

    return sizes[0] * sizes[1];
}
