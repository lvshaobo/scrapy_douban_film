# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WarcraftPipeline(object):

    def process_item(self, item, spider):
        with open('title.txt', 'w+') as file:
            title = item['title']
            comment = item['comment']
            file.write("title:" + str(title) + '\n\n')
            i = 1
            for tag in comment:
                file.write("comment" + str(i) + ":" + str(tag.get_text()) + '\n\n')
                i = i + 1
        return item

