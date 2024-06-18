/* 
    요세푸스
*/

function solution(N, K) {
  const list = Array.from({ length: N }, (v, i) => i + 1);

  let current = 0;

  while (list.length > 1) {
    for (let i = 0; i < K - 1; i++) {
      list.push(list.shift());
    }
    list.shift();
  }

  return list[0];
}

console.log(solution(5, 2));
