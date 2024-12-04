
import asyncio  
import time  
import yaml  
import os  

# TikTokAPI
from crawlers.base_crawler import BaseCrawler
from crawlers.tiktok.endpoints import TikTokAPIEndpoints
from crawlers.utils.utils import extract_valid_urls

# TikTok
from crawlers.tiktok.utils import (
    AwemeIdFetcher,
    BogusManager,
    SecUserIdFetcher,
    TokenManager
)

# TikTok
from crawlers.tiktok.models import (
    UserProfile
)


path = os.path.abspath(os.path.dirname(__file__))

with open(f"{path}/config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)


class TikTokWebCrawler:

    def __init__(self):
        self.proxy_pool = None

    async def get_tiktok_headers(self):
        tiktok_config = config["TokenManager"]["tiktok"]
        kwargs = {
            "headers": {
                "User-Agent": tiktok_config["headers"]["User-Agent"],
                "Referer": tiktok_config["headers"]["Referer"],
                "Cookie": tiktok_config["headers"]["Cookie"],
            },
            "proxies": {"http://": tiktok_config["proxies"]["http"],
                        "https://": tiktok_config["proxies"]["https"]}
        }
        return kwargs


    """-------------------------------------------------------utils-------------------------------------------------------"""

    # msToken
    async def fetch_real_msToken(self):
        result = {
            "msToken": TokenManager().gen_real_msToken()
        }
        return result

    # ttwid
    async def gen_ttwid(self, cookie: str):
        result = {
            "ttwid": TokenManager().gen_ttwid(cookie)
        }
        return result

    # xbogus
    async def gen_xbogus(self, url: str, user_agent: str):
        url = BogusManager.xb_str_2_endpoint(user_agent, url)
        result = {
            "url": url,
            "x_bogus": url.split("&X-Bogus=")[1],
            "user_agent": user_agent
        }
        return result

    # id
    async def get_sec_user_id(self, url: str):
        return await SecUserIdFetcher.get_secuid(url)

    # id
    async def get_all_sec_user_id(self, urls: list):
        # URL
        urls = extract_valid_urls(urls)

        # URL
        return await SecUserIdFetcher.get_all_secuid(urls)

    # id
    async def get_aweme_id(self, url: str):
        return await AwemeIdFetcher.get_aweme_id(url)

    # id
    async def get_all_aweme_id(self, urls: list):
        # URL
        urls = extract_valid_urls(urls)

        # URL
        return await AwemeIdFetcher.get_all_aweme_id(urls)

    # unique_id
    async def get_unique_id(self, url: str):
        return await SecUserIdFetcher.get_uniqueid(url)

    # unique_id
    async def get_all_unique_id(self, urls: list):
        # URL
        urls = extract_valid_urls(urls)

        # URL
        return await SecUserIdFetcher.get_all_uniqueid(urls)
    
    async def get_user_profile(self,  secUid: str, uniqueId: str):
        kwargs = await self.get_tiktok_headers()

        base_crawler = BaseCrawler(proxies=kwargs["proxies"], crawler_headers=kwargs["headers"])
        async with base_crawler as crawler:

            params = UserProfile(secUid=secUid, uniqueId=uniqueId)
            endpoint = BogusManager.model_2_endpoint(
                TikTokAPIEndpoints.USER_DETAIL, params.dict(), kwargs["headers"]["User-Agent"]
            )
            response = await crawler.fetch_get_json(endpoint)
        return response



