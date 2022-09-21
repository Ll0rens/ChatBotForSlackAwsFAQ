import scrapy
from scrapy.selector import Selector
from bs4 import BeautifulSoup
class EC2_faq(scrapy.Spider):
    name = 'ec2'
    start_urls = ['https://aws.amazon.com/ec2/faqs/']
    def parse(self, response):
        response_aux = response.css('p')[1:]
        for i in range(0,len(response_aux) - 1,1):
            if (response_aux[i].css('p').css('b::text').get()) != None:
                answer = ''
                question = response_aux[i].css('p').css('b::text').get()
                while True:
                    i = i + 1
                    answer = answer + response_aux[i].css('p').get() + '\n'
                    if (response_aux[i + 1].css('p').css('b::text').get()) != None:
                        yield {
                            'Question': question,
                            'Answer': BeautifulSoup(answer, "lxml").text
                            }
                        break
