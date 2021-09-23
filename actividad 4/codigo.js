$(document).ready(function () {
    var textoinicial = $(".titulo").text() 
    $("#boton1").click(function () {
        $("img").toggle()
    });
    $("#boton2").click(function () {
        var texto = $(".titulo").text() 
        if (texto == textoinicial) {
            $(".titulo").text("¿Cómo tomo agua pero distinto?")
        }else {
            $(".titulo").text(textoinicial)
        }
    });

});