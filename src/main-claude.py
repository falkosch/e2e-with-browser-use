import asyncio

from browser_use import Browser
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

from __init__ import perform_task

load_dotenv()

llm = ChatAnthropic(model_name="claude-3-5-haiku-20241022")


async def main():
    browser = Browser()
    await perform_task(browser, llm, 'search-senacor-job-listings.feature')
    await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
