
// 로그인 제출 함수
function formCheck() {
  document.getElementById('loginForm').submit();
}


// 아이디, 비밀번호 입력 후 넘어가는 next button
$('.nextBtn').on('click',function(){
  var parentRef =  $(this).parent();
  var inputVal = parentRef.find('input').val();
  if(checkLength(inputVal,1)){
    add_remove_effects(parentRef,'shake');
    $('.container').addClass('error');
    return ;
  } else {
    if(checkLength(inputVal,4)){
      return ;
    }
  }
  if(!parentRef.hasClass('lastField')){
   parentRef.addClass('hide'); 
   parentRef.next().addClass('shown').addClass('visible');
  } else {
  }
  $('.container').removeClass('error');
});


// 아이디 엔터 함수
$("input[name=username]").keypress(function (e) {
  if (e.keyCode == 13) {
    var parentRef = $(this).parent();
    var inputVal = parentRef.find('input').val();
    if(checkLength(inputVal,1)){
      add_remove_effects(parentRef,'shake');
      $('.container').addClass('error');
      return ;
    } else {
      if(checkLength(inputVal,4)){
        return ;
      }
    }
    if(!parentRef.hasClass('lastField')){
    parentRef.addClass('hide'); 
    parentRef.next().addClass('shown').addClass('visible');
    } else {
    }
    $('.container').removeClass('error');
}
});


// 비밀번호 엔터 함수
$("input[name=password]").keypress(function (e) {
  if (e.keyCode == 13) {
    formCheck();
}
});


// 이메일, 비밀번호 체크 관련
function checkLength(data,length){
  data = $.trim(data);
  if(data.length < length){
    return true;
  }
  return false;
}

var add_remove_effects = function(ref,classname){
  var $a = ref.addClass(classname);
  var $b = classname;
    setTimeout(function(){
      $a.removeClass($b);
    },220); // 비밀번호 입력 후 시간
}