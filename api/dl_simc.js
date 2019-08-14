APP_URL = 'http://localhost:5000/';
EX_MAP = {
    'blade': 'k',
    'wand': 'r',
    'bow': 'b',
    'dagger': 'd'
}
function populateSelect(id, data, addDefault = false) {
    var t = id.split('-')[1]
    $(id).empty();
    if (addDefault) {
        $(id).append($('<option>Default</option>')
            .attr({ id: t + '-default', value: 'default' })
        )
    }
    for (let d of data) {
        $(id).append($('<option>' + d + '</option>')
            .attr({ id: t + '-' + d, value: d })
        )
    }
}
function loadAdvSlots() {
    if ($('#input-adv').val() == '') {
        return false;
    }
    $.ajax({
        url: APP_URL + 'adv_slotlist',
        dataType: 'text',
        type: 'get',
        contentType: 'application/x-www-form-urlencoded',
        data: 'adv=' + $(this).val(),
        success: function (data, textStatus, jQxhr) {
            if (jQxhr.status == 200) {
                var slots = JSON.parse(data);
                populateSelect('#input-wep', slots.weapons);
                $('#wep-' + slots.adv_pref_wep).prop('selected', true);
                populateSelect('#input-dra', slots.dragons);
                $('#dra-' + slots.adv_pref_dra).prop('selected', true);
                populateSelect('#input-wp1', slots.amulets, true);
                populateSelect('#input-wp2', slots.amulets, true);
                $('input[id^="ex-"]').prop('checked', false);
                $('input[id^="ex-"]').prop('disabled', false);
                $('#ex-' + slots.adv_wt).prop('checked', true);
                $('#ex-' + slots.adv_wt).prop('disabled', true);
            }
        },
        error: function (jqXhr, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    });
}
function runAdvTest() {
    if ($('#input-adv').val() == '') {
        return false;
    }
    var requestStr =
        'adv=' + $('#input-adv').val() +
        '&dra=' + $('#input-dra').val() +
        '&wep=' + $('#input-wep').val();
    if ($('#input-wp1').val() != '' && $('#input-wp2').val() != '') {
        '&wp1=' + $('#input-wp1').val();
        '&wp2=' + $('#input-wp2').val();
    }
    var exStr = '';
    for (let ex of Object.keys(EX_MAP)) {
        if ($('#ex-' + ex).prop('checked')) {
            exStr += EX_MAP[ex]
        }
    }
    if (exStr != '') {
        requestStr += '&ex=' + exStr;
    }
    if (!isNaN(parseInt($('#input-t').val()))) {
        requestStr += '&t=' + $('#input-t').val();
    }
    console.log(requestStr)

    $.ajax({
        url: APP_URL + 'adv_test',
        dataType: 'text',
        type: 'get',
        contentType: 'application/x-www-form-urlencoded',
        data: requestStr,
        success: function (data, textStatus, jQxhr) {
            if (jQxhr.status == 200) {
                console.log(data)
            }
        },
        error: function (jqXhr, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    });
}

window.onload = function () {
    $('#input-adv').change(loadAdvSlots);
    $('#run-test').click(runAdvTest);
}