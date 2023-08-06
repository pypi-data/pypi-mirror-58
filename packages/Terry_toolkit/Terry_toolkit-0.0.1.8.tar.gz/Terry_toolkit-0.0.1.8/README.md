#关于
Terry-toolkit常用函数整理的工具包
https://pypi.org/project/Terry_toolkit/


## 安装
```
pip3 install Terry_toolkit
```


## 使用
 

```
import Terry_toolkit as tkit

data=[{'aa':'bb'}]
tkit.Json().save(data)

tkit.Json().load()






#更多 https://colab.research.google.com/drive/1j_VEgs7Y3ZzsTh3iX6DBPzEI3X6pQ20S#scrollTo=NZmluI1ptzjy

```

## 生成依赖

pip3 freeze > requirements.txt


## 提交包
python3 setup.py sdist
# #python3 setup.py install
python3 setup.py sdist upload


## 构建文档
```
mkdir docs
cd docs
sphinx-quickstart
cd ../

#使用这个

sphinx-apidoc -f -o docs/source/ Terry_toolkit  -e --ext-autodoc --ext-githubpages --ext-viewcode --ext-todo
cd docs
#不需要 sphinx-build -b html source build 
make html
```



其它库推荐

cacheout  #函数缓存
unqlite nosql数据库已经加载
pip install MagicBaidu


 
创建虚拟环境 

python3 -m venv . 

source ./bin/activate 

# 如何自动生成和安装requirements.txt依赖 

在查看别人的Python项目时，经常会看到一个 

``` 

requirements.txt 

``` 

文件，里面记录了当前程序的所有依赖包及其精确版本号。这个文件有点类似与Rails的 

``` 

Gemfile 

``` 

。其作用是用来在另一台PC上重新构建项目所需要的运行环境依赖。 

  

requirements.txt可以通过 

``` 

pip 

``` 

命令自动生成和安装 

### 生成requirements.txt文件 

``` 

pip freeze > requirements.txt 

```

### 安装requirements.txt依赖 

  

``` 

pip install -r requirements.txt 

``` 