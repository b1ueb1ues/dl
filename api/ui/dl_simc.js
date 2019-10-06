APP_URL = 'https://wildshinobu.pythonanywhere.com/';
EX_MAP = {
    'blade': 'k',
    'wand': 'r',
    'bow': 'b',
    'dagger': 'd'
}
BASE_TEAM_DPS = 6000
function populateSelect(id, data) {
    const t = id.split('-')[1]
    $(id).empty();
    for (let d of data) {
        $(id).append($('<option>' + d + '</option>')
            .attr({ id: t + '-' + d, value: d })
        )
    }
}
colorMap = {
    'attack': 'FireBrick',
    'force_strike': 'Maroon',
    'team_buff': 'IndianRed'
}
colorList = ['MediumSlateBlue', 'CornflowerBlue', 'CadetBlue', 'LightSeaGreen']
// charList = ['&#9636', '&#9637', '&#9639', '&#9640']
// charMap = {
//     'attack': '&#9670;',
//     'force_strike': '&#9671;',
//     'team_buff': '&#9672;'
// }
function createDpsBar(arr, extra, total_dps = undefined) {
    let copyTxt = '';
    const total = parseInt(arr[0])
    total_dps = (total_dps == undefined) ? total : parseInt(total_dps);
    const adv = arr[1];
    let slots = ' ' + arr[6];
    const cond = (arr[7] != undefined && arr[7].includes('<')) ? arr[7].replace('<', '&lt;').replace('>', '&gt;') : '';
    const comment = (arr[8] != undefined) ? arr[8] : '';
    let cond_comment = [];
    let cond_comment_str = '';
    let cond_cpy_str = '';
    if (cond != undefined && !cond.startsWith('!')) {
        if (cond != ''){
            cond_comment.push(cond);
            cond_cpy_str = ' ' + cond;
        }
        if (comment != ''){
            cond_comment.push(comment)
        }
        if (cond_comment.length > 0){
            // cond_comment_cpy = ' ' + cond_comment.join(' ');
            cond_comment_str = '<br/>' + cond_comment.join(' ');
        }
    } else {
        slots = '';
    }
    $('#test-results').append($('<h6>DPS:' + total + slots + cond_comment_str + '</h6>'));
    copyTxt += slots + '```DPS: ' + total + cond_cpy_str + '\n';
    $('#test-results').append($('<div></div>').attr({ id: 'result-' + adv, class: 'result-bar' }));
    let colorIdx = 0;
    let damageTxtArr = [];
    let damageTxtBar = [];
    for (let i = 9; i < arr.length; i++) {
        const dmg = arr[i].split(':')
        if (dmg.length == 2) {
            const dmg_val = parseInt(dmg[1]);
            if (dmg_val > 0) {
                let color = undefined;
                // let char = undefined;
                if (colorMap.hasOwnProperty(dmg[0])) {
                    color = colorMap[dmg[0]]
                    // char = charMap[dmg[0]]
                } else {
                    color = colorList[colorIdx % colorList.length]
                    // char = charList[colorIdx % colorList.length]
                    colorIdx += 1
                }
                // data-toggle="tooltip" data-placement="top" title="Tooltip on top"
                const portion = 100 * (parseInt(dmg[1]) / total_dps);
                let damageTxt = dmg[0] + ':' + dmg[1];
                if (dmg[0] in extra) {
                    damageTxt += ' (' + extra[dmg[0]] + ')'
                }
                damageTxtArr.push(damageTxt);
                // damageTxtBar.push(char.repeat(portion))
                $('#result-' + adv).append($('<a>' + damageTxt + '</a>')
                    .css('width', portion + '%')
                    .css('background-color', color)
                    .attr({
                        'data-toggle': 'tooltip',
                        'data-placement': 'top',
                        'title': damageTxt
                    })
                )
            }
        }
    }
    $('[data-toggle="tooltip"]').tooltip();
    copyTxt += damageTxtArr.join(' |') + '```';
    // copyTxt += damageTxtBar.join('') + '```';
    return copyTxt;
}
function trimAcl(acl_str) {
    return $.trim(acl_str.replace(new RegExp(/\s*([#`])/, 'g'), '\n$1'))
}
function loadAdvWPList() {
    let selectedAdv = 'euden';
    if (localStorage.getItem('selectedAdv')) {
        selectedAdv = localStorage.getItem('selectedAdv');
    }
    $.ajax({
        url: APP_URL + 'simc_adv_wp_list',
        dataType: 'text',
        type: 'get',
        contentType: 'application/x-www-form-urlencoded',
        success: function (data, textStatus, jqXHR) {
            if (jqXHR.status == 200) {
                const advwp = JSON.parse(data);
                advwp.adv.sort();
                populateSelect('#input-adv', advwp.adv);
                $('#adv-' + selectedAdv).prop('selected', true);
                populateSelect('#input-wp1', advwp.amulets);
                populateSelect('#input-wp2', advwp.amulets);

                loadAdvSlots();
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#test-results').html(errorThrown);
        }
    });
}
function loadAdvSlots() {
    if ($('#input-adv').val() == '') {
        return false;
    }
    localStorage.setItem('selectedAdv', $('#input-adv').val());
    $.ajax({
        url: APP_URL + 'simc_adv_slotlist',
        dataType: 'text',
        type: 'get',
        contentType: 'application/x-www-form-urlencoded',
        data: 'adv=' + $('#input-adv').val(),
        success: function (data, textStatus, jqXHR) {
            if (jqXHR.status == 200) {
                const slots = JSON.parse(data);
                populateSelect('#input-wep', slots.weapons);
                $('#wep-' + slots.adv.pref_wep).prop('selected', true);
                populateSelect('#input-dra', slots.dragons);
                $('#dra-' + slots.adv.pref_dra).prop('selected', true);
                $('#wp1-' + slots.adv.pref_wp.wp1).prop('selected', true);
                $('#wp2-' + slots.adv.pref_wp.wp2).prop('selected', true);
                $('input[id^="ex-"]').prop('checked', false);
                $('input[id^="ex-"]').prop('disabled', false);
                $('#ex-' + slots.adv.wt).prop('checked', true);
                $('#ex-' + slots.adv.wt).prop('disabled', true);
                $('#input-acl').blur();
                $('#input-edit-acl').prop('checked', false);
                $('#input-acl').prop('disabled', true);
                $('#input-acl').val(trimAcl(slots.adv.acl));
                if (slots.adv.afflict_res != undefined) {
                    $('#input-afflict').prop('disabled', false);
                    $('#input-afflict').val(slots.adv.afflict_res);
                } else {
                    $('#input-afflict').prop('disabled', true);
                    $('#input-afflict').val(slots.adv.afflict_res);
                }

                runAdvTest();
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            if (errorThrown == 'INTERNAL SERVER ERROR') {
                $('#test-results').html('Something went wrong :(');
            }
        }
    });
}
function runAdvTest() {
    if ($('#input-adv').val() == '') {
        return false;
    }
    $('#test-results').empty();
    $('#copy-results').empty();
    $('div[role="tooltip"]').remove();
    let requestJson = {
        'adv': $('#input-adv').val(),
        'dra': $('#input-dra').val(),
        'wep': $('#input-wep').val()
    }
    if ($('#input-wp1').val() != '' && $('#input-wp2').val() != '') {
        requestJson['wp1'] = $('#input-wp1').val();
        requestJson['wp2'] = $('#input-wp2').val();
    }
    let exStr = '';
    let exArr = [];
    for (let ex of Object.keys(EX_MAP)) {
        if ($('#ex-' + ex).prop('checked')) {
            exStr += EX_MAP[ex];
            exArr.push(ex);
        }
    }
    if (exStr != '') {
        requestJson['ex'] = exStr;
    }
    if (!isNaN(parseInt($('#input-t').val()))) {
        requestJson['t'] = $('#input-t').val();
    }
    if (!isNaN(parseInt($('#input-afflict').val()))) {
        requestJson['afflict'] = $('#input-afflict').val();
    }
    if (!isNaN(parseInt($('#input-teamdps').val()))) {
        requestJson['teamdps'] = $('#input-teamdps').val();
    }
    if ($('#input-edit-acl').prop('checked')) {
        requestJson['acl'] = $('#input-acl').val();
    }

    $.ajax({
        url: APP_URL + 'simc_adv_test',
        dataType: 'text',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify(requestJson),
        success: function (data, textStatus, jqXHR) {
            if (jqXHR.status == 200) {
                const res = JSON.parse(data);
                const result = res.test_output.split('\n');
                const cond_true = result[0].split(',');
                let copyTxt = '**' + cond_true[1] + '** ';
                if (exArr.length > 0){
                    copyTxt += '(co-ab: ' + exArr.join(' ') + ') '
                } else {
                    copyTxt += '(co-ab: none) '
                }
                $('#test-results').append($('<h4>' + cond_true[1] + '</h4>'));
                copyTxt += createDpsBar(cond_true, res.extra)
                if (result.length > 1 && result[1].includes(',')) {
                    cond_false = result[1].split(',')
                    copyTxt += createDpsBar(cond_false, res.extra_no_cond, cond_true[0])
                }
                $('#copy-results').append($('<pre>' + copyTxt + '</pre>').attr({ id: 'copy-txt', rows: (copyTxt.match(/\n/g) || [0]).length + 1}));
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#test-results').html(errorThrown);
        }
    });
}
function editAcl() {
    $('#input-acl').prop('disabled', !$(this).prop('checked'))
}
function debounce(func, interval) {
    var lastCall = -1;
    return function() {
        clearTimeout(lastCall);
        var args = arguments;
        var self = this;
        lastCall = setTimeout(function() {
            func.apply(self, args);
        }, interval);
    };
}
function setDisplay(displayMode) {
    if (displayMode == 'Visual'){
        $('#copy-results').css('display', 'block');
        $('#test-results').css('display', 'none');
        $('#display-mode').html(displayMode);
        localStorage.setItem('displayMode', displayMode);
    }else if(displayMode == 'Markdown'){
        $('#copy-results').css('display', 'none');
        $('#test-results').css('display', 'block');
        $('#display-mode').html(displayMode);
        localStorage.setItem('displayMode', displayMode);
    }
}
function toggleDisplay() {
    if (localStorage.getItem('displayMode') == 'Markdown'){
        setDisplay('Visual');
    }else{
        setDisplay('Markdown');
    }
}

window.onload = function () {
    $('#input-adv').change(debounce(loadAdvSlots, 200));
    $('#run-test').click(debounce(runAdvTest, 200));
    if (!localStorage.getItem('displayMode')) {
        localStorage.setItem('displayMode', 'Visual');
    }
    setDisplay(localStorage.getItem('displayMode'));
    $('#display-mode').click(toggleDisplay);
    $('#input-edit-acl').change(editAcl);
    loadAdvWPList()
}