# buttercms-python

Python Library for ButterCMS API

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
client.posts.all(page=1, page_size=10)
```

```json
{
  "meta": {
    "count": 1,
    "next_page": null,
    "previous_page": null
  },
  "data": [
    {
      "url": "http://www.example.com/blog/this-is-a-blog-post",
      "created": "2015-06-12T13:59:32.441289Z",
      "published": "2015-06-12T00:00:00Z",
      "author": {
        "first_name": "API",
        "last_name": "Test",
        "email": "apitest@buttercms.com",
        "slug": "api-test",
        "bio": "This is my bio.",
        "title": "API",
        "linkedin_url": "https://www.linkedin.com/in/API",
        "facebook_url": "https://www.facebook.com/API",
        "twitter_handle": "buttercmsapi",
        "profile_image": "https://buttercms.com/api.png"
      },
      "categories": [
        {
          "name": "test category",
          "slug": "test-category"
        }
      ],
      "featured_image": null,
      "slug": "this-is-a-blog-post",
      "title": "This is a blog post",
      "body": "<p class=\"\">This is a blog post to test the API.</p>",
      "summary": "This is a blog post to test the API.",
      "seo_title": "This is a blog post",
      "meta_description": "This is a blog post to test the API.",
      "status": "published"
    }
  ]
}
```

```python
client.posts.get('hello-world')
```

```json
{
  "meta": {
    "next_post": null,
    "previous_post": {
      "slug": "google-analytics-is-now-integrated-with-your-butter-blog",
      "title": "Google Analytics is now integrated with your Butter blog",
      "featured_image": "https://d2devwt40at1e2.cloudfront.net/api/file/etSDYJUIFDADGEEAQ/"
    }
  },
  "data": {
    "url": "http://www.example.com/blog/this-is-a-blog-post",
    "created": "2015-06-12T13:59:32.441289Z",
    "published": "2015-06-12T00:00:00Z",
    "author": {
      "first_name": "API",
      "last_name": "Test",
      "email": "apitest@buttercms.com",
      "slug": "api-test",
      "bio": "This is my bio.",
      "title": "API",
      "linkedin_url": "https://www.linkedin.com/in/API",
      "facebook_url": "https://www.facebook.com/API",
      "pinterest_url": "https://www.pinterest.com/API",
      "instagram_url": "https://www.instagram.com/API",
      "twitter_handle": "buttercmsapi",
      "profile_image": "https://buttercms.com/api.png"
    },
    "categories": [
      {
        "name": "test category",
        "slug": "test-category"
      }
    ],
    "featured_image": null,
    "slug": "hello-world",
    "title": "This is a blog post",
    "body": "<p class=\"\">This is a blog post to test the API.</p>",
    "summary": "This is a blog post to test the API.",
    "seo_title": "This is a blog post",
    "meta_description": "This is a blog post to test the API.",
    "status": "published"
  }
}
```

```python
client.posts.search('query', page=1, page_size=10)
```

```json
{
  "meta": {
    "count": 1,
    "next_page": null,
    "previous_page": null
  },
  "data": [
    {
      "url": "http://www.example.com/blog/this-is-a-blog-post",
      "created": "2015-06-12T13:59:32.441289Z",
      "published": "2015-06-12T00:00:00Z",
      "author": {
        "first_name": "API",
        "last_name": "Test",
        "email": "apitest@buttercms.com",
        "slug": "api-test",
        "bio": "This is my bio.",
        "title": "API",
        "linkedin_url": "https://www.linkedin.com/in/API",
        "facebook_url": "https://www.facebook.com/API",
        "twitter_handle": "buttercmsapi",
        "profile_image": "https://buttercms.com/api.png"
      },
      "categories": [
        {
          "name": "test category",
          "slug": "test-category"
        }
      ],
      "featured_image": null,
      "slug": "this-is-a-blog-post",
      "title": "This is a blog post",
      "body": "<p class=\"\">This is a blog post to test the API.</p>",
      "summary": "This is a blog post to test the API.",
      "seo_title": "This is a blog post",
      "meta_description": "This is a blog post to test the API.",
      "status": "published"
    }
  ]
}
```

[To Top](#buttercms-python)

#### Authors

The Author's `.all()` method can take optional parameters to add additional fields to the repsonse. Currently supported parameters are:
* `include=recent_posts`: Adds each author's posts under the `recent_posts` key in that author's returned dictionary

```python
client.authors.all()
```

```json
{
  "data": [
    {
      "first_name": "API",
      "last_name": "Test",
      "email": "apitest@buttercms.com",
      "slug": "api-test",
      "bio": "This is my bio.",
      "title": "API",
      "linkedin_url": "https://www.linkedin.com/in/API",
      "facebook_url": "https://www.facebook.com/API",
      "pinterest_url": "https://www.pinterest.com/API",
      "instagram_url": "https://www.instagram.com/API",
      "twitter_handle": "buttercmsapi",
      "profile_image": "https://buttercms.com/api.png"
    }
  ]
}
```

```python
client.authors.get('jennifer-smith')
```

```json
{
  "data": {
    "first_name": "Jennifer",
    "last_name": "Smith",
    "email": "jennifersmith@buttercms.com",
    "slug": "jennifer-smith",
    "bio": "I love coffee!",
    "title": "President",
    "linkedin_url": "https://www.linkedin.com/in/jennifersmith",
    "facebook_url": "https://www.facebook.com/jennifersmith",
    "pinterest_url": "https://www.pinterest.com/jennifersmith",
    "instagram_url": "https://www.instagram.com/jennifersmith",
    "twitter_handle": "jennifersmith",
    "profile_image": "https://d2devwt40at1e2.cloudfront.net/api/file/etSDYJUIFDADGEEAQ.png"
  }
}
```

[To Top](#buttercms-python)

#### Categories

The Category's `.all()` method can take optional parameters to add additional fields to the repsonse. Currently supported parameters are:
* `include=recent_posts`: Adds posts tagged with that category under the `recent_posts` key in that category's returned dictionary

```python
client.categories.all()
```

```json
{
  "data": [
    {
      "name": "test category",
      "slug": "test-category"
    }
  ]
}
```

```python
client.categories.get('product-updates')
```

```json
{
  "data": {
    "name": "Product Updates",
    "slug": "product-updates"
  }
}
```

[To Top](#buttercms-python)

#### Feeds

```python
client.feeds.get('rss')
```

```json
{
  "data": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<rss xmlns:atom=\"http://www.w3.org/2005/Atom\" xmlns:content=\"http://purl.org/rss/1.0/modules/content/\" xmlns:media=\"http://search.yahoo.com/mrss/\" version=\"2.0\">\n   <channel>\n      <title>Latest blog posts</title>\n      <link>rss/</link>\n      <description />\n      <atom:link href=\"rss/\" rel=\"self\" />\n      <language>en-us</language>\n      <lastBuildDate>Mon, 4 Jul 2016 00:00:00 +0000</lastBuildDate>\n      \n      <item>\n         <title>Test Post</title>\n         <link>test-post</link>\n         <media:content medium=\"image\" url=\"https://d2devwt40at1e2.cloudfront.net/api/file/4RwB3RkGQcmuz5KeLNt1\"/>\n         <dc:creator xmlns:dc=\"http://purl.org/dc/elements/1.1/\">Adam Yala</dc:creator>\n         <pubDate>Mon, 4 Jul 2016 00:00:00 +0000</pubDate>\n         <guid>test-post</guid>\n         <description>Test summary</description>\n         <content:encoded>\n        <![CDATA[<p class=\"\">Test content.&nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras in massa id metus euismod vehicula. Aenean mi dolor, dapibus non dictum ultricies, scelerisque eu neque. Nulla ut sapien purus. Nulla sit amet nunc nec diam convallis viverra. Proin tempus enim enim, quis tristique lacus ullamcorper id. Vestibulum pretium dolor in interdum pretium. Vivamus efficitur convallis diam, in cursus nibh. Curabitur cursus leo pellentesque, rhoncus leo fermentum, scelerisque libero.</p>]]>\n      </content:encoded>\n      </item>\n      \n   </channel>\n</rss>\n\n\n"
}
```

```python
client.feeds.get('atom')
```

```json
{
  "data": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<feed xmlns=\"http://www.w3.org/2005/Atom\" xml:lang=\"en-us\">\n   <title>Latest blog posts</title>\n   <link href=\"rss/\" rel=\"alternate\" />\n   <link href=\"atom/\" rel=\"self\" />\n   <id>rss/</id>\n   <updated>2016-07-04T00:00:00+00:00</updated>\n   \n   <entry>\n      <title>Test Post</title>\n      <link href=\"test-post\" rel=\"alternate\" />\n      <published>2016-07-04T00:00:00+00:00</published>\n      <updated>2016-07-04T00:00:00+00:00</updated>\n      <author>\n         <name>Adam Yala</name>\n      </author>\n      <id>test-post</id>\n      <summary type=\"html\">Test summary</summary>\n   </entry>\n   \n</feed>"
}
```

```python
client.feeds.get('sitemap')
```

```json
{
  "data": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd\">\n \n  <url><loc>http://www.example.com/blog/this-is-a-blog-post</loc></url>\n \n</urlset>"
}
```

[To Top](#buttercms-python)

#### Content Fields

```python
client.content_fields.get(['homepage_headline', 'homepage_title'])
```

```json
{
  "data": {
    "homepage_title": "ButterCMS",
    "homepage_headline": "Blogging platform built for developers"
  }
}
```

[To Top](#buttercms-python)
