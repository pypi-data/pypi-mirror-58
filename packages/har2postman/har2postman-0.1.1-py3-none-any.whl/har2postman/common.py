import re
import json
import jsonpath


def load_har(har_path):
    """

    :param har_path:
    :return:
    """
    with open(har_path, 'r', encoding='utf-8') as har:
        var = json.loads(har.read())
        return jsonpath.jsonpath(var, '$.log.entries..request')


def save_postman_collection(file_path, postman_json):
    with open(file_path, 'w') as postman:
        postman.write(json.dumps(postman_json, indent=4, ensure_ascii=False))


def extract_path(url: str):
    if url.count('/') < 3 or (url.count('3') == 3 and url[-1] == '/'):
        # eg. https://www.baidu.com
        # eg. https://www.baidu.com/
        return []

    if url.find('?') != -1:
        url = url.split('?')[0]
    return re.search('//.+?/(.+)', url).group(1).split('/')


def extract_params(url):
    """
    :param url: (str) eg: https://www.baidu.com/wd?q=testerhome&encoding=utf-8
    :return:
        [
            {
                "key": "q",
                "value": "testerhome"
            },
            {
                 "key": "encoding",
                "value": "utf-8"
            }
        ]
    """
    if url.find('?') == -1:
        return []
    query = []
    query_list = url.split('?')[-1].split('&')
    for i in query_list:
        key, value = i.split('=')
        query.append({
            'key': key,
            'value': value
        })
    return query


def change_dict_key(har_dict):
    """

    :param har_dict: [
        {"name": "", "value": ""},
        ...
    ]
    :return: [
        {"key": "", "value": ""},
        ...
    ]
    """
    for header in har_dict:
        header['key'] = header.pop('name')
    return har_dict


def change_url(har_request):
    """
    :param har_request: {'url': 'https://www.baidu.com/s?wd=12345'}
    :return: {
        'protocol': https,
        'host': ['www', 'baidu', 'com'],
        'path': ['s'],
        'query': [
            {'key': 'wd', 'value': '12345'},
            ...
        ]
    }
    """

    url_tmp: str = har_request['url']

    # 提取协议 http || https
    protocol = re.search('(https*):', url_tmp).group(1)

    # 提取host
    host = re.search('://(.+[^/])/?', url_tmp).group(1).split('.')

    # 提取path
    path = extract_path(url_tmp)

    # 提取query
    query = extract_params(url_tmp)

    return {
        'protocol': protocol,
        'host': host,
        'path': path,
        'query': query
    }


def change_body(har_request):
    mime_type: str = jsonpath.jsonpath(har_request, '$.postData.mimeType')[0]

    if mime_type is None:
        return None

    if mime_type.find('form-data') != -1:
        return {'mode': 'formdata', 'formdata': change_dict_key(har_request['postData']['params'])}

    elif mime_type.find('x-www-form-urlencoded') != -1:
        return {'mode': 'urlencoded', 'urlencoded': change_dict_key(har_request['postData']['params'])}

    elif mime_type.find('json') != -1:
        return {
            'mode': 'raw',
            'raw': har_request['postData']['text']
        }

    else:
        raise Exception('无法识别:%s' % mime_type)
