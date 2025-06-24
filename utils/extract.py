import datetime
import logging
import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess

class FashionStudioDicodingSpider(scrapy.Spider):
    name = "fashion_studio_spider"

    custom_settings = {
        "FEEDS": {"output.json": {"format": "json", "overwrite": True}},
        "USER_AGENT": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        ),
        "LOG_ENABLED": False
    }

    def start_requests(self):
        yield scrapy.Request(
            url="https://fashion-studio.dicoding.dev/?page=1",
            callback=self.parse
        )

    def parse(self, response, **kwargs):
        timestamp = datetime.datetime.now().isoformat()
        collection_cards = response.css("div.collection-card")

        for card in collection_cards:
            try:
                title = card.css("h3.product-title::text").get()
                price = card.css("span.price::text").get()
                rating = card.css("div.product-details > p:nth-child(3)::text").get()
                colors = card.css("div.product-details > p:nth-child(4)::text").get()
                size = card.css("div.product-details > p:nth-child(5)::text").get()
                gender = card.css("div.product-details > p:nth-child(6)::text").get()

                yield {
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Colors": colors,
                    "Size": size,
                    "Gender": gender,
                    "timestamp": timestamp
                }
            except Exception as e:
                self.logger.error("Error processing card: %s", e)
                continue

        next_page = response.css("li.page-item.next > a.page-link::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


def extract():
    try:
        process = CrawlerProcess()
        process.crawl(FashionStudioDicodingSpider)
        process.start()

        try:
            df = pd.read_json("output.json")
            return df
        except Exception as e:
            logging.error("Failed to load output.json: %s", e)
            return pd.DataFrame()

    except Exception as e:
        logging.critical("Scrapy process failed: %s", e)
        return pd.DataFrame()
