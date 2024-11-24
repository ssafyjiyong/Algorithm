const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().trim().split("\n");

function countConnectedComponents(input) {
    const [n, m] = input[0].split(" ").map(Number);
    const edges = input.slice(1).map(line => line.split(" ").map(Number));

    const graph = Array.from({ length: n + 1 }, () => []);
    edges.forEach(([u, v]) => {
        graph[u].push(v);
        graph[v].push(u);
    });

    const visited = Array(n + 1).fill(false);
    let connectedComponents = 0;

    // DFS
    function dfs(node) {
        visited[node] = true;
        for (const neighbor of graph[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor);
            }
        }
    }

    for (let i = 1; i <= n; i++) {
        if (!visited[i]) {
            connectedComponents++;
            dfs(i);
        }
    }

    console.log(connectedComponents);
}

countConnectedComponents(input);
