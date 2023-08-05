# /usr/bin/env python
# -*- coding:utf-8 -*-
import json
import logging
import os
import sys

_ver = sys.version_info

is_py3 = (_ver[0] == 3)

# 域名后缀
file_path = os.path.dirname(__file__)
if is_py3:
    with open(os.path.join(file_path, 'domain_suffix.json'), 'r', encoding='utf8') as fr:
        DOMAIN_SUFFIX = json.load(fr)
    str_type = str
else:
    with open(os.path.join(file_path, 'domain_suffix.json'), 'r') as fr:
        DOMAIN_SUFFIX = json.load(fr, 'utf8')
    str_type = basestring

# 合法的英文域名字符
LEGAL_DOMAIN_CHARACTERS = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                           '.', '-'}

# 次级域名可以使用“_”
SECOND_LEGAL_DOMAIN_CHARACTERS = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
                                  '8', '9', '.', '-', '_'}

def encode_utf8(data):
    if isinstance(data, str_type):
        try:
            if is_py3:
                return data
            else:
                if isinstance(data, unicode):
                    return data.encode('utf8')
                return data
        except Exception as e:
            logging.debug('{data} str to utf8 failed. reason: {e}'.format(e=e, data=data))
            return data
    elif isinstance(data, dict):
        result = {}
        for k, v in data.items():
            result[encode_utf8(k)] = encode_utf8(v)
        return result
    elif isinstance(data, list):
        result = []
        for i in data:
            result.append(encode_utf8(i))
        return result
    else:
        raise TypeError('unsupported types: {data}'.format(data=data))


DOMAIN_SUFFIX = encode_utf8(DOMAIN_SUFFIX)

def encode_idna(data):
    """把字典里的数据编码成idna"""
    if isinstance(data, str_type):
        try:
            if is_py3:
                return str(data.lower().encode('idna'), 'utf8')
            else:
                return data.decode('utf8').lower().encode('idna')
        except Exception as e:
            logging.debug('{domain} str to idna failed. reason: {e}'.format(e=e, domain=data))
            return data
    elif isinstance(data, dict):
        result = {}
        for k, v in data.items():
            result[encode_idna(k)] = encode_idna(v)
        return result
    elif isinstance(data, list):
        result = []
        for i in data:
            result.append(encode_idna(i))
        return result
    else:
        raise TypeError('unsupported types: {data}'.format(data=data))


# 将域名后缀编码为 IDNA
DOMAIN_SUFFIX_IDNA = encode_idna(DOMAIN_SUFFIX)


def unify_period(fun):
    """
    域名中英文字符“.”和中文句号“。”完全等效, 这里把“。”改为 “.”
    :param fun:
    :return:
    """

    def wrapper(domain):
        try:
            return fun(domain.replace('。', '.'))
        except Exception as e:
            logging.debug('unknown error: {0}'.format(e))
            return False

    return wrapper


@unify_period
def verify_domain(domain):
    """
    验证域名
    :param domain: str python3, str python2
    :return: bool
    """
    try:
        if is_py3:
            temp_domain = str(domain.lower().encode('idna'), 'utf8')
        else:  # is_py2:
            temp_domain = domain.decode('utf8').lower().encode('idna')
    except Exception as e:
        logging.debug('{domain} str to idna failed. reason: {e}'.format(e=e, domain=domain))
        return False

    # 检查域名长度是否少于4 或超过 255
    if 255 < len(temp_domain) or len(temp_domain) < 4:
        logging.debug('domain: "{0}" length wrong'.format(domain))
        return False

    # 检查域名的每一个段是否合法
    temp_domain_segment = temp_domain.split('.')
    for segment in temp_domain_segment:
        # 检查域名段长度是否超过 63
        if 63 < len(segment):
            logging.debug('domain: "{0}" segment length wrong'.format(domain))
            return False
        # 检查域名段前后是否是 '-'
        if '-' == segment[0] or '-' == segment[-1]:
            logging.debug('domain: "{0}" hyphens wrong'.format(domain))
            return False
        # # 检查域名段的 '-' 是否连用, 国外可以连用
        # if '--' in segment:
        #     logging.debug('domain: "{0}" hyphens wrong'.format(domain))
        #
        #     return False

    # 检查是否是合法的后缀
    if temp_domain_segment[-1] not in DOMAIN_SUFFIX_IDNA.keys():
        logging.debug('domain: "{0}" suffix wrong'.format(domain))
        return False

    # 检查域名后缀是否有第二级
    suffix = '.{0}'.format('.'.join(temp_domain_segment[-1:]))
    if temp_domain_segment[-2] in DOMAIN_SUFFIX_IDNA[temp_domain_segment[-1]]:
        suffix = '.{0}'.format('.'.join(temp_domain_segment[-2:]))
        # 只是域名后缀的二段域名也是错误的
        # if domain == suffix.lstrip('.'):
        if temp_domain == suffix.lstrip('.'):
            logging.debug('domain: "{0}" wrong'.format(domain))
            return False

    # 检查是否是英文域名合法字符
    a = temp_domain[:-len(suffix)]
    temp_top_domain = '{0}{1}'.format(temp_domain[:-len(suffix)].split('.')[-1], suffix)
    if 0 < len(set(temp_top_domain) - LEGAL_DOMAIN_CHARACTERS):
        logging.debug('domain: "{0}" characters wrong'.format(domain))
        return False

    # 检查是否是英文域名合法字符， 二级域名开始接受“_”
    if 0 < len(set(temp_domain) - SECOND_LEGAL_DOMAIN_CHARACTERS):
        logging.debug('domain: "{0}" characters wrong'.format(domain))
        return False

    return True


@unify_period
def get_domain_suffix(domain):
    """
    获取域名后缀
    :param domain: str
    :return: str
    """
    # 检查域名是否为合法域名
    if not verify_domain(domain):
        logging.debug('wrong domain: {0}'.format(domain))
        return False

    temp_domain_segments = domain.lower().split('.')

    # 获取第二段域名后缀
    try:
        domain_suffix_list = DOMAIN_SUFFIX[temp_domain_segments[-1]]
    except KeyError:
        domain_suffix_list = DOMAIN_SUFFIX_IDNA[temp_domain_segments[-1]]

    # 检查域名后缀是否有第二级
    if temp_domain_segments[-2] in domain_suffix_list:
        return '.{0}'.format('.'.join(temp_domain_segments[-2:]))

    return '.{0}'.format(temp_domain_segments[-1])


@unify_period
def get_top_domain(domain):
    """
    获取顶级域名
    :param domain: str
    :return: str
    """

    # 获取域名后缀
    domain_suffix = get_domain_suffix(domain)
    if not domain_suffix:
        return False

    # 除域名后缀后的域名段
    temp_domain_segments = domain[:-len(domain_suffix)].lower().split('.')

    return '{0}{1}'.format(temp_domain_segments[-1], domain_suffix)


@unify_period
def get_multi_domain(domain):
    """
    获取子域名
    :param domain: str
    :return: list
    """
    # 获取域名后缀
    domain_suffix = get_domain_suffix(domain)
    if not domain_suffix:
        return False

    # 除域名后缀后的域名段
    temp_domain_segments = domain[:-len(domain_suffix)].lower().split('.')

    multi_domain_list = []
    count = 1
    while count <= len(temp_domain_segments):
        multi_domain_list.append('{0}{1}'.format('.'.join(temp_domain_segments[-count:]), domain_suffix))
        count += 1

    return multi_domain_list
