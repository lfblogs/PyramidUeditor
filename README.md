本模块帮助在Pyramid应用中集成百度Ueditor HTML编辑器.

更新历史
============
###[2015-06-05]     Ver:1.0.1
采用 Ueditor 1.4.3
封装了一层接口，实现图片、涂鸦、附件、视频、截图上传
在线文件待续

使用方法
============
##1、安装方法

	* 方法一：将github整个源码包下载回家，在命令行运行：
		python setup.py install
	* 方法二：使用pip工具在命令行运行(推荐)：
	    pip install PyramidUeditor
  2、配置urls
	from pyramid.static import static_view
	from pyramid_ueditor.settings import UEDITOR_STATIC_ROOT
	config.include('pyramid_ueditor')	
    config.add_static_view('uestatic', path=UEDITOR_STATIC_ROOT, cache_max_age=3600)
  3、修改pyramid_ueditor.pyramid_ueditor.settings.py 
	 UEDITOR_UPLOAD_ROOT 为上传路径。可进行修改
  4、自带的访问方式
      /ueditor/
