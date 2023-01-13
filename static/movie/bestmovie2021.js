const sliders5 = document.querySelector(".carouselbox5")
var scrollPerClick;
var ImagePadding = 20;
``
showMovieTheaterData();

setIntervalmovie();

var scrollAmount = 0;

var timer;

function sliderScrollLeft5() {
  sliders5.scrollTo({
    top: 0,
    left: (scrollAmount -= scrollPerClick),
    behavior: "smooth",
  });

  if (scrollAmount < 0) {
    scrollAmount = 0
  };
};

function sliderScrollRight5() {
  if (scrollAmount <= sliders5.scrollWidth - sliders5.clientWidth) {
    sliders5.scrollTo({
      top: 0,
      left: (scrollAmount += scrollPerClick),
      behavior: "smooth"

    });
  };
};

timer = setInterval(sliderScrollRight5, 3000);

function setIntervalmovie() {
  if(scrollAmount <= sliders5.scrollWidth - sliders5.clientWidth){
    timer = setInterval(sliderScrollRight5, 3000);
  } else {
    timer = setInterval(sliderScrollLeft5, 3000);
  };
};

async function showMovieTheaterData() {
  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

    // 2021 인기영화
    var result = await axios.get(
      "https://api.themoviedb.org/3/discover/movie?api_key=" +
      api_key +
      "&?/discover/movie?with_genres=18&primary_release_year=2021"
    )

  result = result.data.results;

  result.map(function (cur, index) {
    sliders5.insertAdjacentHTML(
      "beforeend",
      `<img class="img-${index} slider-img" src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" onclick = "showDetail(${cur.id})"/>`
    );
  });

  scrollPerClick = document.querySelector(".img-1").clientWidth + ImagePadding;
};

async function showDetail(param) {
  // param을 가지고 api 호출해서 영화 1의 정보 가져오기
  // modal 나중에 css absolute나 fixed로 적용
  // 부트스트랩 showmodal 사용

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  // get
  var result = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "?api_key=" + api_key 
  + "&language=ko-KR");
  // console.log(result);
  
  text = result.data;
  

  var result2 = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "/videos?api_key=" + api_key 
  + "&language=ko-KR");

  // https://www.youtube.com/embed/{key}?controls=&autoplay=1&loop=1&mute=1&playlist={key}
  youtube = result2.data.results;
  

  document.getElementById("modalimg").innerHTML = "<div><br><br><br><img src='http://image.tmdb.org/t/p/w185/" + text['poster_path'] + "' style='width:350px; height:480px;'" + " /></div>";
  

  // title, overview, release_date, vote_average
  document.getElementById("modaltext").innerHTML = "<div><br><br><b style='font-size:xx-large'>" + text['title'] + 
  '<div style="float:right;font-size:large;margin-top:10px;"><img src="../../static/img/star.png" style="width:20px;height:20px;" />&nbsp;' + text['vote_average'] + '</div>' +
  '</b></div><div style="font-size:x-small">개봉일자 : ' + text['release_date'] + 
  '</div><br><br><b style="font-size:large">줄거리</b><div><br>' + 
  text['overview'] + '</div><br>' ;
    
  
  // 아이디 modal
  document.getElementById('modal').style.display = 'block';

  const close = modal.querySelector(".modalBox");

  close.addEventListener("click", e => {
    document.getElementById('modal').style.display = 'none';
  });
  
  if(!youtube[0]['key']) {
    document.getElementById("modalyoutube").innerHTML = "<div></div>";
  } else if(!youtube[1]['key']) {
      // console.log(youtube[i]['key']);
      document.getElementById("modalyoutube").innerHTML = 
      '<div><b style="font-size:large;color:white;">예고편</b><div><div><br><iframe src="https://www.youtube.com/embed/' + youtube[0]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + youtube[0]['key'] + '" frameborder="1" style="width:100px;"></iframe><div>';
  } else {
    document.getElementById("modalyoutube").innerHTML = 
    '<div><b style="font-size:large;color:white;">예고편</b></div><div><br><iframe src="https://www.youtube.com/embed/' + youtube[0]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + youtube[0]['key'] + '" frameborder="1"></iframe>' +
    '<iframe src="https://www.youtube.com/embed/' + youtube[1]['key'] + '?controls=&autoplay=0&loop=1&mute=1&playlist=' + youtube[1]['key'] + '" frameborder="1"></iframe><div>';
  };
  
};

if(!youtube[0]['key']) {
  document.getElementById("modalyoutube").innerHTML = "<div></div>";
} else if(!youtube[1]['key']) {
    // console.log(youtube[i]['key']);
    document.getElementById("modalyoutube").innerHTML = 
    '<div><b style="font-size:large;color:white;">예고편</b><div><div><br><iframe src="https://www.youtube.com/embed/' + youtube[0]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + youtube[0]['key'] + '" frameborder="1" style="width:100px;"></iframe><div>';
} else {
  document.getElementById("modalyoutube").innerHTML = 
  '<div><b style="font-size:large;color:white;">예고편</b></div><div><br><iframe src="https://www.youtube.com/embed/' + youtube[0]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + youtube[0]['key'] + '" frameborder="1"></iframe>' +
  '<iframe src="https://www.youtube.com/embed/' + youtube[1]['key'] + '?controls=&autoplay=0&loop=1&mute=1&playlist=' + youtube[1]['key'] + '" frameborder="1"></iframe><div>';
};
