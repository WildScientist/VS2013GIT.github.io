import requests

url="https://api.weixin.qq.com/tcb/invokecloudfunction?access_token=36_9FMGTwR5z80RQCqlCRrBJ1cMLOvMz794ru12dOGVa9p2h7ge2cH15JsAw0yXzxMrqvMKt3jgZVVnKcTdn9VmSOtb9480T7F3qXKqC7_dcbSbL3b9vVyNsi5zPbVbfXImWmQLNlzVIyIKkCRVRMAaADAGBP&env=mypage-j423a&name=login"
response=requests.post(url)

print(response.content)