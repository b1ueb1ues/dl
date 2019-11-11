APP_URL = 'https://wildshinobu.pythonanywhere.com/';
EX_MAP = {
    'blade': 'k',
    'wand': 'r',
    'bow': 'b',
    'dagger': 'd'
}
BASE_SIM_T = 180
BASE_TEAM_DPS = 12000
PREFIX_MAPS = {
    'adv': {
        'g_': 'gala_',
        'b_zardin': 'beautician_zardin',
        'd_': 'dragonyule_',
        'h_': 'halloween_',
        's_maribelle': 'school_maribelle',
        's_': 'summer_',
        'v_': 'valentine_',
        'w_': 'wedding_'
    },
}
Chart.defaults.global.legend.display = false;
function name_fmt(name) {
    return name.replace(/_/g, ' ').replace(/(?:^|\s)\S/g, function (a) { return a.toUpperCase(); });
}
function substitute_prefix(name, t) {
    if (PREFIX_MAPS.hasOwnProperty(t)) {
        prefix_map = PREFIX_MAPS[t];
        name = name.toLowerCase();
        for (let pre in prefix_map) {
            if (name.startsWith(pre)) {
                name = name.replace(pre, prefix_map[pre]);
                break;
            }
        }
    }
    return name_fmt(name);
}
let dps_chart = null;
function populateSelect(id, data) {
    const t = id.split('-')[1];
    let options = [];
    for (let d of data) {
        options.push($('<option>' + substitute_prefix(d, t) + '</option>')
            .attr({ id: t + '-' + d, value: d }))
    }
    options.sort((a, b) => {
        if (a[0].innerText < b[0].innerText) return -1;
        if (a[0].innerText > b[0].innerText) return 1;
        return 0;
    })
    $(id).empty();
    $(id).append(options);
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
function createDpsBar(resDiv, arr, extra, total_dps = undefined) {
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
        if (cond != '') {
            cond_comment.push(cond);
            cond_cpy_str = ' ' + cond;
        }
        if (comment != '') {
            cond_comment.push(comment)
        }
        if (cond_comment.length > 0) {
            // cond_comment_cpy = ' ' + cond_comment.join(' ');
            cond_comment_str = '<br/>' + cond_comment.join(' ');
        }
    } else {
        slots = '';
    }
    resDiv.append($('<h6>DPS:' + total + name_fmt(slots) + cond_comment_str + '</h6>'));
    copyTxt += slots + '```DPS: ' + total + cond_cpy_str + '\n';
    let resBar = $('<div></div>').attr({ class: 'result-bar' });
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
                let damageTxt = dmg[0] + ': ' + dmg[1];
                if (dmg[0] in extra) {
                    damageTxt += ' (' + extra[dmg[0]] + ')'
                }
                damageTxtArr.push(damageTxt);
                // damageTxtBar.push(char.repeat(portion))
                const damageSlice = $('<a>' + name_fmt(damageTxt) + '</a>')
                    .css('width', portion + '%')
                    .css('background-color', color)
                    .attr({
                        'data-toggle': 'tooltip',
                        'data-placement': 'top',
                        'title': damageTxt
                    }).tooltip();
                resBar.append(damageSlice)
            }
        }
    }
    copyTxt += damageTxtArr.join('|') + '```';
    // copyTxt += damageTxtBar.join('') + '```';
    resDiv.append(resBar);
    return copyTxt;
}
function sumDps(data) {
    let summed = [];
    let display = [];
    for (let p of data) {
        let y = 0;
        if (summed.length > 1) {
            y = p.y + summed[summed.length - 1].y;
        } else {
            y = p.y;
        }
        summed.push({ x: p.x, y: y })
        if (p.x > 1 && (display.length == 0 || display[display.length - 1].x + 1 < p.x)) {
            display.push({ x: p.x, y: y / p.x })
        }
    }
    return display;
}
function createChart(data, name) {
    if (dps_chart != null) {
        dps_chart.destroy();
    }
    let ctx = document.getElementById('damage-log').getContext('2d');
    dps_chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'scatter',

        // The data for our dataset
        data: {
            datasets: [{
                backgroundColor: 'rgb(66,139,202)',
                borderColor: 'rgb(66,139,202)',
                data: sumDps(data),
                fill: false,
                showLine: true
            }]
        },

        // Configuration options go here
        options: {
            title: {
                display: true,
                fontSize: 20,
                text: substitute_prefix(name, "adv")
            },
            scales: {
                xAxes: [{
                    ticks: {
                        beginAtZero: true,
                        stepSize: 1,
                    },
                }]
            }
        }
    });

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
        type: 'post',
        contentType: 'application/json',
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
            $('#test-results').html('Failed to load initial data');
        }
    });
}
function loadAdvSlots() {
    clearResults();
    if ($('#input-adv').val() == '') {
        return false;
    }
    localStorage.setItem('selectedAdv', $('#input-adv').val());
    $.ajax({
        url: APP_URL + 'simc_adv_slotlist',
        dataType: 'text',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify({ 'adv': $('#input-adv').val() }),
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
            $('#test-results').html('Failed to load adventurer');
        }
    });
}
function runAdvTest() {
    if ($('#input-adv').val() == '') {
        return false;
    }
    $('#test-error').empty();
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
    const t = $('#input-t').val();
    if (!isNaN(parseInt(t))) {
        requestJson['t'] = t;
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
                if (res.hasOwnProperty('error')) {
                    $('#test-error').html('Error: ' + res.error);
                } else {
                    const result = res.test_output.split('\n');
                    const cond_true = result[0].split(',');
                    const name = substitute_prefix(cond_true[1], 'adv');
                    let copyTxt = '**' + name + ' ' + t + 's** ';
                    if (exArr.length > 0) {
                        copyTxt += '(co-ab: ' + exArr.join(' ') + ')'
                    } else {
                        copyTxt += '(co-ab: none)'
                    }
                    let newResultItem = $('<div></div>').attr({ class: 'test-result-item' });
                    newResultItem.append($('<h4>' + name + '</h4>'));
                    copyTxt += createDpsBar(newResultItem, cond_true, res.extra);
                    if (result.length > 1 && result[1].includes(',')) {
                        cond_false = result[1].split(',');
                        extra = res.extra_no_cond.length > 0 ? res.extra_no_cond : res.extra
                        copyTxt += createDpsBar(newResultItem, cond_false, extra, cond_true[0]);
                    }
                    // createChart(res.log.dmg, name);
                    $('#damage-log').text(res.logs);
                    $('#test-results').prepend(newResultItem);
                    $('#copy-results').prepend($('<pre>' + copyTxt + '</pre>').attr({ class: 'copy-txt', rows: (copyTxt.match(/\n/g) || [0]).length + 1 }));
                }
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#test-error').html('Failed to run damage simulation');
        }
    });
}
function editAcl() {
    $('#input-acl').prop('disabled', !$(this).prop('checked'))
}
function debounce(func, interval) {
    var lastCall = -1;
    return function () {
        clearTimeout(lastCall);
        var args = arguments;
        var self = this;
        lastCall = setTimeout(function () {
            func.apply(self, args);
        }, interval);
    };
}
function setDisplay(displayMode) {
    if (displayMode == 'Visual') {
        $('#copy-results').css('display', 'block');
        $('#test-results').css('display', 'none');
        $('#display-mode').html(displayMode);
        localStorage.setItem('displayMode', displayMode);
    } else if (displayMode == 'Markdown') {
        $('#copy-results').css('display', 'none');
        $('#test-results').css('display', 'block');
        $('#display-mode').html(displayMode);
        localStorage.setItem('displayMode', displayMode);
    }
}
function toggleDisplay() {
    if (localStorage.getItem('displayMode') == 'Markdown') {
        setDisplay('Visual');
    } else {
        setDisplay('Markdown');
    }
}
function clearResults() {
    $('#test-results').empty();
    $('#copy-results').empty();
    $('#test-error').empty();
    $('#input-t').prop('value', BASE_SIM_T);
    $('#input-teamdps').prop('value', BASE_TEAM_DPS);
    if (dps_chart != null) {
        dps_chart.destroy();
    }
}
window.onload = function () {
    $('#input-adv').change(debounce(loadAdvSlots, 200));
    $('#run-test').click(debounce(runAdvTest, 200));
    if (!localStorage.getItem('displayMode')) {
        localStorage.setItem('displayMode', 'Markdown');
    }
    setDisplay(localStorage.getItem('displayMode'));
    $('#display-mode').click(toggleDisplay);
    $('#clear-results').click(clearResults);
    $('#reset-test').click(debounce(loadAdvSlots, 200));
    $('#input-edit-acl').change(editAcl);
    clearResults();
    loadAdvWPList();
}