from unittest import TestCase
from k9.helm import *

class TestHelm(TestCase):

    def test_helm_install(self):

        # Test helm_install()
        helm_install('stable/tomcat', {'domain': 'sandbox.simoncomputing.com'})

        # test helm_ls()
        release_name = 'tomcat'
        result = helm_ls()
        found = [
            release
            for release in result
            if release['name'] == release_name
        ]
        self.assertIsNotNone(found)
        self.assertEqual(release_name, found[0]['name'])

        # test helm_exists()
        self.assertTrue(helm_exists(release_name))

        # test helm_uninstall()
        result = helm_uninstall(release_name)
        print(f'result={result}')
        self.assertTrue(b'uninstalled' in result)
        self.assertFalse(helm_exists(release_name))

    def test_helm_uninstall_fail(self):
        with self.assertRaisesRegex(Exception, 'returned non-zero exit status'):
            helm_uninstall('bogus')

