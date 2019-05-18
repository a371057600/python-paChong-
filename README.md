# python-paChong-
我是一个可爱的简书爬虫项目,简陋但是有效,低效但是稳定.
把
pipline.py中的数据库改成你的数据库哦,详情操作,请自己去百度找SCRAPY的数据库连接教程,非常简单
#这里记得改成你自己的数据库,不然你爬起来会不停地出错哦.

2019.5.17号的小修改
pipline.py中添加了异步下载数据到数据库
class JianshuTwistedPipeline(object):

并且更改了setting内的
ITEM_PIPELINES = {
   # 'jianshu_spider.pipelines.JianshuSpiderPipeline': 300,
   'jianshu_spider.pipelines.JianshuTwistedPipeline': 300,
}
把原本的JianshuSpiderPipeline慢速爬虫，替换成了JianshuTwistedPipeline的异步爬虫

# 5月18日更新了把所有的字段都爬到了数据库,数据库的字节最好都用varchar不然,爬阅读数,点赞数的时候你会爆炸的,亲测,只要替换网址就能用到很多网站.