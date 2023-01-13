const sliders3 = document.querySelector(".carouselbox3")
var scrollPerClick;
var ImagePadding =20;

showHighestMovieData();

var scrollAmount = 0;

var timer;

function sliderScrollLeft3() {
  sliders3.scrollTo({
    top: 0,
    left: (scrollAmount -= scrollPerClick),
    behavior: "smooth"
  });

  if (scrollAmount < 0) {
    scrollAmount = 0
  };
};

function sliderScrollRight3() {
  if (scrollAmount <= sliders3.scrollWidth - sliders3.clientWidth) {
    sliders3.scrollTo({
      top: 0,
      left: (scrollAmount += scrollPerClick),
      behavior: "smooth"
    });
  };
};

timer = setInterval(sliderScrollRight3, 3000);

async function showHighestMovieData() {

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  // highest rated movies
  var result = await axios.get(
    "https://api.themoviedb.org/3/movie/top_rated?api_key=" +
    api_key +
    "&language=ko-KR&page=1"
  );

  result = result.data.results;

  result.map(function(cur, index) {
    sliders3.insertAdjacentHTML(
      "beforeend",
      `<img class="img-${index} slider-img" src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" onclick = "showDetail(${cur.id})"/>`
    );
  });

  scrollPerClick = document.querySelector(".img-1").clientWidth + ImagePadding;
};