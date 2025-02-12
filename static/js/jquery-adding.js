$(document).ready(function() {
    // Обработчик удаления товара
    $('.remove').click(function() {
        const itemId = $(this).closest('.table-item').data('id');

        $.ajax({
            type: "POST",
            url: '/journal/adding-remove/',
            data: {
                item_id: itemId,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function(response) {
                $(`.table-item[data-id="${itemId}"]`).remove();
            },
            error: function(xhr) {
                $('#error').text('Ошибка при удалении товара');
            }
        });
    });

    // Обработчик кнопки "Провести закупку"
    $('#adding-checkout').click(function() {
        const cartData = [];

        $('.table-item').each(function() {
            const itemData = {};

            itemData.itemId = $(this).data('id');
            itemData.quantity = $(this).find('.quantity').val();

            cartData.push(itemData);
        });
        console.log('cartData:', cartData);

        $.ajax({
            type: 'POST',
            url: '/journal/adding-confirm/',
            contentType: 'application/json',
            data: JSON.stringify({
                cart_data: cartData,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(), //'{{ csrf_token }}'
            }),
            success: function(response) {
                location.reload();
            },
            error: function(xhr) {
                console.error('Error:', xhr);
                $('#error').text('Ошибка при проведении закупа');
            }
        });
    });
});
