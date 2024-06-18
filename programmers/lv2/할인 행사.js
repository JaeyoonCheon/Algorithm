/* 
    lv.2 할인 행사

    1.  n일 간의 행사에서 10일 간의 회원가입 행사 기간 중 원하는 품목 & 수량과 동일한 조건의 날짜에만 회원가입하려고 하므로,
        회원가입 가능한 모든 날짜에 향후 10일 간 할인 구매 가능한 품목을 미리 구해놓고 목표와 대조하는 방식으로 풀이.
*/

function solution(want, number, discount) {
  const target = new Map(want.map((el, i) => [el, number[i]]));

  const days = Array.from({ length: discount.length - 10 + 1 }, (v, i) => {
    const day10 = discount.slice(i, i + 10);
    return new Map(
      want.map((el) => [
        el,
        day10.reduce((acc, cur) => (cur === el ? acc + 1 : acc), 0),
      ])
    );
  });

  let count = 0;

  for (const day of days) {
    let isSame = true;

    for (el of want) {
      if (day.get(el) !== target.get(el)) {
        isSame = false;
        continue;
      }
    }

    if (isSame) count += 1;
  }

  return count;
}

console.log(
  solution(
    ["banana", "apple", "rice", "pork", "pot"],
    [3, 2, 2, 2, 1],
    [
      "chicken",
      "apple",
      "apple",
      "banana",
      "rice",
      "apple",
      "pork",
      "banana",
      "pork",
      "rice",
      "pot",
      "banana",
      "apple",
      "banana",
    ],
    3
  )
);
