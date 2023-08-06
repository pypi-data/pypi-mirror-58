# ogpparser
Open Graph Protocolのタグを取得

## インストール方法

```
pip install ogpparser
```

## 使用方法

```python
from ogpparser import ogpparser

result = ogpparser('https://github.com/reeve0930/ogpparser')
```

## 出力

```json
{
    "image": "https://avatars1.githubusercontent.com/u/38152917?s=400&v=4", 
    "site_name": "GitHub", 
    "type": "object", 
    "title": "reeve0930/ogpparser", 
    "url": "https://github.com/reeve0930/ogpparser", 
    "description": "Open Graph Protocolのタグを取得. Contribute to reeve0930/ogpparser development by creating an account on GitHub."
}
```