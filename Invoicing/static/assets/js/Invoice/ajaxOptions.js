
/*
###########################################################
##############INVOICE OPERATIONS AJAX HANDLING#############
###########################################################
*/




/* SAVING OPTION */
// Ajax Func Lunching the modal of invoice's saving 
$(function () {

    const loadForm = function () {
        console.log("HEEEEEEEEEEEEEEO")
        const btn = $(this);

        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {

                $("#modal-invoice-options").modal("show");
            },
            success: function (data) {
                $("#modal-invoice-options .modal-content").html(data.html_form);
            }
        });
    };

    /////
    const saveForm = function () {
        let form = $(this);

        $.ajax({
            url: form.attr('action'),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',

            success: function (data) {
                if (data.form_is_valid) {
                    
                    $("#modal-invoice-options").modal("hide");


                }
                else {
                    alert("Something went wrong!");  // <-- This is just a placeholder for now for testing

                    $("#modal-invoice-options modal-content").html(data.html_form);
                }
            }

        });

        return false;
    };
    //add Article In Invoice
    $(".js-save-invoice").click(loadForm);
    $("#modal-invoice").on("submit", ".js-save-invoice-form", saveForm);

    
});