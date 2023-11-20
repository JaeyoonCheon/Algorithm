/* 
    lv.1 폰켓몬 

    1.  너무 복잡하게 생각해 조합으로 해결하려다 시간이 오래 걸린 문제.
    2.  문제를 잘 읽고, N/2가지 경우의 수와 고를 수 있는 조합의 가짓수 중 더 작은 것을 택하면 되는 문제.
*/

function solution(nums) {
  var answer = 0;

  const dict = new Map();

  for (let i of nums) {
    if (!dict.has(i)) {
      dict.set(i, 1);
    } else {
      const temp = dict.get(i);
      dict.set(i, temp + 1);
    }
  }

  answer = Math.min(dict.size, nums.length / 2);

  return answer;
}

const nums = [3, 1, 2, 3];

console.log(solution(nums));
