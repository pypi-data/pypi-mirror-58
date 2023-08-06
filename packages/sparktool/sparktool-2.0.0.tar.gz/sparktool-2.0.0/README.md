sparktool
========
built to simplified the process of creating sparksession(hccn).

What's New
========
* parser impala/hive view automatically
* use hive cmd to find real kudu.table_name

features
========
* change kudu table to spark view automatically
* split and execute sql scripts
* can parser impala/hive view automatically

install
=======

Python 2/3 

* `pip install sparktool`

functions
=======
reset keytab
--------

[in]

```python
# encoding=utf-8
import sparktool as st

st.switch_keytab('admin@EXAMPLE.COM', keytabpath)
```


execute sql
--------

[in]

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

[out]

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