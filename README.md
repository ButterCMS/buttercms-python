# buttercms-python

Python Library for ButterCMS API. 

## Documentation

For a comprehensive list of examples, check out the [API documentation](https://buttercms.com/docs/api/).

## Jump to:

* [Posts](#posts)
* [Authors](#authors)
* [Categories](#categories)
* [Feeds](#feeds)
* [Content Fields](#content-fields)

## Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    pip install buttercms-python


## Usage

Getting started with the ButterCMS API couldn't be easier. Use your authorization token to create a ButterCMS client.

```python
from butter_cms import ButterCMS

auth_token = "XXXXXXXXXXXXXXXXXXX"
client = ButterCMS(auth_token)
```

All methods return dictionaries. The data can be navigated using keys and indexes like the example below.

```python
response = client.posts.all()

posts = response['data'] 
# posts now contains a list of post dictionaries

my_post = posts[0]
# my_post contains the first returned post

print(my_post)
# {
#   "url": "http://www.example.com/blog/this-is-a-blog-post",
#   "created": "2015-06-12T13:59:32.441289Z",
#   "published": "2015-06-12T00:00:00Z",
#   ...
# }
```

### Making Calls

#### Posts

```python
client.posts.all({'page_size': 3, 'page': 1, 'exclude_body': 'true'})
```


```python
client.posts.get('hello-world')
```


```python
client.posts.search('query', page=1, page_size=10)
```


[To Top](#buttercms-python)

#### Authors

The Author's `.all()` and `.get()` method accept an optional `params` to add additional data to the repsonse.

* `{'include':'recent_posts'}`: Adds each author's posts under the `recent_posts` key in that author's returned dictionary

```python
client.authors.all()
client.authors.all({'include':'recent_posts'})
```


```python
client.authors.get('jennifer-smith')
client.authors.get('jennifer-smith', {'include':'recent_posts'})
```


[To Top](#buttercms-python)

#### Categories

The Category's `.all()` and `.get()` methods accept an optional `params` to add additional data to the repsonse.

* `{'include':'recent_posts'}`: Adds posts tagged with that category under the `recent_posts` key in that category's returned dictionary

```python
client.categories.all()
client.categories.all({'include':'recent_posts'})
```


```python
client.categories.get('product-updates')
client.categories.get('product-updates', {'include':'recent_posts'})
```


[To Top](#buttercms-python)


#### Tags

The Tag's `.all()` and `.get()` methods accept an optional `params` to add additional data to the repsonse.

* `{'include':'recent_posts'}`: Adds posts tagged with that tag under the `recent_posts` key in that tag's returned dictionary

```python
client.tags.all()
client.tags.all({'include':'recent_posts'})
```


```python
client.tags.get('product-updates')
client.tags.get('product-updates', {'include':'recent_posts'})
```


[To Top](#buttercms-python)

#### Feeds

```python
client.feeds.get('rss')
```


```python
client.feeds.get('atom')
```


```python
client.feeds.get('sitemap')
```


[To Top](#buttercms-python)

#### Content Fields

```python
client.content_fields.get(['homepage_headline', 'homepage_title'])
```


[To Top](#buttercms-python)
