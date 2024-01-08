/* 
lv.1 모의고사
 */

function solution(answers) {
  var answer = [];

  const scores = [0, 0, 0];
  const case1 = [1, 2, 3, 4, 5];
  const case2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const case3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === case1[i % case1.length]) {
      scores[0]++;
    }
    if (answers[i] === case2[i % case2.length]) {
      scores[1]++;
    }
    if (answers[i] === case3[i % case3.length]) {
      scores[2]++;
    }
  }

  const maxScore = Math.max(...scores);

  scores.forEach((v, i) => {
    if (v === maxScore) {
      answer.push(i + 1);
    }
  });

  return answer;
}

const answers = [1, 3, 2, 4, 2];

console.log(solution(answers));
