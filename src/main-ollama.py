import asyncio

from browser_use import Browser
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

from __init__ import perform_task

load_dotenv()

# llm = ChatOllama(model='llama3.2:3b-instruct-fp16', num_ctx=64000)
# llm = ChatOllama(model='llama3.1:8b-instruct-fp16', num_ctx=32000)
# llm = ChatOllama(model='qwen2.5:7b', num_ctx=32000)
# llm = ChatOllama(model='granite3.2:8b-instruct-fp16', num_ctx=16000)
# llm = ChatOllama(model='granite3.1-dense:8b-instruct-fp16', num_ctx=16000)
# llm = ChatOllama(model='granite3.1-moe:3b-instruct-fp16', num_ctx=128000)
llm = ChatOllama(model='qwen2.5:7b-instruct-fp16', num_ctx=32000)


async def main():
    browser = Browser()
    await perform_task(browser, llm, 'search-llm-on-google.feature')
    await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
