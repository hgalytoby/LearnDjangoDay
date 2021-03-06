# Django
- django-admain startproject project .
- python manage.py startapp app    or   django-admain startapp app
- python manage.py makemigrations
- python manage.py migrate

## MySQL
- mysql -uroot -ppassword
- create database databasename charset=utf8;
- exit

## SQLite
- 輕量級的嵌入式級的資料庫
- 特點是小
	- 常用場景。
	- Android、IOS、WP
- 資料庫常規操作相似度和 MySQL 達百分之九十五。

## 播放器
- 完美解碼
- 加速撥放
	- 影音同步加速。

## 快捷鍵
- 萬用鍵
	- alt + enter

## 實現一個請求
- 註冊一個路由
	- urls 中
		- url 
			- 參數 匹配規則 正則。
		- 視圖函數
			- 響應的是 views 中的一個函數。
				- 沒有括號  。
- 去 views.py 實現對應的函數
	- 第一個參數是 request。
	- 永遠記得返回 Response。

## html 
- 快鍵鍵 Tab
- ul>li
- ul*5
- ul>li*5

- web 階段
	- Django
	- Flask

- 虛擬化技術
	- 虛擬機
	- 虛擬容器
		- Docker
	-虛擬環境
		- Python專用。
		- 將 Python 依賴隔離。

## 模板配置
- 兩種
	- 在 App 中進行模板配置
		- 只需在 App 的根目錄創建 templates 文件夾即可。
		- 如果想讓程式碼自動提示， 我們標記文件夾為模板文件夾。 
		- 對資料夾右鍵 Mark Diectory as -> Template Folder
	- 在項目中目錄進行模板配置
		- 需要在項目目錄中創建 templates 文件夾並標記。
		- 需要在 settings.py 中進行註冊。
	- 在開發中使用第二種
		- 模板可以繼承，重複用。
		
## 路由優化配置
- 項目如果邏輯過於複雜，可以進行拆分。
- 拆分為多個App。
- 繼續拆分路由器 urls
	- 在 App 中創建自己的 urls。
		- urlpatterns 路由規則列表。
		- 在根 urls 中進行子路由的包含。
	- 子路由使用
		- 根路由規則 + 子路由的規則。
		
## models 使用 ORM 技術
- Object Relational Mapping 對象關係映射
- 將業務邏輯進行了一個解耦合
	- object.save() 儲存。
	- object.delete() 刪除。
- 關聯型資料庫
	- DDL (打開Database，Submit處有 DLL 查看)。
	- 通過 models 定義實現，資料庫表的定義。
- 資料操作
	- 增刪改查
	- 儲存
		- save()。
	- 查詢
		- 查所有 object.all()。
		- 查單個 object.get(pk=xx)  pk=自動生成的 ID 編號。
	- 更新
		- 基於查詢的
		- 查好的對象，修改屬性，然後 save()。
	- 刪除
		- 基於查詢的。
		- 調用 delete()。

## 連接 mysql 驅動

- Test Connection 失敗
	- 在該視窗的 Advanced 尋找 serverTimezone 輸入 UTC。

- sittings.py
	```python
	DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '資料庫名稱',
        'USER': 'root',
        'PASSWORD': '密碼',
        'HOST': '127.0.0.1',
        'PORT': '3306'
				}
		}
	```
	
- settings.py 層的 __init__.py
	```python
	import pymysql

	pymysql.version_info = (1, 4, 13, "final", 0)
	pymysql.install_as_MySQLdb()
	```

- mysqlclinet
	- python2, 3 都能直接使用。
	- 致命弱點 
		- 對 mysql 安裝有要求, 必須指定位置存在配置文件。
- python-mysql
	- python2 支持。
	- python3 不支持。
- pymysql
	- python2, python3 支持。
	- 能偽裝成前面的資料庫。

## django shell
- 集成了 python 環境的 shell 終端。
- 通常在終端中做一些調適工作。

## 如何看待bug
- 看日誌
	- 先看第一條。
	- 在看最後一條。
- 整理思路
	- 程式在哪一個位置和預期出現偏差。


## 表關係
- 1:1 1對1
- 1:M 1對多
- M:N 多對多

## 快捷鍵
- control + p 
	- 參數提示。
	
- shift + f6 重命名. 重構。