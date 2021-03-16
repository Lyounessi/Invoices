// Ajax Func to add or change logo

/*
###########################################################
##############INVOICE AJAX HANDLING################
###########################################################
*/
//Ajax func to select and add a client to the selected invoice
$(function () {

    /* Functions */

    const loadForm = function () {

        const btn = $(this);

        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                //$("#modal-invoice .modal-content").html("");
                $("#modal-invoice").modal("show");
            },
            success: function (data) {
                $("#modal-invoice .modal-content").html(data.html_form);
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


    // save Invoice
    //$(".js-save-invoice").click(loadForm);

});
/*
##########################################################
##############INVOICE ARTICLES AJAX HANDLING##############
##########################################################
*/
// Ajax func to add the new article to the article base
$(function () {
    $(".js-new-article").click(function () {


        $.ajax({
            url: 'addprodInv/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-invoice .modal-content").html("");

                $("#modal-invoice").modal("show");
            },
            success: function (data) {
                $("#modal-invoice .modal-content").html(data.html_form);

            }
        });
    });

});
$("#modal-invoice").on("submit", ".js-article-create-form", function () {
    console.log('HEEEEY');
    let form = $(this);

    $.ajax({
        url: form.attr('action'),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        beforeSend: function () {
            $("#modal-invoice").modal("show");
        },
        success: function (data) {
            if (data.form_is_valid) {
                alert("Article created! check the selection");  // <-- This is just a placeholder for now for testing
                $("#modal-invoice").modal("hide");
                $(".modal-backdrop").modal("hide");


            }
            else {
                alert("Something went wrong!");  // <-- This is just a placeholder for now for testing

                $("#modal-invoice .modal-content").html(data.html_form);
            }
        }

    });

    return false;
});
// Ajax Func Lunching the modal of article selection and add it to an invoice
$(function () {

    const loadForm = function () {

        const btn = $(this);

        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {

                $("#modal-invoice").modal("show");
            },
            success: function (data) {
                $("#modal-invoice .modal-content").html(data.html_form);
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
                    $(".main-one #tbody").html(data.html_select_article);

                    $("#modal-invoice").modal("hide");


                }
                else {
                    alert("Something went wrong!");  // <-- This is just a placeholder for now for testing

                    $("#modal-invoice modal-content").html(data.html_form);
                }
            }

        });

        return false;
    };
    //add Article In Invoice
    $(".js-select-article").click(loadForm);
    $("#modal-invoice").on("submit", ".js-select-article-form", saveForm);

    // Delete an article from an invoice
    $(".main-one").on("click", ".js-delete-article", loadForm);
    $("#modal-invoice").on("submit", ".js-article-delete-form", saveForm);
});





/*
###########################################################
##############INVOICE CLIENTS AJAX HANDLING################
###########################################################
*/
//Ajax func to select and add a client to the selected invoice
$(function () {

    /* Functions */

    const loadForm = function () {

        const btn = $(this);

        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                //$("#modal-invoice .modal-content").html("");
                $("#modal-invoice").modal("show");
            },
            success: function (data) {
                $("#modal-invoice .modal-content").html(data.html_form);
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
    $(".js-select-client").click(loadForm);
    $("#modal-invoice").on("submit", ".js-client-select-form", saveForm);
    // new client
    $(".js-new-client").click(loadForm);
    $("#modal-invoice").on("submit", ".js-client-new-form", saveForm);


});
