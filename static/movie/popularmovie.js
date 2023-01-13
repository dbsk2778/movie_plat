const slider = document.querySelector(".carouselbox")
var scrollPerClick;
var ImagePadding =20;

showHighestMovieData();

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

async function showHighestMovieData() {

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  // highest rated movies
  var result = await axios.get(
    "https://api.themoviedb.org/3/movie/popular?api_key=" +
    api_key +
    "&language=ko-KR&page=1"
  );

  result = result.data.results;

  result.map(function(cur, index) {
    slider.insertAdjacentHTML(
      "beforeend",
      `<img class="img-${index} slider-img" src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" onclick = "showDetail(${cur.id})"/>`
    );
  });

  scrollPerClick = document.querySelector(".img-1").clientWidth + ImagePadding;
};

