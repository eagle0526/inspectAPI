# inspectAPI
想要使用的話，直接修改 app.py 裡面的 url 即可



### 啟用 docker

```shell
# 建置 docker image
$ docker build -t playwright-app .

# 啟用 docker container - 此 container 會 bind 到本機的 /Users/yee0526/Desktop/python/搶票 資料夾
$ docker run -it --name catchapi-bind -v /Users/yee0526/Desktop/python/搶票:/srv playwright-app:latest /bin/bash
```
