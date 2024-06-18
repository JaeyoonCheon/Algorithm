/* 
    두 개의 수로 특정값 만들기
*/

function solution(arr, target) {
  const hashMap = new Map();
  for (el of arr) {
    hashMap.set(el, true);
  }

  for (el of arr) {
    if (target - el === el) continue;
    if (hashMap.has(target - el)) return true;
  }

  return false;
}

console.log(solution([2, 3, 5, 9], 10));
