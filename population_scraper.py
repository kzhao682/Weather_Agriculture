import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector



class PopSpider(scrapy.Spider):
    name = "population"
    start_urls = ["http://www.multpl.com/united-states-population/table"]

    def parse(self, response):
        SECTION_SELECTOR = response.xpath('//tr')
        for section in SECTION_SELECTOR:

            YEAR_SELECTOR = './/td[@class = "left"]/text()'
            POPULATION_SELECTOR = './/td[@class = "right"]/text()'
            #COMMODITY_SELECTOR = './/td[16]/text()'
            #YIELD_SELECTOR = './/td[20]/text()'

            yield {
                'Year': section.xpath(YEAR_SELECTOR).extract(),
                'Population': section.xpath(POPULATION_SELECTOR).extract(),
                #'Commodity': crop.xpath(COMMODITY_SELECTOR).extract_first(),
                #'Yield': crop.xpath(YIELD_SELECTOR).extract_first()
            }



        #NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        #next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        #if next_page:
        #    yield scrapy.Request(
        #        response.urljoin(next_page),
        #        callback=self.parse
        #    )
