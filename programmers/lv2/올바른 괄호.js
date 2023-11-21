/* 
    lv.2 올바른 괄호 

    1.  () 괄호 쌍의 종류에 따라 스택 연산을 할 경우 시간 초과.
    2.  닫는 괄호가 들어올 경우 즉각 여는 괄호가 사라지므로, 여는 괄호의 남은 개수만 카운팅하여 스택처럼 연산.
    3.  닫는 괄호가 먼저 들어오는 경우 카운트가 음수가 되는 예외만 처리.
*/

function solution(s) {
  var answer = true;

  let stack = 0;

  for (let c of s) {
    if (c === "(") stack += 1;
    else if (stack === 0) {
      answer = false;
      break;
    } else stack -= 1;
  }

  if (stack !== 0) answer = false;

  return answer;
}

const s = ")()(";

console.log(solution(s));
