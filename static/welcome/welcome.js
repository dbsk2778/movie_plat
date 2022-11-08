const sliders = document.querySelector(".carouselbox")
var scrollPerClick;
var ImagePadding =20;

showMovieData();

var scrollAmount = 0;

function sliderScrollLeft() {
    sliders.scrollTo({
        top: 0,
        left: (scrollAmount -= scrollPerClick),
        behavior: "smooth"
    });

    if(scrollAmount < 0){
        scrollAmount = 0
    };
};

function sliderScrollRight() {
    if(scrollAmount <= sliders.scrollWidth - sliders.clientWidth){
        sliders.scrollTo({
            top: 0,
            left: (scrollAmount += scrollPerClick),
            behavior: "smooth"

        });
    };
};


async function showMovieData() {
    const api_key = "7f914cd60ea3f7a8f0358344658513a7";
    
    var result = await axios.get(
        "https://api.themoviedb.org/3/discover/movie?api_key=" +
        api_key +
        "&sort_by=popularity.desc"
    );

    result = result.data.results;

    result.map(function (cur,index) {
        sliders.insertAdjacentHTML(
            "beforeend",
            `<img class="img-${index} slider-img" src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" />`
        );
    });

    scrollPerClick = document.querySelector(".img-1").clientWidth + ImagePadding;
};