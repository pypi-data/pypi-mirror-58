# Tushare Json方式
text1 = """
import requests
import pprint
import tushare
import pandas as pd
'''
Tushare金融大数据接口调用代码
接口网址：https: // tushare.pro/document/2
'''
# 格式化输出
pp = pprint.PrettyPrinter(width=80)
# apiURL
url = 'http://api.waditu.com'
token = '6cb93350f16e743007b2499fdea415eb456f9430254441ee110c5d12'
def get_info(api_name, params, fields_en, fields_zh):
    '''
获得接口数据
'''
    data = {
        'api_name': api_name,
        'token': token,
        'params': params,
        'fields': fields_en,
    }
    # 获得数据
    info = requests.post(url, json=data)
    # pp.pprint(info.json()['data']['items'])
    fields = info.json()['data']['fields']
    # pp.pprint(info.json()['data']['items'])
    data = info.json()['data']['items']
    # 初始化数据帧
    df = pd.DataFrame(data, columns=fields_zh)
    # df = pd.DataFrame(data, columns=fields)
    print(df)
    return df
def pd2excel(df):
    df.to_excel('output.xlsx', na_rep='', index=False)
    return
if __name__ == '__main__':
    # 接口名称
    api_name = 'monthly'
    # 输入参数
    params = {
        'ts_code': '601588.SH',
        'trade_date': '20171229',
    }
    # 字段列表
    fields_en = "ts_code,trade_date,close"
    fields_zh = ['股票代码', '交易日期', '月收盘价']
    df = get_info(api_name, params, fields_en, fields_zh)
    # 向excel输出
    pd2excel(df)
"""


# Tushare Sdk使用
text2 = """
import tushare as ts
import pandas as pd
import pprint

pro = ts.pro_api('your token')


def get_info(ts_code):
    # df = pro.index_monthly(ts_code=ts_code, start_date='20130101', end_date='20171231', fields='ts_code,trade_date,close')
    # df = pro.monthly(ts_code=ts_code, start_date='20070101', end_date='20071231', fields='ts_code,trade_date,close')
    # df = ts.pro_bar(ts_code=ts_code, freq='M', adj='hfq', start_date='20130101', end_date='20171231')
    df = pro.daily(ts_code=ts_code, start_date='20171201',end_date='20180101', fields='ts_code,trade_date,close,vol,amount')
    # df = pro.hk_hold(ts_code=ts_code,trade_date='20151231', exchange='SH')
    return df


def pd2excel(df):
    df.to_excel('output.xlsx', na_rep='', index=False)
    return


if __name__ == '__main__':
    ts_code = "600177.SH"
    df = get_info(ts_code)
    pprint.pprint(df)
    pd2excel(df)
"""


# Tushare普通接口
text3 = """
import tushare as ts

df = ts.get_k_data('600388', ktype='D',
                   start='2018-05-01', end='2018-05-10', autype='None')

df.to_csv('output.csv', na_rep='', index=False)
"""


