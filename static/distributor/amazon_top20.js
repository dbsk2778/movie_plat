// 아마존 프라임
const amazon_slider = document.querySelector(".amazon_carouselbox")
// console.log(net_slider)

var amazon_scrollPerClick;
var amazon_ImagePadding = 20;

amazonData();

var amazon_scrollAmount = 0;
var timer;


function amazon_sliderScrollLeft() {
  amazon_slider.scrollTo({
    top:0,
    left: (amazon_scrollAmount -= amazon_scrollPerClick),
    behavior: "smooth",
  });

  if (amazon_scrollAmount < 0) {
    amazon_scrollAmount = 0;
  };
};

function amazon_sliderScrollRight() {
  var amazon_scrollWH = amazon_slider.scrollWidth - amazon_slider.scrollHeight
  // console.log(scrollWH)
  if (amazon_scrollAmount <= amazon_scrollWH) {
    amazon_slider.scrollTo({
      top:0,
      left: (amazon_scrollAmount += amazon_scrollPerClick),
      behavior: "smooth"
    });
  };
};

async function amazonData() {
  amazon_scrollPerClick = document.querySelector(".img-1").clientWidth + amazon_ImagePadding;
}