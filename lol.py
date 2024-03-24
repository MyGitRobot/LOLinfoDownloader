# -*- coding: utf-8 -*-
"""
Program: LOL Info Downloader
Author: MrCrawL
Created Date: 2024-02-16
Last Modified: 2024-03-24
Modified by: MrCrawL
"""

import requests
from jsonpath import jsonpath
import json
import os
from re import findall

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
}

roles_dict = {
    'fighter': '战士',
    'mage': '法师',
    'assassin': '刺客',
    'tank': '坦克',
    'marksman': '射手',
    'support': '辅助'
}

translate_dict = {
    'heroId': '英雄ID',
    'name': '英雄名称',
    'alias': '英文名称',
    'title': '英雄名字',
    'roles': '英雄职业',
    'shortBio': '英雄简介',
    'attack': '进攻',
    'defense': '防守',
    'magic': '法术',
    'difficulty': '难度',
    'hp': '生命值',
    'hpperlevel': '每级提升生命值',
    'mp': '法术值',
    'mpperlevel': '每级提升魔法值',
    'movespeed': '移动速度',
    'armor': '物理防御值',
    'armorperlevel': '每级提升物理防御值',
    'spellblock': '法术防御值',
    'spellblockperlevel': '每级提升法术防御值',
    'attackrange': '攻击范围',
    'hpregen': '生命值回复',
    'hpregenperlevel': '每级提升生命值回复',
    'mpregen': '法术值回复',
    'mpregenperlevel': '每级提升法术值回复',
    'crit': '暴击率',
    'critperlevel': '每级暴击率',
    'attackdamage': '攻击伤害',
    'attackdamageperlevel': '每级提升攻击伤害',
    'attackspeed': '攻击速度',
    'attackspeedperlevel': '每级提升攻击速度',
    'isWeekFree': '周末限免',
    'damageType': '伤害类型',
    'selectAudio': '被选语音',
    'banAudio': '被禁语音',
    'goldPrice': '金币价格',
    'couponPrice': '优惠券价',
    'keywords': '搜索词',
    'skinId': '皮肤ID',
    'mainImg': '高清原图',
    'iconImg': '小头图标',
    'loadingImg': '加载图片',
    'videoImg': '视频图片',
    'centerImg': '焦点图片',
    'kMagic': '法术伤害',
    'kPhysical': '物理伤害',
    'kMixed': '混合伤害'
}

spells_dict = {
    'spellKey': '技能按键',
    'name': '技能名称',
    'description': '技能描述',
    'abilityIconPath': '技能图标',
    'cost': '技能消耗',
    'cooldown': '技能冷却（秒）',
    'range': '范围'
}


def u_decode(string:str):
    """
    字符串处理，避免乱码和UnicodeError
    :param string: 需要处理的字符串
    :return: 处理后的字符串
    """
    string = string.replace('\\/', '/')
    matches = findall(r'\\u[0-9a-fA-F]{4}', string)
    for match in matches:
        string = string.replace(match, chr(int(match[2:], 16)))
    return string


'''符文'''
def save_rune_list():
    """获取符文列表，保存在本地"""
    rune_list_url = 'https://game.gtimg.cn/images/lol/act/img/js/runeList/rune_list.js'
    rune_list_res = requests.get(rune_list_url, headers=headers)
    text = u_decode(rune_list_res.content.decode('utf-8'))
    json_file = json.loads(text)
    with open('rune_list.js', 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_file, indent=4, ensure_ascii=False))
    print('保存成功 rune_list.js')


def load_rune_list():
    """
    加载本地符文列表，返回json格式
    :return: json，可用jsonpath查询所需内容
    """
    if not os.path.exists('rune_list.js'): save_rune_list()
    with open('rune_list.js', 'r', encoding='utf-8') as f:
        text = f.read()
        json_file = json.loads(text)
        return json_file


def show_rune_list():
    """展示符文列表，显示在控制台上"""
    if not os.path.exists('rune_list.js'): save_rune_list()
    with open('rune_list.js', 'r', encoding='utf-8') as f:
        print(f.read())


