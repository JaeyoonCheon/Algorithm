/* 
    10진수를 2진수로 변환하기
*/

function solution(decimal) {
  if (!Number.isInteger(decimal)) {
    return;
  }

  const stack = new Array();

  while (decimal > 0) {
    stack.push(decimal % 2);
    decimal = Number.parseInt(decimal / 2);
  }

  return stack.reverse().join("");
}

console.log(solution(13));
