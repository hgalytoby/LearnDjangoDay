# Day03

## 模板中的點語法
- 字典查詢
- 屬性或方法
	- grade.gname    
- 索引
	- 第0個 grades.0.gname
	- 第1個 grades.1.gname
		

## 模板中的標籤
- 語法 {% tag %}
- 作用
	1.加載外部傳入的變量
	2.在輸出中創建文本
	3.控制循環或邏輯
- 格式
	- if
		- 第一種
			```
			{% if 表達式 %}
				語句
			{% endif %}
			```
		- 第二種
			```
			{% if 表達式 %}
				語句
			{% else %}
				語句
			{% endif %}
			```
		- 第三種
			```
			{% if 表達式 %}
				語句
			{% elif 表達式 %}
				語句
			{% endif %}
			```
	
	- for 
		- empty 空的
			```
			{% for 變量 in 列表 %}
				語句1
			{% empty %}
				語句2 
			{% endfor %}
			```
		- forloop
			- {{ forloop.counter }}
				- 表示當前第幾次循環，從1開始。
			- {{ forloop.counter0 }}
				- 表示當前第幾次循環，從0開始。
			- {{ forloop.recounter }}
				- 表示當前第幾次循環，最後開始到 0 停。
			- {{ forloop.recounter1 }}
				- 表示當前第幾次循環，最後開始到 1 停。
			- {{ forloop.first }}
				- 第一個值
			- {{ forloop.last }}
				- 最後一個值
				
	- 單行注釋
		- {# 被注釋掉的內容 #}
		
	- 多行注釋
		- 
		```
		{% comment %}
			內容
		{% endcomment %}
		```
		
	- 乘除
		- {% widthratio 數 分母 分子 %}
		
	- 除法
		- {% if num|divisibleby:2 %}
	
	- ifequal 如果相等
		- 
		```
		{% ifequal value1 value2 %}
			語句
		{% end ifequal %}
		```
	- ifnotequal 如果不相等
	
	- url: 反向解析
		- {% 'namespace:name' p1 p 2 %}
		
	- csrf_token 用於跨站請求偽造保護
		- 格式{% crsf_token %}
	
	- 過濾器
		- {{ var|過濾器 }}
	
	- 作用
		- 在變量顯示前修改
		- 加	
		```
	    add {{ p.page|add:5 }}
	    ```
		- 減
		```
		add {{ p.page|add:-5 }}
        ```
		- lower 轉大寫
		```
		{{ p.page|lower }}
	    ```
		- upper 轉小寫
		```
		{{ p.page|upper }}
		```
		- join 
		```
        - {{ p.page|join='內容' }}
            - p.page = 123
            - {{ p.page|join='7' }}
                - 映出 172737
		```
		- 預設值: default
		```
        {{ var|default value }}
        如果變量沒有被提供或者為 False, 空, 會使用默認值
		```
		- 日期轉字符串
		```
		{{ dateVal|date:'y-m-d' }}
	    ```
	
	- HTML轉譯
		- 將接收到的數據當成普通字串處理還是當作HTML碼來渲染的一個問題
		- 渲染成 html: {{ code|safe }}，小心使用不然會被注入 javascript 攻擊。
		
		```
		{% autoescape off %}
			code
		{% endautoescape %}
		```	
		- 不想渲染 
		```
		{% autoescape on %}
			code
		{% endautoescape %}
		```
			
## 快捷鍵
- control + d 複製一行，插入到下面。
- alt + shift + 上或下 ，移動一行。


## 標籤
- {% %} 標示符
- 標籤分為標籤和成對的標籤
- 成對的標籤切記不能忽略，開始標籤和結束標籤。 
	

## 結構標籤
- block
	- 块
	- 用來規劃佈局
	- 首次出現，代表規劃。
	- 第二次出現，代表填充以前的規劃。
	- 第三次出現，代表填充以前的規劃，默認動作是覆蓋。
		- 如果不想覆蓋，可以添加{{ block.super }}
		- 這樣就能實現增量是操作。

- extends
	- 繼承
	- 可以獲取父模板中的所有結構

- block + entends 
	- 化整為零。

- include
	- 包含
	- 可以將頁面作為一部份，嵌入到其他頁面中。

- include + block
	- 由零聚一

- 三個標籤也可以混合使用
- 能用 block + entends 搞定的就盡量不要使用 include
- 如果我們繼承自一個父模板，子模板自己直接重寫頁面結構是不生效的，只能在既有的坑中進行填充。


## 靜態資源
- 動靜分離
- 創建靜態文件夾
- 在 settings 中註冊 STATICFILES_DIRS[]
- 在模板中使用
	- 先加載靜態資源 {% load static %}
	- 使用 {% static 'xxx' %} xxx 相對路徑
- 坑點
	- 僅在 debug 模式可以使用
	- 以後需要自己單獨處理

## urls
- 路由器
	- 按照列表的書寫順序進行匹配的。
	- 從上到下匹配，沒有最優匹配的概念。
		- Django 某一個板後更新後，變成re_path() 不會發生匹配的問題。
			- 例子
				- path('abc/', views.abc) 
				- repath(r'^abc/d/' views.abcd)
				
- 路由規則編寫
	- 通常使用指定以^開頭。
	- 在結尾處添加反斜線。

- 路由路徑中的參數使用 () 進行獲取。
	- 一個圓括號對應視圖函數中的一個參數。 
	- 參數
		- 路徑參數
			- 位置參數
				- 按照書寫順序進行匹配。
			- 關鍵字參數
				- 按照參數名稱匹配，和順序就無關了。
		- 參數個數必須和視圖函數參數個數一致(除了默認的 request以外)

- 反向解析
	- 根據根路由中註冊的 namespqce 和在子路由中註冊 name，這兩個參數來動態獲取我們的路徑。
	- 在模板中使用 {% url 'namespace:name' %}。
	- 如果帶有位置 {% url 'namespace:name' value1 value2 ... %}
	- 如果帶有關鍵字參數 {% url 'namespace:name' key=value key=value... %}


## 錯誤頁面定制
- 在模板中重寫對應錯誤狀態碼頁面
- 關閉Debug
- 實現原則
	- 就近原則
		

## 雙R
- Request
	- 內置屬性
		- method
		- path
		- GET
			- 類字典結構
			- 一個 Key 允許對應多個值
			- get
			- getlist
		- POST
		- META
			- 各種客戶端訊息
			- REMOTE_ADDR 遠端訪問IP
			
- Response



## 知識點
- locals
	- 內置函數
	- 將局部變量，使用字典的方式進行打包。
	- key 是變量名，value 是變量中儲存的的資料。
		





## Python 內存分配
- 垃圾回收使用引用計數器
	- Python 中的注釋
		- 單行注釋 #
		- 多行注釋 """ """
- id([1,2,3]) == id([4,5,6])
	- 存在賦值符號 = 才會進行內存劃分
	- 沒有賦值，直接調用會在臨時緩衝區，id 獲取臨時緩衝區的內容，id 一樣。

			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
