import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
class EC2_faq(scrapy.Spider):
    name = 'ec2'
    start_urls = ['https://aws.amazon.com/ec2/faqs/']
    def parse(self, response):
        response_aux = response.css('p')[1:]
        for i in range(0,len(response_aux) - 1,1):
            if ((response_aux[i].css('p').css('b::text').get()) != None) and ((response_aux[i].css('p').css('b::text').get()[0])=='Q'):
                answer = ''
                question = response_aux[i].css('p').css('b::text').get()
                while True:
                    i = i + 1
                    answer = answer + response_aux[i].css('p').get() + ' '
                    if ((response_aux[i + 1].css('p').css('b::text').get()) != None) and ((response_aux[i + 1].css('p').css('b::text').get()[0])=='Q'):
                        yield {
                            'Question': question
                                        .replace('\u00a0',' ')
                                        .replace('\u00ae','')
                                        .replace('\u201c','\'')
                                        .replace('\u201d','\'')
                                        .replace('\u2013','-')
                                        .replace('\u2018','-')
                                        .replace('\u2019','\''),
                            'Answer': (BeautifulSoup(answer, "lxml").text)
                                        .replace('\u00a0',' ')
                                        .replace('\u00ae','')
                                        .replace('\u201c','\'')
                                        .replace('\u201d','\'')
                                        .replace('\u2013','-')
                                        .replace('\u2018','-')
                                        .replace('\u2019','\'')
                            }
                        break
