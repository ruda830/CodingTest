// forked from ogaoga's "JavaScript のオブジェクトを可視化するやーつ" http://jsdo.it/ogaoga/mlE0
// jQuery 1.9.1 で動くようにした。

$(function(){
// ===================================================

    function objectToTable(obj, parent) {
        var table = $("<table>").appendTo(parent);
        var tbody = $("<tbody>").appendTo(table);
        for ( var key in obj ) {
            var tr = $("<tr>").appendTo(tbody);
            var th = $('<th>').appendTo(tr);
            th.append(key);
            var td = $('<td>').appendTo(tr);
            if ( typeof(obj[key]) == 'object' ) {
                if ( obj[key] ) {
                    objectToTable(obj[key], td);
                } else {
                    td.append('<span class="null">null</span>');
                }//if
            }else if ( typeof(obj[key]) == 'boolean' ) {
                var str = (obj[key]) ? 'true' : 'false';
                td.append('<span class="boolean">'+str+'</span>');
            }else if ( typeof(obj[key]) == 'string' ) {
                td.append('<span class="string">"'+obj[key]+'"</span>');
            }else {
                td.append(obj[key].valueOf());
            }//if
        }//for
    }

    $('#show_button').click(function(){
        var value = '';
        var source = $('#source').val();
        if ( source ) {
          var parent = $('#container');
          parent.empty();
          try {
              objectToTable(eval("("+source+")"), parent);
          } catch (e) {
              parent.append('<pre>'+e+'</pre>');
          }//try
        }//if
    });

    $(document).ready(function(){
        $('#show_button').trigger('click');
    });

    $('#source')
		.live('drop', function(e){
            e.stopPropagation();
            e.preventDefault();
            $(this).removeClass('over');
            var files = e.originalEvent.dataTransfer.files;
                if ( files && files.length > 0 ) {
                    var file = files[0];
                    var reader = new FileReader();
                    reader.onload = function(event)	{
                        //console.log(this.result);
                        $('#source').val(this.result);
                        $('#show_button').trigger('click');
                    }
                    reader.readAsText(file);
                }
            })
        .live('dragenter', function(e){
            e.stopPropagation();
            e.preventDefault();
			$(this).addClass('over');
        })
        .live('dragleave', function(e){
            e.stopPropagation();
            e.preventDefault();
			$(this).removeClass('over');
        });

// ===================================================
});