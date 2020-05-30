APP_URL = 'https://wildshinobu.pythonanywhere.com/';
BASE_SIM_T = 180;
BASE_TEAM_DPS = 20000;
BASE_AFFLICT_UPTIME = {
    'poison': 90,
    'burn': 85,
    'paralysis': 85,
    'frostbite': 90
};
WEAPON_TYPES = ['sword', 'blade', 'dagger', 'axe', 'lance', 'bow', 'wand', 'staff'];
RANGED = ['wand', 'bow', 'staff'];
DEFAULT_SHARE = 'Ranzal'
DEFAULT_SHARE_ALT = 'Elisanne'
function name_fmt(name) {
    return name.replace(/_/g, ' ').replace(/(?:^|\s)\S/g, function (a) { return a.toUpperCase(); });
}
const speshul = {
    Lily: 'https://cdn.discordapp.com/emojis/664261164208750592.png'
}
const amulet_name_override = {
    Dear_Diary_Fast_RO: 'Dear_Diary',
    Dear_Diary_Slow_RO: 'Dear_Diary',
    Spirit_of_the_Season_No_HP100: 'Spirit_of_the_Season',
    The_Fires_of_Hate_No_HP100: 'The_Fires_of_Hate',
}
function slots_icon_fmt(data) {
    const adv = data[1];
    const ele = data[3];
    const wt = data[4];
    const img_urls = [];
    if (speshul.hasOwnProperty(adv) && Math.random() < 0.1) {
        img_urls.push('<img src="' + speshul[adv] + '" class="slot-icon character"/>');
    } else {
        img_urls.push('<img src="/dl-sim/pic/character/' + adv + '.png" class="slot-icon character"/>');
    }
    const amulets = data.slice(6, 8);
    for (const a of amulets) {
        if (amulet_name_override.hasOwnProperty(a)) {
            img_urls.push('<img src="/dl-sim/pic/amulet/' + amulet_name_override[a] + '.png" class="slot-icon amulet"/>');
        } else {
            img_urls.push('<img src="/dl-sim/pic/amulet/' + a + '.png" class="slot-icon"/>');
        }
    }
    const dragon = data[8];
    if (!dragon.startsWith('Unreleased')) {
        img_urls.push('<img src="/dl-sim/pic/dragon/' + dragon + '.png" class="slot-icon dragon"/>');
    }
    const weapon = data[9];
    if (weapon === 'HDT2' || (weapon === 'Agito1') || (weapon === 'Agito2')) {
        img_urls.push('<img src="/dl-sim/pic/weapon/' + weapon + '_' + ele + '_' + wt + '.png" class="slot-icon weapon"/>');
    }
    let placehold = 5 - img_urls.length;
    while (placehold > 0) {
        img_urls.push('<img src="/dl-sim/pic/CleoDX.png" class="slot-icon placehold"/>');
        placehold -= 1;
    }
    img_urls.push(' | ');
    const coabs = data.slice(10, 13);
    for (const c of coabs) {
        if (WEAPON_TYPES.includes(c.toLowerCase())) {
            img_urls.push('<img src="/dl-sim/pic/icons/' + c.toLowerCase() + '.png" class="slot-icon coab generic"/>');
        } else {
            if (c === 'Axe2') {
                img_urls.push('<img src="/dl-sim/pic/character/Valentines_Melody.png" class="slot-icon coab unique"/>');
            } else {
                img_urls.push('<img src="/dl-sim/pic/character/' + c + '.png" class="slot-icon coab unique"/>');
            }
        }
    }
    img_urls.push(' | ');
    const share = data.slice(13, 15);
    for (const s of share) {
        if (s != '' && s != 'Weapon') {
            img_urls.push('<img src="/dl-sim/pic/character/' + s + '.png" class="slot-icon skillshare"/>');
        }
    }
    return img_urls;
}
function slots_text_format(data) {
    return '[' + data.slice(6, 8).join('+') +
    '][' + data[8] + '][' + data[9] +
    '][' + data.slice(10, 13).join('|') +
    '][S3:' + data[13] + '|S4:' + data[14] + ']';
}
function populateSelect(id, data) {
    const t = id.split('-')[1];
    let options = [];
    for (let d of data) {
        options.push($('<option>' + name_fmt(d) + '</option>')
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
    let slots = ' ' + slots_text_format(arr);
    const cond = (arr[15] != undefined && arr[15] != '<>' && arr[15].includes('<')) ? arr[15].replace('<', '&lt;').replace('>', '&gt;') : '';
    const comment = (arr[16] != undefined) ? arr[16] : '';
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
    for (let i = 17; i < arr.length; i++) {
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
function getUrlVars() {
    var vars = {};
    window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
        vars[key] = value;
    });
    return vars;
}
function populateSkillShare(skillshare) {
    $('#input-ss3').empty();
    $('#input-ss3').append($('<option>Weapon</option>')
        .attr({ id: 'ss3-weapon', value: '' }));
    $('#input-ss4').empty();
    for (const t of ['ss3', 'ss4']) {
        let options = [];
        for (const ss in skillshare) {
            const ss_data = skillshare[ss];
            const ss_repr = name_fmt(ss) + '\t(S' + ss_data['s'] + ': ' + ss_data['sp'] + ' SP, ' + ss_data['cost'] + ' Cost)';
            options.push($('<option>' + ss_repr + '</option>')
                .attr({ id: t + '-' + ss, value: ss }))
        }
        options.sort((a, b) => {
            if (a[0].innerText < b[0].innerText) return -1;
            if (a[0].innerText > b[0].innerText) return 1;
            return 0;
        })
        $('#input-' + t).append(options);
    }
}
function loadAdvWPList() {
    let selectedAdv = 'euden';
    let urlVars = getUrlVars();
    if (urlVars.adv_name) {
        selectedAdv = urlVars.adv_name.toLowerCase();
    } else if (localStorage.getItem('selectedAdv')) {
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

                populateSkillShare(advwp.skillshare);
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
    history.replaceState && history.replaceState(null, '', location.pathname);
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

                buildCoab(slots.coab, slots.adv.fullname, slots.adv.wt);
                for (const c of slots.adv.pref_coab) {
                    const check = $("input[id$='-" + c.toLowerCase() + "']");
                    check.prop('checked', true);
                    coabSelection(1);
                }

                for (const t of ['ss3', 'ss4']) {
                    $('#input-' + t + ' > option').prop('disabled', false);
                    $('#' + t + '-' + slots.adv.fullname).prop('disabled', true);
                }
                if (slots.adv.pref_share[0]) {
                    $('#ss3-' + slots.adv.pref_share[0]).prop('selected', true);
                } else {
                    $('#ss3-weapon').prop('selected', true);
                }
                if (slots.adv.pref_share[1]) {
                    $('#ss4-' + slots.adv.pref_share[1]).prop('selected', true);
                } else {
                    if (slots.adv.fullname === DEFAULT_SHARE) {
                        $('#ss4-' + DEFAULT_SHARE_ALT).prop('selected', true);
                    } else {
                        $('#ss4-' + DEFAULT_SHARE).prop('selected', true);
                    }
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
                    if (slots.adv.no_config.includes('coab')) {
                        $('input.coab-check').prop('disabled', true);
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
function checkCoabSelection(e) {
    const add = $(e.target).prop('checked') ? 1 : -1
    coabSelection(add);
}
function coabSelection(add) {
    const count = $('#input-coabs').data('selected') + add;
    const max = $('#input-coabs').data('max');
    if (count >= max) {
        $('input:not(:checked).coab-check').prop('disabled', true);
    } else {
        $('.coab-check').prop('disabled', false);
    }
    $('#input-coabs').data('selected', count);
}

function buildCoab(coab, fullname, weapontype) {
    $('#input-coabs > div').empty();
    $('#input-coabs').data('max', 3);
    let found_fullname = null;
    $('#input-coabs').data('selected', 0);
    for (const k in coab) {
        const cid = 'coab-' + k.toLowerCase();
        const kcoab = coab[k];
        const wrap = $('<div></div>').addClass('custom-control custom-checkbox custom-control-inline');
        const check = $('<input>').addClass('custom-control-input').prop('type', 'checkbox').prop('id', cid);
        check.data('name', k);
        check.data('chain', kcoab[0]);
        check.data('ex', kcoab[1]);
        check.change(checkCoabSelection);
        if (k == fullname) {
            if (!kcoab[0] || (kcoab[0].length < 3 || kcoab[0][2] != 'hp≤40')) {
                check.prop('disabled', true);
                check.prop('checked', true);
            } else {
                $('#input-coabs').data('max', 4);
                check.addClass('coab-check');
            }
            found_fullname = kcoab[1];
        } else {
            check.addClass('coab-check');
        }
        const label = $(`<label>${k}</label>`).addClass('custom-control-label').prop('for', cid);
        wrap.append(check);
        wrap.append(label);
        if (kcoab[0]) {
            wrap.prop('title', kcoab[0].join('|') + ' - ' + kcoab[1]);
        } else {
            wrap.prop('title', kcoab[1]);
        }
        if (WEAPON_TYPES.includes(kcoab[1])) {
            $('#input-coabs-' + kcoab[1]).append(wrap);
        } else {
            $('#input-coabs-other').append(wrap);
        }
    }
    let check = $('#coab-all-' + weapontype);
    if (found_fullname) {
        check = $('#coab-all-' + found_fullname);
    }
    check.prop('disabled', true);
    check.prop('checked', true);
    check.removeClass('coab-check');
}
function readCoabList() {
    const coabList = $('input:checked.coab-check');
    if (coabList.length === 0) {
        return null;
    } else {
        const coabilities = [];
        coabList.each(function (idx, res) {
            coabilities.push($(res).data('name'));
        });
        return coabilities;
    }
}
function readSkillShare() {
    const skillShare = [];
    if ($('#input-ss3').val() != '') {
        skillShare.push($('#input-ss3').val());
    }
    if ($('#input-ss4').val() != '') {
        skillShare.push($('#input-ss4').val());
    }
    if (skillShare.length === 0) {
        return null;
    } else {
        return skillShare;
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
    requestJson['share'] = readSkillShare();
    requestJson['coab'] = readCoabList();
    const t = $('#input-t').val();
    if (!isNaN(parseInt(t))) {
        requestJson['t'] = t;
    }
    const afflict_res = readResistDict();
    if (afflict_res != null) {
        requestJson['afflict_res'] = afflict_res;
    }
    if (!isNaN(parseInt($('#input-teamdps').val()))) {
        const dps = $('#input-teamdps').val();
        requestJson['teamdps'] = dps;
        localStorage.setItem('teamdps', dps);
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
                    const name = name_fmt(cond_true[1]);
                    const icon_urls = slots_icon_fmt(cond_true);
                    let copyTxt = '**' + name + ' ' + t + 's** ';
                    let newResultItem = $('<div></div>').attr({ class: 'test-result-item' });
                    newResultItem.append($(
                        '<h4 class="test-result-slot-grid"><div>' +
                        icon_urls[0] + '</div><div>' + name + '</div><div>' + icon_urls.slice(1).join('') + '</div></h4>'));
                    copyTxt += createDpsBar(newResultItem, cond_true, res.extra, undefined);
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
    if (localStorage.getItem('teamdps')) {
        selectedAdv = localStorage.getItem('teamdps');
        $('#input-teamdps').val(localStorage.getItem('teamdps'));
    } else {
        $('#input-teamdps').val(BASE_TEAM_DPS);
        localStorage.setItem('teamdps', BASE_TEAM_DPS);
    }
    $('#input-missile').val(0);
    const resistList = $('#affliction-resist > div > input[type="text"]');
    resistList.each(function (idx, res) { $(res).val(''); });
    $('input:checked.coab-check').prop('check', false);
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
    $('#reset-test').click(loadAdvSlots);
    $('#input-edit-acl').change(editAcl);
    $('#input-wep').change(weaponSelectChange);
    $('#input-sim-afflict-type').change(simAfflictSelectChange);
    clearResults();
    loadAdvWPList();
}