function checkForm() {
    var sub = document.getElementById("search1");
    // 아이디 입력 유무 체크
    if(sub.length == 0) {
        window.alert("검색어를 입력해주세요");
        // document.sf.search1.focus();
        // document.getElementById('sub').select();
        // alert("검색어를 입력해주세요.")
        
        return false; // 입력이 안되어 있다면 submit 이벤트를 중지
    }
}