def normalize_url(url):
    start_url = len('http://')
    if url[:start_url] == 'http://':
        return 'https://{}'.format(url[start_url:])
    else:
        return url


print(normalize_url('http://ya.ru'))
