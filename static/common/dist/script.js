// 아이디, 비밀번호 입력 후 넘어가는 next button 관련
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
    $('.container').html('<link href="https://127.0.0.1:8000/home/">');
  }
  $('.container').removeClass('error');
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
    },450);     
}

