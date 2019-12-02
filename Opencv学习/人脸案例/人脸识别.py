import json
import requests
api1 = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=lVfov6E1oaWZR9f4qIhd9Hjy&client_secret=Gubrc6RnMTdA3Eb8WumHIGrz4vHgCTdy"

api2 = "https://aip.baidubce.com/rest/2.0/face/v3/match?access_token="
list = ["马云1.jpeg","马云2.jpg","张威.jpg","夏纪文.jpg","刘强东.jpg","任正非.jpg","马化腾.jpg"]
text = 3;
# 1. 读取图片数据
def get_img(img1, img2):
    import base64
    with open(img1, "rb") as f:
        pic1 = f.read()
    with open(img2, "rb") as f:
        pic2 = f.read()

    params = json.dumps([
        {"image": str(base64.b64encode(pic1), "utf-8"), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
        {"image": str(base64.b64encode(pic2), "utf-8"), "image_type": "BASE64", "face_type": "IDCARD","quality_control": "LOW"},
    ])
    return params

# 2. 获取token值 拼接API
def get_token():
    response = requests.get(api1)
    access_token = eval(response.text)['access_token']
    api_url = api2 + access_token
    return api_url

# 3. 请求API拿到最终结果
def than_img(img1, img2):
    api_url = get_token()
    params = get_img(img1, img2)

    content = requests.post(api_url, params).text
    score = eval(content)['result']['score']

    if score > 80:
        print("图片相似度：" + str(score) + ",同一个人")
        return  0
    else:
        print("图片相似度：" + str(score) + ",不是同一个人")
        return 1
if __name__ == '__main__':

    for i in list:

        # print(i)


        if than_img("夏纪文.jpg",i)==0:
            str = i
            for j in str:
                if j==".":
                    strs = j
            print("这个人是：", str)
            break

