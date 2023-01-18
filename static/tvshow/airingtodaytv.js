const slider4 = document.querySelector(".carouselbox4")
var scrollPerClick;
var ImagePadding =20;

showAiringTodayTV();

var scrollAmount = 0;

var timer;

function sliderScrollLeft4() {
  slider4.scrollTo({
    top: 0,
    left: (scrollAmount -= scrollPerClick),
    behavior: "smooth"
  });

  if (scrollAmount < 0) {
    scrollAmount = 0
  };
};



function sliderScrollRight4() {
  if (scrollAmount <= slider4.scrollWidth - slider4.clientWidth) {
    slider4.scrollTo({
      top: 0,
      left: (scrollAmount += scrollPerClick),
      behavior: "smooth"
    });
  };
};

timer = setInterval(sliderScrollRight4, 3000);

async function showAiringTodayTV() {

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";
  // https://api.themoviedb.org/3/tv/airing_today?api_key=<<api_key>>&language=en-US&page=1
  var result = await axios.get(
    "https://api.themoviedb.org/3/tv/airing_today?api_key=" +
    api_key +
    "&language=ko-KR&page=1"
  )

  result = result.data.results;
  // console.log(result)

  result.map(function(cur, index) {
    slider4.insertAdjacentHTML(
      "beforeend",
      `<img class="img-${index} slider-img" src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" onclick = "showTvDetail(${cur.id})"/>`
    );
  });

  scrollPerClick = document.querySelector(".img-1").clientWidth + ImagePadding;
};


