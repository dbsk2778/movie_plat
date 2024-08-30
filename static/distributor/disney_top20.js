// 디즈니 플러스
const disney_slider = document.querySelector(".disney_carouselbox")
// console.log(net_slider)

var disney_scrollPerClick;
var disney_ImagePadding = 20;

disneyData();

var disney_scrollAmount = 0;
var timer;


function disney_sliderScrollLeft() {
  disney_slider.scrollTo({
    top:0,
    left: (disney_scrollAmount -= disney_scrollPerClick),
    behavior: "smooth",
  });

  if (disney_scrollAmount < 0) {
    disney_scrollAmount = 0;
  };
};

function disney_sliderScrollRight() {
  var disney_scrollWH = disney_slider.scrollWidth - disney_slider.scrollHeight
  // console.log(scrollWH)
  if (disney_scrollAmount <= disney_scrollWH) {
    disney_slider.scrollTo({
      top:0,
      left: (disney_scrollAmount += disney_scrollPerClick),
      behavior: "smooth"
    });
  };
};

async function disneyData() {
  disney_scrollPerClick = document.querySelector(".img-1").clientWidth + disney_ImagePadding;
}