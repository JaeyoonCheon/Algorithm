/* 
    lv.2 H-Index
    
    1.  어떤 논문 x가 있을 떄, h가 x보다 작다고 가정하자.
        x를 포함해 x보다 더 많이 인용된 논문들의 개수가 a라고 하면
        a가 x이하일 경우 h-index일 조건을 만족한다.
    2.  따라서, 정렬 후 순회하면서 x이상의 논문 수(전체길이 - 인덱스)가 x보다 작은 경우
        무조건 h-index를 만족하므로 갱신한다.
    3.  index는 증가하므로 한번 h-index를 찾았다면 그 이상의 h-index는 발견되지 않으므로 종료.
*/
function solution(citations) {
  let answer = 0;
  const length = citations.length;

  citations.sort((a, b) => a - b);

  for (let [i, value] of citations.entries()) {
    if (value >= length - i) {
      const newHIndex = length - i;

      answer = Math.max(answer, newHIndex);
      break;
    }
  }

  return answer;
}

const citations = [0, 5, 5, 5, 5, 5, 5, 5];

console.log(solution(citations));
