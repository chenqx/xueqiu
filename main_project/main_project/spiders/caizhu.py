# http://www.caixunzz.com/ scrapy this website.

import json
import re
from scrapy.selector import Selector

try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider

#from main_project.items import *
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


# from main_project.misc.log import *

class DmozSpider(scrapy.spiders.Spider):
    name = "caixunzz"
    allowed_domains = ["caixunzz.com"]
    start_urls = ["http://www.caixunzz.com"]

    #rules = [Rule(sle(allow=("/position.php\?&start=\d{,4}#a")), follow=True, callback='parse_item')]

    '''
    def parse(self,response):
        filename=response.url.split('/')[-2]
        with open(filename,'wb') as f:
            f.write(response.body)
    '''

