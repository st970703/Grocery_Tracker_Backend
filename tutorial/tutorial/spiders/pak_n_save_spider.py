import scrapy
import json
from scrapy.http import Request


class PakNSaveSpider(scrapy.Spider):
    name = "paknsave"

    base_urls = [
        "https://www.paknsaveonline.co.nz/category/fresh-foods-and-bakery?pg=",
        "https://www.paknsaveonline.co.nz/category/chilled-frozen-and-desserts?pg=",
        "https://www.paknsaveonline.co.nz/category/pantry?pg=",
        "https://www.paknsaveonline.co.nz/category/drinks?pg=",
        "https://www.paknsaveonline.co.nz/category/beer-cider-and-wine?pg=",
        "https://www.paknsaveonline.co.nz/category/personal-care?pg=",
        "https://www.paknsaveonline.co.nz/category/baby-toddler-and-kids?pg=",
        "https://www.paknsaveonline.co.nz/category/pets?pg=",
        "https://www.paknsaveonline.co.nz/category/kitchen-dining-and-household?pg=",
    ]

    start_urls = []

    for url in base_urls:
        for i in range(1, 56, 1):
            start_urls.append(url + str(i))

    # def start_requests(self, URL=base_url):
    #     for i in range(1, 56, 1):
    #         yield Request(url=URL + str(i), callback=self.parse)

    def parse(self, response):
        for card in response.css('div.fs-product-card'):
            footer_raw = " ".join(card.css('div.fs-product-card__footer-container::attr(data-options)'
                                           ).get().strip().split())
            footer_json = json.loads(footer_raw)

            yield {
                'title': card.css('h3.u-p2::text').get(),
                'unit': card.css('p.u-p3::text').get(),
                'link': 'https://www.paknsaveonline.co.nz' + card.css('a.fs-product-card__details::attr(href)').get(),
                'img_link': card.css('div.fs-product-card__product-image::attr(data-src-s)').get(),
                'footer_json': footer_json,
                'productId': footer_json["productId"],
                'productName': footer_json["productName"],
                'productVariants': footer_json["productVariants"],
                'restricted': footer_json["restricted"],
                'tobacco': footer_json["tobacco"],
                'liquor': footer_json["liquor"],
                'BoozeGateConfirmationHeader': footer_json["BoozeGateConfirmationHeader"],
                'BoozeGateConfirmationBody': footer_json["BoozeGateConfirmationBody"],
                'loginRegisterModalTitle': footer_json["loginRegisterModalTitle"],
                'loginRegisterBodyCopy': footer_json["loginRegisterBodyCopy"],
                'ProductDetails': footer_json["ProductDetails"],
                'PricePerItem': footer_json["ProductDetails"]["PricePerItem"],
            }

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)