## DataClient

### Introduction
this is a request tool which packaging method server

### Usage
1. init requester
```python
from stormer import Requester
requester = Requester(host="www.baidu.com")

```

2. register method
```python
requester.register(action="get", func="bd_download", uri="download")
```

3. call method
```python
rlt = requester.bd_download()
response = rlt.resp
print(response)
```




