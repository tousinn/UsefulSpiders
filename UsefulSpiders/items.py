# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field

class ParadaItem(Item):
    id = Field()
    baseid = Field()
    name = Field()
    state = Field()
    url = Field()
    col = Field()
    cat = Field()
    subcol = Field()
    subcat = Field()
    metal = Field()
    material = Field()
    color = Field()
    theme = Field()
    stone = Field()
    release = Field()
    price = Field()
    design = Field()
    newest = Field()
    pindex = Field()
    findex = Field()
    desc = Field()
    imageurl = Field()


