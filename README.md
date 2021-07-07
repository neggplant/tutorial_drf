# tutorial_drf

## 请求与相应
###请求
```bash
request.POST  # 只处理表单数据  只适用于'POST'方法
request.data  # 处理任意数据  适用于'POST'，'PUT'和'PATCH'方法
```
### 响应
```bash
return Response(data)  # 渲染成客户端请求的内容类型。
```
### 包装（wrapping）API视图
REST框架提供了两个可用于编写API视图的包装器（wrappers）。

用于基于函数视图的@api_view装饰器。  
用于基于类视图的APIView类。