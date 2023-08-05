# domainhelper -- 域名助手

> 支持 python2，python3

功能：
1. verify_domain(domain)  
    验证域名是否正确
    ```
    in:  verify_domain('a.b.c.www.baidu.com.cn')
    out: True
    ```
   
2. get_domain_suffix(domain)  
    获取域名后缀  
    示例：
    ```
    in:  get_domain_suffix('a.b.c.www.baidu.com.cn')
    out: '.com.cn'
    ```
    
3. get_top_domain(domain)  
    获取顶级域名  
    示例： 
    ```
    in:  get_top_domain('a.b.c.www.baidu.com.cn') 
    out: 'baidu.com.cn'
    ```
4. get_multi_domain(domain)  
    获取次级域名  
    示例：  
    ```
    in:  get_multi_domain('a.b.c.www.baidu.com.cn')
    out: ['baidu.com.cn', 'www.baidu.com.cn', 'c.www.baidu.com.cn', 'b.c.www.baidu.com.cn', 'a.b.c.www.baidu.com.cn']
    ```
注意：
参数domain 必须是 str 类型