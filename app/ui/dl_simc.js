APP_URL = 'https://wildshinobu.pythonanywhere.com/';
EX_MAP = {
    'blade': 'k',
    'wand': 'r',
    'bow': 'b',
    'dagger': 'd',
    'axe2': 'm',
    'sword': 's',
    'g_euden': 'g',
    'tobias': 't'
}
AXE2_ADV = ['h_mym', 'v_melody']
UNIQUE_ADV = ['g_euden', 'tobias']
RANGED = ['wand', 'bow', 'staff']
BASE_SIM_T = 180
BASE_TEAM_DPS = 20000
BASE_AFFLICT_UPTIME = {
    'poison': 90,
    'burn': 75,
    'paralysis': 80,
    'frostbite': 90
}
PREFIX_MAPS = {
    'adv': {
        'g_': 'gala_',
        'b_zardin': 'beautician_zardin',
        'd_': 'dragonyule_',
        'h_': 'halloween_',
        's_maribelle': 'student_maribelle',
        's_': 'summer_',
        'v_': 'valentines_',
        'w_': 'wedding_',
        'mh_': 'hunter_',
        't_hope': 'templar_hope'
    },
}
function name_fmt(name) {
    return name.replace(/_/g, ' ').replace(/(?:^|\s)\S/g, function (a) { return a.toUpperCase(); });
}
const speshul = {
    Lily: 'https://cdn.discordapp.com/emojis/664261164208750592.png',
    // Gala_Luca: 'https://cdn.discordapp.com/emojis/619420426770186240.png',
    // Gala_Cleo: 'https://cdn.discordapp.com/emojis/637119887071772673.png',
    // Gala_Elisanne: 'https://cdn.discordapp.com/emojis/651238318327201792.png',
    // Gala_Euden: 'https://cdn.discordapp.com/emojis/495873033203089418.png',
    // Gala_Ranzal: 'https://cdn.discordapp.com/emojis/512920940963692566.png',
    // Gala_Sarisse: 'https://cdn.discordapp.com/emojis/622190324059734028.png',
    // Gala_Mym: 'https://cdn.discordapp.com/emojis/589506568148615178.gif'
}
const amulet_name_override = {
    Dear_Diary_Fast_RO: 'Dear_Diary',
    Dear_Diary_Slow_RO: 'Dear_Diary',
    Spirit_of_the_Season_No_HP100: 'Spirit_of_the_Season',
    The_Fires_of_Hate_No_HP100: 'The_Fires_of_Hate',
}
function slots_icon_fmt(adv, ele, wt, slots) {
    const img_urls = [];
    if (speshul.hasOwnProperty(adv) && Math.random() < 0.1) {
        img_urls.push('<img src="' + speshul[adv] + '" class="slot-icon character"/>');
    } else {
        img_urls.push('<img src="/dl-sim/pic/character/' + adv + '.png" class="slot-icon character"/>');
    }
    const slots_list = slots.replace(/\[/g, '').split(']');
    const amulets = slots_list[0].split('+');
    for (a of amulets) {
        if (amulet_name_override.hasOwnProperty(a)) {
            img_urls.push('<img src="/dl-sim/pic/amulet/' + amulet_name_override[a] + '.png" class="slot-icon"/>');
        } else {
            img_urls.push('<img src="/dl-sim/pic/amulet/' + a + '.png" class="slot-icon"/>');
        }
    }
    const dragon = slots_list[1];
    if (!dragon.startsWith('Unreleased')) {
        img_urls.push('<img src="/dl-sim/pic/dragon/' + dragon + '.png" class="slot-icon"/>');
    }
    const weapon = slots_list[2];
    if (weapon === 'HDT2' || (weapon === 'Agito')) {
        img_urls.push('<img src="/dl-sim/pic/weapon/' + weapon + '_' + ele + '_' + wt + '.png" class="slot-icon"/>');
    }
    return img_urls;
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
    'team_buff': 'IndianRed',
    'dx': 'mediumpurple',
    'ds': 'blueviolet'
}
nameMap = {
    'ds': 'dragon_skill',
    'dx': 'dragon_attack'
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
    const cond = (arr[7] != undefined && arr[7] != '<>' && arr[7].includes('<')) ? arr[7].replace('<', '&lt;').replace('>', '&gt;') : '';
    const comment = (arr[8] != undefined) ? arr[8] : '';
    let cond_comment = [];
    let cond_comment_str = '';
    let cond_cpy_str = '';
    if (cond != undefined && !cond.startsWith('!')) {
        if (cond != '') {
            cond_comment.push(cond);
        }
        if (comment != '') {
            cond_comment.push(comment);
        }
        if (cond_comment.length > 0) {
            cond_comment_str = '<br/>' + cond_comment.join(' ');
            cond_cpy_str = ' ' + cond_comment.join(' ');
        }
    } else {
        slots = '';
    }
    resDiv.append($('<h6>DPS:' + total + slots + cond_comment_str + '</h6>'));
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
                if (nameMap.hasOwnProperty(dmg[0])) {
                    damageTxt = nameMap[dmg[0]] + ': ' + dmg[1];
                }
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
function trimAcl(acl_str) {
    return $.trim(acl_str.replace(new RegExp(/[\n] +/, 'g'), '\n'));
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
    const adv_name = $('#input-adv').val();
    localStorage.setItem('selectedAdv', $('#input-adv').val());
    $.ajax({
        url: APP_URL + 'simc_adv_slotlist',
        dataType: 'text',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify({ 'adv': adv_name }),
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
                if (AXE2_ADV.includes(adv_name)) {
                    $('#ex-axe2').prop('checked', true);
                    $('#ex-axe2').prop('disabled', true);
                } else if (UNIQUE_ADV.includes(adv_name)) {
                    $('#ex-' + adv_name).prop('checked', true);
                    $('#ex-' + adv_name).prop('disabled', true);
                } else if (adv_name != 'megaman') {
                    $('#ex-' + slots.adv.wt).prop('checked', true);
                    $('#ex-' + slots.adv.wt).prop('disabled', true);
                }
                if (RANGED.includes(slots.adv.wt)) {
                    $('#input-missile').prop('disabled', false);
                } else {
                    $('#input-missile').prop('disabled', true);
                }
                $('#input-acl').blur();
                $('#input-edit-acl').prop('checked', false);
                $('#input-acl').prop('disabled', true);
                const acl = trimAcl(slots.adv.acl);
                $('#input-acl').val(acl);
                $('#input-acl').data('default_acl', acl);
                if (slots.adv.afflict_res != undefined) {
                    for (const key in slots.adv.afflict_res) {
                        $('#input-res-' + key).val(slots.adv.afflict_res[key]);
                    }
                } else {
                    for (const key in slots.adv.afflict_res) {
                        $('#input-res-' + key).removeAttr('value');
                    }
                }
                if (slots.adv.no_config != undefined) {
                    if (slots.adv.no_config.includes('wp')) {
                        $('#input-wp1').prop('disabled', true);
                        $('#input-wp2').prop('disabled', true);
                    }
                    if (slots.adv.no_config.includes('acl')) {
                        $('#input-edit-acl').prop('disabled', true);
                    }
                } else {
                    $('#input-wp1').prop('disabled', false);
                    $('#input-wp2').prop('disabled', false);
                    $('#input-edit-acl').prop('disabled', false);
                }
                runAdvTest();
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#test-results').html('Failed to load adventurer');
        }
    });
}
function buildConditionList(conditions) {
    const conditionDiv = $('#input-conditions');
    conditionDiv.empty();
    for (cond in conditions) {
        const newCondCheck = $('<div></div>').attr({ class: 'custom-control custom-checkbox custom-control-inline' });
        const newCondCheckInput = $('<input/>').attr({ id: 'input-cond-' + cond, type: 'checkbox', class: 'custom-control-input' }).prop('checked', conditions[cond]).data('cond', cond);
        const newCondCheckLabel = $('<label>' + cond + '</label>').attr({ for: 'input-cond-' + cond, class: 'custom-control-label' });
        newCondCheck.append(newCondCheckInput);
        newCondCheck.append(newCondCheckLabel);
        conditionDiv.append(newCondCheck);
    }
}
function readConditionList() {
    let conditions = {};
    const condCheckList = $('#input-conditions > div > input[type="checkbox"]');
    if (condCheckList.length === 0) {
        return null;
    } else {
        condCheckList.each(function (idx, condCheck) {
            conditions[$(condCheck).data('cond')] = $(condCheck).prop('checked');
        });
        return conditions;
    }
}
function readResistDict() {
    let resists = {};
    const resistList = $('#affliction-resist > div > input[type="text"]');
    if (resistList.length === 0) {
        return null;
    } else {
        resistList.each(function (idx, res) {
            const resVal = parseInt($(res).val());
            if (!isNaN(resVal)) {
                const parts = $(res).attr('id').split('-');
                resists[parts[parts.length - 1]] = resVal;
            }
        });
        return resists;
    }
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
    const afflict_res = readResistDict();
    if (afflict_res != null) {
        requestJson['afflict_res'] = afflict_res;
    }
    if (!isNaN(parseInt($('#input-teamdps').val()))) {
        requestJson['teamdps'] = $('#input-teamdps').val();
    }
    if (!isNaN(parseInt($('#input-missile').val()))) {
        requestJson['missile'] = $('#input-missile').val();
    }
    if ($('#input-edit-acl').prop('checked')) {
        requestJson['acl'] = $('#input-acl').val();
    }
    if ($('#input-sim-afflict').val() !== 'none' && !isNaN(parseInt($('#input-sim-afflict-time').val()))) {
        requestJson['sim_afflict_type'] = $('#input-sim-afflict-type').val();
        requestJson['sim_afflict_time'] = $('#input-sim-afflict-time').val();
    }
    if (!isNaN(parseInt($('#input-sim-buff-str').val()))) {
        requestJson['sim_buff_str'] = $('#input-sim-buff-str').val();
    }
    if (!isNaN(parseInt($('#input-sim-buff-def').val()))) {
        requestJson['sim_buff_def'] = $('#input-sim-buff-def').val();
    }
    const condition = readConditionList();
    if (condition !== null) {
        requestJson['condition'] = condition;
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
                    buildConditionList(res.condition);
                    const result = res.test_output.split('\n');
                    const cond_true = result[1].split(',');
                    const name = substitute_prefix(cond_true[1], 'adv');
                    const icon_urls = slots_icon_fmt(cond_true[1], cond_true[3], cond_true[4], cond_true[6]);
                    let copyTxt = '**' + name + ' ' + t + 's** ';
                    if (exArr.length > 0) {
                        copyTxt += '(co-ab: ' + exArr.join(' ') + ')'
                    } else {
                        copyTxt += '(co-ab: none)'
                    }
                    let newResultItem = $('<div></div>').attr({ class: 'test-result-item' });
                    newResultItem.append($('<h4 class="test-result-slot-grid"><div>' + icon_urls[0] + '</div><div>' + name + '</div><div>' + icon_urls.slice(1).join('') + '</div></h4>'));
                    copyTxt += createDpsBar(newResultItem, cond_true, res.extra);
                    if (result.length > 2 && result[2].includes(',')) {
                        cond_false = result[2].split(',');
                        extra = Object.keys(res.extra_no_cond).length > 0 ? res.extra_no_cond : res.extra
                        copyTxt += createDpsBar(newResultItem, cond_false, extra, cond_true[0]);
                    }
                    // createChart(res.log.dmg, name);
                    const logs = ['dragon', 'summation', 'action', 'timeline'].map(key => {
                        if (res.logs[key] !== undefined && res.logs[key] !== "") {
                            return res.logs[key];
                        } else {
                            return false;
                        }
                    }).filter(l => (l));
                    $('#damage-log').html(logs.join('<hr class="log-divider">'));
                    $('#test-results').prepend(newResultItem);
                    $('#copy-results').prepend($('<textarea>' + copyTxt + '</textarea>').attr({ class: 'copy-txt', rows: (copyTxt.match(/\n/g) || [0]).length + 1 }));
                }
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $('#test-error').html('Failed to run damage simulation');
        }
    });
}
function editAcl() {
    $('#input-acl').prop('disabled', !$(this).prop('checked'));
    $('#input-acl').val($('#input-acl').data('default_acl'));
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
        $('#display-mode').html('Visual Display');
        localStorage.setItem('displayMode', displayMode);
    } else if (displayMode == 'Markdown') {
        $('#copy-results').css('display', 'none');
        $('#test-results').css('display', 'block');
        $('#display-mode').html('Text Display');
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
    $('#input-t').val(BASE_SIM_T);
    $('#input-teamdps').val(BASE_TEAM_DPS);
    $('#input-missile').val(0);
    const resistList = $('#affliction-resist > div > input[type="text"]');
    resistList.each(function (idx, res) { $(res).val(''); });
    $('#input-sim-afflict-type')[0].selectedIndex = 0;
    $('#input-sim-afflict-time').removeAttr('value');
    $('#input-sim-afflict-time').prop('disabled', true);
    $('#input-sim-afflict-time').empty();
    $('#input-sim-buff-str').removeAttr('value');
    $('#input-sim-buff-def').removeAttr('value');
    $('#input-conditions').empty();
}
function weaponSelectChange() {
    const weapon = $('#input-wep').val();
    if (weapon.startsWith('Agito') || weapon.startsWith('UnreleasedAgito')) {
        $('#input-edit-acl').prop('checked', true);
        $('#input-acl').prop('disabled', false);
        const acl = $('#input-acl').val().split('\n');
        let new_acl = '`s3, not self.s3_buff\n';
        for (const line of acl) {
            if (!line.startsWith('`s3')) {
                new_acl += line + '\n';
            }
        }
        $('#input-acl').val(new_acl);
    } else {
        $('#input-edit-acl').prop('checked', false);
        $('#input-acl').prop('disabled', true);
        $('#input-acl').val($('#input-acl').data('default_acl'));
    }
}
function simAfflictSelectChange() {
    const simAfflict = $('#input-sim-afflict-type').val();
    if (simAfflict !== 'none') {
        $('#input-sim-afflict-time').prop('disabled', false);
        $('#input-sim-afflict-time').val(BASE_AFFLICT_UPTIME[simAfflict]);
    } else {
        $('#input-sim-afflict-time').prop('disabled', true);
        $('#input-sim-afflict-time').removeAttr('value');
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
    $('#input-wep').change(weaponSelectChange);
    $('#input-sim-afflict-type').change(simAfflictSelectChange);
    clearResults();
    loadAdvWPList();
}