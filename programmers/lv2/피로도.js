/* 
    lv.2 피로도

    1.  주어지는 던전에 대한 가능성 여부를 dfs로 경우의 수 탐색.
*/

function recursion(dungeon, visited, k) {
  if (visited.every((el) => el === true)) {
    return 0;
  }

  let count = 0;

  for (let i = 0; i < visited.length; i++) {
    if (visited[i]) continue;

    const [need, used] = dungeon[i];
    if (k < need) continue;

    visited[i] = true;
    count = Math.max(count, recursion(dungeon, visited, k - used));
    visited[i] = false;
  }

  return count + 1;
}

function solution(k, dungeons) {
  var answer = 0;

  const visited = new Array(dungeons.length).fill(false);
  answer = recursion(dungeons, visited, k);

  return answer;
}

const k = 80;
const dungeons = [
  [80, 20],
  [50, 40],
  [30, 10],
];

console.log(solution(k, dungeons));
