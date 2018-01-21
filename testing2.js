    url = 'http://api.yomomma.info/'
    r = requests.get(url)

    datastore = json.loads(r.text)

    print datastore