import json

fileJSON = 'api1.json'

# Opening JSON file
def openJSON():
    data = {}
    with open(fileJSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def get_link_img():
    data = openJSON()
    listMSV = []
    for s in data['sinhvien']:
        listMSV.append(s)
    return listMSV

def data_by_key(keyDict):
    data = openJSON()
    return data[keyDict]

def get_msv_by_class(classID):
    dsmsv = []
    for item in data_by_key('dslop'):
        if item['MaLop'] == classID:
            dsmsv.append(item['MaSV'])
    return dsmsv

def get_sv_by_class(classID):
    dsmsv = []
    dssv = []
    for item in data_by_key('dslop'):
        if item['MaLop'] == classID:
            dsmsv.append(item['MaSV'])
    for item in data_by_key('sinhvien'):
        if item['MaSV'] in dsmsv:
            dssv.append(item)
    return dssv

def get_baocao_by_class(classID):
    dsmsv = []
    
    dssv = []
    for item in data_by_key('baocao'):
        if item['MaLop'] == classID:
            dsmsv.append(item['MaSV'])
    for item in data_by_key('sinhvien'):
        if item['MaSV'] in dsmsv:
            dssv.append(item)
    return dssv

def get_baocao_all_class(classID):
    dssv = []
    for item in data_by_key('baocao_all'):
        if item['MaLop'] == classID:
            dssv.append(item)
    return dssv

def get_sv_by_msv(msv):
    data = openJSON()
    for s in data['sinhvien']:
        if s['MaSV'] == msv:
            return s

