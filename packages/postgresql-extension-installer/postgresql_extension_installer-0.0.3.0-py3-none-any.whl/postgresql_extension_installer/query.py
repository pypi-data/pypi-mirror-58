import os
import re
import json

###############
# GET
###############

def get_provider_from(query):
    if "info" in query:
        if "provider" in query["info"]:
            return query["info"]["provider"]
    return []

def get_version_from(query):
    if "info" in query:
        if "version" in query["info"]:
            return query["info"]["version"][0]
    return ""

def get_package_name_from(query):
    if "info" in query:
        if "name" in query["info"]:
            return query["info"]["name"][0]
    return ""

def get_key_name_from(low_key):
    if low_key:
        return low_key.replace("--","").replace(">","").replace("<","").lower()
    return ""

def get_sub_key_data_from(low_data_stack):
    sub_data = {}
    key = low_data_stack[0][1]
    while low_data_stack:
        item = low_data_stack.pop()
        if item[0] == 0:
            if key == "info":
                item[2] = item[2].split("\n")
                del item[2][-1]
            sub_data.update({item[1]:item[2]})
        elif item[0] == 1:
            return item[1], sub_data

def get_query_from(path):
    data = {}
    if os.path.isfile(path) is True:
        f = open(path, 'r')
        line = f.readline()

        stack = []
        key_re = re.compile("--[<|>]([A-Z|a-z|_])+[<|>]--")        
        data = {}

        while line:
            line = line.replace("\n","")
            if key_re.match(line) is not None:
                if line[2] == '>':
                    if stack:
                        sub_key_data = get_sub_key_data_from(stack)
                        data.update({sub_key_data[0]:sub_key_data[1]})
                    stack.append([1, get_key_name_from(line),""])
                else:
                    stack.append([0, get_key_name_from(line),""])
            else:
                if stack:
                    stack[-1][-1] += line +"\n"
                else:
                    break
            line = f.readline()
        if stack:
            sub_key_data = get_sub_key_data_from(stack)
            data.update({sub_key_data[0]:sub_key_data[1]})
        f.close()
    return data

def get_lib_from(query):
    if "info" in query:
        if "lib" in query["info"]:
            return query["info"]["lib"]
    return []

###############
# SQL
###############

def install_sql(plpy, query):
    name = get_package_name_from(query)
    SQL = ""+\
        "INSERT INTO m_installer_information(version, sql, name) "+\
            "VALUES($1, $2, $3);"
    plan = plpy.prepare(SQL, ["text","json","text"])
    plpy.execute(plan,[get_version_from(query), json.dumps(query), name])

def uninstall_sql(plpy, query):
    name = get_package_name_from(query)
    SQL = ""+\
        "DELETE FROM m_installer_information "+\
            "WHERE name=$1;"
    plan = plpy.prepare(SQL, ["text"])
    plpy.execute(plan,[name])

def update_sql(plpy, query):
    SQL = ""+\
        "UPDATE m_installer_information "+\
            "SET version=$1, sql=$2 "+\
                "WHERE name=$3;"
    plan = plpy.prepare(SQL, ["text","json","text"])
    plpy.execute(plan,[get_version_from(query), json.dumps(query), get_package_name_from(query)])

###############
# KEY
###############

def install_from_key(plpy, query, key):
    if key in query:
        sub_keys = list(query[key].keys())
        sub_keys.reverse()
        for sub_key in sub_keys:
            plpy.execute(query[key][sub_key])
        return True
    return False

def uninstall_from_key(plpy, query, key):
    if key in query:
        for sub_key in query[key]:
            SQL = "DROP " + key + " IF EXISTS " + sub_key + " CASCADE;"
            try:
                plpy.execute(SQL)
            except:
                pass
        return True
    return False

def update_from_key(plpy, old_query, new_query, key):
    old_verison = get_version_from(old_query)
    new_verison = get_version_from(new_query)
    if old_verison != new_verison:
        uninstall_from_key(plpy, old_query, key)
        install_from_key(plpy, new_query, key)

###############
# ACTION
###############

def install(plpy, query):
    for key in query:
        if key != 'info':
            install_from_key(plpy, query, key)
    return True

def uninstall(plpy, query):
    for key in query:
        if key != 'info':
            uninstall_from_key(plpy, query, key)
    return True

def update(plpy, old_query, new_query):
    old_verison = get_version_from(old_query)
    new_version = get_version_from(new_query)
    if old_verison != new_version:
        uninstall(plpy, old_query)
        install(plpy, new_query)
    return True

###############
# MAIN
###############

if __name__ == "__main__":
    import os
    base_file = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/default.py"

    query = get_query_from(base_file)

    print(get_provider_from(query))
    print(get_version_from(query))
