/* 
    lv.2 괄호 회전하기

    1.  괄호 짝 맞추기 문제를 모든 케이스에 대해 시행하는 문제.
*/

function solution(s) {
  let answer = 0;
  const pair = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  for (let i = 0; i < s.length; i++) {
    const rotated = s.substring(i) + s.substring(0, i);

    const stack = [];

    for (c of rotated) {
      if (c === "(" || c === "{" || c === "[") {
        stack.push(c);
      } else {
        if (pair[stack[stack.length - 1]] === c) {
          stack.pop();
        } else {
          stack.push(c);
        }
      }
    }

    answer += stack.length === 0 ? 1 : 0;
  }

  return answer;
}

console.log(solution("[](){}"));
