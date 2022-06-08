import requests
from bs4 import BeautifulSoup

def fetch_google_img_url(params):
    print(params)
    img_keyword = "-".join(params["product_category"].split(" "))
    print(img_keyword)
    img_site_url = f"https://www.everypixel.com/search?q={img_keyword}&stocks_type=free"
    response = requests.get(img_site_url)
    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.findAll('img')
    example = images[0]
    img_url = example.attrs['src']
    return img_url


def gen_SERP_preview(params, output_single):
    serp_pic = str(fetch_google_img_url(params))
    html_output = f"""<html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>HTML 5 Boilerplate</title>
            <style>
                    div span {{display: inline-block;}}
                    p {{margin-block-start: 0; margin-block-end: 0;}}
                    div.a {{line-height: 1.2; padding: 5;}}
                    div.b {{line-height: 1.2; font-size: 0.875em; font-family: "Lucida Console", "Courier New", monospace; color: #545454; padding-top: 5px;}}
                    div.container {{display: flex;justify-content: space-between;}}
            </style>
        </head>
        <body>
            <div class="container">
            <div class="a">
            <p style="font-family:sans-serif; color:#545454; font-size: 11px; padding-bottom: 5px;">https://{params["company_name"].lower().split(" ")[0]}.com > {params["product_name"]}</p><p style="font-family:Courier; color:#1A0DAB; font-size: 16px; padding: 0;"></p>
            <p style="font-family:sans-serif; color:#1A0DAB; font-size: 16px; padding-bottom: 5px"><span>{params["product_name"]} by {params["company_name"]}</span></p><p style="font-family:Courier; color:#1A0DAB; font-size: 16px; padding: 0; </div>;"></p>
            <p style="font-family:sans-serif; color:#545454; font-size: 12px;"><span>{output_single}</span> </p><p style="font-family:Courier; color:#1A0DAB; font-size: 16px;"></p>
            </div>
            <img src={serp_pic} style="width: auto; height: 60px; object-fit: contain; padding: 5px; padding-left: 20px";
            object-fit: contain;/>
            </div>
        <script src="index.js"></script>
        </body>
        </html>"""
    return html_output
