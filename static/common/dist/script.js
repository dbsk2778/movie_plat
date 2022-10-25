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
   $('.bullets span.active').removeClass('active').next().addClass('active');
  } else {  // 이메일,비밀번호 입력 후 성공시 진행되는 페이지 관련
    $('.container').css('background','#0C0C0C').html($('.spinnerWrapper').html());
    setTimeout(function(){
      $('.container').html('<div class="success"><i class="fa fa-check"></i><h2>Account Created</h2></div>');
    },4000);
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

