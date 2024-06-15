/* 
    lv.1 크레인 인형 뽑기 게임
*/

function solution(board, moves) {
  var answer = 0;
  const BOOM = 2;

  const boardTranspose = board[0].map((_, i) =>
    board.map((row) => row[i]).filter((v) => v !== 0)
  );

  const basket = [];
  let top = -1;

  moves.forEach((move) => {
    const picked = boardTranspose[move - 1].shift();
    if (!picked) return;
    const current = basket[top];

    basket.push(picked);
    top += 1;

    if (current === picked) {
      for (let i = 0; i < BOOM; i++) {
        basket.pop();
      }
      top -= BOOM;
      answer += BOOM;
    }
  });

  return answer;
}
