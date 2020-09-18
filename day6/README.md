# Day06

## 緩存
- 提升伺服器響應速度。
- 將執行過的操作資料儲存下來，在一定時間內，再次獲取資料的時候，直接從緩存中獲取。
- 比較理想的方案，緩存使用內存級緩存。
- Django 內置緩存框架，並提供了幾種常用的緩存。
	- 基於Memcached緩存。
	- 使用資料庫進行緩存。
	- 使用文件系統進行緩存。
	- 使用本地內存進行緩存。
	- 提供緩存擴展接口。
	
	
## AOP 中間件
- 實現統計功能
	- 統計IP
	- 統計瀏覽器
- 實現權重控制
	- 黑名單 
	- 白名單
-實現反爬
	- 反爬蟲
		- 十秒之內
	- 實現頻率控制
- 介面友好化
- 應用交互友好化


## 中間件
- 調用順序
	- 中間件註冊的時候是一個列表。
	- 如果沒有在切點處直接進行返回，中間件會依次執行。
	- 如果直接進行了返回，後續的中間件就不再執行了。
- 切點
	- process_request
	- process_view
	- process_template_reponse
	- process_response
	- precess_exeption
- 切面






	
	
## 緩存配置  
- 1. 創建緩存表  
	- python manage.py createcachetable [table_name]  
- 2. 緩存配置  
``` 
	CACHES = {  
		'default': {  
		'BACKEND': 'django.core.cache.backends.db.DatabaseCache',  
		'LOCATION': 'my_cache_table',  
		'TIMEOUT': '60',  
		'OPTIONS': {  
			'MAX_ENTRIES': '300',  
			},  
		'KEY_PREFIX': 'rock',  
		'VERSION': '1',  
		}  
	}  
```


## 緩存使用
- 在 views.py 中使用（使用最多的場景。
- @cache_page()。
	- time 秒 60*5 緩存五分鐘  。
	- cache 緩存配置, 默認default。
	- key_prefix 前置字符串。


## 緩存底層  
- 獲取cache
	```
	from django.core.cache import caches  
	cache = caches['cache_name'] 
	```
- 獲取cache
	```
	from django.core.cache import cache
	```

## 緩存操作   
- cache.set   
	- key   
	- value   
	- timeout  
- get  
- add  
- get__or \_set_  
- get_many  
- set_many  
- delete  
- delete_many   
- clear  
- incr 增加  
	- incr(key, value) key對應的值上添加 value  
- decr 減少  
	- decr(key, value) key對應的值上減少value  
	- 如果value不寫，默認變更為1  
	

## 使用Redis做緩存   
- 常見的有兩個實現  
	- django-redis  
		- [http://django-redis-chs.readthedocs.io/zh_CN/latest/#django](http://django-redis-chs.readthedocs.io/zh_CN/latest/#django)  
	- django-redis-cache  
		- [https://pypi.python.org/pypi/django-redis-cache/](https://pypi.python.org/pypi/django-redis-cache/)  
- 配置和內置的緩存配置基本一致  
```
- CACHES = {  
	"default": {  
	"BACKEND": "django_redis.cache.RedisCache",  
	"LOCATION": "redis://127.0.0.1:6379/1",  
	"OPTIONS": {  
		"CLIENT_CLASS": "django_redis.client.DefaultClient",  
		}  
	}  
}  
``` 
- 用法和內置緩存使用一樣





















