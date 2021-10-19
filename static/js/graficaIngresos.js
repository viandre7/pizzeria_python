/*Se carga la visualización de la API y el paquete corechart*/
/* global google */


google.charts.load('current', {'packages':['corechart']});

/* Código que obtiene los datos del servidor, para lo cual haremos una
 * petición ajax que devolverá un JSON con la información a graficar
 * que se se almacenará en la variable datos*/
var datos;

$(function(){ 
  google.charts.setOnLoadCallback(dibujarGrafica);  
 
});


function dibujarGrafica() {  
    
  var parametros={
    accion: "Grafico2"
  };
  $.ajax({
      url: '../../Controlador/PedidoController.php',    
      data:parametros,    
      dataType: "json",
      type: 'post',
      async: false,
      success: function (resultado) {
          console.log(resultado);
          if(resultado.estado){
            var datos = resultado.datos;
            //Se crea una tabla y se llena con los datos obtenidos
            var data = new google.visualization.arrayToDataTable(datos);  
            /* Se definen algunas opciones para el gráfico*/
            var opciones = {
              title: 'Ingresos Venta Pizzas por Mes ',                        
                is3D: true,  
                legend : 'none'              
              };          
          /* se crea un objeto de la clase google.visualization.ColumnChart  */            
          var grafica2 = new google.visualization.PieChart(document.getElementById('grafica2'));
          /* Se llama al método draw para dibujar la gráfica*/  
          grafica2.draw(data,opciones);            
        }else{
            alert("no hay datos para gtraficar")
        }            
    },
    error: function (error) {
      console.log(error.responseText);
    }
  });  
}



