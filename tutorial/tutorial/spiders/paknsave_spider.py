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

    def parse(self, response):
        for card in response.css('div.fs-product-card'):
            footer_raw = " ".join(card.css('div.fs-product-card__footer-container::attr(data-options)'
                                           ).get().strip().split())
            footer_json = json.loads(footer_raw)

            yield {

                'title': str(card.css('h3.u-p2::text').get()).strip(),
                'unit': str(card.css('p.u-p3::text').get()).strip(),
                'link': 'https://www.paknsaveonline.co.nz' + str(card.css('a.fs-product-card__details::attr(href)').get()).strip(),
                'img_link': str(card.css('div.fs-product-card__product-image::attr(data-src-s)').get()).strip(),

                'productId': str(footer_json["productId"]).strip(),
                'productName': str(footer_json["productName"]).strip(),
                'productVariants': str(footer_json["productVariants"]).strip(),
                'restricted': str(footer_json["restricted"]).strip(),
                'tobacco': str(footer_json["tobacco"]).strip(),
                'liquor': str(footer_json["liquor"]).strip(),
                'BoozeGateConfirmationHeader': str(footer_json["BoozeGateConfirmationHeader"]).strip(),
                'BoozeGateConfirmationBody': str(footer_json["BoozeGateConfirmationBody"]).strip(),
                'loginRegisterModalTitle': str(footer_json["loginRegisterModalTitle"]).strip(),
                'loginRegisterBodyCopy': str(footer_json["loginRegisterBodyCopy"]).strip(),
                'ProductDetails': str(footer_json["ProductDetails"]).strip(),
                'PricePerItem': str(footer_json["ProductDetails"]["PricePerItem"]).strip(),
            }
