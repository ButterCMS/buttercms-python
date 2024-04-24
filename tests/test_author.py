from butter_cms.author import Author
from requests.exceptions import HTTPError
from test_vcr_config import TestCaseWithAPIKey, vcr_setup

vcr = vcr_setup()

class TestListAuthor(TestCaseWithAPIKey):
    @vcr.use_cassette('authors/test_author_all_invalid_token.json')
    def test_invalid_token(self):
        with self.assertRaises(HTTPError):
            author = Author('invalid_token')
            author.all()

    @vcr.use_cassette('authors/test_author_all.json')
    def test_all(self):
        author = Author(self.token)
        response = author.all()

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

        author_data = data[0]
        self.assertEqual(
            author_data, 
            {
                'first_name': 'SDK',
                'last_name': 'Tests',
                'email': 'sdktests@buttercms.com',
                'slug': 'sdk-tests',
                'bio': '',
                'title': '',
                'linkedin_url': '',
                'facebook_url': '',
                'instagram_url': '',
                'pinterest_url': '',
                'twitter_handle': '',
                'profile_image': '',
            }
        )
        self.assertIsNone(author_data.get('recent_posts'))

    @vcr.use_cassette('authors/test_author_all_with_posts.json')
    def test_all_include_recent_posts(self):
        author = Author(self.token)
        response = author.all(params={'include': 'recent_posts'})
        
        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

        author_data = data[0]
        self.assertIn('recent_posts', author_data)
        self.assertGreater(len(author_data['recent_posts']), 0)
        self.assertEqual(
            author_data, 
            {
                'first_name': 'SDK',
                'last_name': 'Tests',
                'email': 'sdktests@buttercms.com',
                'slug': 'sdk-tests',
                'bio': '',
                'title': '',
                'linkedin_url': '',
                'facebook_url': '',
                'instagram_url': '',
                'pinterest_url': '',
                'twitter_handle': '',
                'profile_image': '',
                'recent_posts': [
                    {
                        'created': '2024-05-17T14:13:46.787544Z',
                        'published': '2024-05-17T14:13:46.787109Z',
                        'url': None,
                        'slug': 'example-post',
                        'featured_image': 'https://cdn.buttercms.com/WUkiXJ6RCqZmjR8xihEL',
                        'featured_image_alt': '',
                        'author': {
                            'first_name': 'SDK',
                            'last_name': 'Tests',
                            'email': 'sdktests@buttercms.com',
                            'slug': 'sdk-tests',
                            'bio': '',
                            'title': '',
                            'linkedin_url': '',
                            'facebook_url': '',
                            'instagram_url': '',
                            'pinterest_url': '',
                            'twitter_handle': '',
                            'profile_image': '',
                        },
                        'tags': [
                            {
                                'name': 'Example Tag',
                                'slug': 'example-tag'
                            }
                        ],
                        'categories': [
                            {
                                'name': 'Example Category',
                                'slug': 'example-category'
                            }
                        ],
                        'title': 'Example Post',
                        'body': "<p>Welcome to ButterCMS! This an example blog post written using Butter.</p>\n<h3>Blog Engine Demo</h3>\n<p>Here's a helpful walkthrough of our Blog Engine solution.</p>\n<p>\n\n<!-- Outer Div sets maximum width for iframe on extra wide screens -->\n<div style=\"max-width:800px; height: auto; margin: auto;\">\n<!-- Inner div allows for responsive iframe scaling, including on mobile -->\n<div style=\"position: relative; padding-bottom: 56.25%; padding-top: 35px; height: 0; overflow: hidden; margin:auto;\">\n<iframe style=\"position: absolute; top:0; left: 0; width: 100%; height: 100%; z-index: 9999;\" src=\"https://www.youtube.com/embed/0dJbHy2XqoY\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen=\"allowfullscreen\"></iframe>\n</div>\n</div>\n<br /><a href=\"https://buttercms.com/demo/blog-engine-why-our-blog-engine/\">https://buttercms.com/demo/blog-engine-why-our-blog-engine/</a></p>\n<p></p>\n<h3>What's happening here?</h3>\n<p>If you're viewing this post from your website or command line, you've successfully made a request to&nbsp;the <a href=\"https://buttercms.com/docs/api\">Butter API</a>. If you haven't already, make sure you have our <a href=\"https://buttercms.com/docs/\">development guides</a> pulled up for step-by-step instructions on setting up Butter.</p>\n<h3>How does&nbsp;editing work?</h3>\n<p>Butter's WYSIWYG editor supports standard text formatting including headings, links, quotes, code, text alignment, and more. You can upload, crop, and resize images which are automatically hosted and delivered through a CDN (see below). You can also edit HTML directly when needed.</p>\n<figure class=\"image\"><img src=\"https://d2wzhk7xhrnk1x.cloudfront.net/rgPM9aHoSSKnjk44TQlD_butter-blog-post.jpg\" alt=\"Delivered to you via CDN\" />\n<figcaption>Delivered to you via CDN</figcaption>\n</figure>\n<h3>Can I use Butter as a full CMS for&nbsp;things other than a&nbsp;blog?</h3>\n<p>Yes. Butter can be used as a full CMS for managing dynamic content and creating pages across your entire website or app. Check out our <a href=\"https://buttercms.com/docs/\">development guides</a> for step-by-step tutorials on setting this up.</p>\n",
                        'summary': 'This is an example blog post. Pretty neat huh?',
                        'updated': '2024-05-17T14:13:46.813008Z',
                        'deleted': None,
                        'seo_title': 'Example Post SEO Optimized Title',
                        'meta_description': 'This is our example blog posts SEO optimized meta description.',
                        'status': 'published'
                    }
                ]
            }
        )

