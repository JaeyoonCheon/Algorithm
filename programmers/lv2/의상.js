/* lv.2 의상

1.  각 타입의 의상을 최소 한가지 입는 조합의 수는 (각 의상의 가지수 + 1)의 곱에 -1(아무것도 입지 않은 경우)를
    제한 결과. */

function solution(clothes) {
  var answer = 1;

  const dict = {};

  for (let cloth of clothes) {
    const type = cloth[1];
    if (!dict[type]) {
      dict[type] = 1;
    } else {
      dict[type] += 1;
    }
  }

  for (let num of Object.values(dict)) {
    answer *= num + 1;
  }

  answer -= 1;

  return answer;
}

const clothes = [
  ["yellow_hat", "headgear"],
  ["blue_sunglasses", "eyewear"],
  ["green_turban", "headgear"],
];

console.log(solution(clothes));
