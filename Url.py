def domain_name(url):
    url1 = url.split('.')
    if 'www' in url:
        print(url1)
        return url1[1]
    else:
        return url1[0].split('//')[1]
