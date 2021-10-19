$(function(){

    $("#txtCorreo").change(function(){
        consultarCliente();       
     });
     
    $("#btnAgregarClienteModal").click(function(){
        if(($("#txtCorreoModal").val()!="") 
                && ($("#txtNombre").val()!="") && ($("#txtTelefono").val())){
            agregarCliente();
        }else{
            $("#mensajeModal").html("Faltan Datos para poder registrar el cliente");
        }
  
    });
});

/**
 * Peticion ajax para registrar un cliente
 */

function agregarCliente(){
    $.ajax({
        url: "/agregarCliente",
        data: $("#frmAgregarCliente").serialize(),
        type: "post",
        dataType: "json",
        cache: false,
        success: function(resultado){
            console.log(resultado);
            if(resultado.estado){                
                $("#idCliente").val(resultado.datos);
                $("#txtNombreCliente").val($("#txtNombre").val());                
                $("#txtNombre").val("");
                $("#txtCorreoModal").val("");
                $("#txtTelefono").val("");
                $("#btnCancelarModal").html("Regresar");
            }
            $("#mensajeModal").html(resultado.mensaje);
        },
        error: function(resultado){
            console.log(resultado);
        }

    });
}

/**
 * Petición ajax para consultar cliente
 * por correo electrónico
 */
 function consultarCliente(){
    $("#datosCliente").html("");
    var parametros = {        
        txtCorreo: $("#txtCorreo").val()
    };
    $.ajax({
        url: "/buscarClientePorCorreo",
        data: parametros,
        type: "post",
        dataType: "json",
        cache: false,
        success: function(resultado){
            console.log(resultado);
            if(resultado.estado){
                $("#datosCliente").html("<b>Nombre:</b> " + 
                resultado.datos[1] + "<br> <b>Teléfono:</b> " + resultado.datos[3])
                $("#idCliente").val(resultado.datos[0]);
                $("#txtNombreCliente").val(resultado.datos[1]);
            }else{
                $("#datosCliente").html("");
                $("#txtCorreoModal").val($("#txtCorreo").val());
                $("#modalAgregarCliente").modal();
            }
        },
        error: function(resultado){
            console.log(resultado);
        }
    });
}