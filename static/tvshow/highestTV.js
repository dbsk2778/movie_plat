const slider = document.querySelector(".carouselbox")
var scrollPerClick;
var ImagePadding =20;

showHighestTV();

var scrollAmount = 0;

var timer;

function sliderScrollLeft() {
  slider.scrollTo({
    top: 0,
    left: (scrollAmount -= scrollPerClick),
    behavior: "smooth"
  });

  if (scrollAmount < 0) {
    scrollAmount = 0
  };
};


function sliderScrollRight() {
  if (scrollAmount <= slider.scrollWidth - slider.clientWidth) {
    slider.scrollTo({
      top: 0,
      left: (scrollAmount += scrollPerClick),
      behavior: "smooth"
    });
  };
};

timer = setInterval(sliderScrollRight, 4000);

async function showHighestTV() {

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  var result = await axios.get(
    "https://api.themoviedb.org/3/tv/top_rated?api_key=" +
    api_key +
    "&language=ko-KR&page=1"
  )

  result = result.data.results;
  // console.log(result)

  result.map(function(cur, index) {
    slider.insertAdjacentHTML(
      "beforeend",
      `<img class="img-${index} slider-img" src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" onclick = "showTvDetail(${cur.id})"/>`
    );
  });

  scrollPerClick = document.querySelector(".img-1").clientWidth + ImagePadding;
};

async function showTvDetail(param) {

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  // https://api.themoviedb.org/3/tv/{tv_id}?api_key=<<api_key>>&language=en-US
  var result = await axios.get("https://api.themoviedb.org/3/tv/" + param + 
  "?api_key=" + api_key + "&language=ko-KR");

  text = result.data;

  // console.log()

  genre = text['genres']

  

  // 영화 제목 - 모달창 밖으로 숨김
  document.getElementById("modaltitle").innerHTML = "<span style='opacity: 0;'>" + text['name'] + "</span>";
  // 영화 포스트 - 모달창 밖으로 숨김
  document.getElementById("modalposter").innerHTML = "<span style='opacity: 0;'>" + text['poster_path'] + "</span>";

  document.getElementById("modalimg").innerHTML = 
  "<div><br><br><br><img src='http://image.tmdb.org/t/p/w185/" + text['poster_path'] + "' class='modal_img'" + " /></div>";
  
  // genre가 없는 경우 에러 뜸(디테일 페이지 안열림), if문 작성
  if(genre.length == 0) {

    document.getElementById("modaltext").innerHTML = 
    '<div class="detail_title"><br>' + text['name'] + 
    '<div class="vote"><img src="../../static/img/star.png" id="star"/>&nbsp;&nbsp;' + text['vote_average'] + 
    '</div></div><div class="genre"></div><br>' + 
    '<div class="start_date">방영 시작일 : ' + text['first_air_date'] + '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp최근 방영일 : ' + text['last_air_date'] + 
    '<br><br><div class="season">시즌 : '+ text['number_of_seasons'] + '개</div><br><div class="story">줄거리</div><br><div class="overview">' + text['overview'] + 
    '</div><br><div class="homepage"><a href="'+ text['homepage'] + '">메인 홈페이지로 이동</a></div><br>' ;

  } else if(genre.length == 1) {

    document.getElementById("modaltext").innerHTML = 
    '<div class="detail_title"><br>' + text['name'] + 
    '<div class="vote"><img src="../../static/img/star.png" id="star"/>&nbsp;&nbsp;' + text['vote_average'] + 
    '</div></div><div class="genre">' + text['genres'][0]['name'] + '</div><br>' + 
    '<div class="start_date">방영 시작일 : ' + text['first_air_date'] + '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp최근 방영일 : ' + text['last_air_date'] + 
    '<br><br><div class="season">시즌 : '+ text['number_of_seasons'] + '개</div><br><div class="story">줄거리</div><br><div class="overview">' + text['overview'] + 
    '</div><br><div class="homepage"><a href="'+ text['homepage'] + '">메인 홈페이지로 이동</a></div><br>' ;

  } else {

    // title, overview, release_date, vote_average
    document.getElementById("modaltext").innerHTML = 
    '<div class="detail_title"><br>' + text['name'] + 
    '<div class="vote"><img src="../../static/img/star.png" id="star"/>&nbsp;&nbsp;' + text['vote_average'] + 
    '</div></div><div class="genre">' + text['genres'][0]['name'] + ', ' + text['genres'][1]['name'] + '</div><br>' + 
    '<div class="start_date">방영 시작일 : ' + text['first_air_date'] + '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp최근 방영일 : ' + text['last_air_date'] + 
    '<br><br><div class="season">시즌 : '+ text['number_of_seasons'] + '개</div><br><div class="story">줄거리</div><br><div class="overview">' + text['overview'] + 
    '</div><br><div class="homepage"><a href="'+ text['homepage'] + '">메인 홈페이지로 이동</a></div><br>' ;
  
  } 
    
  // modal 디폴트
  document.getElementById('modal').style.display = 'block';
  
  // background를 누르면 modal이 꺼지는 함수 ('modal'.style.display = 'block' -> 'none')
  const close = modal.querySelector(".modal_background");
  close.addEventListener("click", e => {
    document.getElementById('modal').style.display = 'none';
  });

};


// 버튼누르면 콘솔에 영화 제목 출력
function changeT() {
  var movieTitle = document.getElementById("modaltitle").innerText;
  console.log( movieTitle);
  return movieTitle;
}
// 버튼누르면 콘솔에 영화 poster_path 출력
function changeP() {
  var moviePoster = document.getElementById("modalposter").innerText;
  console.log(moviePoster);
  return moviePoster;
}


// 좋아요 
$('.likethis').on('click', function() {
  var movie_title = changeT();
  var movie_poster = changeP();
  alert("좋아요 하셨습니다.")

  $.ajax({
    type: "GET", 
    url: "/movie/likethis/", 
    data: {
      "title": movie_title,
      "poster": movie_poster
    }, 
    dataType: "json",
    contentType: 'application/x-www-form-urlencoded; ',
    success: function (json) { 
        console.log("data pass success",json);
    },
      error: function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText);
      }
    
 });
});