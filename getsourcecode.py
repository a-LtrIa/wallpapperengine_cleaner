from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# 配置 Edge 浏览器选项
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True

# 使用已有用户数据（确保 Steam 已登录）
edge_options.add_argument(r"user-data-dir=C:/Users/Altria/AppData/Local/Microsoft/Edge/User Data/Default")

# 可选：禁用证书验证（临时调试使用）
edge_options.add_argument('--ignore-certificate-errors')
edge_options.add_argument('--allow-insecure-localhost')

# 启动 Edge 浏览器
service = Service(executable_path='E:\ArkProject\壁纸引擎清理器\edgedriver_win64\msedgedriver.exe')  # 替换为你的 msedgedriver 路径
driver = webdriver.Edge(service=service, options=edge_options)

# 要抓取的页面 URL 列表
urls = [
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=1&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=2&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=3&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=4&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=5&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=6&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=7&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=8&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=9&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=10&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=11&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=12&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=13&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=14&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=15&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=16&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=17&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=18&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=19&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=20&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=21&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=22&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=23&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=24&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=25&numperpage=30",
    "https://steamcommunity.com/profiles/76561199063205577/myworkshopfiles/?appid=431960&browsefilter=mysubscriptions&p=26&numperpage=30"
]

try:
    # 打开目标登录页面
    url = "https://store.steampowered.com/login/"
    driver.get(url)
    
    # 提示用户手动登录
    print("请在浏览器中完成登录操作...")
    input("登录完成后按 Enter 键继续...")

    # 添加随机延迟，模拟人类行为
    time.sleep(random.uniform(2, 5))

    # 等待页面加载（根据实际页面元素调整选择器）
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))  # 等待 body 加载
        )
        print("登录页面加载完成。")
    except Exception as e:
        print(f"页面加载异常：{e}")

    # 获取并保存多个页面源码到 sourcecode.txt
    with open("sourcecode.txt", "w", encoding="utf-8") as f:
        for i, page_url in enumerate(urls, start=1):
            print(f"正在获取第 {i} 页内容：{page_url}")
            driver.get(page_url)  # 访问页面
            
            # 等待页面主体加载完成
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )

            # 添加随机延迟
            time.sleep(random.uniform(2, 4))

            # 获取页面源码
            page_source = driver.page_source
            f.write(f"===== 第 {i} 页内容开始 =====\n")
            f.write(f"URL: {page_url}\n")
            f.write(page_source)
            f.write(f"\n===== 第 {i} 页内容结束 =====\n\n\n")

        print("所有页面源码已保存到 sourcecode.txt")

    # 保持浏览器打开
    print("操作已完成，浏览器窗口保持打开状态。")

except Exception as e:
    print(f"发生错误：{e}")
    print("浏览器窗口保持打开状态。")