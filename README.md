yaoleme
=======

issues of license plate of Beijing, processed by unclechen

=========================================
文件结构
pdf：是从官方网站http://www.bjhjyd.gov.cn/的公布栏下载的“四类”摇号结果的文件。分别是：个人普通、个人新能源、企业普通、企业新能源。
localtxt：是用Foxit Reader（不是Adobe PDF Reader）打开从官方网站下载的所有摇号结果的pdf文件后，复制文本，保存下来的txt。
saemysql：是用python脚本程序personal_txt2mysql.py和enterprise_txt2mysql.py处理之后，得到的csv文件。这些csv文件可以直接导入mysql数据库中。

PS：自2014年起，北京市小汽车摇号结果在每个双月的26号更新一期。

=========================================

更新Note：2014-10-4

在处理2014年的第4期的数据时，发现用Adobe PDF Reader打开官方的pdf文件和Foxit Reader打开后，复制文本，保存到txt中的结果是不一样的。

例如，用Foxit Reader打开后，拷贝出来的文本如下：

22 22 0117100681872
-2-23 23 0118103984622
24 24 0119103849135

------------------------------------

而Adobe PDF Reader打开后，保存的txt如下：

22 22 0117100681872
-2-
23 23 0118103984622
24 24 0119103849135

所以，最好用Adobe PDF Reader来打开文件，这样拷贝出来的文本比较规则，写自动化转换脚本的时候也比较好写。
只有页码那一行被分开了，这样比较好写文本处理的脚本，应该personal和enterprise只要写一个脚本就ok了。