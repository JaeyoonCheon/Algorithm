/* 
    lv.2 주식가격

    1.  스택 + 투 포인터 전략으로 이해
    2.  n개 가격에 대해 순회하면서 스택에 저장된 이전 가격 대비 오름차순일 경우 스택에 저장.
        내림차순인 경우 스택에 저장되었던 이전 가격의 오름차순이 끊기는 길이를 계산할 수 있다.
*/

function solution(prices) {
  const answer = Array.from({ length: prices.length }, () => 0);
  const stack = [];

  for (let i = 0; i < prices.length; i++) {
    while (stack.length !== 0 && prices[stack.at(-1)] > prices[i]) {
      const top = stack.pop();

      answer[top] = i - top;
    }

    stack.push(i);
  }

  for (let el of stack) {
    answer[el] = prices.length - el - 1;
  }

  return answer;
}

const prices = [1, 2, 3, 2, 3];

console.log(solution(prices));
