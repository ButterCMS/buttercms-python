from butter_cms.page import Page
from requests.exceptions import HTTPError
from test_vcr_config import TestCaseWithAPIKey, vcr_setup

vcr = vcr_setup()

class TestListPages(TestCaseWithAPIKey):
    @vcr.use_cassette('pages/test_page_all_invalid_token.json')
    def test_invalid_token(self):
        with self.assertRaises(HTTPError):
            page = Page('invalid_token')
            page.all('landing-page')

    @vcr.use_cassette('pages/test_page_all.json')
    def test_list_pages(self):
        page = Page(self.token)
        response = page.all('landing-page')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        pages = response['data']
        self.assertIsNotNone(pages)
        self.assertIsInstance(pages, list)
        self.assertGreater(len(pages), 0)

        page_1 = pages[0]
        self.assertEqual(
            page_1,
            {
                "slug": "landing-page-with-components",
                "name": "Landing Page with Components",
                "published": "2024-05-17T14:14:41.484894Z",
                "updated": "2024-05-17T14:14:41.522160Z",
                "page_type": "landing-page",
                "fields": {
                    "seo": {
                        "title": "Sample Landing Page with Components - powered by ButterCMS",
                        "description": "Sample Landing Page with Components - powered by ButterCMS"
                    },
                    "body": [
                        {
                            "type": "hero",
                            "fields": {
                                "headline": "Welcome to your ButterCMS Proof of Concept",
                                "subheadline": "Use this app as your own proof of concept to explore Butter's capabilities for yourself. When you're ready, host this app and invite your team to try it out all well!",
                                "image": "https://cdn.buttercms.com/DVG5DLMQ9ywaCwfEAgL2",
                                "button_label": "Update this Page in Butter",
                                "button_url": "https://buttercms.com/pages/",
                                "scroll_anchor_id": "home"
                            }
                        },
                        {
                            "type": "two_column_with_image",
                            "fields": {
                                "headline": "ButterCMS is your content backend",
                                "subheadline": "Butter has three core content solutions: Pages, Posts, and Collections. Combine this with advanced capabilities like localization, Write API, multi-site + multi-env and Butter is your centralized content backend no matter how much content you're managing.",
                                "image": "https://cdn.buttercms.com/yg7mFNnNSpyXLpwvp0KX",
                                "image_position": "left",
                                "button_label": "Update this Page in Butter",
                                "button_url": "https://buttercms.com/pages/",
                                "scroll_anchor_id": "about"
                            }
                        },
                        {
                            "type": "features",
                            "fields": {
                                "headline": "This page is built using ButterCMS Components",
                                "subheadline": "This page is an example of utilizing Butter Components which allow you to build dynamic landing pages by choosing Components from a Component Library. Reuse and reorder Components in any way you want!",
                                "scroll_anchor_id": "features",
                                "features": [
                                    {
                                        "headline": "Components on this page",
                                        "description": "This sample page has four component types: hero, two column with image, features, and testimonials.",
                                        "icon": "https://cdn.buttercms.com/1evWeDvPQ3eby8N5pZsg"
                                    },
                                    {
                                        "headline": "Build your own",
                                        "description": "This page is just an example set of Components. You can build your own custom Component library!",
                                        "icon": "https://cdn.buttercms.com/WX5OIKIPQAmu0YCAjZpH"
                                    },
                                    {
                                        "headline": "Reorder them",
                                        "description": "Components are great because you can reorder them from your Butter dashboard",
                                        "icon": "https://cdn.buttercms.com/h2nnt9PZSbaj20FLScbP"
                                    },
                                    {
                                        "headline": "Infinite possibilities",
                                        "description": "Build carousels, call to actions, testimonials, and much more. There's infinite flexbility.",
                                        "icon": "https://cdn.buttercms.com/FwNLtx6dR7ybtG1WenrK"
                                    }
                                ]
                            }
                        },
                        {
                            "type": "two_column_with_image",
                            "fields": {
                                "headline": "Customize this page",
                                "subheadline": "<p>Try updating the content of this page to reflect your own. You can also explore modifying these components or creating your own in your Butter dashboard.  Learn more about <a href=\"https://buttercms.com/kb/creating-editing-and-deleting-pages-and-page-types\">Page Types</a> and <a href=\"https://buttercms.com/kb/how-to-modify-components\">Components</a>.</p>",
                                "image": "https://cdn.buttercms.com/AJPaLE3ToKRoLwWQeaww",
                                "image_position": "right",
                                "button_label": "Update this Page in Butter",
                                "button_url": "https://buttercms.com/pages/",
                                "scroll_anchor_id": "tryit"
                            }
                        },
                        {
                            "type": "testimonials",
                            "fields": {
                                "headline": "What our customers say",
                                "scroll_anchor_id": "testimonials",
                                "testimonial": [
                                    {
                                        "quote": "Super Flexible CMS Solution",
                                        "name": "Hampton Catlin",
                                        "title": "Creator of Sass and Haml"
                                    },
                                    {
                                        "quote": "A breath of fresh air in the CMS world, once you go headless with butter you'll never go back.",
                                        "name": "Bryan MacMillan",
                                        "title": "IT Admin"
                                    },
                                    {
                                        "quote": "I was able to quickly draft new pages, circulate them to the team, edit them, and then ultimately publish intuitively.",
                                        "name": "Kim Kohatsu",
                                        "title": "CMO"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        )

    @vcr.use_cassette('pages/test_page_all_without_page_type.json')
    def test_list_pages_without_page_type(self):
        page = Page(self.token)
        response = page.all('*')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        pages = response['data']
        self.assertIsNotNone(pages)
        self.assertIsInstance(pages, list)
        self.assertEqual(1, len(pages))

        page_1 = pages[0]
        self.assertEqual(
            page_1,
            {
                "slug": "simple-page",
                "name": "Simple Page",
                "published": "2024-05-17T14:14:47.533297Z",
                "updated": "2024-05-17T14:14:47.550734Z",
                "page_type": None,
                "fields": {
                    "seo_title": "Anvils and Dynamite | Acme Co",
                    "headline": "Acme Co provides supplies to your favorite cartoon heroes.",
                    "hero_image": "https://cdn.buttercms.com/c8oSTGcwQDC5I58km5WV",
                    "call_to_action": "Buy Now",
                    "customer_logos": [
                        {
                            "logo_image": "https://cdn.buttercms.com/1FNvDuOJSROw1fybRCYU"
                        },
                        {
                            "logo_image": "https://cdn.buttercms.com/1FNvDuOJSROw1fybRCYU"
                        }
                    ]
                }
            }
        )

class TestRetrievePage(TestCaseWithAPIKey):
    @vcr.use_cassette('pages/test_page_get_invalid_token.json')
    def test_invalid_token(self):
        with self.assertRaises(HTTPError):
            page = Page('invalid_token')
            page.get('landing-page', 'landing-page-with-components')
        
    @vcr.use_cassette('pages/test_page_get.json')
    def test_get_page(self):
        page = Page(self.token)
        response = page.get('landing-page', 'landing-page-with-components')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIsNotNone(data)
        self.assertNotIsInstance(data, list)
        self.assertEqual(
            data,
            {
                "slug": "landing-page-with-components",
                "name": "Landing Page with Components",
                "published": "2024-05-17T14:14:41.484894Z",
                "updated": "2024-05-17T14:14:41.522160Z",
                "page_type": "landing-page",
                "fields": {
                    "seo": {
                        "title": "Sample Landing Page with Components - powered by ButterCMS",
                        "description": "Sample Landing Page with Components - powered by ButterCMS"
                    },
                    "body": [
                        {
                            "type": "hero",
                            "fields": {
                                "headline": "Welcome to your ButterCMS Proof of Concept",
                                "subheadline": "Use this app as your own proof of concept to explore Butter's capabilities for yourself. When you're ready, host this app and invite your team to try it out all well!",
                                "image": "https://cdn.buttercms.com/DVG5DLMQ9ywaCwfEAgL2",
                                "button_label": "Update this Page in Butter",
                                "button_url": "https://buttercms.com/pages/",
                                "scroll_anchor_id": "home"
                            }
                        },
                        {
                            "type": "two_column_with_image",
                            "fields": {
                                "headline": "ButterCMS is your content backend",
                                "subheadline": "Butter has three core content solutions: Pages, Posts, and Collections. Combine this with advanced capabilities like localization, Write API, multi-site + multi-env and Butter is your centralized content backend no matter how much content you're managing.",
                                "image": "https://cdn.buttercms.com/yg7mFNnNSpyXLpwvp0KX",
                                "image_position": "left",
                                "button_label": "Update this Page in Butter",
                                "button_url": "https://buttercms.com/pages/",
                                "scroll_anchor_id": "about"
                            }
                        },
                        {
                            "type": "features",
                            "fields": {
                                "headline": "This page is built using ButterCMS Components",
                                "subheadline": "This page is an example of utilizing Butter Components which allow you to build dynamic landing pages by choosing Components from a Component Library. Reuse and reorder Components in any way you want!",
                                "scroll_anchor_id": "features",
                                "features": [
                                    {
                                        "headline": "Components on this page",
                                        "description": "This sample page has four component types: hero, two column with image, features, and testimonials.",
                                        "icon": "https://cdn.buttercms.com/1evWeDvPQ3eby8N5pZsg"
                                    },
                                    {
                                        "headline": "Build your own",
                                        "description": "This page is just an example set of Components. You can build your own custom Component library!",
                                        "icon": "https://cdn.buttercms.com/WX5OIKIPQAmu0YCAjZpH"
                                    },
                                    {
                                        "headline": "Reorder them",
                                        "description": "Components are great because you can reorder them from your Butter dashboard",
                                        "icon": "https://cdn.buttercms.com/h2nnt9PZSbaj20FLScbP"
                                    },
                                    {
                                        "headline": "Infinite possibilities",
                                        "description": "Build carousels, call to actions, testimonials, and much more. There's infinite flexbility.",
                                        "icon": "https://cdn.buttercms.com/FwNLtx6dR7ybtG1WenrK"
                                    }
                                ]
                            }
                        },
                        {
                            "type": "two_column_with_image",
                            "fields": {
                                "headline": "Customize this page",
                                "subheadline": "<p>Try updating the content of this page to reflect your own. You can also explore modifying these components or creating your own in your Butter dashboard.  Learn more about <a href=\"https://buttercms.com/kb/creating-editing-and-deleting-pages-and-page-types\">Page Types</a> and <a href=\"https://buttercms.com/kb/how-to-modify-components\">Components</a>.</p>",
                                "image": "https://cdn.buttercms.com/AJPaLE3ToKRoLwWQeaww",
                                "image_position": "right",
                                "button_label": "Update this Page in Butter",
                                "button_url": "https://buttercms.com/pages/",
                                "scroll_anchor_id": "tryit"
                            }
                        },
                        {
                            "type": "testimonials",
                            "fields": {
                                "headline": "What our customers say",
                                "scroll_anchor_id": "testimonials",
                                "testimonial": [
                                    {
                                        "quote": "Super Flexible CMS Solution",
                                        "name": "Hampton Catlin",
                                        "title": "Creator of Sass and Haml"
                                    },
                                    {
                                        "quote": "A breath of fresh air in the CMS world, once you go headless with butter you'll never go back.",
                                        "name": "Bryan MacMillan",
                                        "title": "IT Admin"
                                    },
                                    {
                                        "quote": "I was able to quickly draft new pages, circulate them to the team, edit them, and then ultimately publish intuitively.",
                                        "name": "Kim Kohatsu",
                                        "title": "CMO"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        )

    @vcr.use_cassette('pages/test_page_get_non_existent.json')
    def test_get_non_existent_page(self):
        with self.assertRaises(HTTPError):
            page = Page(self.token)
            response = page.get('page_type', 'non-existent')

            self.assertIsNotNone(response)
            self.assertIn('detail', response)
            self.assertEqual('Not found', response['detail'])

class TestSearchPage(TestCaseWithAPIKey):
    @vcr.use_cassette('pages/test_page_search_invalid_token.json')
    def test_invalid_token(self):
        with self.assertRaises(HTTPError):
            page = Page('invalid_token')
            page.search('sample landing page')

    @vcr.use_cassette('pages/test_page_search.json')
    def test_search_page(self):
        page = Page(self.token)
        response = page.search('sample landing page')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        pages = response['data']
        self.assertIsNotNone(pages)
        self.assertIsInstance(pages, list)
        self.assertEqual(1, len(pages))

        page_1 = pages[0]
        self.assertEqual(
            page_1,
            {
                "slug": "landing-page-with-components",
                "name": "Landing Page with Components",
                "published": "2024-05-17T14:14:41.484894Z",
                "updated": "2024-05-17T14:14:41.522160Z",
                "page_type": "landing-page",
                "fields": {
                    "seo": {
                        "title": "Sample Landing Page with Components - powered by ButterCMS",
                        "description": "Sample Landing Page with Components - powered by ButterCMS"
                    },
                    "body": [
                        {
                            "type": "hero",
                            "fields": {
                                "headline": "Welcome to your ButterCMS Proof of Concept",
                                "subheadline": "Use this app as your own proof of concept to explore Butter's capabilities for yourself. When you're ready, host this app and invite your team to try it out all well!",
                                "image": "https://cdn.buttercms.com/DVG5DLMQ9ywaCwfEAgL2",
                                "button_label": "Update this Page in Butter",
                                "button_url": "https://buttercms.com/pages/",
                                "scroll_anchor_id": "home"
                            }
                        },
                        {
                            "type": "two_column_with_image",
                            "fields": {
                                "headline": "ButterCMS is your content backend",
                                "subheadline": "Butter has three core content solutions: Pages, Posts, and Collections. Combine this with advanced capabilities like localization, Write API, multi-site + multi-env and Butter is your centralized content backend no matter how much content you're managing.",
                                "image": "https://cdn.buttercms.com/yg7mFNnNSpyXLpwvp0KX",
                                "image_position": "left",
                                "button_label": "Update this Page in Butter",
                                "button_url": "https://buttercms.com/pages/",
                                "scroll_anchor_id": "about"
                            }
                        },
                        {
                            "type": "features",
                            "fields": {
                                "headline": "This page is built using ButterCMS Components",
                                "subheadline": "This page is an example of utilizing Butter Components which allow you to build dynamic landing pages by choosing Components from a Component Library. Reuse and reorder Components in any way you want!",
                                "scroll_anchor_id": "features",
                                "features": [
                                    {
                                        "headline": "Components on this page",
                                        "description": "This sample page has four component types: hero, two column with image, features, and testimonials.",
                                        "icon": "https://cdn.buttercms.com/1evWeDvPQ3eby8N5pZsg"
                                    },
                                    {
                                        "headline": "Build your own",
                                        "description": "This page is just an example set of Components. You can build your own custom Component library!",
                                        "icon": "https://cdn.buttercms.com/WX5OIKIPQAmu0YCAjZpH"
                                    },
                                    {
                                        "headline": "Reorder them",
                                        "description": "Components are great because you can reorder them from your Butter dashboard",
                                        "icon": "https://cdn.buttercms.com/h2nnt9PZSbaj20FLScbP"
                                    },
                                    {
                                        "headline": "Infinite possibilities",
                                        "description": "Build carousels, call to actions, testimonials, and much more. There's infinite flexbility.",
                                        "icon": "https://cdn.buttercms.com/FwNLtx6dR7ybtG1WenrK"
                                    }
                                ]
                            }
                        },
                        {
                            "type": "two_column_with_image",
                            "fields": {
                                "headline": "Customize this page",
                                "subheadline": "<p>Try updating the content of this page to reflect your own. You can also explore modifying these components or creating your own in your Butter dashboard.  Learn more about <a href=\"https://buttercms.com/kb/creating-editing-and-deleting-pages-and-page-types\">Page Types</a> and <a href=\"https://buttercms.com/kb/how-to-modify-components\">Components</a>.</p>",
                                "image": "https://cdn.buttercms.com/AJPaLE3ToKRoLwWQeaww",
                                "image_position": "right",
                                "button_label": "Update this Page in Butter",
                                "button_url": "https://buttercms.com/pages/",
                                "scroll_anchor_id": "tryit"
                            }
                        },
                        {
                            "type": "testimonials",
                            "fields": {
                                "headline": "What our customers say",
                                "scroll_anchor_id": "testimonials",
                                "testimonial": [
                                    {
                                        "quote": "Super Flexible CMS Solution",
                                        "name": "Hampton Catlin",
                                        "title": "Creator of Sass and Haml"
                                    },
                                    {
                                        "quote": "A breath of fresh air in the CMS world, once you go headless with butter you'll never go back.",
                                        "name": "Bryan MacMillan",
                                        "title": "IT Admin"
                                    },
                                    {
                                        "quote": "I was able to quickly draft new pages, circulate them to the team, edit them, and then ultimately publish intuitively.",
                                        "name": "Kim Kohatsu",
                                        "title": "CMO"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        )