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
		- 統計、打印。
		- 優先級調度
			- 黑名單
			- 白名單
		- 反爬、頻率控制
			- N 時間段之內只能請求一次
			- 單位時間之內最多訪問 N 次
				- 我們需要紀錄每次請求時間。
				- 資料結構 key-value value = []。
				- 在判斷資單位時間請求次數的時候，判斷是列表長度。
				- 在判斷之前進行簡單的資料清洗。
	- process_view
		- CSRF
		- 首先判斷了兩個豁免條件
		- 判斷請求是否安全
		- POST 請求如何驗證 CSRF
			- 在 request.POST.get('csrftokenmiddleware')
			- 驗證和請求對應的 token 是否正確
	- process_template_reponse
	- process_response
		- 跨域處理
			- ip 和 端口不一致，只要有一個不一樣就是不一樣。
			- 跨域的行為校驗是瀏覽器行為。
			- 實現領域
				- 伺服器端添加屬性允許所有域名訪問
				- 在客戶端偽裝
		- 對響應進行統一處理
	- precess_exeption
- 切面


## Paginator
- 對象創建
	- Paginator(資料集，每一頁資料集)
- 屬性
	- count 
		- 對象總數。
	- num_pages
		- 頁面總碼。
	- page_range
		- 頁碼列表，從 1 開始。
- 方法
	- page(整數)
		- 獲得一個 page 對象。
- 常見錯誤
	- InavliPage
		- page() 傳送無效頁碼。
	- PageNotAnlnteger
		- page() 傳送的不是整數。
	- Empty
		- page() 傳送的值有效，但是沒有資料。
- Page
	- 對象獲得，通過 Paginator 的 page() 方法獲得。
- 屬性
	- object_list
		- 當前頁面上所有的資料對象。
	- number 
		- 當前頁的頁碼值。
	- paginator
		- 當前 page 關聯的 Paginator 對象。
- 方法
	- has_next()
		- 判斷是否有下一頁
	- has_previous()
		- 判斷是否有上一頁
	- has_other_page()
		- 判斷是否有上一頁或下一頁
	- next_page_number()
		- 返回下一頁的頁碼
	- previous_page_number()
		- 返回上一頁的頁碼
	- len()
		- 返回當前頁的資料的個數
	
	
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


## 驗證碼
- 防止惡意用戶，驗證是個人類
- 原生繪製
	- pillow
		- Image
			- 尺寸
			- 顏色
			- 模式
				- RGB
		- ImageDraw
			- 屬於哪一個畫布
			- 畫完的東西在哪
			- 封裝繪製 API
				- 文字
				- 點
				- 線
				- 弧
		- ImageFont
			- 畫筆的輔助工具
			- 字體
			- 設定繪製的樣式
- 需要將畫布轉換成二進制流，並且添加格式限定
- 內存流
	- BytesIO
	- 將圖片存到內存中
	- 從流中獲取到資料值
- 通過 HttpResponse 返回圖片內容
	- content_type
	- MIME
		- 標示打開資料的一個應用程序。
		- image/png
- 驗證碼
	- 客戶端驗證
	- 服務端驗證
		- 驗證碼生成的時候，儲存驗證碼。
		- 在提交的時候驗證驗證碼的有效性。
- 驗證碼刷新
	- 瀏覽器緩存策略
		- 是以 URL 為標示。
	- 解決方案
		- 每次給不同的地址。
		- 對地址進行一個參數拼接，每次傳遞不同的參數。


