# Tushare常用接口文档
text4 = """
# Tushare常用接口文档

[TOC]

## 股票列表

接口：stock_basic
描述：获取基础信息数据，包括股票代码、名称、上市日期、退市日期等

输入参数

| 名称        | 类型 | 必选 | 描述                                           |
| :---------- | :--- | :--- | :--------------------------------------------- |
| is_hs       | str  | N    | 是否沪深港通标的，N否 H沪股通 S深股通          |
| list_status | str  | N    | 上市状态： L上市 D退市 P暂停上市               |
| exchange    | str  | N    | 交易所 SSE上交所 SZSE深交所 HKEX港交所(未上线) |

输出参数

| 名称        | 类型 | 描述                                   |
| :---------- | :--- | :------------------------------------- |
| ts_code     | str  | TS代码                                 |
| symbol      | str  | 股票代码                               |
| name        | str  | 股票名称                               |
| area        | str  | 所在地域                               |
| industry    | str  | 所属行业                               |
| fullname    | str  | 股票全称                               |
| enname      | str  | 英文全称                               |
| market      | str  | 市场类型 （主板/中小板/创业板/科创板） |
| exchange    | str  | 交易所代码                             |
| curr_type   | str  | 交易货币                               |
| list_status | str  | 上市状态： L上市 D退市 P暂停上市       |
| list_date   | str  | 上市日期                               |
| delist_date | str  | 退市日期                               |
| is_hs       | str  | 是否沪深港通标的，N否 H沪股通 S深股通  |

接口示例 

```python
pro = ts.pro_api()

#查询当前所有正常上市交易的股票列表

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

#查询当前所有正常上市交易的股票列表

data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

```

## 日线行情

 接口：daily
数据说明：交易日每天15点～16点之间。本接口是未复权行情，停牌期间不提供数据。
调取说明：基础积分每分钟内最多调取200次，每次4000条数据，相当于超过18年历史，用户获得超过5000积分无频次限制。 

输入参数 

| 名称       | 类型 | 必选 | 描述               |
| :--------- | :--- | :--- | :----------------- |
| ts_code    | str  | N    | 股票代码（二选一） |
| trade_date | str  | N    | 交易日期（二选一） |
| start_date | str  | N    | 开始日期(YYYYMMDD) |
| end_date   | str  | N    | 结束日期(YYYYMMDD) |

注：日期都填YYYYMMDD格式，比如20181010

输出参数

| 名称       | 类型  | 描述                                                         |
| :--------- | :---- | :----------------------------------------------------------- |
| ts_code    | str   | 股票代码                                                     |
| trade_date | str   | 交易日期                                                     |
| open       | float | 开盘价                                                       |
| high       | float | 最高价                                                       |
| low        | float | 最低价                                                       |
| close      | float | 收盘价                                                       |
| pre_close  | float | 昨收价                                                       |
| change     | float | 涨跌额                                                       |
| pct_chg    | float | 涨跌幅 （未复权，如果是复权请用 [通用行情接口](https://tushare.pro/document/2?doc_id=109) ） |
| vol        | float | 成交量 （手）                                                |
| amount     | float | 成交额 （千元）                                              |

接口示例 

```python
pro = ts.pro_api()

df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')
#or

df = pro.query('daily', ts_code='000001.SZ', start_date='20180701', end_date='20180718')
#or 通过日期取历史某一天的全部历史
df = pro.daily(trade_date='20180810')
```

## 周线行情

 接口：weekly
描述：获取A股周线行情
限量：单次最大3700，总量不限制

输入参数

| 名称       | 类型 | 必选 | 描述                                        |
| :--------- | :--- | :--- | :------------------------------------------ |
| ts_code    | str  | N    | TS代码 （ts_code,trade_date两个参数任选一） |
| trade_date | str  | N    | 交易日期 （每周五日期，YYYYMMDD格式）       |
| start_date | str  | N    | 开始日期                                    |
| end_date   | str  | N    | 结束日期                                    |

输出参数 

| 名称       | 类型  | 默认显示 | 描述                                                         |
| :--------- | :---- | :------- | :----------------------------------------------------------- |
| ts_code    | str   | Y        | 股票代码                                                     |
| trade_date | str   | Y        | 交易日期                                                     |
| close      | float | Y        | 周收盘价                                                     |
| open       | float | Y        | 周开盘价                                                     |
| high       | float | Y        | 周最高价                                                     |
| low        | float | Y        | 周最低价                                                     |
| pre_close  | float | Y        | 上一周收盘价                                                 |
| change     | float | Y        | 周涨跌额                                                     |
| pct_chg    | float | Y        | 周涨跌幅 （未复权，如果是复权请用 [通用行情接口](https://tushare.pro/document/2?doc_id=109) ） |
| vol        | float | Y        | 周成交量                                                     |
| amount     | float | Y        | 周成交额                                                     |

接口用法

```python
pro = ts.pro_api()

df = pro.weekly(ts_code='000001.SZ', start_date='20180101', end_date='20181101', fields='ts_code,trade_date,open,high,low,close,vol,amount')

#or
df = pro.weekly(trade_date='20181123', fields='ts_code,trade_date,open,high,low,close,vol,amount')
```

## 月线行情

接口：monthly
描述：获取A股月线数据
限量：单次最大3700，总量不限制
积分：用户需要至少300积分才可以调取，具体请参阅[积分获取办法](https://tushare.pro/document/1?doc_id=13)

**输入参数**

| 名称       | 类型 | 必选 | 描述                                              |
| :--------- | :--- | :--- | :------------------------------------------------ |
| ts_code    | str  | N    | TS代码 （ts_code,trade_date两个参数任选一）       |
| trade_date | str  | N    | 交易日期 （每月最后一个交易日日期，YYYYMMDD格式） |
| start_date | str  | N    | 开始日期                                          |
| end_date   | str  | N    | 结束日期                                          |

**输出参数**

| 名称       | 类型  | 默认显示 | 描述                                                         |
| :--------- | :---- | :------- | :----------------------------------------------------------- |
| ts_code    | str   | Y        | 股票代码                                                     |
| trade_date | str   | Y        | 交易日期                                                     |
| close      | float | Y        | 月收盘价                                                     |
| open       | float | Y        | 月开盘价                                                     |
| high       | float | Y        | 月最高价                                                     |
| low        | float | Y        | 月最低价                                                     |
| pre_close  | float | Y        | 上月收盘价                                                   |
| change     | float | Y        | 月涨跌额                                                     |
| pct_chg    | float | Y        | 月涨跌幅 （未复权，如果是复权请用 [通用行情接口](https://tushare.pro/document/2?doc_id=109) ） |
| vol        | float | Y        | 月成交量                                                     |
| amount     | float | Y        | 月成交额                                                     |

**接口用法**

```python
pro = ts.pro_api()

df = pro.monthly(ts_code='000001.SZ', start_date='20180101', end_date='20181101', fields='ts_code,trade_date,open,high,low,close,vol,amount')
```

或者

```python
df = pro.monthly(trade_date='20181031', fields='ts_code,trade_date,open,high,low,close,vol,amount')
```

## A股复权行情

**接口名称** ：pro_bar
**接口说明** ：复权行情通过[通用行情接口](https://tushare.pro/document/2?doc_id=109)实现，利用Tushare Pro提供的[复权因子](https://tushare.pro/document/2?doc_id=28)进行计算，目前暂时只在SDK中提供支持，http方式无法调取。
**Python SDK版本要求**： >= 1.2.26

 **复权说明**

| 类型   | 算法                                     | 参数标识 |
| :----- | :--------------------------------------- | :------- |
| 不复权 | 无                                       | 空或None |
| 前复权 | 当日收盘价 × 当日复权因子 / 最新复权因子 | qfq      |
| 后复权 | 当日收盘价 × 当日复权因子                | hfq      |

注：目前支持A股的日线/周线/月线复权，分钟复权稍后支持

 **接口参数**

| 名称       | 类型 | 必选 | 描述                                                         |
| :--------- | :--- | :--- | :----------------------------------------------------------- |
| ts_code    | str  | Y    | 证券代码                                                     |
| pro_api    | str  | N    | pro版api对象                                                 |
| start_date | str  | N    | 开始日期 (格式：YYYYMMDD)                                    |
| end_date   | str  | N    | 结束日期 (格式：YYYYMMDD)                                    |
| asset      | str  | Y    | 资产类别：E股票 I沪深指数 C数字货币 F期货 FD基金 O期权，默认E |
| adj        | str  | N    | 复权类型(只针对股票)：None未复权 qfq前复权 hfq后复权 , 默认None |
| freq       | str  | Y    | 数据频度 ：1MIN表示1分钟（1/5/15/30/60分钟） D日线 ，默认D   |
| ma         | list | N    | 均线，支持任意周期的均价和均量，输入任意合理int数值          |

日线复权

```python
#取000001的前复权行情
df = ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20180101', end_date='20181011')

#取000001的后复权行情
df = ts.pro_bar(ts_code='000001.SZ', adj='hfq', start_date='20180101', end_date='20181011')
```

周线复权

```python
#取000001的周线前复权行情
df = ts.pro_bar( ts_code='000001.SZ', freq='W', adj='qfq', start_date='20180101', end_date='20181011')

#取000001的周线后复权行情
df = ts.pro_bar(ts_code='000001.SZ', freq='W', adj='hfq', start_date='20180101', end_date='20181011')
```

月线复权

```python
#取000001的月线前复权行情
df = ts.pro_bar(ts_code='000001.SZ', freq='M', adj='qfq', start_date='20180101', end_date='20181011')

#取000001的月线后复权行情
df = ts.pro_bar(ts_code='000001.SZ', freq='M', adj='hfq', start_date='20180101', end_date='20181011')
```

## 通用行情接口

**接口名称**：pro_bar
**更新时间**：股票和指数通常在15点～17点之间，数字货币实时更新，具体请参考各接口文档明细。
**描述**：目前整合了股票（未复权、前复权、后复权）、指数、数字货币、ETF基金、期货、期权的行情数据，未来还将整合包括外汇在内的所有交易行情数据，同时提供分钟数据。
**其它**：由于本接口是集成接口，在SDK层做了一些逻辑处理，目前暂时没法用http的方式调取通用行情接口。用户可以访问Tushare的Github，查看源代码完成类似功能。

输入参数

| 名称       | 类型 | 必选 | 描述                                                         |
| :--------- | :--- | :--- | :----------------------------------------------------------- |
| ts_code    | str  | Y    | 证券代码                                                     |
| api        | str  | N    | pro版api对象，如果初始化了set_token，此参数可以不需要        |
| start_date | str  | N    | 开始日期 (格式：YYYYMMDD)                                    |
| end_date   | str  | N    | 结束日期 (格式：YYYYMMDD)                                    |
| asset      | str  | Y    | 资产类别：E股票 I沪深指数 C数字货币 FT期货 FD基金 O期权 CB可转债（v1.2.39），默认E |
| adj        | str  | N    | 复权类型(只针对股票)：None未复权 qfq前复权 hfq后复权 , 默认None |
| freq       | str  | Y    | 数据频度 ：支持分钟(min)/日(D)/周(W)/月(M)K线，其中1min表示1分钟（类推1/5/15/30/60分钟） ，默认D。目前有120积分的用户自动具备分钟数据试用权限（每分钟5次），正式权限请在QQ群私信群主。 |
| ma         | list | N    | 均线，支持任意合理int数值                                    |
| factors    | list | N    | 股票因子（asset='E'有效）支持 tor换手率 vr量比               |
| adjfactor  | str  | N    | 复权因子，在复权数据是，如果此参数为True，返回的数据中则带复权因子，默认为False。 该功能从1.2.33版本开始生效 |

输出指标

具体输出的数据指标可参考各行情具体指标：

股票Daily：https://tushare.pro/document/2?doc_id=27

基金Daily：https://tushare.pro/document/2?doc_id=127

期货Daily：https://tushare.pro/document/2?doc_id=138

期权Daily：https://tushare.pro/document/2?doc_id=159

指数Daily：https://tushare.pro/document/2?doc_id=95

数字货币：https://tushare.pro/document/41?doc_id=4

接口用例

```python
#取000001的前复权行情
df = ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20180101', end_date='20181011')

ts_code     trade_date     open     high    low    close  trade_date
20181011    000001.SZ   20181011  1085.71  1097.59  1047.90  1065.19
20181010    000001.SZ   20181010  1138.65  1151.61  1121.36  1128.92
20181009    000001.SZ   20181009  1130.00  1155.93  1122.44  1140.81
20181008    000001.SZ   20181008  1155.93  1165.65  1128.92  1128.92
20180928    000001.SZ   20180928  1164.57  1217.51  1164.57  1193.74
```

```python
#取上证指数行情数据

df = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20180101', end_date='20181011')

In [10]: df.head()
Out[10]:
     ts_code trade_date      close       open       high        low
0  000001.SH   20181011  2583.4575  2643.0740  2661.2859  2560.3164
1  000001.SH   20181010  2725.8367  2723.7242  2743.5480  2703.0626
2  000001.SH   20181009  2721.0130  2713.7319  2734.3142  2711.1971
3  000001.SH   20181008  2716.5104  2768.2075  2771.9384  2710.1781
4  000001.SH   20180928  2821.3501  2794.2644  2821.7553  2791.8363

   pre_close    change  pct_chg          vol       amount
0  2725.8367 -142.3792     -5.2233  197150702.0  170057762.5
1  2721.0130    4.8237      0.1773  113485736.0  111312455.3
2  2716.5104    4.5026      0.1657  116771899.0  110292457.8
3  2821.3501 -104.8397     -3.7159  149501388.0  141531551.8
4  2791.7748   29.5753      1.0594  134290456.0  125369989.4
```

```python
#均线

df = ts.pro_bar(ts_code='000001.SZ', start_date='20180101', end_date='20181011', ma=[5, 20, 50])
```

注：Tushare pro_bar接口的均价和均量数据是动态计算，想要获取某个时间段的均线，必须要设置start_date日期大于最大均线的日期数，然后自行截取想要日期段。例如，想要获取20190801开始的3日均线，必须设置start_date='20190729'，然后剔除20190801之前的日期记录。

```python
#换手率tor，量比vr

df = ts.pro_bar(ts_code='000001.SZ', start_date='20180101', end_date='20181011', factors=['tor', 'vr'])
```

**说明**

对于pro_api参数，如果在一开始就通过 ts.set_token('xxxx') 设置过token的情况，这个参数就不是必需的。

例如：

```python
df = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20180101', end_date='20181011')
```

## 通用行情接口Old

 get_k_data()

输入参数

| 名称   | 类型 | 必选 | 描述                                                         |
| :----- | :--- | :--- | :----------------------------------------------------------- |
| code   | str  | Y    | 证券代码：支持沪深A、B股, 支持全部指数, 支持ETF基金          |
| ktype  | str  | N    | 数据类型：默认为D日线数据, D=日k线 W=周 M=月, 5=5分钟 15=15分钟, 30=30分钟 60=60分钟 |
| start  | str  | N    | 开始日期 (格式：YYYY-MM-DD 为空时取当前日期)                 |
| end    | str  | N    | 结束日期 (格式：YYYY-MM-DD)                                  |
| autype | str  | N    | 复权类型：qfq-前复权 hfq-后复权 None-不复权，默认为qfq       |
| index  | str  | N    | 是否为指数：默认为False, 设定为True时认为code为指数代码      |

**输出参数**

| 名称   | 类型  | 默认显示 | 描述                                                         |
| :----- | :---- | :------- | :----------------------------------------------------------- |
| date   | str   | Y        | 日期和时间: 低频数据时为：YYYY-MM-DD, 高频数为：YYYY-MM-DD HH:MM |
| open   | float | Y        | 开盘价                                                       |
| close  | float | Y        | 收盘价                                                       |
| high   | float | Y        | 最高价                                                       |
| low    | float | Y        | 最低价                                                       |
| volume | float | Y        | 成交量                                                       |
| code   | float | Y        | 证券代码                                                     |
"""
