from crawlers.tiktok.web_crawler import TikTokWebCrawler
import pandas as pd
import asyncio

async def main():
    tiktok_crawler = TikTokWebCrawler()

    data = pd.read_csv('user_id.csv')
    print(data['unique_id'][0])
    print(len(data))

    user_data = []

    for i in range(len(data)):
        uniqueId = data['unique_id'][i]
        secUid = ""  

        try:
            user_profile = await tiktok_crawler.get_user_profile(secUid, uniqueId)
            # print(user_profile.get('userInfo'))
            # break
            user_info = user_profile.get('userInfo')
            # print(user_info)
            stats = user_info.get('stats')
            user = user_info.get('user')

            extracted_data = {
                "uid": user.get('uniqueId'),
                "name": user.get('nickname'),
                "followers": stats.get('followerCount'),
                "likes": stats.get('heartCount'),
                "bio": user.get('signature'),
            }

            # print(extracted_data)
            user_data.append(extracted_data)

        except Exception as e:
            print(f"Could not get user with uniqueId: {uniqueId}. Error: {e}")

    if user_data:
        pd.DataFrame(user_data).to_csv("user_data.csv", index=False)
        print("Dữ liệu đã được lưu vào user_data.csv")

asyncio.run(main())
