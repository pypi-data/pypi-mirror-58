# time_utils

Basic python package to time processes similar to a stopwatch.  This package also includes various pre-formated timestamps for sql, s3 key prefixes, and s3 glues prefixes.

### stopWatch 

A class intended to minimic the functionality of a stop watch.  The lap function will return a human readable string of how much total time was elapsed as well as the lap time.  

basic usage:
```python
>>> from time_utils import time_utils as tu
>>> sw = tu.stopWatch()
>>> sw.lap()
Total Time:
4 second(s)

Lap 1:
4 second(s)

datetime.timedelta(seconds=4, microseconds=218298)
>>> sw.lap()
Total Time:
15 second(s)

Lap 2:
11 second(s)

datetime.timedelta(seconds=11, microseconds=440822)
```

### preformatted datetime outputs
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
