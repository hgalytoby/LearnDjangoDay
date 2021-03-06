# Day02

## Model
- 在企業開發中，通常都是從資料開始開發的。
	
	
## ORM
- 對象關係映射。
- 可以理解為翻譯機。
- 核心思想，解耦合。
	- 將業務邏輯和SQL進行解耦。
	

## 資料庫中數據類型
- 字符串。
- 數字。
- 日期。

	
## 模型過濾
- filter
- exclude
- 連續使用
	- 鏈式調用
	- Person.objects.filter().fiter().xxx.exclude().exclude().yyy
	
	
## 快捷鍵
- .re 快捷生成 return
- .if 多用點看看世界的美好
	

## 方法
- 對象方法
	- 可以調用對象的屬性，也可以調用類的屬性。
- 類方法
	- 不能調用對象屬性，只能調用類屬性。
- 靜態方法
	- 什麼都不能調用，不能取得對象屬性，也不能取得類屬性。
	- 只是寄生在我們這個類上面而已。
	
	
## 狀態碼
- 2XX
	- 請求成功。
- 3XX
	- 轉發或重定向。
- 4XX
	- 客戶端錯誤。
- 5XX
	- 伺服器錯誤。
	- 後端開發人員最不想看到的。

		
## 獲取單個對象
- 查詢條件沒有匹配的對象，會出現異常，DoesNotExist。
- 如果查詢條件對應多個對象，會拋異常，MultipleObjectsReturned。
	

## first 和 last
- 默認情況下可以正常從QuerySet中獲得
- 隱藏 Bug
	- 可能會出現 fist 和 last 獲取到的是相同的對象。
		- 顯示， 手動寫排序規則。
			
			
## 切片
- 和 Python 中的切片不太一樣。
- QuerySet[5:15] 取得第五條到第十五條數據。
	- 相當於 SQL 中的 limit 和 offset
- 不支持負數查詢
	

## 緩存集
- filter
- exclude
- all
- 都不會真正去查資料庫
- 只有我們在迭代結果集，或者取得單個對象屬性的時候，才會去查資料庫。
- 懶查詢
	- 為了優畫我們結構和查詢。


## 查詢條件
- 屬性__運算符 = 值
- gt 大於
- gte 大於等於
- it 小於
- ite 小於等於
- in 在某一集合中
- range 在...範圍內
- year 日期字段的年份
- month 日期字段的月份
- day 日期字段的日
- isnull True/False
- contains 類似於 模糊查詢 like
- startswith 以 xx 開始 本質也是 like
- endswith 以 xx 結束 也是 like
- exact  精確查詢

- 前面同時添加 i，ignore 忽略大小寫
	- iexact
	- icontains
	- istartswith
	- iendswith
- django 中查詢條件有時區問題
	- 關閉 django 中自定義的時區。
		- settings.py 最下面 USE_TZ 改成 False
	- 在 資料庫中創建對應的時區表。


## 聚合函數
- 使用 aggregate()函數返回聚合函數的值
	- Avg: 平均值
	- Count: 數量
	- Max: 最大
	- Min: 最小
	- Sun 求和
	- Student.objects().aggregate(Max('sage'))
		
		
## F
- 可以取得我們屬性的值。
- 可以實現一個模型的不同屬性的運算操作。
- 還可以支持算術運算。
	

## Q
- 可以對條件封裝
- 封裝之後，可以支持邏輯運算
	- 與 & and 
	- 或 | or
	- 非 ~ not


## 模型成員
- 顯性屬性
	- 開發者手動書寫的屬性
- 隱性屬性
	- 開發者沒有書寫，ORM 自動生成的
	- 如果把隱性屬性手動聲明，系統就不會產生隱性屬性了。

	
	
## 定義屬性

### 概述
- django 根據屬性的類型確定以下信息。
	- 當前選擇的資料庫支持字段的類型。
	- 渲染管理表單時使用的默認 html 控件。
	- 在管理站點最低限度的驗證。

- django 會為表增加自動增長得主鍵列， 每個模型只能有一個主鍵列，如果使用選項設置某屬性為主鍵列後， 則 django 不會再生成默認的主鍵列。

