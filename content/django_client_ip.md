Date: 2015-11-10
Title: Django获取真实客户端IP
Published: true
Type: post
Tags: django, python
Category: Coding
Slug: django-client-ip
Header_Cover: /images/bg1.jpg

Django 老的版本（<=1.6）里一般用 `request.META` 的 `REMOTE_ADDR` 或者`HTTP_X_FORWARDED_FOR` 判断而来。如下：

```python
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
```

新版本的 `HttpRequest` 对象具有一个`get_host` 的方法，可以获取客户端的真实IP，在使用反向代理的情况下，还需要配置 settings 中的 `USE_X_FORWARDED_HOST` 为 `True`。
