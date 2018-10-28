# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re


def extract_links(raw_url,document,include_pattern = None,exclude_pattern=None):
    dom = BeautifulSoup(document, 'html.parser')
    links = dom.find_all("a")
    protocol_path = raw_url.split("//")
    domain_resource = protocol_path[1].split("/")

    prefix = protocol_path[0]+"//"+domain_resource[0]
    include_p = None
    exclude_p = None
    if include_pattern:
        include_p = re.compile(include_pattern)
    if exclude_pattern:
        exclude_p = re.compile(exclude_pattern)

    returns = []
    for link in links:
        href = link.get("href")
        if href is None or href.startswith("javascript"):
            continue
        if href.startswith("/"):
            href = prefix+'/'+href
        if exclude_p is not None and exclude_p.match(href):
            continue
        if include_p is None or include_p.match(href):
            returns.append(href)
    return returns