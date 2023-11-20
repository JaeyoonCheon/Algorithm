/* 
  lv.2 전화번호 목록 

  1.  주어진 배열을 순회하면서 접두사가 존재하는 지 확인하는 문제.
  2.  백만 길이의 배열이라도 정렬 과정을 거친 후 검사하는 것이 확실히 빠름.
*/

function solution(phone_book) {
  var answer = true;

  answer = phone_book
    .sort()
    .every((num, idx, arr) => !arr[idx + 1]?.startsWith(num));

  return answer;
}

const phone_book = ["123", "456", "789"];

console.log(solution(phone_book));
