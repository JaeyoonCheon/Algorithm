/* 
lv.2 소수찾기

1.  만들 수 있는 모든 조합에 대해 소수를 검사해야 하는 문제로 1) 소수 탐색 2) 가능한 조합 구하기 2가지 동작을 거쳐야 한다.
2.  소수는 2~999999의 경우에서 에라토스테네스의 체 방식으로 가능한 소수들을 미리 모두 찾아놓는다.
3.  자바스크립트는 리스트의 조합을 기본 제공하지 않으므로 재귀 방식으로 가능한 조합을 구한 뒤 정규화/중복제거/숫자형 변경을 거쳐 조합을 구한다.
4.  이후 조합 원소들에 대해 소수인 지 판별하여 개수를 센다.
 */

function makeErathos(n) {
  const sieiv = Array.from(new Array(n + 1), () => true);

  sieiv[0] = false;
  sieiv[1] = false;
  for (let i = 2; i < Math.sqrt(sieiv.length); i++) {
    let m = 2;
    if (!i) {
      continue;
    }
    while (i * m < sieiv.length) {
      sieiv[i * m] = false;
      m++;
    }
  }

  return sieiv;
}

function permutation(arr, n) {
  const array = [];

  if (n === 1) {
    return arr.map((el) => [el]);
  }

  arr.forEach((val, index, ori) => {
    const rest = [...ori.slice(0, index), ...ori.slice(index + 1)];
    const perm = permutation(rest, n - 1);
    const attached = perm.map((el) => [val, ...el]);
    array.push(...attached);
  });

  return array;
}

function solution(numbers) {
  var answer = 0;

  const sieiv = makeErathos(1000000);
  const permutated = [];
  const toArr = [...numbers];

  for (let i = 1; i <= toArr.length; i++) {
    permutated.push(permutation(toArr, i).map((el) => parseInt(el.join(""))));
  }
  const normalized = [...new Set(permutated.flat())];
  normalized.forEach((val) => {
    if (sieiv[val]) answer++;
  });

  return answer;
}

const numbers = "011";

console.log(solution(numbers));
