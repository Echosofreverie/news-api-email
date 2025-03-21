import requests
import smtplib
from email.mime.text import MIMEText

from pyexpat.errors import messages
topic = "tesla"
api_key = "79263...."  #去https://newsapi.org/登录使用自己的API
url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-02-21&sortBy=publishedAt&"
       "apiKey=7926374a8.....&"
       "language=en")
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
print(content)
# Get a list of articles
body = " "
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None and article["url"] is not None:
        body = body + article["title"] + "\n" + article["description"] +"\n"+article["url"]+ 2*"\n"


def send_message(message):
    qq_email = "2....@qq.com"
    auth_code = "xfc...."
    smtp_server = "smtp.qq.com"
    smtp_port = 465
    msg = MIMEText(message)
    msg['Subject'] = "Today's news"
    msg['From'] = qq_email
    msg['To'] = "2.....@qq.com"

    try:
        # 创建SSL加密连接
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(qq_email, auth_code)
            server.send_message(msg)
            print("邮件发送成功！🎉")
    except Exception as e:
        print("邮件发送失败！", e)

send_message(message=body)