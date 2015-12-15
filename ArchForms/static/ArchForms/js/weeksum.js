$(function(){
    
    var calc = []
    
    $(".HoursToday").each(function(){
        calc.push(
            $(this).text()
        )
        
    })
    
    var result = 0
    for(i in calc){
        result+= parseFloat(calc[i])
    }
    
    $(".total").text(result)
    
})