- 屬性命名限制
	- 遵循標識福規則
	- 由於 django 的查詢方式， 不允許使用連續的下滑縣。


### 資料庫
- 定義屬性時，需要字段類型，字段類型被定義在 django.db.models.fields 目錄下，為了方便使用，被導入到 django.db.models 中。

- 使用方法
	- 導入 from django.db import models
	- 通過 models.Field 創建字段類型的對象，賦值給屬性。
	
	
### 邏輯刪除
- 對於重要資料都做邏輯刪除，不做物理刪除，實現方法式定義 isDelete 屬性，類行為 BooleanField，默認值為 False。
	
	
### 字段類型
- AutoField
	- 一個根據實際 ID 自動增長的 IntegerField，通常不指定如果不指定，一個主鍵字段就自動被添加到模型中。
	
- CharField(max_length=字符長度)
	- 字符串，默認的表單樣式是 TextInput。
	
- TextField
	- 大文本字段，一般超過 4000 使用，默認的表單控鍵是 Textarea。
	
- IntegerField
	- 整數。
	
- DecimalField(max_digits=None, decimal_places=None)
	- 使用 python 的 Decimal 實例表示的十進制浮點數。
	- 參數說明
		- DecimalField.max_digits
			- 位數總數
		- DecimalField.decimal_places
			- 小數點後的數字位數

- FloatField
	- 用 Python 的 float 實例來表示的浮點數。

- BooleanField
	- True / Flase 字段，此字段的默認表單控制是 CheckboxIpnut。
	
- NullBooleanField
	- 支持 Null、True、False 三種值。 

- DateField([auto_now=False, auto_now_add=False])
	- 使用 Python 的 datetime.date 實例表示的日期
	- 參數說明
		- DateField.auto_now
			- 每次保存對象時，自動設置該字段為當前時間，用於"最後一次修改"的時間戳， 它總是使用當前日期，默認為 False。
		- DateField.auto_now_add
			- 當對象第一次被創建時自動設置當前時間，用於創建的時間戳，它總是使用當前日期，默認為 False。
	- 說明
		- 該字段默認對應的表單控鍵是一個TextInput，在管理員站點添加一個JavaScript寫的日立控鍵，和一個Today的快捷按鈕，包含了一個額外的 invail
	- 注意
		- auto_now_add, auto_now, and default 這些設置是相互排斥的，他們之間的任何組合將會發生錯誤的結果。

- TimeField
	- 使用 Python 的 datetime.time 實例表示的時間， 參數如同DateField。

- DateTimeField
	- 使用 Python 的 datetime.datetime 實例表示的日期和時間，參數如同DateField。

- FileField
	- 一個上傳文字的字串。
	
- imageField
	- 繼承了FileField的所有屬性和方法，但對上傳的對象進行校驗，確保它是個有效的image。


## 字段選項
- 概述
	- 通過字段選項，可以實現對字段的約束。
	- 在字段對象時通過關鍵字參數指定。
	
- null
	- 如果是 True， Django 將空值以 Null 儲存到資料庫中，默認值是 False。

- blank 
	- 如果是 True，則該字段允許為空白，默認值是 False。

- 注意
	- null 是資料庫範疇的概念，則使用屬性的名稱。

- db_colum
	- 字段的名稱，如果未指定，則使用屬性的名稱。
	
- db_index
	- 若值為 True，則在表中會為此字段創建索引。

- default
	- 預設值。

- primary_key
	- 若為 True，則該字段會成為模型的主鍵字段。

- unique
	- 如果為 True，這個字段在表中必須有唯一值。


## 關係
- 分類
	- ForeiqnKey: 一對多，將字段定義在多的端中。
	- ManyToManyField: 多對多，將字段定義在兩端中。
	- OneToOneField: 一堆一，將字段定義在任意一端中。

- 用一訪問多
	- 格式
		- 對象.模型類小寫_set
	- 示範例子
		- grade.students_set
		
- 用一訪問一
	- 格式
		- 對象.模型類小寫
	- 示範例子
		- grade.students

- 訪問id
	- 格式
		- 對象.屬性_id
	- 示範例子
		- student.sqrade_id
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			