from pyppeteer.page import Page


async def extract_all_text_by_xpath(page: Page, x: str):
    items = await page.xpath(x)
    return [await page.evaluate('(element) => element.textContent', item) for item in items]


async def extract_text_by_xpath(page: Page, x: str):
    elem = await page.waitForXPath(x)
    return await page.evaluate('(element) => element.textContent', elem)


async def extract_property(elem, property_name: str):
    if elem is None:
        return
    return await (await elem.getProperty(property_name)).jsonValue()


async def extract_properties_from_xpath(page: Page, x: str, property_name: str):
    items = await page.xpath(x)
    return [await extract_property(elem, property_name) for elem in items]


async def extract_attribute_by_xpath(page: Page, x: str, attribute_name: str):
    elem = await page.waitForXPath(x)
    return await page.evaluate('(element, attribute_name) => element.getAttribute(attribute_name)',
                               elem, attribute_name)
