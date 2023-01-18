const sliders5 = document.querySelector(".carouselbox5")
var scrollPerClick;
var ImagePadding = 20;
<<<<<<< HEAD

=======
``
>>>>>>> e6440649888e20617df7fe60bac43092bd34082f
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

<<<<<<< HEAD
// Detail 띄우는 함수
=======
>>>>>>> e6440649888e20617df7fe60bac43092bd34082f
async function showDetail(param) {

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  // get (param = tmdb movie id에 맞는 정보 값 가져오기)
  var result = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "?api_key=" + api_key 
  + "&language=ko-KR");
  // console.log(result);
  
  text = result.data;
<<<<<<< HEAD
=======
  
>>>>>>> e6440649888e20617df7fe60bac43092bd34082f

  var result2 = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "/videos?api_key=" + api_key 
  + "&language=ko-KR");

  youtube = result2.data.results;
  
<<<<<<< HEAD
  // 이미지 하나 띄우기
  document.getElementById("modalimg").innerHTML = "<div><br><br><br><img src='http://image.tmdb.org/t/p/w185/" + text['poster_path'] + "' style='width:350px; height:480px;'" + " /></div>";
 
  // 정보 띄우기 
=======

  document.getElementById("modalimg").innerHTML = "<div><br><br><br><img src='http://image.tmdb.org/t/p/w185/" + text['poster_path'] + "' style='width:350px; height:480px;'" + " /></div>";
  

  // title, overview, release_date, vote_average
>>>>>>> e6440649888e20617df7fe60bac43092bd34082f
  document.getElementById("modaltext").innerHTML = "<div><br><br><b style='font-size:xx-large'>" + text['title'] + 
  '<div style="float:right;font-size:large;margin-top:10px;"><img src="../../static/img/star.png" style="width:20px;height:20px;" />&nbsp;' + text['vote_average'] + '</div>' +
  '</b></div><div style="font-size:x-small;">개봉일자 : ' + text['release_date'] + 
  '</div><br><br><b style="font-size:large">줄거리</b><div><br>' + 
  text['overview'] + '</div><br>' ;
    
  
  // detail modal창 띄울 때 modalbox 클릭하게 되면 detail 닫힘
  document.getElementById('modal').style.display = 'block';

  const close = modal.querySelector(".modalBox");

  close.addEventListener("click", e => {
    document.getElementById('modal').style.display = 'none';
  });
  
<<<<<<< HEAD
  // youtube 있을 경우 youtube 띄우기
  // youtube는 사용자가 조작 못함(youtube 자체 권한 때문인듯?)
=======
>>>>>>> e6440649888e20617df7fe60bac43092bd34082f
  if(!youtube[0]['key']) {
    
    document.getElementById("modalyoutube").innerHTML = "<div></div>";
<<<<<<< HEAD

=======
>>>>>>> e6440649888e20617df7fe60bac43092bd34082f
  } else if(!youtube[1]['key']) {
      // console.log(youtube[i]['key']);
      document.getElementById("modalyoutube").innerHTML = 
      '<div><b style="font-size:large;color:white;">예고편</b><div><div><br><iframe src="https://www.youtube.com/embed/' + youtube[0]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + youtube[0]['key'] + '" frameborder="1" style="width:100px;"></iframe><div>';
<<<<<<< HEAD
  
=======
>>>>>>> e6440649888e20617df7fe60bac43092bd34082f
  } else {
    document.getElementById("modalyoutube").innerHTML = 
    '<div><b style="font-size:large;color:white;">예고편</b></div><div><br><iframe src="https://www.youtube.com/embed/' + youtube[0]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + youtube[0]['key'] + '" frameborder="1"></iframe>' +
    '<iframe src="https://www.youtube.com/embed/' + youtube[1]['key'] + '?controls=&autoplay=0&loop=1&mute=1&playlist=' + youtube[1]['key'] + '" frameborder="1"></iframe><div>';
  };
  
};
<<<<<<< HEAD
=======

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
>>>>>>> e6440649888e20617df7fe60bac43092bd34082f
