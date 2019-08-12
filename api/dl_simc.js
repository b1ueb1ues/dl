APP_URL = 'http://localhost:5000/adv_slotlist';
function populateSelect(id, data) {
    var t = id.split('-')[1]
    $(id).empty();
    for (let d of data) {
        $(id).append($('<option>' + d[1] + '</option>')
            .attr({ id: t + '-' + d[1], value: d[1] })
        )
    }
}
function loadAdvSlots() {
    console.log($(this).val())
    $.ajax({
        url: APP_URL,
        dataType: 'text',
        type: 'get',
        contentType: 'application/x-www-form-urlencoded',
        data: 'adv=' + $(this).val(),
        success: function (data, textStatus, jQxhr) {
            if (jQxhr.status == 200) {
                var slots = JSON.parse(data);
                populateSelect('#input-wep', slots.weapons);
                populateSelect('#input-dra', slots.dragons);
                populateSelect('#input-wp1', slots.amulets);
                $('#wp1-RR').prop('selected', true);
                populateSelect('#input-wp2', slots.amulets);
                $('#wp2-CE').prop('selected', true);
                console.log(data)
            }
        },
        error: function (jqXhr, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    });
}

window.onload = function () {
    $('#input-adv').change(loadAdvSlots)
}