/* 
    lv.1 같은 숫자는 싫어 

    1.  쉽게 생각할 수 있는 스택 top을 이용한 방식으로는 풀이 가능하나 효율성 통과 x.
    2.  간단하게 순회하면서 이전 인덱스의 값과 다를 경우 push하지 않는 방식 사용.
*/

function solution(arr) {
  const answer = [];

  arr.forEach((val, idx, arr) => {
    if (val === arr[idx - 1]) {
      return;
    } else {
      answer.push(val);
    }
  });

  return answer;
}

const arr = [1, 1, 3, 3, 0, 1, 1];

console.log(solution(arr));
