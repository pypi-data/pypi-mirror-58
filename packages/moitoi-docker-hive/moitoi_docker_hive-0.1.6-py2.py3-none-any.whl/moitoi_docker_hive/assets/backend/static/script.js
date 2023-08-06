
$( document ).ready(function() {

    function postJSON( url, data, callback ) {
        return jQuery.ajax({
            url: url,
            type: "POST",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify(data),
            success: callback,
            error: function( jqXhr, textStatus, errorThrown ){
                console.log( errorThrown );
                }
        })
    }


    $("#clusterCreateForm").submit(function (event) {

        // Stop form from submitting normally
        event.preventDefault();

        // Get some values from elements on the page:
        var $form = $(this),
            _clusters = $form.find("input[name='clusters']").val(),
            _replicas = $form.find("input[name='replicas']").val();

        // Send the data using post
        var posting = postJSON('/Service', {"clusters": _clusters, "replicas": _replicas },  function (data, status, xhr) {

                   $("#result").empty().append("Done!");
                   Object.keys(data).forEach(function(key,index) {
                       console.log(key + ':' + data[key]);
                              Object.keys(key).forEach(function(_key,_index) {
                                  console.log(_key + ':' + key[_key]);
                                  $("#result").append('<p>' + _key + ':' + key[_key] + '</p>');
                              });

                    });
        });

    });

});
