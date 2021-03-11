// Ajax Func to add or change logo




//Ajax func to add or select clients
$(function () {
    $(".js-select-client").click(function () {


        $.ajax({
            url: 'client/select/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-select-client").modal("show");
            },
            success: function (data) {
                $("#modal-select-client .modal-content").html(data.html_form);
            }
        });
    });

});

//Ajax func to the modal content//////////////////////////////////
$(function () {
    $(".js-new-article").click(function () {


        $.ajax({
            url: 'addprodInv/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-new-article").modal("show");
            },
            success: function (data) {
                $("#modal-new-article .modal-content").html(data.html_form);
            }
        });
    });

});

// Ajax func to add the new article to the article base
$("#modal-new-article").on("submit", ".js-article-create-form", function () {
    console.log('HEEEEY');
    let form = $(this);

    $.ajax({
        url: form.attr('action'),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        beforeSend: function () {
            $("#modal-new-article").modal("show");
        },
        success: function (data) {
            if (data.form_is_valid) {
                alert("Article created!");  // <-- This is just a placeholder for now for testing
                $("#modal-new-article ").modal('hide');

            }
            else {
                alert("Something went wrong!");  // <-- This is just a placeholder for now for testing

                $("#modal-new-article .modal-content").html(data.html_form);
            }
        }

    });

    return false;
});



// Ajax Func Lunching the modal of article selection and add it to an invoice
$(function () {

    const loadForm = function () {

        const btn = $(this);
        console.log(btn.attr("data-url"));
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-select-article .modal-content").html("");
                $("#modal-select-article").modal("show");
            },
            success: function (data) {
                $("#modal-select-article .modal-content").html(data.html_form);
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
                    $(".table #tbody").html(data.html_select_article);
                    alert("Article is well Added to the Invoice");// <-- This is just a placeholder for now for testing
                    $("#modal-select-article").modal("hide");


                }
                else {
                    alert("Something went wrong!");  // <-- This is just a placeholder for now for testing

                    $("#modal-select-article .modal-content").html(data.html_form);
                }
            }

        });

        return false;
    };




    //add Article In Invoice
    $(".js-select-article").click(loadForm);
    $("#modal-select-article").on("submit", ".js-select-article-form", saveForm);

    // Delete an article from an invoice
    $("#articles-table").on("click", ".js-delete-article", loadForm);
    $("#modal-delete-article").on("submit", ".js-article-delete-form", saveForm);
});