class TestRetrieveAuthor(TestCaseWithAPIKey):
    @vcr.use_cassette('authors/test_author_get_invalid_token.json')
    def test_invalid_token(self):
        with self.assertRaises(HTTPError):
            author = Author('invalid_token')
            author.get('sdk-tests')

    @vcr.use_cassette('authors/test_author_get.json')
    def test_get(self):
        author = Author(self.token)
        response = author.get('sdk-tests')

        self.assertIsNotNone(response)
        self.assertIn('data', response)
        
        author_data = response['data']
        self.assertIsNotNone(author_data)
        self.assertIsNone(author_data.get('recent_posts'))
        self.assertEqual(
            author_data, 
            {
                'first_name': 'SDK',
                'last_name': 'Tests',
                'email': 'sdktests@buttercms.com',
                'slug': 'sdk-tests',
                'bio': '',
                'title': '',
                'linkedin_url': '',
                'facebook_url': '',
                'instagram_url': '',
                'pinterest_url': '',
                'twitter_handle': '',
                'profile_image': '',
            }
        )
    
    @vcr.use_cassette('authors/test_author_get_with_posts.json')
    def test_get_include_recent_posts(self):
        author = Author(self.token)
        response = author.get('sdk-tests', params={'include': 'recent_posts'})
        
        self.assertIsNotNone(response)
        self.assertIn('data', response)

        author_data = response['data']
        self.assertIsNotNone(author_data)
        self.assertIn('recent_posts', author_data)
        self.assertGreater(len(author_data['recent_posts']), 0)
        self.assertEqual(
            author_data, 
            {
                'first_name': 'SDK',
                'last_name': 'Tests',
                'email': 'sdktests@buttercms.com',
                'slug': 'sdk-tests',
                'bio': '',
                'title': '',
                'linkedin_url': '',
                'facebook_url': '',
                'instagram_url': '',
                'pinterest_url': '',
                'twitter_handle': '',
                'profile_image': '',
                'recent_posts': [
                    {
                        'created': '2024-05-17T14:13:46.787544Z',
                        'published': '2024-05-17T14:13:46.787109Z',
                        'url': None,
                        'slug': 'example-post',
                        'featured_image': 'https://cdn.buttercms.com/WUkiXJ6RCqZmjR8xihEL',
                        'featured_image_alt': '',
                        'author': {
                            'first_name': 'SDK',
                            'last_name': 'Tests',
                            'email': 'sdktests@buttercms.com',
                            'slug': 'sdk-tests',
                            'bio': '',
                            'title': '',
                            'linkedin_url': '',
                            'facebook_url': '',
                            'instagram_url': '',
                            'pinterest_url': '',
                            'twitter_handle': '',
                            'profile_image': '',
                        },
                        'tags': [
                            {
                                'name': 'Example Tag',
                                'slug': 'example-tag'
                            }
                        ],
                        'categories': [
                            {
                                'name': 'Example Category',
                                'slug': 'example-category'
                            }
                        ],
                        'title': 'Example Post',
                        'body': "<p>Welcome to ButterCMS! This an example blog post written using Butter.</p>\n<h3>Blog Engine Demo</h3>\n<p>Here's a helpful walkthrough of our Blog Engine solution.</p>\n<p>\n\n<!-- Outer Div sets maximum width for iframe on extra wide screens -->\n<div style=\"max-width:800px; height: auto; margin: auto;\">\n<!-- Inner div allows for responsive iframe scaling, including on mobile -->\n<div style=\"position: relative; padding-bottom: 56.25%; padding-top: 35px; height: 0; overflow: hidden; margin:auto;\">\n<iframe style=\"position: absolute; top:0; left: 0; width: 100%; height: 100%; z-index: 9999;\" src=\"https://www.youtube.com/embed/0dJbHy2XqoY\" frameborder=\"0\" allow=\"accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen=\"allowfullscreen\"></iframe>\n</div>\n</div>\n<br /><a href=\"https://buttercms.com/demo/blog-engine-why-our-blog-engine/\">https://buttercms.com/demo/blog-engine-why-our-blog-engine/</a></p>\n<p></p>\n<h3>What's happening here?</h3>\n<p>If you're viewing this post from your website or command line, you've successfully made a request to&nbsp;the <a href=\"https://buttercms.com/docs/api\">Butter API</a>. If you haven't already, make sure you have our <a href=\"https://buttercms.com/docs/\">development guides</a> pulled up for step-by-step instructions on setting up Butter.</p>\n<h3>How does&nbsp;editing work?</h3>\n<p>Butter's WYSIWYG editor supports standard text formatting including headings, links, quotes, code, text alignment, and more. You can upload, crop, and resize images which are automatically hosted and delivered through a CDN (see below). You can also edit HTML directly when needed.</p>\n<figure class=\"image\"><img src=\"https://d2wzhk7xhrnk1x.cloudfront.net/rgPM9aHoSSKnjk44TQlD_butter-blog-post.jpg\" alt=\"Delivered to you via CDN\" />\n<figcaption>Delivered to you via CDN</figcaption>\n</figure>\n<h3>Can I use Butter as a full CMS for&nbsp;things other than a&nbsp;blog?</h3>\n<p>Yes. Butter can be used as a full CMS for managing dynamic content and creating pages across your entire website or app. Check out our <a href=\"https://buttercms.com/docs/\">development guides</a> for step-by-step tutorials on setting this up.</p>\n",
                        'summary': 'This is an example blog post. Pretty neat huh?',
                        'updated': '2024-05-17T14:13:46.813008Z',
                        'deleted': None,
                        'seo_title': 'Example Post SEO Optimized Title',
                        'meta_description': 'This is our example blog posts SEO optimized meta description.',
                        'status': 'published'
                    }
                ]
            }
        )


