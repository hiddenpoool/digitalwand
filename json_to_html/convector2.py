import json
b = []
def main():
    path = 'source.json'
    with open(path,'r') as f:
        text = json.loads(f.read())
        print(text)
    a = str()
    for i in text:
        for  p in i.keys():
            a = '%s<%s>%s</%s>' %(a,p,i[p],p)
    print(a)
    print('<h3>Title #1</h3><div>Hello, World 1!</div>' == a)

    return 0


if __name__ == '__main__':
    main()