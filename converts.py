def w2_records(queryset):
    import re
    json_str = '['
    for obj in queryset:
        json_str = json_str + '{'
        for name in dir(obj):
            key_value = getattr(obj, name)
            if not name.startswith('__') and not callable(key_value) and not name.startswith(
                    '_') and name != 'sqlmeta' and len(re.findall('[A-Z]', name)) == 0 and name != 'id':
                json_str = json_str + name + ':"' + str(key_value).replace('\n', '') + '",'
            if name == 'id':
                json_str = json_str + 'recid:"' + str(key_value).replace('\n', '') + '",'
        json_str = json_str + '},'
    json_str = json_str + ']'
    # with open('a.txt', 'w', encoding='utf8') as f:
    #    f.write(json_str)
    return json_str


def format_field_id(s):
    return (''.join(list(filter(str.isdigit, str(s)))))[-6:]


def format_field_percentage(s):
    if isinstance(s, str):
        return float(s.rstrip('%'))
    else:
        return s


def format_field_name(s):
    return s.replace(' ', '')


def format_field_status(s):
    if '正常' in s:
        return '正常'
    elif '停牌' in s:
        return '停牌'


def unique(queryset, attr):
    unique_list = []
    if queryset.count() > 0:
        for i in queryset:
            try:
                if str(getattr(i, attr)) not in unique_list:
                    unique_list.append(str(getattr(i, attr)))
            except Exception as e:
                print("Error:" + str(e))
                break
    return unique_list


def isgood(key, key_value):
    import re
    if not key.startswith('__') and not callable(key_value) and not key.startswith('_') and key != 'sqlmeta' and len(
            re.findall('[A-Z]', key)) == 0:
        if key != 'id' and key != 'project' and key != 'adviser' and key != 'guarantor' and key != 'posterior':
            return True
        else:
            return False
    else:
        return False


def obj2dict(obj):
    pr = {}
    for key in dir(obj):
        key_value = getattr(obj, key)
        if isgood(key, key_value):
            pr[key] = key_value
    return pr


def df2w2(df):
    w2_str = "["
    for r in range(len(df)):
        w2_str = w2_str + "{recid:%s," % str(r + 1)
        for c in df.columns:
            w2_str = w2_str + '%s:"%s",' % (c, str(df[c].iloc[r]))
        w2_str = w2_str + "},"
    w2_str = w2_str + "]"
    return w2_str


def df2cl(df):
    w2_str = ""
    for c in df.columns:
        w2_str = w2_str + '"%s",' % (c)
    return w2_str


def w2_project(queryset):
    w2_str = "["
    for p in queryset:
        w2_str = w2_str + ('{"id":"%s","text":"%s"},' % (str(p.id), str(p)))
    w2_str = w2_str[0:-1] + "]"
    return w2_str
