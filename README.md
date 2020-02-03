# Pyppeteer annoying
Some shortcuts for pyppeteer

This is because the future plan of pyppeteer:
>Future Plan<br>
> 1. Catch up development of puppeteer<br>
>   * **Not intend to add original API which puppeteer does not have**
>

## Undetected browser
`undetected_page` meant to return an undetectable page:
`undetected_page` accepts same arguments of `pyppeteer.launch`, like `executablePath`, `headless`, etc.<br>
Additionally, it also accepts `view_port` as a dict, to control the size of the browser.<br>

By default:
```
headless=True
ignoreHTTPSErrors=True
userDataDir='./tmp'
view_port={'width': 1400, 'height': 900}
```
Examples:
```python
from pyppeteer_annoying import undetected_page

async def main():
    page = await undetected_page()
    # Do whatever you want.
...
```

## Extract node's text by xpath
```python
from pyppeteer_annoying import undetected_page, extract_all_text_by_xpath, extract_text_by_xpath

...
page = await undetected_page()
l_text = await extract_all_text_by_xpath(page, '//div')
text = await extract_text_by_xpath(page, '//div')
```

## Extract node's attribute by xpath
```python
from pyppeteer_annoying import extract_attribute_by_xpath

...
attr = await extract_attribute_by_xpath(page, '//div', 'class')

```