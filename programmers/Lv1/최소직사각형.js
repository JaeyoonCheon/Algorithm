/* 
    lv.1 최소직사각형

    1.  실생활에서 카드를 정리하는 것 처럼 모든 카드를 한 쪽 면이 작도록(가로 < 세로 혹은 가로 > 세로)
        정렬한 뒤 전체 변에서 가장 큰 수를 골라 곱하면 정답.
*/

function solution(sizes) {
  let answer = 0;
  const MAX_LEN = 0;
  let maxRow = MAX_LEN;
  let maxCol = MAX_LEN;

  const resized = sizes.map(([row, col]) =>
    row >= col ? [row, col] : [col, row]
  );

  resized.forEach(([row, col]) => {
    if (maxRow < row) {
      maxRow = row;
    }
    if (maxCol < col) {
      maxCol = col;
    }
  });

  answer = maxRow * maxCol;

  return answer;
}

const sizes = [
  [60, 50],
  [30, 70],
  [60, 30],
  [80, 40],
];

console.log(solution(sizes));
