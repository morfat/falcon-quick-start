#implement pagination wrapper classes here

from urllib import parse

from collections import OrderedDict

def get_next_link(url,page,offset,limit,count):
    if offset + limit >= count:
        return None
    page=page+1
    return replace_query_param(url, 'page', page)

def get_previous_link(url,page,offset,limit):
    if offset <= 0:
        return None
    page=page-1
    if offset - limit <= 0:
        return remove_query_param(url, 'page')
    return replace_query_param(url, 'page', page)

def replace_query_param(url, key, val):
    """
    Given a URL and a key/val pair, set or replace an item in the query
    parameters of the URL, and return the new URL.
    """
    (scheme, netloc, path, query, fragment) = parse.urlsplit(url)
    query_dict = parse.parse_qs(query, keep_blank_values=True)
    query_dict[str(key)] = [val]
    query = parse.urlencode(sorted(list(query_dict.items())), doseq=True)
    return parse.urlunsplit((scheme, netloc, path, query, fragment))

def remove_query_param(url, key):
    """
    Given a URL and a key/val pair, remove an item in the query
    parameters of the URL, and return the new URL.
    """
    (scheme, netloc, path, query, fragment) = parse.urlsplit(url)
    query_dict = parse.parse_qs(query, keep_blank_values=True)
    query_dict.pop(key, None)
    query = parse.urlencode(sorted(list(query_dict.items())), doseq=True)
    return parse.urlunsplit((scheme, netloc, path, query, fragment))

def get_paginated_response(url,page_size,page,offset,limit,count):
    return OrderedDict([('count', count),('page_size',page_size),('next', get_next_link(url,page,offset,limit,count)),
                        ('previous', get_previous_link(url,page,offset,limit)),
                        ])