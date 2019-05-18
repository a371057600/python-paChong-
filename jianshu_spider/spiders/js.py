# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import ArticleItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//a[@class='avatar']/img/@src").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get().replace("*","")
        # https://www.jianshu.com/p/d30d0f91554a?utm_campaign=maleskine&utm_content=note&utm_medium=pc_all_hots&utm_source=recommendation
        # https://www.jianshu.com/p/d30d0f91554a
        url = response.url
        # ['https://www.jianshu.com/p/d30d0f91554a','utm_campaign=maleskine&utm_content=note&utm_medium=pc_all_hots&utm_source=recommendation']
        # ['https://www.jianshu.com/p/d30d0f91554a']
        url1 = url.split("?")[0]
        article_id = url1.split('/')[-1]

        content = response.xpath("//div[@class='show-content']").get()

        word_count = response.xpath("//span[@class='wordage']/text()").get()
        comment_count = response.xpath("//span[@class='comments-count']/text()").get()
        read_count = response.xpath("//span[@class='views-count']/text()").get()
        like_count = response.xpath("//span[@class='likes-count']/text()").get()

        subjects = ",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())

        item = ArticleItem(
            title=title,
            avatar=avatar,
            author = author,
            pub_time = pub_time,
            origin_url = response.url,
            article_id = article_id,
            content = content,
            subjects = subjects,
            word_count = word_count,
            comment_count = comment_count,
            read_count = read_count,
            like_count = like_count
        )
        yield item
