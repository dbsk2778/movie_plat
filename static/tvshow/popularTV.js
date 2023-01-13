const slider3 = document.querySelector(".carouselbox3")
var scrollPerClick;
var ImagePadding =20;

showPopularTV();

var scrollAmount = 0;

var timer;

function sliderScrollLeft3() {
  slider3.scrollTo({
    top: 0,
    left: (scrollAmount -= scrollPerClick),
    behavior: "smooth"
  });

  if (scrollAmount < 0) {
    scrollAmount = 0
  };
};



function sliderScrollRight3() {
  if (scrollAmount <= slider3.scrollWidth - slider3.clientWidth) {
    slider3.scrollTo({
      top: 0,
      left: (scrollAmount += scrollPerClick),
      behavior: "smooth"
    });
  };
};

timer = setInterval(sliderScrollRight3, 3000);

async function showPopularTV() {

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";
  // https://api.themoviedb.org/3/tv/popular?api_key=<<api_key>>&language=en-US&page=1
  var result = await axios.get(
    "https://api.themoviedb.org/3/tv/popular?api_key=" +
    api_key +
    "&language=ko-KR&page=1"
  )

  result = result.data.results;
  // console.log(result)

  result.map(function(cur, index) {
    slider3.insertAdjacentHTML(
      "beforeend",
      `<img class="img-${index} slider-img" src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" onclick = "showTvDetail(${cur.id})"/>`
    );
  });

  scrollPerClick = document.querySelector(".img-1").clientWidth + ImagePadding;
};


