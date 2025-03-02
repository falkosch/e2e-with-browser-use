import asyncio

from browser_use import Browser, Agent
from browser_use.browser.context import BrowserContext, BrowserContextConfig
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

initial_actions = [
    # {'open_tab': {'url': 'https://www.google.com'}}
]
task = 'Geh auf reddit.de, suche nach "LLM AI agents" und fasse die gefundenen Posts zusammen.'

llm = ChatOllama(model='qwen2.5:7b', num_ctx=64000)

browser = Browser()
browser_context_config = BrowserContextConfig()
browser_context = BrowserContext(browser=browser, config=browser_context_config)


async def main():
    async with await browser.new_context() as context:
        agent = Agent(task=task, browser_context=context, initial_actions=initial_actions, llm=llm,
                      max_actions_per_step=1)

        await agent.run()

    input('Press Enter to close the browser...')
    await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
