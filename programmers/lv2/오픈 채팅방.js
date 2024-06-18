/* 
    lv.2 오픈 채팅방
*/

function solution(records) {
  const db = new Map();
  const q = [];

  for (const record of records) {
    const [op, id, nickname] = record.split(" ");

    if (op === "Change") {
      db.set(id, nickname);
    } else if (op === "Enter") {
      db.set(id, nickname);
      q.push([op, id]);
    } else {
      q.push([op, id]);
    }
  }

  return q.map((el) => {
    const [op, id] = el;

    if (op === "Enter") return `${db.get(id)}님이 들어왔습니다.`;
    else return `${db.get(id)}님이 나갔습니다.`;
  });
}

console.log(
  solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
  ])
);
