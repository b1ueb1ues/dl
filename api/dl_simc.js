APP_URL = 'http://localhost:5000/adv_slotlist';
EX_MAP = {
    'blade': 'k',
    'wand': 'r',
    'bow': 'b',
    'dagger': 'd'
}
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
    if ($('#input-adv').val() == '') {
        return false;
    }
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
    // adv_name = request.args.get('adv', default='euden')
    // wp1 = request.args.get('wp1', default=None)
    // wp2 = request.args.get('wp2', default=None)
    // dra = request.args.get('dra', default=None)
    // ex  = request.args.get('ex', default='')
    // wep = request.args.get('wep', default=None)
    // t   = abs(int(request.args.get('t', default=180)))
    if ($('#input-adv').val() == '') {
        return false;
    }
    var requestStr =
        'adv=' + $('#input-adv').val() +
        '&dra=' + $('#input-dra').val() +
        '&wp1=' + $('#input-wp1').val() +
        '&wp1=' + $('#input-wp1').val();
    var exStr = '';
    for (let ex of Object.keys(EX_MAP)) {
        console.log('#ex-' + ex);
        console.log($('#ex-' + ex).prop('checked'));
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

    // $.ajax({
    //     url: APP_URL,
    //     dataType: 'text',
    //     type: 'get',
    //     contentType: 'application/x-www-form-urlencoded',
    //     data: requestStr,
    //     success: function (data, textStatus, jQxhr) {
    //         if (jQxhr.status == 200) {
    //             console.log(data)
    //         }
    //     },
    //     error: function (jqXhr, textStatus, errorThrown) {
    //         console.log(errorThrown);
    //     }
    // });
}

window.onload = function () {
    $('#input-adv').change(loadAdvSlots);
    $('#run-test').click(runAdvTest);
}