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
                $("#modal-article .modal-content").html("");
                $("#modal-article").modal("show");
            },
            success: function (data) {
                $("#modal-article .modal-content").html(data.html_form);
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
                    $("#modal-article").modal("hide");
                }
                else {
                    $("#modal-article .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Article Deletion
    $(".js-deactivate-article").click(loadForm);
    
    
    // Unit Add
    $('.js-add-unit').click(loadForm);
});