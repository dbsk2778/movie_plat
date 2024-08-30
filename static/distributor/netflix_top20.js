const net_slider = document.querySelector(".net_carouselbox")
// console.log(net_slider)

var net_scrollPerClick;
var net_ImagePadding = 20;

netFlixData();

var net_scrollAmount = 0;
var timer;


function net_sliderScrollLeft() {
  net_slider.scrollTo({
    top:0,
    left: (net_scrollAmount -= net_scrollPerClick),
    behavior: "smooth",
  });

  if (net_scrollAmount < 0) {
    net_scrollAmount = 0;
  };
};

function net_sliderScrollRight() {
  var net_scrollWH = net_slider.scrollWidth - net_slider.scrollHeight
  // console.log(scrollWH)
  if (net_scrollAmount <= net_scrollWH) {
    net_slider.scrollTo({
      top:0,
      left: (net_scrollAmount += net_scrollPerClick),
      behavior: "smooth"
    });
  };
};

async function netFlixData() {
  net_scrollPerClick = document.querySelector(".img-1").clientWidth + net_ImagePadding;
}



