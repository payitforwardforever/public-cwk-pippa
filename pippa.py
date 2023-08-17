import os
import sys

from utils import list_openai_models, list_files, pippa_log, read_url_body_content, read_file_content

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.indexes import VectorstoreIndexCreator


import settings

os.environ["OPENAI_API_KEY"] = settings.APIKEY


def pre_process_prompt(prompt):

    if not isinstance(prompt, str):
        raise ValueError("Prompt must be a string.")

    # pre-process url: read the content of the url and append it to the prompt
    if 'url:' in prompt:
        url = prompt.split('url:')[1].strip()
        url_content = read_url_body_content(url, hide_browser=True)
        prompt = prompt.replace(f"url:{url}", url_content)
        prompt = prompt[:settings.MAX_PROMPT_LENGTH]

        if settings.DEBUG_MODE: pippa_log(prompt)

    # pre-process path: read the content of the given path
    elif 'path:' in prompt:
        path = prompt.split('path:')[1].strip()
        file_content = read_file_content(path)
        if settings.DEBUG_MODE: pippa_log(f'path:{path}', 'debug')
        prompt = prompt.replace(f"path:{path}", file_content)
        prompt = prompt[:settings.MAX_PROMPT_LENGTH]

    return prompt


def pippa(custom_instructions_only=True):

    prompt = None
    if len(sys.argv) > 1:
        prompt = sys.argv[1]

    if custom_instructions_only:
        pippa_log(f'Using Custom Instructions Only: {settings.CUSTOM_INSTRUCTIONS}' )
        loader = TextLoader(settings.CUSTOM_INSTRUCTIONS)
    else:
        pippa_log(f'Reading all given data files in: {settings.DATA_FOLDER}"')
        loader = DirectoryLoader(settings.DATA_FOLDER)

    index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model=settings.GPT_MODEL, max_tokens=settings.MAX_TOKENS),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    chat_history = []
    while True:
        if not prompt:
            prompt = input("👨‍🦰 Bundy: ")
        if prompt.endswith('quit') or prompt.endswith('exit') :
            sys.exit()

        prompt = pre_process_prompt(prompt)

        result = chain({"question": prompt, "chat_history": chat_history})
        print("👧 Pippa:", result['answer'])

        chat_history.append((prompt, result['answer']))
        prompt = None


if __name__ == "__main__":
    list_openai_models()
    if settings.CUSTOM_INSTRUCTIONS_ONLY:
        pippa_log("CS Only Mode", log_type='info')
    else:
        list_files(settings.DATA_FOLDER)
    pippa(settings.CUSTOM_INSTRUCTIONS_ONLY)

