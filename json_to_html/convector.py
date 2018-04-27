import json
b = {
    'title': '<h1>%s</h1>',
    'body': '<p>%s</p>',
    'h3': '<h3>%s</h3>',
    'div': '<div>%s</div>'

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
    print('<h3>Title #1</h3><div>Hello, World 1!</div>' == a)

    return 0


if __name__ == '__main__':
    main()