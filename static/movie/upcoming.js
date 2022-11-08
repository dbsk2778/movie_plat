const sliders5 = document.querySelector(".carouselbox5")
var scrollPerClick;
var ImagePadding =20;

showUpcomingMovieData();
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

function setIntervalmovie() {
  if(scrollAmount <= sliders5.scrollWidth - sliders5.clientWidth){
    timer = setInterval(sliderScrollRight5, 3000);
  } else {
    timer = setInterval(sliderScrollLeft5, 3000);
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
    sliders5.insertAdjacentHTML(
      "afterbegin",
      `<img class="img-${index} slider-img" src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" /><br>`,
      "beforeend",
      `<p>${cur.original_title}</p>`,
      // `<div>${cur.original_title}</div>`,
    );
    // sliders5.insertAdjacentHTML(
    //   "afterend",
    //   `<div>${cur.original_title}</div>`,
    // );
  });
 
  scrollPerClick = document.querySelector(".img-1").clientWidth + ImagePadding;
};
