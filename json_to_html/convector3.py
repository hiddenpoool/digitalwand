import json
def abc(arg):
    a = ''
    for p in arg.keys():
        a += '<%s>%s</%s>' % ( p, arg[p], p)
    return a

def pars(arg):
    a = ''
    for  i in arg:
        for p in i.keys():
            a = '%s<%s>%s</%s>' % (a, p, i[p], p)
    return a

def pars1(arg, rrr):
    a = ''
    for i in arg:
        if rrr :
            a += '<li>%s</li>' % abc(i)
        else:
            a +=  abc(i)
    return a

def func(arg):
    a = str()
    is_list = type(arg) is list
    if is_list:
        a += '<ul>%s</ul>' % pars1(arg, is_list)

    else:
        a += pars1(arg, is_list)
    return a


def main():
    path = 'source.json'
    with open(path,'r') as f:
        text = json.loads(f.read())
    out = '<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li><li><h3>Title #2</h3><div>Hello, World 2!</div></li></ul>'
    result = func(text)
    print(out == result)
    return 0


if __name__ == '__main__':
    main()