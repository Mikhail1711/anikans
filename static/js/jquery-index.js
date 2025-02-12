$(document).ready(function() {
    // Обработчик кнопок "Закуп" и "Продажа"
    $('.checkout').click(function() {
        const itemId = $(this).closest('.table-item').data('id');
        const to_list = $(this).val();
        const quantity = $(this).closest('.table-item').find('.quantity').val();
        
        $(this).hide();

        $.ajax({
            type: "POST",
            url: '/add_to_list/',
            data: {
                item_id: itemId,
                to_list: to_list,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function(response) {
            },
            error: function(xhr) {
                $('#error').text('Ошибка при удалении товара');
            }
        });
    });
});
