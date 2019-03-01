# -*- coding: utf-8 -*-

def cfg_parser():
    import json
    with open('deepblue_selector.cfg') as f:
        config_text = f.read().decode('utf-8-sig').replace('\\', '\\\\')
        config_dict = json.loads(config_text)
    return config_dict


def projects_list():
    data = cfg_parser()
    values = []
    for key, value in data['projects_list'].items():
        values.append(value)
    values.sort()
    return values


def get_project_propertys(name):
    data = cfg_parser()
    project = ''
    values = {}
    # get project name by value
    for key, value in data['projects_list'].items():
        if value == name:
            project = key 
    for key, value in data[project].items():
        values[key] = value
    return values


def run_project(name):
    import subprocess
    data = get_project_propertys(unicode(name))
    run_file = data['execute']
    propertys_file = data['prprtfile']
    for prop in data.items():
        update_deepblue_config(prop, propertys_file)
    subprocess.Popen(run_file)

def update_deepblue_config(prop, propertys_file):
    filedata = ""
    # Read Data
    with open(propertys_file, 'r') as f:
        for row in f.readlines():
            line = row.split('=')
            if line[0] == prop[0]:
                row = row.replace(line[1], "S" + prop[1] + '\n')
            filedata += row
    with open(propertys_file, 'w') as f: f.write(filedata)

