import re
with open('xpathprocess.html','r') as f:
    origin = f.read()
    slice = origin.split('</td>')
    w = []
    for i in slice:
        if 'contenteditable' in i:
            t = re.findall(r"true\"\>(.+?)$", i)
            if len(t) > 0:
                print(t[0])
                w.append(t[0])
    print(w)
    with open('processxpathresult.txt','a') as p:
        for u in w:
            p.write(u + '\n')