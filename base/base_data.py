import yaml
import  os

def data_file(filename,datakey):
    list_data=[]
    with open("."+ os.sep +"data"+ os.sep + filename,"r",encoding="UTF-8")as f:
        data1=yaml.load(f)
        data2=data1[datakey]
        for i in data2.values():
            list_data.append(i)
    return list_data

