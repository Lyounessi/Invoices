/*
###########################################
##################DELETE CLIENT############
##################FROM LIST################
###########################################
*/

$(function () {

    /* Functions */

    const loadForm = function () {

        const btn = $(this);

        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-client .modal-content").html("");
                $("#modal-client").modal("show");
            },
            success: function (data) {
                $("#modal-client .modal-content").html(data.html_form);
            }
        });
    };

    const saveForm = function () {
        const form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#AddC").text(data.html_select_client);
                    $("#modal-invoice").modal("hide");
                }
                else {
                    $("#modal-invoice .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // select client 
    $(".js-deactivate-client").click(loadForm);
    
    

});