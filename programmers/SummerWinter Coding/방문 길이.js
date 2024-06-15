/* 
    방문 길이

    1.  경로 길이 계산 문제의 변형 문제. 일반적으로 주어지는 정점 개수가 아닌 방문한 간선의 수를 구하는 문제.
    2.  어떤 정점에서 정점으로 이동하면서 생기는 간선은 무향 그래프를 따라야 한다.(방향과 관계 없이 해당 간선의 이용 여부만 체크)
    3.  따라서 Map에 양 방향에서의 정점-정점 정보를 저장하고, 최종적으로 기록된 사용된 간선 수를 절반으로 가져온다.
*/

function checkBorder(next, r) {
  if (
    next[0] < 0 ||
    next[0] >= 2 * r + 1 ||
    next[1] < 0 ||
    next[1] >= 2 * r + 1
  )
    return false;
  return true;
}

function solution(dirs) {
  var answer = 0;

  const way = new Map();

  let pos = [5, 5];
  const op = {
    U: [-1, 0],
    D: [1, 0],
    R: [0, 1],
    L: [0, -1],
  };

  for (move of dirs) {
    next = [pos[0] + op[move][0], pos[1] + op[move][1]];
    console.log(next);

    if (checkBorder(next, 5)) {
      way.set(`${pos[0]}${pos[1]}${next[0]}${next[1]}`, true);
      way.set(`${next[0]}${next[1]}${pos[0]}${pos[1]}`, true);

      pos = next;
    }
  }

  console.log(way);

  return way.size / 2;
}

console.log(solution("LULLLLLLU"));
