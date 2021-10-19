var primeraFila;
$(function(){

    primeraFila=$("#fila"); 
   

    $("#btnAgregarPedido").click(function(){
        if(($("#txtCorreo").val()!="") && ($("#txtDireccion").val()!="") && ($("#txtCantidad").val())){
            agregarPedido();
        }else{
            $("#mensajePedido").html("Faltan Datos para realizar el pedido");
        }
       
    })
});

/**
 * Funcion que permite recargar los pedidos 
 * cada cierto tiempo en la vista del usuario
 */
function recargarPedidos(){
    setInterval(
        function(){
            listarPedidos();
        },30000
    );
}

/**
 * Peticion para registrar un pedido
 */
function agregarPedido(){
    $.ajax({
        url: "/registrarPedido",
        data: $("#frmPedido").serialize(),
        type: "post",
        dataType: "json",
        cache: false,
        success: function(resultado){
            console.log(resultado);
            if(resultado.estado){  
                $("#datosCliente").html("");              
                $("#idCliente").val("");
                $("#txtDireccion").val("");               
                $("#txtCantidad").val("");
                $("#txtCorreo").val("");  
                swal("¡Correcto!!", resultado.mensaje + 
                " En 20 minutos llegará su pedido a la dirección registrada.", "success");            
            }
            
        },
        error: function(resultado){
            console.log(resultado);
            swal("Problemas!!", resultado.mensaje, "error");
        }

    });
}


/**
 * Se utiliza para publicar los pedidos en un tabla
 */
function listarPedidos(){
    $(".otraFila").remove();
    $("#tblPedidos tbody").append(primeraFila);
    $.ajax({
        url: "/listarPedidos",
        type: "post",
        dataType: "json",
        cache: false,
        success: function(resultado){
            console.log(resultado);
            pedidos=resultado.datos;
                $.each(pedidos, function (i, pedido) {  
                    if(pedido[5]=="Por Atender"){                  
                        $("#cPedido").html(pedido[3]); 
                        $("#tPedido").html(pedido[4]); 
                        $("#kPedido").html(pedido[1]); 
                        $("#fPedido").html(pedido[2]);                     
                        $("#btnEstadoPedido").attr("class","btn btn-danger");
                        $("#btnEstadoPedido").attr("onclick","actualizarEstadoPedido("+ pedido[0]+")");
                        $("#btnEstadoPedido").html(pedido[5]);
                        $("#tblPedidos tbody").append($("#fila").clone(true).attr("class","otraFila"));
                    }                 
                });             
                $(".primeraFila").remove();
            
        },
        error: function(resultado){
            console.log(resultado);
        }

    });    
}

/**
 * Funcion con peticion ajax para actualizar el pedido
 */
function actualizarEstadoPedido(idPedido){   
    var parametros = {
        actualizaPed :idPedido
    };
    console.log(parametros)
    $.ajax({
        url: "/actualizarPedidos",
        data: parametros,
        type: "post",
        dataType: "json",
        cache: false,
        success: function(resultado){
            console.log(resultado);
            if(resultado.estado){
                swal("¡Actualización Pedido!!", "Se ha actualizado el estado del Pedido. Se despacha el pedido al cleinte" , "success");           
                listarPedidos();
            }else{
                swal("¡Problemas!!", resultado.mensaje , "warning");           
            }
           
        },
        error: function(resultado){
            console.log(resultado);
        }

    });    

}

