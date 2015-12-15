//include("http://code.jquery.com/jquery-2.1.4.js");
$(document).ready(function(){
    $('label').each(function(){
        $(this).wrapAll("<p></p>");
        }
    )
    var label = document.querySelectorAll('label')
    for(i in label){
    $(label[i]).wrap('<p>')
}
    // source http://stackoverflow.com/q/12362447/2394499
    var nav = $('.postNav'),
    first = nav.filter(':eq(0)'),
    notF  = nav.filter(':gt(0)'),
    index = first.find('.active').index();

    notF.each(function(){
        $(this).find('li').removeClass('active').eq(index).addClass('active');
    });
});

