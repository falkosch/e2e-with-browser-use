import asyncio

from browser_use import Browser, Agent
from browser_use.browser.context import BrowserContext, BrowserContextConfig
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

from __init__ import read_task_from_file

load_dotenv()

task = read_task_from_file('search-llm-on-google.feature')

# llm = ChatOllama(model='llama3.2:3b-instruct-fp16', num_ctx=64000)
# llm = ChatOllama(model='llama3.1:8b-instruct-fp16', num_ctx=32000)
# llm = ChatOllama(model='qwen2.5:7b', num_ctx=32000)
llm = ChatOllama(model='qwen2.5:7b-instruct-fp16', num_ctx=32000)
# llm = ChatOllama(model='granite3.2:8b-instruct-fp16', num_ctx=16000)
# llm = ChatOllama(model='granite3.1-dense:8b-instruct-fp16', num_ctx=16000)
# llm = ChatOllama(model='granite3.1-moe:3b-instruct-fp16', num_ctx=128000)

browser = Browser()
browser_context_config = BrowserContextConfig()
browser_context = BrowserContext(browser=browser, config=browser_context_config)


async def main():
    async with await browser.new_context() as context:
        agent = Agent(task=task, browser_context=context, llm=llm, max_actions_per_step=1, max_failures=5)

        await agent.run()

    await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
