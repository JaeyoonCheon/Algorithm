/* 
    lv.2 짝지어 제거하기

    1.  짝을 짓지 못하는 홀수 길이인 경우 배제.
    2.  스택을 이용해 판정하여 문자열 순회하는 즉시 연산이 가능한 O(N) 방식으로 풀이.
*/

function solution(s) {
  const stack = [];

  if (stack.length % 2 === 1) return 0;

  for (c of s) {
    if (stack[stack.length - 1] === c) {
      stack.pop();
    } else {
      stack.push(c);
    }
  }

  return stack.length === 0 ? 1 : 0;
}

console.log(solution("baabaa"));
