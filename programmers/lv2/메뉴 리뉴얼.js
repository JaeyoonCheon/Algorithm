/* 
    lv.2 메뉴 리뉴얼
*/

function getAllCombinations(str) {
  const result = [];

  function generateCombinations(prefix, remaining) {
    if (remaining.length === 0) {
      if (prefix !== "") {
        result.push(prefix);
      }
      return;
    }

    // 첫 번째 문자를 포함하지 않는 조합
    generateCombinations(prefix, remaining.slice(1));

    // 첫 번째 문자를 포함하는 조합
    generateCombinations(prefix + remaining[0], remaining.slice(1));
  }

  generateCombinations("", str);
  return result;
}

function solution(orders, course) {
  // 전체 주문 조합 각각에 대해, 가능한 n개의 조합 별 가짓수 카운트
  const comb = orders
    .sort()
    .map((order) => getAllCombinations(order))
    .reduce((acc, cur) => [...acc, ...cur], []);

  const courseComb = course.map((len) => {
    const counter = new Map();
    comb
      .filter((el) => el.length === len)
      .forEach((el) =>
        counter.has(el)
          ? counter.set(el, counter.get(el) + 1)
          : counter.set(el, 1)
      );
    return counter;
  });

  const result = [];

  // 가짓수 별 최대 조합 개수
  for (const hash of courseComb) {
    const tempArr = [];
    const maxCount = Math.max(...hash.values());

    if (maxCount < 2) continue;

    for (const [k, v] of hash.entries()) {
      if (v === maxCount) tempArr.push(k);
    }

    result.push(...tempArr);
  }

  result.sort();

  return result;
}

console.log(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]));
