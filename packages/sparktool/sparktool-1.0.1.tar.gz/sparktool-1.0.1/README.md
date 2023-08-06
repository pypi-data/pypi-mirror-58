sparktool
========
built to simplified the process of creating sparksession(hccn).

特点
========
* 自动识别kudu表转换为临时视图
* 拆分并批量执行sql脚本
* 暂时不支持读取视图的功能
* MIT 授权协议

安装
=======

代码对 Python 2/3 均兼容

* 自动安装： `pip install sparktool`


功能
=======
重置keytab认证, 首次运行库时建议执行
--------

代码示例

```python
# encoding=utf-8
import sparktool as st

st.switch_keytab('admin@EXAMPLE.COM', keytabpath)
```

识别kudu表并批量执行sql脚本
--------

代码示例

```python
# encoding=utf-8
import sparktool as st

ss = st.SparkCreator(appname='ryan_ttt', param={"spark.task.maxFailures":"10"})
sql = '''
select 1;
select
    cc.skp_client
from
    owner_ogg.ft_ccase_2_ccase_ad cc
    join owner_ogg.clt_ccase_2_ccase_relation re
      on cc.skp_ccase_2_ccase_relation = re.skp_ccase_2_ccase_relation
     and re.code_ccase_relation = 'FIRST_POS' 
limit 1
;
'''
ss.batch_excutesql(sql)
```

输出

```python
Tranform Table:
+--------------------------------------+--------------------------------------+--------------+
|             Origin Table             |            Temporary View            | If Transform |
+--------------------------------------+--------------------------------------+--------------+
|    OWNER_OGG.FT_CCASE_2_CCASE_AD     |    owner_ogg_ft_ccase_2_ccase_ad     |     New      |
| OWNER_OGG.CLT_CCASE_2_CCASE_RELATION | owner_ogg_clt_ccase_2_ccase_relation |     New      |
+--------------------------------------+--------------------------------------+--------------+
Excute Progress: 2/2
DataFrame[skp_client: decimal(38,0)]
```