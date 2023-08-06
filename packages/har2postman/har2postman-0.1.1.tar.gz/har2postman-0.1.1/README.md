## Har2Postman
[![travis-ci](https://api.travis-ci.org/whitexie/Har2Postman.svg?branch=master)](https://travis-ci.org/whitexie/Har2toPostman)
![coveralls](https://coveralls.io/repos/github/whitexie/Har2Postman/badge.svg?branch=master)
> 将har文件转换为postman可导入文件

## 安装
```shell script
pip isntall Har2toPostman
```

## 使用
1.将har文件转换为postman可导入文件
```shell script
harto postman_echo.har

# INFO:root:read postman_echo.har
# INFO:root:Generate postman collection successfully: postman_echo.json
```
2.在postman中导入postman_echo.json文件
![](https://github.com/whitexie/Har2Postman/blob/master/postman_collection1.png)
