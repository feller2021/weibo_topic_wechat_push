from urllib.parse import quote


# encode=quote('打工人')
# kk=quote('=61&q=#社会队树洞#&t=0')
#
# url2='https://m.weibo.cn/api/container/getIndex?containerid=231522type'+kk+'&page_type=searchall'
# print(url2)
def urlencode(china):
    china=china
    encode = '=61&q=#'+china+'#&t=0'
    kk = quote(encode)
    return kk

# if __name__ == '__main__':
#
#     dfp=urlencode('社会队树洞')
#     print(dfp)
