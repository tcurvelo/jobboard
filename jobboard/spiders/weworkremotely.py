# -*- coding: utf-8 -*-
import scrapy


class WeworkremotelySpider(scrapy.Spider):
    name = 'weworkremotely'
    allowed_domains = ['weworkremotely.com']
    start_urls = [
        'https://weworkremotely.com/categories/remote-programming-jobs'
    ]

    def parse(self, resp):
        jobs = resp.xpath('//*[@id="job_list"]/section/article/ul/li/a/@href')
        for job in jobs:
            yield resp.follow(job, self.parse_job)

    def parse_job(self, resp):
        return {
            'title': resp.css('.listing-header-container h1 ::text').extract_first(),
            'text': ''.join(
                resp.css( '.job .listing-container ::text').extract()
            ),
        }
