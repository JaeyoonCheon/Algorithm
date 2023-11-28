/* 
    lv.2 다리를 지나는 트럭

    1.  정직하게 Queue를 구성해 시뮬레이션하여 풀이.
    2.  문제에서 1초에 수행되는 동작은 1) 다리에서 내리는 동작 2) 다리에 올라타는 동작
        두 가지가 순차적으로 1초에 수행됨.
*/

class Bridge {
  constructor(length, durability) {
    this.length = length;
    this.durability = durability;
    this.front = 0;
    this.rear = length;
    this.weight = 0;
    this.q = new Array(length).fill(0);
  }
  isDurable(car) {
    return this.durability < this.weight + car ? false : true;
  }
  push(car) {
    this.q[this.rear] = car;
    this.rear++;
    this.weight += car;
  }
  pop() {
    const poped = this.q[this.front];
    this.front++;
    this.weight -= poped;

    return poped;
  }
  set weight(weight) {
    this._weight = weight;
  }
  get weight() {
    return this._weight;
  }
}

function solution(bridge_length, weight, truck_weights) {
  var answer = 0;

  const bridge = new Bridge(bridge_length, weight);
  const carList = truck_weights.reverse();

  while (bridge.weight !== 0 || carList.length !== 0) {
    bridge.pop();

    if (carList.length !== 0) {
      const next = carList.pop();
      if (bridge.isDurable(next)) {
        bridge.push(next);
      } else {
        carList.push(next);
        bridge.push(0);
      }
    }
    answer += 1;
  }

  return answer;
}

const bridge_length = 2;
const weight = 10;
const truck_weights = [7, 4, 5, 6];

console.log(solution(bridge_length, weight, truck_weights));
