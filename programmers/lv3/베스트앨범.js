/* 
    lv.3 베스트앨범 

    1.  장르 별 최다 재생 순 정렬
    2.  해당 장르 내에서 재생 내림차순-고유번호 오름차순 정렬
*/

function solution(genres, plays) {
  var answer = [];
  const length = genres.length;

  const genreTotal = {};
  const genrePlays = {};

  for (let i = 0; i < length; i++) {
    const index = i;
    const genre = genres[i];
    const play = plays[i];

    if (!genreTotal[genre]) {
      genreTotal[genre] = play;
    } else {
      genreTotal[genre] += play;
    }

    if (!genrePlays[genre]) {
      genrePlays[genre] = [[play, index]];
    } else {
      genrePlays[genre].push([play, index]);
    }
  }

  for (let genre of genres) {
    genrePlays[genre].sort((prev, curr) => {
      if (prev[0] > curr[0]) return -1;
      if (prev[0] <= curr[0]) return 1;

      if (prev[1] < curr[1]) return -1;
      if (prev[1] >= curr[1]) return 1;
    });
  }

  const sortedGenreTotal = Object.entries(genreTotal)
    .sort(([, a], [, b]) => b - a)
    .map((entry) => entry[0]);

  for (let genre of sortedGenreTotal) {
    const genreTop2 = genrePlays[genre].slice(0, 2);
    const top2Numbers = genreTop2.map((entry) => entry[1]);
    answer = answer.concat(top2Numbers);
  }

  return answer;
}

const genres = ["classic", "pop", "classic", "classic", "pop"];
const plays = [500, 600, 150, 800, 2500];

console.log(solution(genres, plays));
