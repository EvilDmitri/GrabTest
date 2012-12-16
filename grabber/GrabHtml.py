# coding=utf-8
__author__ = 'dimas'

from grab import Grab

import random

def grab_quote(address='http://bash.im/'):
    g = Grab()
    g.go(address)

    # Составляем список, содержащий все цитаты
    ListOfQuotes = g.xpath_list('//div[@class="text"]')

    RandomQuote = ListOfQuotes[random.randint(1,len(ListOfQuotes))]

    for child in RandomQuote.getchildren():
        if child.tag == "br":
            child.text = "\n"


    return RandomQuote.text_content()




