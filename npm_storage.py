import os
import numpy as np

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

def uneven_list(ls):
    uneven_list = []
    for i in ls:
        # print(ls.index(i))
        if ls.index(i) % 2 == 0:
            uneven_list.append(i)
        else :
            continue
    return uneven_list

serverPath = "./server/package.json"
clientPath = "./client/package.json"

def download_npm(path,start_dep,end_dep):
    print("plase make sure your Verdaccio server is set before starting")
    hostname = input("enter your ip address or hostname >>>")
    os.system('npm set registry http://{0}:4873'.format(hostname))
# with open('./server/package.json') as f: s = f.read()
    contents = open(path).read().splitlines()
    # print(contents[14:38])
    dep = contents[start_dep-1:end_dep-1]
    res = map(lambda x: x.split(":"), dep)
    # print( flatten_list(list(res)))
    count = 0
    result = flatten_list(list(res))
    result = uneven_list(result)
    # print(result)
    added = []
    failed = []
    for item in result :
        os.system('npm i --legacy-peer-deps {0}'.format(item))
        # os.system('npm i ${item}')
    os.system('npm config set registry https://registry.npmjs.org/')
    print ("your registry was set back to  default")
# mybe use the npx download-tgz package-json package.json insed
download_npm(serverPath,15,40)