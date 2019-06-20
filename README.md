# meet_words

生成会标的一个程序

平常开会的时候，会使用到会标。
之前的做法是：
1.在Excel中编辑文字，
2.然后将文字进行排版，
3.然后打印预览，
4.使用微信/QQ的截图功能进行截取。
5.然后使用美图秀秀进行更改图片的尺寸为本机尺寸。

而使用本程序的做法是：
1.打开程序
2.输入要生成的会标的文字
3.生成会标文件



# 所需要的运行环境
1.python3.7
2.pycharm进行编辑
3.pyinstaller(打包为EXE文件的包)
4.pillow(PIL操作图片的包)
5.貌似在安装pycharm的时候还需要安装Java的运行环境，难道pycharm是使用Java开发的吗？
6.https://blog.csdn.net/jin80506/article/details/83111848   安装pip程序

打包命令：pyinstaller -F -w  xx.py

遇到的问题：
在使用pycharm下载需要的包的时候，速度特别的慢。
这里需要调用
国内的站点有：
	
	清华: https://pypi.tuna.tsinghua.edu.cn/simple（我使用的站点）
	 
	豆瓣: http://pypi.douban.com/simple/
	 
	阿里: http://mirrors.aliyun.com/pypi/simple/


