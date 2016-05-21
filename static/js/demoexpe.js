var nombre_tabla ="#tabla_experiencias";
var nombre_boton_eliminar = ".delete";
var nombre_formulario_modal = "#frmEliminar";
var nombre_ventana_modal = "#myModal";




//servicios tercera parte

   $(document).on('ready',function(){
        $(nombre_boton_eliminar).on('click',function(e){
            e.preventDefault();
            var Eid = $(this).attr('id');
            var name = $(this).data('name');
            $('#modal_idExperiencia').val(Eid);
            $('#modal_name').text(name);
        });

        var options = {
                success:function(response)
                {
                    if(response.status=="True"){
                        alert("Eliminado!");
                        var idExpe = response.experienc_id;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idExpe).remove();
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


