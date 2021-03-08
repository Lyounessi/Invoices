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

//Ajax func to add or select Products x services
$(function () {
    $(".js-new-article").click(function () {
        console.log('Hellllo');


        $.ajax({
            url: 'addprodInv/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-new-article").modal("show");
            },
            success: function (data) {
                if (data.form_is_valid) {
                    alert("Article created!");  // <-- This is just a placeholder for now for testing
                }
                else {
                    $("#modal-new-article .modal-content").html(data.html_form);
                }
            }

        });

    });
});
