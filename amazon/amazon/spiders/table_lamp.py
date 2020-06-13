# -*- coding: utf-8 -*-
import scrapy

class TableLampSpider(scrapy.Spider):
    name = 'table_lamp'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=table+lamp&ref=nb_sb_noss']
    
    def parse(self, response):
        titles = response.xpath("//div[@class='a-section a-spacing-none a-spacing-top-small']//span[@class='a-size-base-plus a-color-base a-text-normal']/text()").extract()
        hrefs = response.xpath("//div[@class='a-section a-spacing-none a-spacing-top-small']//a[@class='a-link-normal a-text-normal']/@href").extract()
        prices = response.xpath("//span[@class='a-price']/span[@class='a-offscreen']/text()").extract()

        for item in zip(titles, hrefs, prices):
            yield {
                "title":item[0],
                "url":item[1],
                "price":item[2]
                }
        
    #     next_page=response.xpath('//a[@id="pagnNextLink"]/@href').extract_first()
        
    #     if next_page!=None:
    #         next_url='https://www.amazon.com'+next_page
    #         yield Request(next_url)