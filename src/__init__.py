import os

from browser_use import Agent, Browser, BrowserContextConfig
from junitparser import TestCase, TestSuite, JUnitXml, Error
from langchain_core.language_models.chat_models import BaseChatModel


def read_task_from_file(file_name: str) -> str:
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


async def perform_task(browser: Browser, llm: BaseChatModel, task_file_name: str, **kwargs: dict):
    task = read_task_from_file(task_file_name)
    test_case = TestCase(task)
    test_suite = TestSuite(task_file_name)
    test_suite.add_testcases([test_case])
    xml = JUnitXml()
    xml.add_testsuite(test_suite)

    context_config = BrowserContextConfig(
        cookies_file='cookies.tmp.json',
        browser_window_size={'width': 1280, 'height': 1100},
    )

    async with await browser.new_context(context_config) as context:
        agent = Agent(task, llm, browser_context=context, **kwargs)

        history = await agent.run()
        result = history.final_result()
        if result:
            test_case.system_out = str(result)
        else:
            test_case.result = [Error('No result')]
        xml.write(f'{task_file_name}.report.xml')
        print(xml.tostring())
