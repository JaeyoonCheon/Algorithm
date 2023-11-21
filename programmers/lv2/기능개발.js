/* 
    lv.2 기능개발 

    1.  날짜 1일 단위로 증가시키며 top의 값이 100이 될 때 100이상인 작업들을 모두 pop하면서 추가.
    2.  JS에서 별도로 스택이나 큐를 구현하지 않고 뒤집어 마지막 인덱스를 대상으로 스택 연산.
*/

function solution(progresses, speeds) {
  var answer = [];

  progresses.reverse();
  speeds.reverse();

  while (progresses.length !== 0) {
    progresses = progresses.map((element, idx) => {
      return (element += speeds[idx]);
    });

    let finished = 0;

    while (progresses.length !== 0 && progresses.at(-1) >= 100) {
      progresses.pop();
      speeds.pop();
      finished += 1;
    }

    if (finished > 0) {
      answer.push(finished);
    }
  }

  return answer;
}

const progresses = [95, 90, 99, 99, 80, 99];
const speeds = [1, 1, 1, 1, 1, 1];

console.log(solution(progresses, speeds));
