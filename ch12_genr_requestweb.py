"""A simple program to illustrate the difference between listcomps and generators."""
import requests

urls = ('http://gamespot.com', 'http://oglaf.com', 'http://ranajayontheroad.com')

print('Using a [Listcomp]:')
for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), '->', resp.status_code, '->', resp.url)


print('\nUsing a (Generator):')
for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)


print('\nNow the same thing using a (Generator) function:')


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url       # Use yield instead of return


for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, status, url, sep=' -> ')
