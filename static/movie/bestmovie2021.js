const sliders5 = document.querySelector(".carouselbox5")
var scrollPerClick;
var ImagePadding = 20;

showMovieTheaterData();

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

timer = setInterval(sliderScrollRight5, 4000);

function setIntervalmovie() {
  if(scrollAmount <= sliders5.scrollWidth - sliders5.clientWidth){
    timer = setInterval(sliderScrollRight5, 4000);
  } else {
    timer = setInterval(sliderScrollLeft5, 4000);
  };
};

async function showMovieTheaterData() {
  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

    // 2021 인기영화
    var result = await axios.get(
      "https://api.themoviedb.org/3/discover/movie?api_key=" +
      api_key +
      "&?/discover/movie?with_genres=18&primary_release_year=2021"
    )

  result = result.data.results;
    
  // 이미지를 불러와서 hover을 줘서 그냥 마우스 올렸을 때, 10초 20초 30초 (세가지 단계로 구분) ? 이건 진짜 어렵다 ^^
  // 슬라이더 넘어가는 시간 조정해야 할듯 (너무 빠르게 넘어 감)
  // 일단 redirect로 html로 값 받아야 할듯

  result.map(function (cur, index) {   
    sliders5.insertAdjacentHTML(
      "beforeend",
      `<img class="img-${index} slider-img" src="http://image.tmdb.org/t/p/w185/${cur.poster_path}" onclick = "showDetail(${cur.id})"/>`
    );
  });

  scrollPerClick = document.querySelector(".img-1").clientWidth + ImagePadding;
};


// Detail 띄우는 함수
async function showDetail(param) {

  let start = '';
  start = new Date().getSeconds();

  // console.log(start);

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  var result = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "?api_key=" + api_key 
  + "&language=ko-KR");

  text = result.data;
  var sum = 0;

  // 데이터베이스에 넣는 ajax로 처리 가능할듯
  $.ajax({
    type: "GET", 
    url: "/movie/staytimeread/", 
    async:false,
    data: {
      "title": text['title']
    }, 
    dataType: "json",
    contentType: 'application/x-www-form-urlencoded; ',
    success: function (json) { 
        // console.log(json)

        for(var i in json) {
          // console.log(json[i]) 
          // console.log(json[i].length)

          for(var j in json[i]) {
            // console.log(json[i][j]['second'])
            
            sum += json[i][j]['second']
            
          }
          sum = sum / json[i].length
          // console.log(sum)
    }} 
 });

  // 영화 제목 - 모달창 밖으로 숨김
  document.getElementById("modaltitle").innerHTML = "<span style='opacity: 0;'>" + text['title'] + "</span>";

  // 영화 포스트 - 모달창 밖으로 숨김
  document.getElementById("modalposter").innerHTML = "<span style='opacity: 0;'>" + text['poster_path'] + "</span>";
  
  // 디테일 페이지 - 영화 포스터 
  // sum 값에 따라 이미지 채워지는 정도 다르게! 
  if (sum > 15) {
  document.getElementById("modalimg").innerHTML = "<div class='imgHoverEvent event1'><div class='imgBox'><img src='http://image.tmdb.org/t/p/w185/" 
  + text['poster_path'] + "' style='width:350px; height:480px;'/></div><div class='hoverBox'></div></div>";
  } else if (sum > 10) {
    document.getElementById("modalimg").innerHTML = "<div class='imgHoverEvent event1'><div class='imgBox'><img src='http://image.tmdb.org/t/p/w185/" 
  + text['poster_path'] + "' style='width:350px; height:480px;'/></div><div class='hoverBox'></div></div>";
  } else if (sum > 5) {
    document.getElementById("modalimg").innerHTML = "<div class='imgHoverEvent event1'><div class='imgBox'><img src='http://image.tmdb.org/t/p/w185/" 
  + text['poster_path'] + "' style='width:350px; height:480px;'/></div><div class='hoverBox'></div></div>";
  } else {
    document.getElementById("modalimg").innerHTML = "<div class='imgHoverEvent event1'><div class='imgBox'><img src='http://image.tmdb.org/t/p/w185/" 
  + text['poster_path'] + "' style='width:350px; height:480px;'/></div><div class='hoverBox'></div></div>";
  };

  // sum 값(데이터베이스 staytime 값이 있으면 sum 출력 / 없으면 sum 출력 안함!)
  // sum 값이 0 ~ 5 / 5 ~ 10 / 10 ~ 15 일때 if문 따로 돌려서 이미지 div class 값을 다르게 해서 이미지 색 칠하는 건 어떨까?
  if(sum) {
    // 디테일 페이지 - title, overview, release_date, vote_average 
    document.getElementById("modaltext").innerHTML = "<div class='detail_title'><br>" + text['title'] + 
    '<div class="vote"><img src="../../static/img/star.png" id="star"/>&nbsp;' + text['vote_average'] + '</div></div>' +
    '<div class="release_date">개봉일자 : ' + text['release_date'] + 
    '</div><br><div class="story">줄거리</div><br><div class="overview">' + text['overview'] + '</div><br>' + 
    '<div class="staytime">사용자들이 이 페이지에 평균적으로 머무른 시간은 ' + Math.round(sum) + '초 입니다.<div>' +
    '<br><div class="modal_youtube" onclick="showYoutube(' + param + ')">예고편 보러 가기</div>';
  } else {
    document.getElementById("modaltext").innerHTML = "<div class='detail_title'><br>" + text['title'] + 
    '<div class="vote"><img src="../../static/img/star.png" id="star"/>&nbsp;' + text['vote_average'] + '</div></div>' +
    '<div class="release_date">개봉일자 : ' + text['release_date'] + 
    '</div><br><div class="story">줄거리</div><br><div class="overview">' + text['overview'] + '</div><br>' + 
    '<br><div class="modal_youtube" onclick="showYoutube(' + param + ')">예고편 보러 가기</div>';
  }
  
  // modalyoutube창 로그 안남게 초기화
  document.getElementById("modalyoutube").innerHTML = '<div></div>'
  
  // modal 디폴트
  document.getElementById('modal').style.display = 'block';
  
  // background를 누르면 modal이 꺼지는 함수 ('modal'.style.display = 'block' -> 'none')
  const close = modal.querySelector(".modal_background");

  // date 객체가 여러개 생성되는 문제 발생 + 아마 detail 페이지의 종료 시점이 X , 이걸 강제로 초기화 해주기
  // 이벤트 버블링 발생
  close.addEventListener("click", e => {
    e.stopPropagation();

    document.getElementById('modal').style.display = 'none';
    // document.getElementById('modal').reset();

    let end = '';
    end = new Date().getSeconds(); // 종료

    // console.log(end);
    if (end - start > 0){
      let second = end - start;
      start = ''; 
      end = '';
      console.log(second); // 경과시간(밀리초)
    } else { 
      let second = 1;
      console.log(second);
    };

    $.ajax({
      type: "GET", 
      url: "/movie/staytime/", 
      data: {
        "title": text['title'],
        "second": second
      }, 
      dataType: "json",
      contentType: 'application/x-www-form-urlencoded; ',
      async: false
    });

    second='';

  }, {capture:false});
  
};

