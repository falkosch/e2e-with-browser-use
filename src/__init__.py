import os

from browser_use import Agent, Browser, BrowserContextConfig
from langchain_core.language_models.chat_models import BaseChatModel


def read_task_from_file(file_name: str) -> str:
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


async def perform_task(browser: Browser, llm: BaseChatModel, task_file_name: str, **kwargs: dict):
    task = read_task_from_file(task_file_name)

    context_config = BrowserContextConfig(
        browser_window_size={'width': 1024, 'height': 768},
    )

    async with await browser.new_context(context_config) as context:
        agent = Agent(task, llm, browser_context=context, **kwargs)

        await agent.run()