'''召唤者技能'''
def save_summonerskill_list():
    """获取召唤者技能列表，保存在本地"""
    summonerskill_list_url = 'https://game.gtimg.cn/images/lol/act/img/js/summonerskillList/summonerskill_list.js'
    summonerskill_list_res = requests.get(summonerskill_list_url, headers=headers)
    text = u_decode(summonerskill_list_res.content.decode('utf-8'))
    json_file = json.loads(text)
    with open('summonerskill_list.js', 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_file, indent=4, ensure_ascii=False))
    print('保存成功 summonerskill_list.js')


def load_summonerskill_list():
    """
    加载本地召唤者技能列表，返回json格式
    :return: json，可用jsonpath查询所需内容
    """
    if not os.path.exists('summonerskill_list.js'): save_summonerskill_list()
    with open('summonerskill_list.js', 'r', encoding='utf-8') as f:
        text = f.read()
        json_file = json.loads(text)
        return json_file


def show_summonerskill_list():
    """展示召唤者技能列表，显示在控制台上"""
    if not os.path.exists('summonerskill_list.js'): save_summonerskill_list()
    with open('summonerskill_list.js', 'r', encoding='utf-8') as f:
        print(f.read())


'''英雄列表'''
def save_hero_list():
    """获取英雄列表，保存在本地"""
    hero_list_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    hero_list_res = requests.get(hero_list_url, headers=headers)
    text = u_decode(hero_list_res.content.decode('utf-8'))
    json_file = json.loads(text)
    with open('hero_list.js', 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_file, indent=4, ensure_ascii=False))
    print('保存成功 hero_list.js')
    

def load_hero_list():
    """
    加载本地英雄列表，返回json格式
    :return: json，可用jsonpath查询所需内容
    """
    if not os.path.exists('hero_list.js'): save_hero_list()
    with open('hero_list.js', 'r', encoding='utf-8') as f:
        text = f.read()
        json_file = json.loads(text)
        return json_file


def show_hero_list():
    """展示英雄列表，显示在控制台上"""
    if not os.path.exists('hero_list.js'): save_hero_list()
    with open('hero_list.js', 'r', encoding='utf-8') as f:
        print(f.read())


'''装备'''
def save_items():
    """获取装备列表，保存在本地"""
    items_url = 'https://game.gtimg.cn/images/lol/act/img/js/items/items.js'
    items_res = requests.get(items_url, headers=headers)
    text = u_decode(items_res.content.decode('utf-8'))
    json_file = json.loads(text)
    with open('items.js', 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_file, indent=4, ensure_ascii=False))
    print('保存成功 items.js')
    

def load_items():
    """
    加载本地装备列表，返回json格式
    :return: json，可用jsonpath查询所需内容
    """
    if not os.path.exists('items.js'): save_items()
    with open('items.js', 'r', encoding='utf-8') as f:
        text = f.read()
        json_file = json.loads(text)
        return json_file


def show_items():
    """展示装备列表，显示在控制台上"""
    if not os.path.exists('items.js'): save_items()
    with open('items.js', 'r', encoding='utf-8') as f:
        print(f.read())


'''英雄'''
def save_hero_js(hero_id:str):
    """
    保存heroId对应英雄的全信息
    :param hero_id: 英雄的heroId
    :return:
    """
    hero_url = f'https://game.gtimg.cn/images/lol/act/img/js/hero/{hero_id}.js'
    hero_res = requests.get(hero_url, headers=headers)
    text = u_decode(hero_res.content.decode('utf-8'))
    json_file = json.loads(text)
    hero_name = jsonpath(json_file, '$..hero.name')[0]
    with open(f'{hero_id}.js', 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_file, indent=4, ensure_ascii=False))
    print(f'保存成功 {hero_name}({hero_id}.js)')


def load_hero_js(hero_id:str):
    """
    加载本地英雄js，返回json格式
    :param hero_id: json，可用jsonpath查询所需内容
    :return:
    """
    if not os.path.exists(f'{hero_id}.js'): save_hero_js(hero_id)
    with open(f'{hero_id}.js', 'r', encoding='utf-8') as f:
        text = f.read()
        json_file = json.loads(text)
        return json_file


def show_hero_js(hero_id:str):
    """展示装备列表，显示在控制台上"""
    if look_up_heroId(hero_id):
        if not os.path.exists(f'{hero_id}.js'): save_hero_js(hero_id)
        with open(f'{hero_id}.js', 'r', encoding='utf-8') as f:
            print(f.read())


