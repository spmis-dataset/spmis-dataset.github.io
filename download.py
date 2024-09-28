import os
import requests

# 定义要下载的图标及其URL（来自 Font Awesome 网站）
icons = {
    "github": "https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/svgs/brands/github.svg",
    "paper": "https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/svgs/solid/file-alt.svg"
}

# 本地保存路径
save_dir = "icons"
os.makedirs(save_dir, exist_ok=True)

# 下载并保存图标
for icon_name, url in icons.items():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(save_dir, f"{icon_name}.svg")
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {icon_name} icon to {file_path}")
        else:
            print(f"Failed to download {icon_name} icon, status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {icon_name} icon: {e}")

print("All icons downloaded.")
