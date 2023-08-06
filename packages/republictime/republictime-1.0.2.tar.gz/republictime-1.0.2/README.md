___
## Republic Time : Python module to access latest news and more from republictime.com.
**Republic Time** module is a **Reusable python app** which provides a features to access latest news and more from republictime.com.
___


## Installation:
You can install **Republic Time** module from PyPI using **pip**.
``` pip install republictime ```
___


## Configuration :
1\. In order to use **Republic Time** module it required an **API Key**, You can generate the API Key from **[republictime.com](http://republictime.pythonanywhere.com/)**.

2\. Open your **Text Editor/Python CLI** and write the **following code**.
```python
from republictime.articles import Article
article = Article("article", "PASTE_YOUR_CRICAPI_API_KEY_HERE")
```

3\. Access **Breaking News** from **Republic Time**.
>> To access Breaking News it requires to invoke the get_article() method.
```python
article.get_article()
```

4\. Access **Promoted News** from **Republic Time**.
>> To access Promoted News it requires to set ```promoted=True```.
```python
article.get_article(promoted=True)
```

5\. Access **Trending News** from **Republic Time**.
>> To access the Trending News it requires to set ```trending=True```.
```python
article.get_article(trending=True)
```

6\. Access both **Promoted & Trending News** from **Republic Time**.
>> To access Promoted & Trending News it requires to set ```promoted=True, trending=True```.
```python
article.get_article(promoted=True, trending=True)
```
___