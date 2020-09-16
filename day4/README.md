# Day04

## MIME
- 作用: 制定傳輸資料使用哪種形式打開
- 格式: 大類型 / 小類型  
	- image/pang
	- image/jpg

## Json
- jsonObject
	- {]
	- key : value
- jsonArray
	- []
	- 列表中可以是普通資料類型，也可以是 jsonObject。
- jsonObject 和 jsonArray 可以嵌套
- 給移動端的 json
- 給 Ajax 
	- 前後端
	- DRF
	
	
## HttpResponse
- htppResponseRedirect
	- 重定向，暫時。
	- 302
	- 簡寫 redirect

- jsonResponse
	- 以 json 格式返回資料
	- 重寫了 \__init__，指定content_type
	
- HttpResponsePermanentRedirect
	- 重定向，永久性。
	- 301
	
- HttpResponseBadRequest
	- 400

- HttpResponseNotFound
	- 404

-  HttpResponseForbidden
	- 405

- HttpResponseNotAllowed
	- 405

- HttpResponseServerError
	- 500

- Http404
	- Exception
	- raise 主動拋異常出來

## 會話技術
- 出現場景
	- 伺服器如何辨識客戶端。
	- Http 在 Web 開發中基本都是短連接。
	
- 請求生命週期
	- 從 Request 開始
	- 到 Response 結束

- 種類
	- Cookie
		- 客戶端會話技術
			- 資料儲存在客戶端
		- 鍵值對儲存
		- 支持過期時間
		- 默認Cookie會自動攜帶，本網站所有 Cookie
		- Cookie 跨域名，跨網站
		- 通過 HttpResponse 
		- Cookie 默認不支持中文
		- 可以加鹽
			- 加密
			- 取得時需要解密
	- Session
		- 伺服器端會話技術。
		- 資料儲存在伺服器中。
		- 默認 Session 儲存在內存中。
		- Django 中默認會把 Session 持久化到資料庫中。
		- Django 中 Session 的默認過期時間是14天。
		- 主鍵是字符串。
		- 資料是使用了資料安全。
			- 使用 base64
			- 在前面添加了一個混淆串
		- Session 依賴於 Cookie
	- Token
		- 伺服端會話技術
		- 自定義的 Session
		- 如果 Web 頁面開發中，使用起來和 Session 基本一致。
		- 如果使用在移動端或客戶端開發中，通常以 Json 形式傳輸，需要移動端自動儲存 Token，需要取得 Token 關聯資料的時候，主動傳送 Token。
	- Cookie 和 Session，Token 對比
		- Cookie 使用更簡潔，伺服器壓力小，資料不是很安全。
		- Session  伺服器要維護 Session，相對安全。
		- Token 擁有 Session 所有優點，自己維護有點麻煩，支持更多的終端。
	
## CSRF
- 防跨站攻擊。
- 防止惡意註冊，確保客戶端是我們自己的客戶端。
- 使用了 cookie 中 csrftoken 進行驗證，傳輸。
- 服務端發送給客戶端，客戶端將 cookie 取出來，還要進行編碼轉換 (資料安全)。
- 如何實現的
	- 在我們存在 csrf_token 標籤的頁面中，響應會自動設置一個 cookie，csrftoken。
	- 當提交的時候，會自動驗證 csrftoken。
	- 驗證通過，正常執行以後流程，驗證不通過，直接 403。
	
	
## 目前狀態
- MTV
	- 基本完成。
	- Template 基本完成。
	- Views 基本完成。
	- Model
		- Model 關係。
		- Model 繼承。

- 高級
	- 第三方差件
	- 底成的部分原理
		- AOP 面相切面編程
			- 反扒。
			- 安全。
	- 文件上傳
	- 前後端分離。
		- RESTful
	- 日誌
	- 後台管理
	- 用戶角色，用戶權限
	- 部屬
	- 第三方支付
	

## 算法
- 編碼解碼
	- Base64
	- urlencode
- 摘要算法，指紋算法，雜湊算法
	- MD5，SHA
		- MD5 默認是 128 的二進制
		- 32 位的十六進制
		- 32 位的 Unicode
	- 單向不可逆的
	- 不管輸入多長，輸出都是固定長度
	- 只要輸入有任意的變更，輸入都會發生巨大的變化
	- 鑰匙一旦丟失，所有資料就全玩完了
- 加密
	- 對稱加密
		- 一把鑰匙
		- DES，AES
	- 非對稱加密
		- 兩把鑰匙，成對的
		- 公鑰和私鑰
		- RSA，PGP
		- 安全性最高
		- 算法複雜，需要時間長
		- 第三方支付大部分都是 RSA


## 編碼
- ASCII
- Unicode

	
## reverse
- Python 程式碼中的反向解析
- reverse('namespace:name')
- 位置參數
	- reverse('namespace:name', arg=(value1, value2 ...))
- 關鍵字參數
	- reverse('namespace:name', kwargs={key1:value1, key2:value2 ...})
	
	
## 登入
- 首先有一個頁面
	- 頁面中有輸入框
	- 有登入按鈕
- 點完登入，默認進入個人中心。
- 個人中心可以顯示用戶名。
	

## 爬蟲
- 模擬人去請求資料
- 提取資料
- 儲存資料


## 核心內容
- 資料爬取
- 資料提取
- 數據儲存
- 提升效率
	- 執行續
	- 處理程序
	- 協程