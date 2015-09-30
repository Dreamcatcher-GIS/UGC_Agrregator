UGC_Agrregator
=================================

众源时空信息聚合平台
--------------------------

###使用Python 库：
1.jieba分词<br />
https://github.com/fxsjy/jieba<br />
2.snownlp 自然语言处理<br />
https://github.com/isnowfy/snownlp<br />
3.baidu_python 百度地图SDK<br />
https://github.com/Dreamcatcher-GIS/baidu_python<br />
4.easygo_python 宜出行SDK<br />
https://github.com/Dreamcatcher-GIS/easygo_python

###Example

获取指定范围内的旅行社poi数据,并持久化到mysql中
```python
from Service.baidumapService import BaiduMapService

baiduMapService = BaiduMapService()
baiduMapService.getPoi(118.243339,32.195425,118.500901,32.496076,'旅行社')
```
