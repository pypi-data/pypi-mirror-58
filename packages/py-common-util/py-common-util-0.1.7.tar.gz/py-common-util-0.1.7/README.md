# py-common-util
python common util

### Specifics
- 代码遵循google python规范：https://github.com/google/styleguide/blob/gh-pages/pyguide.md

### download
- pip install py-common-util

### Dependencies
- datetime

### ENV
1. 本地开发环境：pycharm + python3.6.1+Anaconda3+python3+pip3 + local cpu/gpu
2. 远程开发测试环境：pycharm + remote ssh + (远程python3.6.1+pip3+Anaconda3+gpu)
remote host url 如：ssh user@192.168.xx.xx
remote python interpreter path: /home/user/anaconda3/bin/python3
本地pycharm设置环境变量：Run>Edit Configurations>Environment variables>PYTHONUNBUFFERED=1;PATH=/usr/local/cuda/bin:/home/user/anaconda3/bin:$PATH;LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/lib
3. 线上环境：待定

### 相关链接
如何将自己的Python代码打包发布到pypi上 https://blog.csdn.net/wdxin1322/article/details/56685094
发布你自己的轮子 - PyPI 打包上传实践 https://juejin.im/entry/58c612e2128fe100603dfc9c

### 上传到pypi的相关命令
# 第二章 - 将你的扩展包在PyPI上发布 
http://www.wbh-doc.com.s3.amazonaws.com/Python-OpenSource-Project-Developer-Guide/Chapter2%20-%20PyPI.html
1. 升级__version__(参考common/version.py)
2. 查看打包文件清单MANIFEST.in是否包含应该包含的文件
3. 删除build,dist,py_common_util.egg-info目录

###### （$python3 setup.py install (生成build,dist,egg-info目录)
###### 创建zip安装包
###### 打包 $ python3 setup.py sdist （生成dist,egg-info目录，并install到本机pythonx.x/site-packages/的类库中；也可以在IDEA的其它项目中依赖该项目模块而改动代码不必打包）
###### 或者创建全版本通用的wheel安装包
###### 安装twine $pip3 install twine**
 
构建 $ python3 setup.py sdist
######or $ python3 setup.py sdist bdist_wheel --universal
###### then install to local: $ pip3 install -U ./dist/skydl-*-py2.py3-none-any.whl
 
######$ twine check dist/
######注册包(可能不需要) $ twine register dist/py-common-util-0.0.41.tar.gz -r pypi
######打包并上传 $ python3 setup.py sdist upload -r pypi ）
 
上传到pypi $ twine upload --skip-existing --verbose --repository pypi dist/*
可以访问公网查看：https://pypi.org/search/?q=py-common-util

######（强制更新 $pip3 install --upgrade --no-deps --force-reinstall py-common-util --index https://pypi.mirrors.ustc.edu.cn/simple/ ） 


$ pip3 search py-common-util

===注意====

如果$pip3 install -U py-common-util有缓存旧的版本，则可在一台没有缓存的机器去下载最新版本就可以更新pypi上的缓存

install from tar.gz file: $pip3 install -U  py-common-util-0.0.42.tar.gz

===========

其它项目安装py-common-util依赖 $pip3 install -U py-common-util
或者$ easy_install py-common-util

===========

###### if CLion open this project reported Unknown Module Type Error, then fixed: Delete the ".idea/" in your project folder and then reopen your project using clion, you'll be glad to find everything works fine.

#### 使用 py-common-util
>>import py_common_util
>>from py_common_util.common.date_utils import DateUtils
>>from py_common_util.tensorflow.tf_utils import TFUtils
>>print(DateUtils.now())
>>py_common_util.__version

### config .pypirc and $chmod 600 ~/.pypirc
[distutils]
index-servers=
pypi
testpypi
[pypi]
repository: https://upload.pypi.org/legacy/
username: <username>
password: <password>
[testpypi]
repository: https://test.pypi.org/legacy/
username: <username>
password: <password>

### jarfile
stanford-segmenter-3.9.1.jar https://nlp.stanford.edu/software/segmenter.shtml#Download
1.进入到解压后的文件目录中，输入下面代码
./segment.sh pku test.simp.utf8 UTF-8 0

### feature list
#####v0.0.44 增加now_to_str的时间格式输出方法
#####v0.0.43 增加ring buffer功能
#####v0.0.36 增加request的hooks_exception_callback功能