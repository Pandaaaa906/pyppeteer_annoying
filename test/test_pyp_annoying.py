import unittest

from pyppeteer.page import Page

from pyppeteer_annoying.browser import undetected_page
from pyppeteer_annoying.functions import extract_all_text_by_xpath, extract_text_by_xpath, extract_property, \
    extract_attribute_by_xpath


class PyppeteerAnnoyingTestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self._page = await undetected_page(autoClose=False, headless=False)
        with open('html/test.html') as f:
            html = f.read()
        await self._page.setContent(html)

    async def test_page_initialed(self):
        self.assertIsInstance(self._page, Page)

    async def test_extract_all_text_by_xpath(self):
        ret = await extract_all_text_by_xpath(self._page, '//div')
        self.assertEqual(ret, ['text1', 'text2', 'text3', ])

    async def test_extract_text_by_xpath(self):
        ret = await extract_text_by_xpath(self._page, '//div[2]')
        self.assertEqual(ret, 'text2')

    async def test_extract_attribute_by_xpath(self):
        ret = await extract_attribute_by_xpath(self._page, '//div', 'class')
        self.assertEqual(ret, 'property-value')

    async def asyncTearDown(self):
        await self._page.close()


if __name__ == '__main__':
    unittest.main()
