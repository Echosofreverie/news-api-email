import requests
import smtplib
from email.mime.text import MIMEText

from pyexpat.errors import messages

api_key = "7926374a804d45dc9ea439b6251f17ef"  #去https://newsapi.org/登录使用自己的API
url = ("https://newsapi.org/v2/everything?q=tesla&"\
       "from=2025-02-18&sortBy=publishedAt&apiKey="\
       "7926374a804d45dc9ea439b6251f17ef")
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
print(content)
# Get a list of articles
body = " "
for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"


def send_message(message):
    qq_email = "2244089290@qq.com"
    auth_code = "xfchtrwoqtofdidh"
    smtp_server = "smtp.qq.com"
    smtp_port = 465
    msg = MIMEText(message)
    msg['Subject'] = "New Email of News"
    msg['From'] = qq_email
    msg['To'] = "2244089290@qq.com"

    try:
        # 创建SSL加密连接
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(qq_email, auth_code)
            server.send_message(msg)
            print("邮件发送成功！🎉")
    except Exception as e:
        print("邮件发送失败！", e)

send_message(message=body)