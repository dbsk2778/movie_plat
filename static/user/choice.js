function autologin(img) {
    if(img.checked) {
        img.checked = false;
        img.src="/경로/off.gif"
    } else {
        img.checked = true;
        img.src="/경로/on.gif"
            }
}


function 폼전송() {
    var frm	= document.frm;
        if(j$('.checkbox').is(':checked')){
            j$("input[name=fruit]",frm).val('Y');
        } else {
        j$("input[name=fruit]",frm).val('N');
        }

        frm.action	= "${choice.html}";
        frm.submit();
}