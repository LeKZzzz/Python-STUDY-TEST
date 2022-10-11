# -*- coding: UTF-8 -*- 
# Creator：LeK
# Date：2022/10/9


import asyncio
import requests


async def download_image(url):
    # 发送网络请求，下载图片
    print('开始下载', url)

    # request模块默认不支持异步操作，想要实现异步操作可以使用线程池进行转换
    # 第一步：内部会先调用 ThreadPoolExeutor的submit方法申请一个线程去执行函数，并返回一个concurrent.futures.Future对象
    # 第二步：调用asyncio.wrap_future方法将concurrent.futures.Future对象包装为asyncio.Future对象
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, requests.get, url)
    response = await future
    print('下载完成')

    # 将图片保存到本地
    file_name = url.rsplit('_')[-1]
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)


if __name__ == '__main__':
    url_list = [

    ]

    tasks = [download_image(url) for url in url_list]
    asyncio.run(asyncio.wait(tasks))
