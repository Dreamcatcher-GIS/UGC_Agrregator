UGC_Agrregator
=================================

众源时空信息聚合平台
--------------------------

##使用Python 库：
1.sinaweibopy<br />
https://github.com/fxsjy/jieba<br />

一个用于访问新浪微博api的python库<br />

2.selenium<br />
可以直接使用pip进行安装<br />

Selenium也是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。<br />


##使用驱动:
1.Chrome驱动<br />
下载地址：http://npm.taobao.org/mirrors/chromedriver<br />

selenium调用需要，需下载系统对应版本，将其放置到系统能直接访问的文件夹，如放在{PYTHON_HOME}/Scripts文件夹中<br />


##数据库：

###weibo
1.api_account<br />
```sql
DROP TABLE IF EXISTS `api_account`;
CREATE TABLE `api_account` (
  `ID` bigint(20) DEFAULT NULL,
  `APP_KEYsId` longtext,
  `APP_SECRET` longtext,
  `access_tok` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
2.weibo_comment<br />
```sql
DROP TABLE IF EXISTS `weibo_comment`;
CREATE TABLE `weibo_comment` (
  `guid` varchar(40) DEFAULT NULL,
  `userID` bigint(20) DEFAULT NULL,
  `weiboID` varchar(20) DEFAULT NULL,
  `pageNum` int(11) DEFAULT NULL,
  `commPeople` varchar(40) DEFAULT NULL,
  `commentText` longtext,
  `commentTime` varchar(20) DEFAULT NULL,
  `crawlTime` varchar(30) DEFAULT '',
  `likeNum` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
3.weibo_content<br />
```sql
DROP TABLE IF EXISTS `weibo_content`;
CREATE TABLE `weibo_content` (
  `ID` bigint(20) DEFAULT NULL,
  `weiboid` bigint(20) DEFAULT NULL,
  `text` longtext,
  `lat` longtext,
  `lon` longtext,
  `title` longtext,
  `userid` longtext,
  `location` longtext,
  `userdescription` longtext,
  `gender` longtext,
  `created_at` longtext,
  `fax` longtext,
  `locality` longtext,
  `formatted` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
4.weibo_id<br />
```sql
DROP TABLE IF EXISTS `weibo_id`;
CREATE TABLE `weibo_id` (
  `guid` varchar(40) NOT NULL,
  `userID` bigint(20) NOT NULL,
  `weiboID` varchar(20) NOT NULL,
  `pageNum` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
