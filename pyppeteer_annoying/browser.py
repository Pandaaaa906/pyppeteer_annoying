from os import path

from pyppeteer import launch
from pyppeteer.page import Page


BASE_DIR, *_ = path.split(__file__)

default_args = ['--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-infobars',
                '--window-position=0,0',
                '--ignore-certifcate-errors',
                '--ignore-certifcate-errors-spki-list',
                '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3312.0 Safari/537.36'
                ]

with open(path.join(BASE_DIR, "js/preload.js"), 'r') as f:
    preload_js = f.read()


async def undetected_page(headless=True, view_port=None, args=None, **kwargs) -> Page:
    """:arg
    Accept same kwargs as pyppeteer.launch like:
        ignoreHTTPSErrors
        userDataDir
        view_port
        executablePath
        etc
    """
    if args is None:
        args = default_args
    ignoreHTTPSErrors = kwargs.pop('ignoreHTTPSErrors', True)
    userDataDir = kwargs.pop('userDataDir', './tmp')
    view_port = view_port or {'width': 1400, 'height': 900}

    browser = await launch(ignoreHTTPSErrors=ignoreHTTPSErrors,
                           headless=headless,
                           userDataDir=userDataDir,
                           args=args,
                           **kwargs)
    page, *_ = await browser.pages()
    await page.setViewport(view_port)
    await page.evaluateOnNewDocument(preload_js)
    return page
