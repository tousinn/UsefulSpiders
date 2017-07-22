import scrapy
import json
from UsefulSpiders.items import ParadaItem
class ParadaSpider(scrapy.Spider):
    name = "Parada"
    start_urls = ['http://www.pandora.net/en-nz/feeds/products/json/',]
    image_url = 'https://www.pandora.net/assets/content?sku={0}&format=jpg&width={1}&height={2}'
    def parse(self, response):
        parsed_json = json.loads(response.body)
        for product in parsed_json['data']['products']['product']:
            item = ParadaItem()
            item['id'] = product.get('@id')
            item['baseid'] = product.get('@baseid')
            item['name'] = product.get('@name')
            item['state'] = product.get('@state')
            item['url'] = product.get('@url')
            item['col'] = product.get('@col')
            item['cat'] = product.get('@cat')
            item['subcol'] = product.get('@subcol')
            item['subcat'] = product.get('@subcat')
            item['metal'] = product.get('@metal')
            item['material'] = product.get('@material')
            item['color'] = product.get('@color')
            item['theme'] = product.get('@theme')
            item['stone'] = product.get('@stone')
            item['release'] = product.get('@release')
            item['price'] = product.get('@price')
            item['design'] = product.get('@design')
            item['newest'] = product.get('@newest')
            item['pindex'] = product.get('@pindex')
            item['findex'] = product.get('@findex')
            item['desc'] = product.get('desc').get('#cdata-section')
            item['imageurl'] = self.image_url.format(item['id'],'400','400')
            yield item

