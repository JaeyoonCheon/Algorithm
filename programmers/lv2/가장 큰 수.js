function solution(numbers) {
  var answer = "";

  numbers.sort((a, b) => {
    return Number("" + b + a) - Number("" + a + b);
  });

  answer = String(BigInt(numbers.join("")));

  return answer;
}

const numbers = [565, 56];

console.log(solution(numbers));
