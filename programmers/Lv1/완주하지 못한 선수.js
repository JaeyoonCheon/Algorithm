/* lv.1 완주하지 못한 선수

1.  완주자 목록을 dict로 만들어 참가자 수와 대조. 초기화 작업 중요 */

function solution(participant, completion) {
  let answer = "";

  const list = {};

  for (let c of completion) {
    if (!list[c]) {
      list[c] = 1;
    } else {
      list[c] += 1;
    }
  }

  for (let p of participant) {
    if (!list[p]) {
      answer = p;
      break;
    }

    list[p] -= 1;

    if (list[p] < 0) {
      answer = p;
      break;
    }
  }

  return answer;
}

const participant = ["marina", "josipa", "nikola", "vinko", "filipa"];
const completion = ["josipa", "filipa", "marina", "nikola"];

console.log(solution(participant, completion));
