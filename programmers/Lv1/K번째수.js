function solution(array, commands) {
  var answer = [];

  for (let command of commands) {
    const _from = command[0];
    const _to = command[1];

    const newArray = array.slice(_from - 1, _to);
    newArray.sort((a, b) => a - b);

    answer.push(newArray[command[2] - 1]);
  }

  return answer;
}

const array = [1, 5, 2, 6, 3, 7, 4];
const commands = [
  [2, 5, 3],
  [4, 4, 1],
  [1, 7, 3],
];

console.log(solution(array, commands));
