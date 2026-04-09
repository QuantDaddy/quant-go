'''
指数日线行情
'''
import tushare as ts

import db_utils as db   


token = db.select("SELECT token FROM token_t WHERE id = 1").token[0]

ts.set_token(str(token))

# 2. 初始化pro接口
pro = ts.pro_api()

try:
    df = pro.stock_basic(list_status='L', 
                         fields='ts_code,symbol,name,industry,market,list_date')
    
    # 4. 查看结果
    print(f"查询成功，共获取 {len(df)} 只股票信息。")
    print("\n前10只股票信息预览：")
    print(df.head(10))
    
    # 5. (可选) 将数据保存到本地CSV文件
    # df.to_csv('stock_list.csv', index=False, encoding='utf-8-sig')
    # print("\n数据已保存至 stock_list.csv")

except Exception as e:
    print(f"查询出错: {e}")