def look_up_heroId(hero_name:str):
    """
    查询英雄的id
    :param hero_name: 英雄的名称，如“黑暗之女”、“狂战士”
    :return: 英雄的id
    """
    js = load_hero_list()
    try:
        hero_id:str = jsonpath(js, f'$.hero[?(@.name == "{hero_name}")].heroId')[0]
        return hero_id
    except TypeError:
        print('查无此英雄，请确认英雄名称后重试')
        return False


def save_img(file_name:str, img_url:str):
    with open(f'{file_name}.jpg', 'wb') as f:
        f.write(requests.get(img_url, headers=headers).content)
        # print(f'{file_name}.jpg 保存成功')
    

def get_hero_info(hero_id:str):
    """
    保存英雄信息
    :param hero_id: 英雄id，可通过look_up_heroId("英雄名称")查询
    :return:
    """
    hero_info = []
    js = load_hero_js(hero_id)
    hero_info.append(['heroId', jsonpath(js, '$.hero.heroId')[0]])
    hero_info.append(['name', jsonpath(js, '$.hero.name')[0]])
    hero_info.append(['alias', jsonpath(js, '$.hero.alias')[0]])
    hero_info.append(['title', jsonpath(js, '$.hero.title')[0]])
    roles_origin:list = jsonpath(js, '$.hero.roles')[0]
    roles_list = []
    for role in roles_origin:
        roles_list.append(roles_dict[role])
    roles = '、'.join(roles_list)
    hero_info.append(['roles', roles])
    hero_info.append(['shortBio', jsonpath(js, '$.hero.shortBio')[0]])
    hero_info.append(['attack', jsonpath(js, '$.hero.attack')[0]])
    hero_info.append(['defense', jsonpath(js, '$.hero.defense')[0]])
    hero_info.append(['magic', jsonpath(js, '$.hero.magic')[0]])
    hero_info.append(['difficulty', jsonpath(js, '$.hero.difficulty')[0]])
    hero_info.append(['hp', jsonpath(js, '$.hero.hp')[0]])
    hero_info.append(['hpperlevel', jsonpath(js, '$.hero.hpperlevel')[0]])
    hero_info.append(['mp', jsonpath(js, '$.hero.mp')[0]])
    hero_info.append(['mpperlevel', jsonpath(js, '$.hero.mpperlevel')[0]])
    hero_info.append(['movespeed', jsonpath(js, '$.hero.movespeed')[0]])
    hero_info.append(['armor', jsonpath(js, '$.hero.armor')[0]])
    hero_info.append(['armorperlevel', jsonpath(js, '$.hero.armorperlevel')[0]])
    hero_info.append(['spellblock', jsonpath(js, '$.hero.spellblock')[0]])
    hero_info.append(['spellblockperlevel', jsonpath(js, '$.hero.spellblockperlevel')[0]])
    hero_info.append(['attackrange', jsonpath(js, '$.hero.attackrange')[0]])
    hero_info.append(['hpregen', jsonpath(js, '$.hero.hpregen')[0]])
    hero_info.append(['hpregenperlevel', jsonpath(js, '$.hero.hpregenperlevel')[0]])
    hero_info.append(['mpregen', jsonpath(js, '$.hero.mpregen')[0]])
    hero_info.append(['mpregenperlevel', jsonpath(js, '$.hero.mpregenperlevel')[0]])
    hero_info.append(['crit', jsonpath(js, '$.hero.crit')[0]])
    hero_info.append(['critperlevel', jsonpath(js, '$.hero.critperlevel')[0]])
    hero_info.append(['attackdamage', jsonpath(js, '$.hero.attackdamage')[0]])
    hero_info.append(['attackdamageperlevel', jsonpath(js, '$.hero.attackdamageperlevel')[0]])
    hero_info.append(['attackspeed', jsonpath(js, '$.hero.attackspeed')[0]])
    hero_info.append(['attackspeedperlevel', jsonpath(js, '$.hero.attackspeedperlevel')[0]])
    if jsonpath(js, '$.hero.isWeekFree')[0] == '0':
        hero_info.append(['isWeekFree', '否'])
    else:
        hero_info.append(['isWeekFree', '是'])
    hero_info.append(['damageType', translate_dict[jsonpath(js, '$.hero.damageType')[0]]])
    hero_info.append(['selectAudio', jsonpath(js, '$.hero.selectAudio')[0]])
    hero_info.append(['banAudio', jsonpath(js, '$.hero.banAudio')[0]])
    hero_info.append(['goldPrice', jsonpath(js, '$.hero.goldPrice')[0]])
    hero_info.append(['couponPrice', jsonpath(js, '$.hero.couponPrice')[0]])
    hero_info.append(['keywords', jsonpath(js, '$.hero.keywords')[0]])
    return hero_info


