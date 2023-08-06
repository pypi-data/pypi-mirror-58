# time_utils

Basic python package to time processes similar to a stopwatch.  This package also includes various pre-formated timestamps for sql, s3 key prefixes, and s3 glues prefixes.

### stopWatch basic usage
```python
>>> from time_utils.time_utils import stopWatch
>>> sw = stopWatch()
>>> sw.lap()
Lap 1:
15 second(s)
datetime.timedelta(seconds=15, microseconds=693657)
>>> sw.lap()
Lap 2:
4 second(s)
datetime.timedelta(seconds=4, microseconds=751870)
```

### preformated datetime outputs
All functions default to utcnow(), however a datetime object can be passed in to any function.

#### ts_dict
```python
>>> tu.time_utils.ts_dict()
{
'year': '2019', 
'month': '12', 
'day': '29', 
'hour': '00', 
'min': '24', 
'sec': '43'
}
```

#### sql_ts
```python
>>> tu.time_utils.sql_ts()
'2019-12-29 00:25:00'
```

#### s3_ts
```python
>>> tu.time_utils.s3_ts()
'/2019/12/29/'
```

#### s3_glue_ts
```python
>>> tu.time_utils.s3_glue_ts()
'/year=2019/month=12/day=29/'
```
