const sliders2 = document.querySelector(".carouselbox2")
var scrollPerClick;
var ImagePadding =20;

showUpcomingMovieData();

setIntervalmovie();

var scrollAmount = 0;

var timer;

function sliderScrollLeft2() {
  sliders2.scrollTo({
    top: 0,
    left: (scrollAmount -= scrollPerClick),
    behavior: "smooth",
  });

  if (scrollAmount < 0) {
    scrollAmount = 0
  };
};

function sliderScrollRight2() {
  if (scrollAmount <= sliders2.scrollWidth - sliders2.clientWidth) {
    sliders2.scrollTo({
      top: 0,
      left: (scrollAmount += scrollPerClick),
      behavior: "smooth"

    });
  };
};

function setIntervalmovie() {
  if(scrollAmount <= sliders2.scrollWidth - sliders2.clientWidth){
    timer = setInterval(sliderScrollRight2, 3000);
  } else {
    timer = setInterval(sliderScrollLeft2, 3000);
  };
};

async function showUpcomingMovieData() {
  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

    // 개봉 예정작
    var result = await axios.get(
      "https://api.themoviedb.org/3/movie/upcoming?api_key=" +
      api_key +
      "&language=ko-Kr&page=1"
    );

  result = result.data.results;

  result.map(function (cur, index) {
    sliders2.insertAdjacentHTML(
      "beforeend",
      `<img class="img-${index} slider-img" src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" onclick = "showDetail(${cur.id})"/>`
    );
 
  });
 
  scrollPerClick = document.querySelector(".img-1").clientWidth + ImagePadding;
};


async function showDetail(param) {

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  // get
  var result = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "?api_key=" + api_key 
  + "&language=ko-KR");

  text = result.data
  // console.log(text)

  document.getElementById("modalimg").innerHTML = "<img src='http://image.tmdb.org/t/p/w185/" + text['poster_path'] + "' style='width:300px; height:400px;'" + " />";
      
  // title, overview, release_date, vote_average
  document.getElementById("modaltext").innerHTML = "<div><b style='font-size:large'>" + text['title'] + 
        '</b></div><br><div>개봉일자 : ' + text['release_date'] + 
        '</div><br><br><div>줄거리 : ' +text['overview'] + 
        '</div><br><br><div>평점 :' + text['vote_average'] + '</div>';
}

