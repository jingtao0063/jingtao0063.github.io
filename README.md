# 密码管理器

## 密钥测试工具
上传至Github的json文件是加密后的数据, 可以通过在线工具进行解密得到明文密码

如果使用在线工具解密 设置如下:
* 提供完整的Base64加密字符串(json内容)
* 提供主密码(SHA256加密后的字符串, 可使用该工具:https://www.jyshare.com/crypto/sha256/)
* 选择AES-256-CBC模式
* 指定PKCS7填充
* 偏移量为空

AES工具可以使用https://box.newban.cn或者https://www.iamwawa.cn/aes.html

测试密钥如下:

```
U2FsdGVkX19C3sF931NAFd/EE1MsLH8IHlTKQcG4jyL+AJ4STnINEBJFFfrUd4itwSBmhuECLtgvYtsiGb4t++Bof16AfTp21my498Hwae3tzYA+AaIlh9FoJHBLAcBu4uEj2kgW18y/6zuso0jHJ1sT5Q7jKBgCfVmMgJQvHPiNBpd4Q3Muy9Q6JLoJNm7g6OHUf811Dbiq6Kn/CoLNU9HqrhtM3R5P3AtkdZJ/D/ScRQGnydnICqvfgyw7x3PAtJUBd7PCgRREjT91C5+BuX9dCYtlBwS0d/22yrN+KJU=
```
SHA256加密前原始密码: 123


## 加解密技术原理
​​加密过程​​:
* 主密码通过SHA256哈希生成256位密钥
* 使用AES-256-CBC模式加密
* 加密结果包含16字节IV + 密文
* 最终结果使用Base64编码存储

​​解密过程​​:
* Base64解码获取原始字节
* 分离IV和密文
* 使用主密码派生相同密钥
* AES解密并移除PKCS7填充
* 解析JSON数据

## 功能实现
* 数据导入导出
* 数据自定义存储(本地、Github、Webdav等)
* 数据分类
* 数据加密存储
* 历史版本回退
* 配置文件的导出
* 网站纯本地运行 不涉及第三方后台 安全性高
* 密钥分享 (待开发)

## 网站部署

直接将该仓库的代码上传到你自己的静态服务器上即可使用
网站示例: [点击进入](https://mi.newban.cn/)
