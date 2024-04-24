from butter_cms.content_field import ContentField
from requests.exceptions import HTTPError
from test_vcr_config import TestCaseWithAPIKey, vcr_setup

vcr = vcr_setup()

class TestListContentField(TestCaseWithAPIKey):
    @vcr.use_cassette('content_fields/test_content_field_all_invalid_token.json')
    def test_invalid_token(self):
        with self.assertRaises(HTTPError):
            content_field = ContentField('invalid_token')
            content_field.get(keys=[])

    @vcr.use_cassette('content_fields/test_content_field_all.json')
    def test_list_content_fields_without_filtering(self): 
        content_field = ContentField(self.token)
        response = content_field.get(keys=[])

        self.assertIsNotNone(response)
        self.assertNotIn('data', response)

    @vcr.use_cassette('content_fields/test_content_field_all_filtered.json')
    def test_list_filtered_content_fields(self): 
        content_field = ContentField(self.token)
        response = content_field.get(keys=['navigation_menu', 'navigation_menu_item'])

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        content_fields = response['data']
        self.assertIsNotNone(content_fields)
        self.assertIn('navigation_menu', content_fields)
        self.assertIn('navigation_menu_item', content_fields)

        navigation_menu_field = content_fields['navigation_menu']
        self.assertEqual(len(navigation_menu_field), 1)
        
        navigation_menu_item_field = content_fields['navigation_menu_item']
        self.assertGreater(len(navigation_menu_item_field), 1)
        self.assertEqual(
            navigation_menu_item_field,
            [
                {
                    'meta': {
                        'id': 735745
                    },
                    'label': 'Home',
                    'url': '#home'
                },
                {
                    'meta': {
                        'id': 735746
                    },
                    'label': 'About',
                    'url': '#about'
                },
                {
                    'meta': {
                        'id': 735747
                    },
                    'label': 'Features',
                    'url': '#features'
                },
                {
                    'meta': {
                        'id': 735748
                    },
                    'label': 'Try It',
                    'url': '#tryit'
                },
                {
                    'meta': {
                        'id': 735749
                    },
                    'label': 'Testimonials',
                    'url': '#testimonials'
                },
                {
                    'meta': {
                        'id': 735750
                    },
                    'label': 'Blog',
                    'url': '#blog'
                }
            ]
        )

    @vcr.use_cassette('content_fields/test_content_field_all_non_existent_key.json')
    def test_list_non_existent_content_field(self):
        with self.assertRaises(HTTPError):
            content_field = ContentField(self.token)
            response = content_field.get(keys=['non-existent-key'])

            self.assertIsNotNone(response)
            self.assertIn('detail', response)
            self.assertEqual('Content key non-existent-key not found', response['detail'])

class TestRetrieveContentField(TestCaseWithAPIKey):
    @vcr.use_cassette('content_fields/test_content_field_get_invalid_token.json')
    def test_invalid_token(self):
        with self.assertRaises(HTTPError):
            content_field = ContentField('invalid_token')
            content_field.get_collection('navigation_menu_item')

    @vcr.use_cassette('content_fields/test_content_field_get.json')
    def test_get_content_field_without_filtering(self):
        content_field = ContentField(self.token)
        response = content_field.get_collection('navigation_menu_item')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        content_fields = response['data']
        self.assertIsNotNone(content_fields)
        self.assertIn('navigation_menu_item', content_fields)

        navigation_menu_item_field = content_fields['navigation_menu_item']
        self.assertGreater(len(navigation_menu_item_field), 1)
        self.assertEqual(
            navigation_menu_item_field,
            [
                {
                    'meta': {
                        'id': 735745
                    },
                    'label': 'Home',
                    'url': '#home'
                },
                {
                    'meta': {
                        'id': 735746
                    },
                    'label': 'About',
                    'url': '#about'
                },
                {
                    'meta': {
                        'id': 735747
                    },
                    'label': 'Features',
                    'url': '#features'
                },
                {
                    'meta': {
                        'id': 735748
                    },
                    'label': 'Try It',
                    'url': '#tryit'
                },
                {
                    'meta': {
                        'id': 735749
                    },
                    'label': 'Testimonials',
                    'url': '#testimonials'
                },
                {
                    'meta': {
                        'id': 735750
                    },
                    'label': 'Blog',
                    'url': '#blog'
                }
            ]
        )

    @vcr.use_cassette('content_fields/test_content_field_get_filtered.json')
    def test_get_filtered_content_field(self):
        content_field = ContentField(self.token)
        response = content_field.get_collection('navigation_menu_item', fields=[{'label': 'Testimonials'}])

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        content_fields = response['data']
        self.assertIsNotNone(content_fields)
        self.assertIn('navigation_menu_item', content_fields)

        navigation_menu_item_field = content_fields['navigation_menu_item']
        self.assertEqual(1, len(navigation_menu_item_field))
        self.assertEqual(
            navigation_menu_item_field,
            [
                {
                    'meta': {
                        'id': 735749
                    },
                    'label': 'Testimonials',
                    'url': '#testimonials'
                }
            ]
        )

    @vcr.use_cassette('content_fields/test_content_field_get_non_existent_field.json')
    def test_get_non_existent_content_field(self):
        with self.assertRaises(HTTPError):
            content_field = ContentField(self.token)
            response = content_field.get_collection('not-existent-field')

            self.assertIsNotNone(response)
            self.assertIn('detail', response)
            self.assertEqual('Not found', response['detail'])