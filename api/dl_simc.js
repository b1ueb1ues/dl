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
colorMap = {
    'attack': 'FireBrick',
    'force_strike': 'Maroon'
}
colorList = ['MediumSlateBlue', 'CornflowerBlue', 'CadetBlue', 'LightSeaGreen']
function createDpsBar(arr, total_dps = undefined) {
    total = parseInt(arr[0])
    total_dps = (total_dps == undefined) ? total : parseInt(total_dps);
    adv = arr[1];
    slots = ' ' + arr[6];
    cond = (arr[7] != undefined && arr[7].includes('<')) ? arr[7].replace('<', '&lt;').replace('>', '&gt;') : '';
    comment = (arr[8] != undefined) ? arr[8] : '';
    cond_comment_str = ''
    if (!cond.startsWith('!')) {
        console.log(cond, comment)
        console.log(cond.length, comment.length)
        cond_comment_str = '<br/>';
        if (cond.length == 0 && comment.length == 0) {
            cond_comment_str = ''
        } else if (cond.length > 0 && comment.length == 0) {
            cond_comment_str += cond
        } else if (cond.length == 0 && comment.length > 0) {
            cond_comment_str += comment
        } else if (cond.length > 0 && comment.length > 0) {
            cond_comment_str += cond + '; ' + comment
        }
    }
    $('#test_results').append($('<h6>DPS:' + total + slots + cond_comment_str + '</h6>'))
    $('#test_results').append($('<div></div>').attr({ id: 'result-' + adv, class: 'result-bar' }))
    colorIdx = 0
    for (var i = 9; i < arr.length; i++) {
        dmg = arr[i].split(':')
        if (dmg.length == 2) {
            dmg_val = parseInt(dmg[1]);
            if (dmg_val > 0) {
                color = undefined
                if (colorMap.hasOwnProperty(dmg[0])) {
                    color = colorMap[dmg[0]]
                } else {
                    color = colorList[colorIdx % colorList.length]
                    colorIdx += 1
                }
                // data-toggle="tooltip" data-placement="top" title="Tooltip on top"
                portion = 100 * (parseInt(dmg[1]) / total_dps)
                $('#result-' + adv).append($('<a></a>')
                    .css('width', portion + '%')
                    .css('background-color', color)
                    .attr({
                        'data-toggle': 'tooltip',
                        'data-placement': 'top',
                        'title': dmg[0] + ': ' + dmg[1]
                    })
                )
            }
        }
    }
    $('[data-toggle="tooltip"]').tooltip()
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
    $('#test_results').empty()
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

    $.ajax({
        url: APP_URL + 'adv_test',
        dataType: 'text',
        type: 'get',
        contentType: 'application/x-www-form-urlencoded',
        data: requestStr,
        success: function (data, textStatus, jQxhr) {
            if (jQxhr.status == 200) {
                console.log(data)
                result = data.split('\n')
                cond_true = result[0].split(',')
                $('#test_results').append($('<h4>' + cond_true[1] + '</h4>'))
                createDpsBar(cond_true)
                if (result.length > 1 && result[1].includes(',')) {
                    cond_false = result[1].split(',')
                    createDpsBar(cond_false, cond_true[0])
                }
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