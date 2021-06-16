# Day15
### 需求
- 存在級聯資料
- 用戶和收貨地址
- 地址

### 分析
- 資料開始
    - 模型定義
    - 用戶和收貨地址 一對多
        - 用戶表
        - 地址表
            - ForeignKey
        - 序列化
            - 級聯資料如何序列化
        - 節流

### 節流器
- BaseThrottle
    - allow_request
        - 是否允許的請求的核心
    - get_ident
        - 取得客戶端的唯一標示
    - wait
- SimpleRateThrottle
    - get_cache_key
        - 取得緩存標示
    - get_rate
        - 取得頻率
    - parse_rate
        - 轉換頻率
            - num/duraction
                - duraction
                    - s
                    - m
                    - h 
                    - d
    - allow_request
        - 是否允許請求
        - 重寫方法
    - throttle_success
        - 允許請求，進行請求紀錄
    - throttle_failure
        - 不允許請求
    - wait 
        - 還有多少時間之後允許
- AnonRateThrottle
    - get_cache_key
        - 取得緩存原則
- UserRateThrottle
    - 和上面一模一樣
- ScopedRateThrottle
    - 和上面一樣
    - 多寫了從屬性中取得頻率


### 技能點
- HTTP_X_FORWARDED_FOR
    - 取得原始 IP
        - 通過普通的代理發送請求的請求
        - 如果取得 REMOTE_ADDR 取到的是代理 IP
- 代理
    - 普通代理
    - 高級代理
        - 效率越低，請求越慢
   