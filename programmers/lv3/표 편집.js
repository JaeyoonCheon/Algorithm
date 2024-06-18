/* 
    lv.3 표 편집

    1. 문제점
      1) 백만개 행에 대한 연산이므로 단순 동작 구현으로는 시간 효율이 나오지 않으므로 인덱스 조작으로 수행해야 함
      2) 행 삭제 / 복구 시 그에 따라 다른 행들의 인덱스가 변동됨
    2. 목표
      1) 행을 선택할 때 삭제된 행을 고려해 행을 선택해야 함
      2) 행을 삭제/복원 시 원래 위치했던 행으로 복구되어야 함
      3) 행 조작 시 선택된 행의 위치는 올바른 위치이어야 함
    3. 해결 방안
      1) 행을 선택할 시 각 행이 인접한 행의 인덱스를 가지고 있도록 하여 삭제된 행을 뛰어넘을 수 있도록 개선
      2) 1)을 쉽게 하기 위해, 각 인덱스의 바로 위 인덱스 번호를 가지는 upside, 아래 인덱스 번호를 가지는 downside를 생성
      3) 행 삭제 : 해당 행의 인덱스를 보관한 뒤, 그 행은 접근되지 않도록 아래 행의 upside와 위 행의 downside의 인덱스를 뛰어 넘도록 조작
      4) 행 복원 : 행 삭제와 반대로 해당 행을 접근할 수 있도록 아래 행의 upside와 위 행의 downside의 인덱스를 해당 행의 인덱스로 변경
*/

function solution(n, k, cmd) {
  let current = k;
  const stack = [];
  const upside = Array.from({ length: n + 2 }, (v, i) => i - 1);
  const downside = Array.from({ length: n + 2 }, (v, i) => i + 1);

  for (op of cmd) {
    if (op.length > 1) {
      const [dir, step] = op.split(" ");

      if (dir === "D") {
        for (let i = 0; i < step; i++) {
          current = downside[current];
        }
      } else {
        for (let i = 0; i < step; i++) {
          current = upside[current];
        }
      }

      console.log(`selected ${current}`);
    } else {
      if (op === "C") {
        stack.push(current);
        console.log(`deleted ${current}`);

        // 아래 행과 위 행을 연결
        upside[downside[current]] = upside[current];
        downside[upside[current]] = downside[current];

        // 행 이동
        current = downside[current] >= n ? upside[current] : downside[current];
      } else {
        const restored = stack.pop();
        console.log(`restored ${restored}`);

        // 아래 행과 위 행에 현재 행 연결
        upside[downside[restored]] = restored;
        downside[upside[restored]] = restored;
      }
    }
  }

  const arr = Array.from({ length: n }, () => "O");

  for (num of stack) {
    arr[num] = "X";
  }

  return arr.join("");
}

console.log(
  solution(8, 2, [
    "D 2",
    "C",
    "U 3",
    "C",
    "D 4",
    "C",
    "U 2",
    "Z",
    "Z",
    "U 1",
    "C",
  ])
);
