# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from unsplash import settings
import os
import requests
class UnsplashPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:

            if not os.path.exists(settings.IMAGES_STORE):
                os.makedirs(settings.IMAGES_STORE)
            for index in range(len(item['image_urls'])):
                image_url = item['image_urls'][index]
                image_id = item['image_ids'][index]
                file_name = image_id+'.jpg'
                file_path = settings.IMAGES_STORE+'/'+file_name
                # 保存图片
                with open(file_path,'wb') as f:
                    response = requests.get(image_url,headers = settings.DEFAULT_REQUEST_HEADERS,verify=False)
                    for chunk in response.iter_content(1024):
                        if not chunk:
                            break
                        f.write(chunk)
                item['image_paths'] = [file_path]


        return item
