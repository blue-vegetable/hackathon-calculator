本计算器是一个非常简单的计算器<br>

为了大整数运算偷懒所以用前后端分离的方式,

让运算在后端进行(python自带大整数运算),然后返回结果给前端

后端已经运行在我的服务器上并且相关配置已经完成。

可以直接这些文件在pycharm中作为flask项目运行

也可以在linux下用运行

```bash
flask run --host=0.0.0.0 --port=5000
```

也可以直接访问 http://47.98.132.72:5000/



环境:

后端:ubuntu 18.04, FLASK2.0.0 

前端:html5

