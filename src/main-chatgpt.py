import asyncio

from browser_use import Browser
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from __init__ import perform_task

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0.0)


async def main():
    browser = Browser()
    await perform_task(browser, llm, 'search-llm-on-google.feature')
    await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
