// 아마존 프라임
const apple_slider = document.querySelector(".apple_carouselbox")
// console.log(net_slider)

var apple_scrollPerClick;
var apple_ImagePadding = 20;

appleData();

var apple_scrollAmount = 0;
var timer;


function apple_sliderScrollLeft() {
  apple_slider.scrollTo({
    top:0,
    left: (apple_scrollAmount -= apple_scrollPerClick),
    behavior: "smooth",
  });

  if (apple_scrollAmount < 0) {
    apple_scrollAmount = 0;
  };
};

function apple_sliderScrollRight() {
  var apple_scrollWH = apple_slider.scrollWidth - apple_slider.scrollHeight
  // console.log(scrollWH)
  if (apple_scrollAmount <= apple_scrollWH) {
    apple_slider.scrollTo({
      top:0,
      left: (apple_scrollAmount += apple_scrollPerClick),
      behavior: "smooth"
    });
  };
};

async function appleData() {
  apple_scrollPerClick = document.querySelector(".img-1").clientWidth + apple_ImagePadding;
}