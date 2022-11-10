const sliders4 = document.querySelector(".carouselbox4")
var scrollPerClick;
var ImagePadding =20;

showMovieTheaterData();

var scrollAmount = 0;

var timer;

function sliderScrollLeft4() {
  sliders4.scrollTo({
    top: 0,
    left: (scrollAmount -= scrollPerClick),
    behavior: "smooth",
  });

  if (scrollAmount < 0) {
    scrollAmount = 0
  };
};


function sliderScrollRight4() {
  if (scrollAmount <= sliders4.scrollWidth - sliders4.clientWidth) {
    sliders4.scrollTo({
      top: 0,
      left: (scrollAmount += scrollPerClick),
      behavior: "smooth"

    });
  };
};

timer = setInterval(sliderScrollRight4, 3000);

async function showMovieTheaterData() {
  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

    // 2021 인기영화
    var result = await axios.get(
      "https://api.themoviedb.org/3/discover/movie?api_key=" +
      api_key +
      "&?/discover/movie?with_genres=18&primary_release_year=2021"
    )

  result = result.data.results;

  result.map(function (cur, index) {
    sliders4.insertAdjacentHTML(
      "beforeend",
      `<img class="img-${index} slider-img" src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" onclick = "showDetail(${cur.id})"/>`
    );
  });

  scrollPerClick = document.querySelector(".img-1").clientWidth + ImagePadding;
};
async function showDetail(param) {
  // param을 가지고 api 호출해서 영화 1의 정보 가져오기
  // modal 나중에 css absolute나 fixed로 적용
  // 부트스트랩 showmodal 사용

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  // get
  var result = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "?api_key=" + api_key 
  + "&language=ko-KR");

  text = result.data;
  // console.log(text)

  var result2 = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "/videos?api_key=" + api_key 
  + "&language=ko-KR");

  // https://www.youtube.com/embed/{key}?controls=&autoplay=1&loop=1&mute=1&playlist={key}
  youtube = result2.data.results;
  

  document.getElementById("modalimg").innerHTML = "<div><br><br><img src='http://image.tmdb.org/t/p/w185/" + text['poster_path'] + "' style='width:350px; height:480px;'" + " /></div>";
  

  // title, overview, release_date, vote_average
  document.getElementById("modaltext").innerHTML = "<div><br><br><b style='font-size:xx-large'>" + text['title'] + 
    '</b></div><div style="font-size:x-small">개봉일자 : ' + text['release_date'] + 
    '</div><br><br><b style="font-size:large">줄거리</b><div><br>' + 
    text['overview'] + '</div><br><br><div>★' + text['vote_average'] + '</div>' ;

  // document.getElementById("modaltext").innerHTML = "<div><br><br><b style='font-size:xx-large'>" + text['title'] + 
  //   '</b></div>' + '</div><img src="../img/star.png" style="float:right"' + text['vote_average'] + ' />' + '<br><br><div style="font-size:x-small">개봉일자 : ' + text['release_date'] + 
  //   '</div><br><br><b style="font-size:large">줄거리</b><div><br>' + 
  //   text['overview'] ;
    
  
  // 아이디 modal
  document.getElementById('modal').style.display = 'block';

  const close = modal.querySelector(".modalBox");

  close.addEventListener("click", e => {
    document.getElementById('modal').style.display = 'none';
  });
  console.log(youtube);

  // for(var i=0; i<=2; i++){
  //   console.log(youtube[i]['key']);
  //   document.getElementById("modalyoutube").innerHTML = 
  //    '<iframe src="https://www.youtube.com/embed/' + youtube[i]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + youtube[i]['key'] + '"></iframe>';
  //      // 'beforeend', 
  //      // `<iframe src="https://www.youtube.com/embed/' + ${youtube[i]['key']} + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + ${youtube[i]['key']} + '">동영상 없음~!~!</iframe>'`
  //  };

  if(!youtube[0]['key']) {
    document.getElementById("modalyoutube").innerHTML = "<div></div>";
  } else {
    for(var i=0; i<=2; i++){
      console.log(youtube[i]['key']);
      document.getElementById("modalyoutube").innerHTML = 
     '<iframe src="https://www.youtube.com/embed/' + youtube[i]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + youtube[i]['key'] + '"></iframe>';
      // document.getElementById("modalyoutube").insertAdjacentHTML(
      //   'beforeend',
      //   `<iframe src="https://www.youtube.com/embed/${youtube[i]['key']}?controls=&autoplay=1&loop=1&mute=1&playlist=${youtube[i]['key']}"></iframe>`
    }
  };
  
};

// async function showYoutube(param) {
//   // document.getElementById.innerHTML = '<h1>' + param + '</h1>';
//   console.log(param);
// }


