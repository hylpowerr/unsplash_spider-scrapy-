#-*- coding:utf-8 -*-
import scrapy,json
from unsplash.items import UnsplashItem
class UnsplashSpider(scrapy.Spider):

    name = 'unsplash'

    start_urls = ['http://unsplash.com/napi/feeds/home']

    # def start_requests(self):
    #     yield scrapy.Request(self.start_urls[0],callback=self.parse)
    def __init__(self):
        self.download_format = 'https://unsplash.com/photos/{}/download?force=true'

    def parse(self, response):
        # try:
        dic = json.loads(response.text)
        photos = dic['photos']
        next_page = dic['next_page']
        # print("next_page: %s" % dic['next_page'])
        for photo in photos :
            image_id = photo['id']
            item = UnsplashItem()
            item['image_ids'] = [image_id]
            image_url = self.download_format.format(image_id)
            item['image_urls'] = [image_url]
            yield item
        yield scrapy.Request(url=next_page,callback=self.parse)
        # except:
        #     print('error')