def get_hero_skills(hero_id:str):
    js = load_hero_js(hero_id)
    skills = jsonpath(js, '$.spells')[0]
    for skill in skills:
        try:
            skill['cost'] = '/'.join(skill['cost'])
        except TypeError: continue
        try:
            skill['cooldown'] = '/'.join(skill['cooldown'])
        except TypeError: continue
        try:
            skill['range'] = '/'.join(skill['range'])
        except TypeError: continue
    return skills


def get_hero_skin(hero_id:str):
    js = load_hero_js(hero_id)
    skins_from_js = jsonpath(js, '$.skins')[0]
    skins = []
    for skin_info in skins_from_js:
        if skin_info['mainImg'] != '':
            skins.append(skin_info)
    return skins


def save_hero_skin(hero_id:str):
    skins = get_hero_skin(hero_id)
    count = 1
    for skin in skins:
        save_img(f'{hero_id}-{skin["heroName"]}/{skin["name"]}-{translate_dict["mainImg"]}', skin['mainImg'])
        save_img(f'{hero_id}-{skin["heroName"]}/{skin["name"]}-{translate_dict["iconImg"]}', skin['iconImg'])
        save_img(f'{hero_id}-{skin["heroName"]}/{skin["name"]}-{translate_dict["loadingImg"]}', skin['loadingImg'])
        save_img(f'{hero_id}-{skin["heroName"]}/{skin["name"]}-{translate_dict["centerImg"]}', skin['centerImg'])
        print(f'\r全皮肤图片下载中 - {count}/{len(skins)}', end='', flush=True)
        count += 1
    print(f'\n{skins[0]["heroName"]}全皮肤图片下载完毕')


def save_hero_info(hero_id:str):
    hero_info = get_hero_info(hero_id)
    hero_skills = get_hero_skills(hero_id)
    hero_name = hero_info[1][1]
    os.makedirs(f'{hero_id}-{hero_name}', exist_ok=True)
    with open(f'{hero_id}-{hero_name}/{hero_name}.txt', 'w', encoding='utf-8') as f:
        for info in hero_info:
            f.write(f'{translate_dict[info[0]]}：{info[1]}\n')
        f.write('\n----------技能----------\n\n')
        for skill in hero_skills:
            for key in spells_dict:
                f.write(f'{spells_dict[key]}：{skill[key]}\n')
            f.write('\n')
    with open(f'{hero_id}-{hero_name}/{hero_name}-被选语音.ogg', 'wb') as f:
        ogg_res = requests.get(hero_info[-5][1], headers=headers)
        f.write(ogg_res.content)
    with open(f'{hero_id}-{hero_name}/{hero_name}-被禁语音.ogg', 'wb') as f:
        ogg_res = requests.get(hero_info[-4][1], headers=headers)
        f.write(ogg_res.content)
    print(f'保存成功 {hero_name}.txt')
    save_hero_skin(hero_id)
    print(f'请前往"{hero_id}-{hero_name}"文件夹查看')


if __name__ == '__main__':
    
    '''保存英雄列表'''
    # save_hero_list()
    '''加载英雄列表'''
    # hero_list = load_hero_list()
    '''展示英雄列表'''
    # show_hero_list()
    
    '''保存装备列表'''
    # save_items()
    '''加载装备列表'''
    # items = load_items()
    '''展示装备列表'''
    # show_hero_list()
    
    '''保存英雄.js'''
    # save_hero_js('2')
    '''加载英雄.js'''
    # load_hero_js('1')
    '''展示英雄.js'''
    # show_hero_js('1')
    
    '''保存英雄皮肤'''
    # save_hero_skin('1')
    '''保存英雄信息'''
    # save_hero_info('4')
    
    heroName = input('请输入英雄名称，如黑暗之女、狂战士：')
    while heroName != '0':
        heroId = look_up_heroId(heroName)
        if heroId is False: pass
        else: save_hero_info(heroId)
        heroName = input('请输入英雄名称（输入0退出）：')
