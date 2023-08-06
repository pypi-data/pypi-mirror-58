# syz
常用python工具

## tools
```python
import syz
```
+ 时间工具
+ 文件名后缀
+ 日志工具
+ CPU物理核心数

## nlp
```python
import syz.nlp
```
+ 去掉中文停用词

# 打包方法
1. 修改版本 setup.py
2. 运行
```bash
python setup.py sdist
twine upload dist/syz-0.0.2.tar.gz
```
