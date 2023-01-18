// console.log(typeof(document.getElementById('movie_info')))  // type = object

// movie_dict = document.getElementById('movie_info').innerHTML
// let result = movie_dict.substring(1, movie_dict.length-1)
// result = result.substring(0, result.indexOf('}')+1)
// console.log(result)
// movie_dict_temp =JSON.stringify(result)
// console.log(movie_dict_temp)
// for (var key in movie_dict) {
//   console.log(movie_dict[key]);
// }

myData()

var temp = [];

function myData() {
  // querySelectorAll()은 리스트 타입 반환, 전체 다 가져오
  // getAttribute 사용하면 여기서부터 for문 돌려야 함(만약 안되면 해보기)
  var movie_id = document.querySelectorAll(".a");
  console.log(movie_id);
  var tmp = {};

  // for문 여기부터 돌리기
  // for (var i = 0; i < movie_id.length; i++) {
  // tmp["movie_id"] = movie_id;
  // temp.push(tmp)
  // console.log(tmp);
  //   var image = images[i];
  //   alert(image.getAttribute(src));
  // }
  // 

}





