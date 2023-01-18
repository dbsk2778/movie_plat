// console.log(document.getElementById("meta_id").innerHTML)

const img = document.querySelector(".poster_img_box")

// const title = document.querySelector(".title_box")

meta_id = document.getElementById("meta_id").innerHTML
meta_id = meta_id .replace("{'movie_id': [","")
meta_id = meta_id .replace("]}","")

// meta_id 배열로 변환
const meta_arr = meta_id.split(',')
// console.log(meta_arr)

showMetaRecommend()

async function showMetaRecommend(){
    
    const api_key = "7f914cd60ea3f7a8f0358344658513a7";

    for(let i=0; i < meta_arr.length; i++) {
        param = meta_arr[i]

        var result = await axios.get("https://api.themoviedb.org/3/movie/" + param 
        + "?api_key=" + api_key 
        + "&language=ko-KR");

        text = result.data;

        // console.log(`${text.poster_path}`)
        
        img.insertAdjacentHTML(
            "beforeend",
            `<div class="total"><div class="ImgDiv"><img src="http://image.tmdb.org/t/p/w185/${text.poster_path}" 
            class="posterImg" onclick = "showDetail(${text.id})"/></div><div class="title_name"">${text.title}</div></div>`
          );
    }
}

// Detail 띄우는 함수
async function showDetail(param) {

    const api_key = "7f914cd60ea3f7a8f0358344658513a7";
  
    // get (param = tmdb movie id에 맞는 정보 값 가져오기)
    var result = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
    "?api_key=" + api_key 
    + "&language=ko-KR");
  
    text = result.data;
  
    var result2 = await axios.get("https://api.themoviedb.org/3/movie/" + param + 
    "/videos?api_key=" + api_key 
    + "&language=ko-KR");
  
    youtube = result2.data.results;
    
    // 이미지 하나 띄우기
    document.getElementById("modalimg").innerHTML = "<div><br><br><br><img src='http://image.tmdb.org/t/p/w185/" + text['poster_path'] + "' style='width:350px; height:480px;'" + " /></div>";
   
    // 정보 띄우기 
    document.getElementById("modaltext").innerHTML = "<div><br><br><b style='font-size:xx-large'>" + text['title'] + 
    '<div style="float:right;font-size:large;margin-top:10px;"><img src="../../static/img/star.png" style="width:20px;height:20px;" />&nbsp;' + text['vote_average'] + '</div>' +
    '</b></div><div style="font-size:x-small;">개봉일자 : ' + text['release_date'] + 
    '</div><br><br><b style="font-size:large">줄거리</b><div><br>' + 
    text['overview'] + '</div><br>' ;
      
    
    // detail modal창 띄울 때 modalbox 클릭하게 되면 detail 닫힘
    document.getElementById('modal').style.display = 'block';
  
    const close = modal.querySelector(".modalBox");
  
    close.addEventListener("click", e => {
      document.getElementById('modal').style.display = 'none';
    });
    
    // youtube 있을 경우 youtube 띄우기
    // youtube는 사용자가 조작 못함(youtube 자체 권한 때문인듯?)
    if(!youtube[0]['key']) {
      
      document.getElementById("modalyoutube").innerHTML = "<div></div>";
  
    } else if(!youtube[1]['key']) {
        // console.log(youtube[i]['key']);
        document.getElementById("modalyoutube").innerHTML = 
        '<div><b style="font-size:large;color:white;">예고편</b><div><div><br><iframe src="https://www.youtube.com/embed/' + youtube[0]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + youtube[0]['key'] + '" frameborder="1" style="width:100px;"></iframe><div>';
    
    } else {
      document.getElementById("modalyoutube").innerHTML = 
      '<div><b style="font-size:large;color:white;">예고편</b></div><div><br><iframe src="https://www.youtube.com/embed/' + youtube[0]['key'] + '?controls=&autoplay=1&loop=1&mute=1&playlist=' + youtube[0]['key'] + '" frameborder="1"></iframe>' +
      '<iframe src="https://www.youtube.com/embed/' + youtube[1]['key'] + '?controls=&autoplay=0&loop=1&mute=1&playlist=' + youtube[1]['key'] + '" frameborder="1"></iframe><div>';
    };
    
  };