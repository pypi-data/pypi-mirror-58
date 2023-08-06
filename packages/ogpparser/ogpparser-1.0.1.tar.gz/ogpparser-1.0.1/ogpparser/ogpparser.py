import requests
from bs4 import BeautifulSoup

def ogpparser(url):
    '''
    url : input URL to parse
    '''
    response = requests.get(url)
    response.encoding = response.apparent_encoding
 
    bs = BeautifulSoup(response.text, 'html.parser')
    
    result = {}
    for header in bs.find_all('head'):
        meta_list = header.find_all('meta')
        for meta in meta_list:
            if meta.has_attr('property'):
                if meta['property'][:3]=='og:':
                    tag = meta['property'].strip('og:')
                    content = meta['content'].strip()
                    if tag not in result.keys():
                        result[tag] = content
                    else:
                        if type(result[tag])==str:
                            result[tag] = [result[tag]]
                            result[tag].append(content)
                        else:
                            result[tag].append(content)
    
    return result