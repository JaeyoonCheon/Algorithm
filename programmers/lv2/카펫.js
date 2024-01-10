/* 
lv.2 카펫

1.  테두리/내부의 타일 개수와 총 넓이가 정해져 있으면 가능한 가로/세로는 정확히 하나의 케이스만 존재한다.
2.  총 넓이에서 테두리를 뺀 내부 넓이를 가능한 모든 가로x세로의 경우를 따져봐도 시간에 초과하지 않는다.
 */

function solution(brown, yellow) {
  var answer = [];

  const total = brown + yellow;

  for (let i = 3; i < total / 3 + 1; i++) {
    if (!Number.isInteger(total / i)) {
      continue;
    }

    if ((i - 2) * (total / i - 2) === yellow) {
      answer = [total / i, i];
      break;
    }
  }

  return answer;
}

const brown = 10;
const yellow = 2;

console.log(solution(brown, yellow));
