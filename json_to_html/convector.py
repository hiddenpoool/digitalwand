import json
b = {
    'title': '<h1>%s</h1>',
    'body': '<p>%s</p>',

}
def main():
    path = 'source.json'
    with open(path,'r') as f:
        text = json.loads(f.read())
        print(text)
    a = str()
    for i in text:
        for  p in i.keys():
            if p in b.keys():
                a = a + b[p] % i[p]
    print(a)
    print('<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World2!</p>' == a)

    return 0


if __name__ == '__main__':
    main()