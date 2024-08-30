const img = document.querySelector(".poster_img_box")

// 이 값에서 [] 제거한 게 파라미터 값

var movie_id = document.getElementById("tmdb_id").innerHTML
movie_id = movie_id.replace('[','')
movie_id = movie_id.replace(']','')
// console.log(movie_id)

showTmdbRecommend(movie_id)

// tmdb_recommend.html에서 받아온 movie_id parameter 값으로 poster_path 띄우는 함수
async function showTmdbRecommend(param) {
    // console.log(param)
    const api_key = "7f914cd60ea3f7a8f0358344658513a7";

    // 검색 기반 추천 영화
    var result = await axios.get(
      "https://api.themoviedb.org/3/movie/" + param + "/recommendations?api_key=" + api_key + "&language=ko-KR&page=1"
    )

    result = result.data.results;
    // console.log(result)
   
    result.map(function (cur, index) {
      img.insertAdjacentHTML(
        "beforeend",
        `<div class="total"><div class="ImgDiv"><img src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" 
        class="posterImg" onclick = "showDetail(${cur.id})"/></div><div class="title_name">${cur.title}</div></div>`
      );
    });
}

// Detail 띄우는 함수
async function showDetail(param) {
  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  var result = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "?api_key=" + api_key 
  + "&language=ko-KR");

  text = result.data;

  // 영화 제목 - 모달창 밖으로 숨김
  document.getElementById("modalid").innerHTML = "<span style='opacity: 0;'>" + text['title'] + "</span>";
  
  // 디테일 페이지 - 영화 포스터
  document.getElementById("modalimg").innerHTML = 
  "<div><br><br><br><img src='http://image.tmdb.org/t/p/w185/" + text['poster_path'] + "' class='modal_img'" + " /></div>";
 
  // 정보 띄우기 
  document.getElementById("modaltext").innerHTML = "<div class='detail_title'><br>" + text['title'] + 
  '<div class="vote"><img src="../../static/img/star.png" id="star"/>&nbsp;' + text['vote_average'] + '</div></div>' +
  '<div class="release_date"><br>개봉일자 : ' + text['release_date'] + 
  '</div><br><br><div class="story">줄거리</div><br><div class="overview">' + text['overview'] + '</div>' +
  '<br><br><div class="modal_youtube" onclick="showYoutube(' + param + ')">예고편 보러 가기</div>' ;

  // modalyoutube창 로그 안남게 초기화
  document.getElementById("modalyoutube").innerHTML = '<div></div>'

  // modal 디폴트
  document.getElementById('modal').style.display = 'block';
  
  // background를 누르면 modal이 꺼지는 함수 ('modal'.style.display = 'block' -> 'none')
  const close = modal.querySelector(".modal_background");
  close.addEventListener("click", e => {
    document.getElementById('modal').style.display = 'none';
  });

};


async function showYoutube(param) {

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  var result = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "?api_key=" + api_key 
  + "&language=ko-KR");

  text = result.data;

  console.log(text)

  var result2 = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "/videos?api_key=" + api_key 
  + "&language=ko-KR");
  console.log(result2)
  youtube = result2.data.results;

  console.log(youtube)

  // 다 유튜브 값이 있기는 있음 array(0)일 뿐,, 이건 어떻게 처리하는 거지?
  if(youtube.length != 0) { 
    document.getElementById("modalyoutube").innerHTML = 
    '<br><br><div class="youtube"><a href="https://www.youtube.com/embed/' + youtube[0]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + youtube[0]['key'] + '" frameborder="1" class="youtube">클릭시 유튜브로 이동합니다.</a></div>';
    
  } else {
    document.getElementById("modalyoutube").innerHTML = "<br><br><div class='no_youtube';>예고편 없음</div>";
  };

};