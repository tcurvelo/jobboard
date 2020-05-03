# -*- coding: utf-8 -*-
import scrapy


class PythonOrgSpider(scrapy.Spider):
    name = 'python_org'
    allowed_domains = ['python.org']
    start_urls = ['https://www.python.org/jobs/']

    def parse(self, response):
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page)

        for job in response.css('.list-recent-jobs li'):
            link = job.css('h2 a::attr(href)').get()
            yield response.follow(link, callback=self.parse_job)

    def parse_job(self, response):
        yield {
            'url': response.url,
            'title': response.css('.company-name::text').get(),
            'description': ''.join(response.css('.job-description ::text').getall()),
        }
