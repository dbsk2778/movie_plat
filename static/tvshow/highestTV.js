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

timer = setInterval(sliderScrollRight, 3000);

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
  // param을 가지고 api 호출해서 영화 1의 정보 가져오기
  // modal 나중에 css absolute나 fixed로 적용
  // 부트스트랩 showmodal 사용

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  // https://api.themoviedb.org/3/tv/{tv_id}?api_key=<<api_key>>&language=en-US
  var result = await axios.get("https://api.themoviedb.org/3/tv/" + param + 
  "?api_key=" + api_key 
  + "&language=ko-KR");

  text = result.data;
  // console.log(text)

  genre = text['genres'][0]['name']
  genre = text['genres'][1]['name']
  // console.log(genre)
  document.getElementById("modalimg").innerHTML = "<div><br><br><br><img src='http://image.tmdb.org/t/p/w185/" + text['poster_path'] + "' style='width:350px; height:480px;'" + " /></div>";
  

  // title, overview, release_date, vote_average
  document.getElementById("modaltext").innerHTML = 
  '<div><br><br><b style="font-size:xx-large">' + text['name'] + 
  '<div style="float:right;font-size:large;margin-top:10px;"><img src="../../static/img/star.png" style="width:20px;height:20px;" />&nbsp;' + text['vote_average'] + '</div></b></div>' +
  '<div style="font-size:medium;color:gray">' + text['genres'][0]['name'] + ', ' + text['genres'][1]['name'] + '</div><br>' + 
  '<div style="font-size:small"><b>방영 시작일</b> : ' + text['first_air_date'] + 
  '<b>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp최근 방영일</b> : ' + text['last_air_date'] + 
  '<br><br><div style="color:red;font-size:large"><b>시즌 : '+ text['number_of_seasons'] + '개</b></div><br><b style="font-size:large">줄거리</b><div><br>' + text['overview'] + 
  '</div><br><div style="font-size:large"><b><a href="'+ text['homepage'] + '">메인 홈페이지로 이동</a></b></div><br>' ;
    

  // 아이디 modal
  document.getElementById('modal').style.display = 'block';

  const close = modal.querySelector(".modalBox");

  close.addEventListener("click", e => {
    document.getElementById('modal').style.display = 'none';
  });


};

