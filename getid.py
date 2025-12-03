from bs4 import BeautifulSoup
import re

# 读取 sourcecode.txt 文件内容
with open("sourcecode.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 用 BeautifulSoup 解析整个 HTML 内容
soup = BeautifulSoup(content, "lxml")

# 查找所有 class 包含 workshopItemSubscription 的 div 标签
items = soup.find_all("div", class_=lambda c: c and "workshopItemSubscription" in c.split())

if not items:
    print("未找到任何 workshopItemSubscription 数据。")
else:
    data_list = []

    for item in items:
        # 获取完整的 id 属性
        item_id_full = item.get("id", "未知")
        
        # 只保留 Subscription 开头的有效项
        if not item_id_full.startswith("Subscription"):
            continue

        # 提取数字部分用于构造详情页链接
        item_id_match = re.search(r"Subscription(\d+)", item_id_full)
        item_id_num = item_id_match.group(1) if item_id_match else None

        # 构造详情页链接
        detail_url = f"https://steamcommunity.com/sharedfiles/filedetails/?id={item_id_num}" if item_id_num else "未知"

        # 获取 backgroundImg 图片链接
        img_tag = item.find("img", class_="backgroundImg")
        img_src = img_tag["src"] if img_tag and img_tag.has_attr("src") else "未知"
        img_src = img_src.replace("&amp;", "&")  # 还原 HTML 实体

        # 获取标题
        title_div = item.find("div", class_="workshopItemTitle")
        title = title_div.get_text(strip=True) if title_div else "未知"

        # 构建数据字典
        data = {
            "ID": item_id_num if item_id_num else "未知",
            "详情页链接": detail_url,
            "图片链接": img_src,
            "标题": title
        }
        data_list.append(data)

    # 将结果写入 id.txt 文件
    with open("id.txt", "w", encoding="utf-8") as output_file:
        for data in data_list:
            output_file.write(f"ID: {data['ID']}\n")
            output_file.write(f"详情页链接: {data['详情页链接']}\n")
            output_file.write(f"图片链接: {data['图片链接']}\n")
            output_file.write(f"标题: {data['标题']}\n")
            output_file.write("-" * 40 + "\n")

    print(f"已成功将 {len(data_list)} 条记录写入 id.txt 文件。")