async function showYoutube(param) {

  const api_key = "7f914cd60ea3f7a8f0358344658513a7";

  var result = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "?api_key=" + api_key 
  + "&language=ko-KR");

  text = result.data;

  // console.log(text)

  var result2 = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
  "/videos?api_key=" + api_key 
  + "&language=ko-KR");

  // console.log(result2);
  youtube = result2.data.results;

  // console.log(youtube);

  // 배열의 길이가 0일 경우 예고편 없는 영화
  if(youtube.length != 0) { 
    // 유튜브를 다른 창에 띄어야 함! 그래야 detail 페이지가 꺼지지 않음! 계속 time 측정
    document.getElementById("modalyoutube").innerHTML = 
    '<br><div class="youtube"><a href="https://www.youtube.com/embed/' + youtube[0]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' 
                                  + youtube[0]['key'] + '" frameborder="1" class="youtube" target="_blank">클릭시 유튜브로 이동합니다.</a></div>';
  } else {
    document.getElementById("modalyoutube").innerHTML = "<br><br><div class='no_youtube';>예고편 없음</div>";
  };
  
  
};


// 버튼누르면 콘솔에 영화 제목 출력
function changeT() {
  var movieTitle = document.getElementById("modaltitle").innerText;
  console.log('좋아요한 영화:', movieTitle);
  return movieTitle;
}
// 버튼누르면 콘솔에 영화 poster_path 출력
function changeP() {
  var moviePoster = document.getElementById("modalposter").innerText;
  console.log('좋아요한 포스트:', moviePoster);
  return moviePoster;
}

// 좋아요 
$('.likethis').on('click', function() {
  var movie_title = changeT();
  var movie_poster = changeP();
  alert("좋아요 하셨습니다.")

  $.ajax({
    type: "GET", 
    url: "/movie/likethis/", 
    data: {
      "title": movie_title,
      "poster": movie_poster
    }, 
    dataType: "json",
    contentType: 'application/x-www-form-urlencoded; ',
    success: function (json) { 
        console.log("data pass success",json);
    },
    error: function(xhr,errmsg,err) {
      console.log(xhr.status + ": " + xhr.responseText);
    }
    
 });
});