import scrapy

from unidecode import unidecode
import json


class UpworkSpider(scrapy.Spider):
    name = 'upwork_spider'

    start_urls = [
        'https://www.upwork.com/o/jobs/browse/?amount=500,100000&contractor_tier=2,3&sort=create_time%2Bdesc&workload=full_time,none']

    def parse(self, response):
        filename = '/home/yml/Documents/Stuff/Defrag/Templates/project_scraper/spiders/data/data1.html'
        with open(filename, 'wb') as f:
            data = response.xpath('//script[@type="text/javascript"]/text()').re(r'(?<=var phpVars \= ).*}(?=;)')
            data = unidecode(data[0])
            f.write(data)
            # f.write(response.body)
        # product_panels = response.xpath(
        #     '//div[@id="product_rows"]//div[@class="product_wrap"]')
        # for panel in product_panels:
        #     product_page = panel.xpath('.//a[contains(@href, "/product/")]/@href').extract_first()
        #     yield scrapy.Request(product_page, callback=self.parse_product_page)

    # def parse_product_page(self, response):
    #     title = response.xpath('//h2[@itemprop="name"]/text()').extract_first()
    #     price = response.xpath('//span[@itemprop="price"]/@content').extract_first()
    #     image = response.xpath('//div[@id="product_image"]//img/@src').extract_first()
    #     long_description = response.xpath('//div[@id="prod_desc"]/p/text()').extract_first()
    #     attributes = response.xpath('//div[@id="prod_feature"]').extract_first()
    #     attributes = attributes.split('\n')
    #     if len(attributes) > 1:
    #         attributes = attributes[1:len(attributes) - 1]
    #     attributes = [{
    #         'name': re.search(r'(?<=strong"\>).*(?=\<\/span\>)', attribute).group(),
    #         'value': re.search(r'(?<=\<\/span\>\s:\s).*(?=\<br\>)', attribute).group()}
    #         for attribute in attributes]
    #     # Convert attributes in json string
    #     attributes = json.dumps(attributes)
    #     yield {
    #         'title': title,
    #         'productUrl': response.url,
    #         'category': CATEGORY.id,
    #         'price': price,
    #         'image': image,
    #         'shortDescription': '',
    #         'longDescription': long_description,
    #         'attributeData': attributes}
