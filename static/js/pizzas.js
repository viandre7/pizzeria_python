var primeraCard;
var primeraFila;
$(function(){
    primeraCard=$("#cardPrimera");
    primeraFila=$("#fila");

    $("#btnAbrirModalAgregar").click(function(){
        $("#modalAgregarPizza").modal();
    });

    $("#btnRegistrarPizza").click(function(){
        registrarPizza();
    })
});


function limpiarFormularioAgregarPizza(){
    $('#txtNombre').val(""),
    $('#txtIngredientes').val(""),
    $('#txtValor').val("");
    $('#fileFoto').val("");
}

/**
 * Peticion ajax para registrar la pizza
 */

function registrarPizza(){    
    
    const formPizza = new FormData($("#frmAgregarPizza")[0]);
    $.ajax({
        url: "/agregarPizza",
        data: formPizza,
        type:"post",
        dataType: "json",
        cache:false,
        contentType: false,
        processData: false,
        success: function(resultado){
            console.log(resultado);
            if(resultado.estado){
                swal("¡Correcto!!", resultado.mensaje, "success");
                limpiarFormularioAgregarPizza();
            }else{
                swal("Problemas!!", resultado.mensaje, "warning");
            }
        },
        error: function(resultado){
            swal("Problemas al Registrar!!", resultado.mensaje, "error");      
        }
    });
}

/**
 * ListarPizza
 */
function listarPizzas(){
    $.ajax({
        url: "/listarPizzas",
        type:"post",
        dataType: "json",
        cache:false,
        success: function(resultado){
            console.log(resultado);
            if(resultado.estado){
                pizzas = resultado.datos;
                $.each(pizzas, function (i, pizza) {                                                          
                    $("#img").attr("src","static/fotos/" + pizza[0]+".jpg");
                    $("#cTitulo").html(pizza[1]);
                    $("#cDescripcion").html("<b>Ingredientes:</b><br>" + pizza[2] + "<br><br>" + "<b>Precio:</b> " + pizza[3]);                
                    $("#cPedido").attr("href","/crearPedido?idPizza="+pizza[0]+"&nombrePizza="+pizza[1]);
                    $(".card-columns").append($("#cardPrimera").clone(true).attr("class","card otra"));

                });
                $("#cardPrimera").remove();
            }else{
                $("#mensaje").html(resultado.mensaje);
            }        
          
        },
        error: function(resultado){
            console.log(resultado);
        }
    });
}

/**
 * Peticion ajax para obteber listado de pizzas y publicarlas
 * en una tabla para gestionarlas
 */

function listarPizzasTabla(){
    $.ajax({
        url: "/listarPizzas",
        type:"post",
        dataType: "json",
        cache:false,
        success: function(resultado){
            console.log(resultado);
            if(resultado.estado){
                pizzas = resultado.datos;
                $.each(pizzas, function (i, pizza) {             
                    // alert(pizza)                                          
                    $("#pNombre").html(pizza[1]);
                    $("#pIngredientes").html(pizza[2]);                
                    $("#pValor").html("$ "+pizza[3]);
                    $("#tblPizzas tbody").append($("#fila").clone(true).attr("class","otraFila"));
                });
                $(".primeraFila").remove();
            }else{
                $("#mensaje").html(resultado.mensaje);
            }        
            $("#tblPizzas").dataTable();
        },
        error: function(resultado){
            console.log(resultado);
        }
    });
}