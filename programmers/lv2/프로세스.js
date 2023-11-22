/* 
  lv.2 프로세스 

  1.  큐를 통한 순차적 task 처리 과정 시뮬레이션.
  2.  자바스크립트에서 지원하는 큐 자료구조가 없으므로(배열의 pop/shift를 사용해 구현 가능)
      큐를 만들어 풀이에 사용해 보았다.
*/

class Queue {
  constructor(arr) {
    this.front = 0;
    this.rear = 0;
    this.queue = [];

    arr.forEach((element, index) => {
      this.put([element, index]);
    });
  }

  put(value) {
    this.queue.push(value);
    this.rear++;
  }
  get() {
    const result = this.queue[this.front];
    delete this.queue[this.front];
    this.front++;
    return result;
  }
  qsize() {
    return this.rear - this.front;
  }
  isMax(value) {
    for (let i = this.front; i < this.rear; i++) {
      const item = this.queue[i];
      if (item[0] > value[0]) {
        return false;
      }
    }
    return true;
  }
}

function solution(priorities, location) {
  var answer = 0;

  const q = new Queue(priorities);

  while (true) {
    const top = q.get();
    if (!q.isMax(top)) {
      q.put(top);
      continue;
    }
    answer += 1;

    if (top[1] === location) {
      break;
    }
  }

  return answer;
}

const priorities = [1, 1, 9, 1, 1, 1];
const location = 0;

console.log(solution(priorities, location));
