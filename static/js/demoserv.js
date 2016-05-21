//segunda tabla servicios
var nombre_tabla ="#tabla_servicios";
var nombre_boton_eliminar = ".delete";
var nombre_formulario_modal = "#frmEliminar";
var nombre_ventana_modal = "#myModal";




//servicios segunda parte

   $(document).on('ready',function(){
        $(nombre_boton_eliminar).on('click',function(e){
            e.preventDefault();
            var Sid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idServicio').val(Sid);
            $('#modal_name').text(name);
        });

        var options = {
                success:function(response)
                {
                    if(response.status=="True"){
                        alert("Eliminado!");
                        var idServ = response.servic_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idServ).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }
                        
                    }else{
                        alert("Hubo un error al eliminar!");
                        $(nombre_ventana_modal).modal('hide');
                    };
                }
            };

        $(nombre_formulario_modal).ajaxForm(options);
    });


