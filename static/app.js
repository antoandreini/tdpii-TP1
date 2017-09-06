$(document).ready(function(){

	$("#frec-form").submit(function(e){
	    e.preventDefault();

	    $.ajax({
	    	type:'POST',
	    	url:'/api/frecuencia',
	    	data : $(this).serialize(),
	    	success:function(data){
	    		alert('Frecuencia actualizada');
	    	},
	    	error:function(data){
	    		console.log(data);
	    		alert('Error');
	    	}
	    })
	});

	actualizarDatos();

});


function actualizarDatos(){
	$.ajax({
		type:'GET',
		url:'/api/clima',
		success: function(data){
			var datos = JSON.parse(data);
			$('#temp').text(datos.temperatura);
			$('#hum').text(datos.humedad);
			$('#pres').text(datos.presion);
			$('#viento').text(datos.viento);
		},
		complete:function(){
			setTimeout(actualizarDatos,1000);
		}
	});
}