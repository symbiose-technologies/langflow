## LLM
from typing import Any

from langchain import llms
from langchain.llms.openai import OpenAIChat

llm_type_to_cls_dict = llms.type_to_cls_dict
llm_type_to_cls_dict["openai-chat"] = OpenAIChat


## Memory

from langchain.memory.buffer_window import ConversationBufferWindowMemory
from langchain.memory.chat_memory import (
    ChatMessageHistory,
    BaseChatMemory
)
from langchain.memory.combined import CombinedMemory
from langchain.memory.entity import ConversationEntityMemory
from langchain.memory.kg import ConversationKGMemory
from langchain.memory.readonly import ReadOnlySharedMemory
from langchain.memory.simple import SimpleMemory
from langchain.memory.summary import ConversationSummaryMemory
from langchain.memory.summary_buffer import ConversationSummaryBufferMemory
memory_type_to_cls_dict: dict[str, Any] = {
    "CombinedMemory": CombinedMemory,
    "ConversationBufferWindowMemory": ConversationBufferWindowMemory,
    "SimpleMemory": SimpleMemory,
    "BaseChatMemory": BaseChatMemory,
    "ConversationSummaryBufferMemory": ConversationSummaryBufferMemory,
    "ConversationKGMemory": ConversationKGMemory,
    "ConversationEntityMemory": ConversationEntityMemory,
    "ConversationSummaryMemory": ConversationSummaryMemory,
    "ChatMessageHistory": ChatMessageHistory,
    # "ConversationStringBufferMemory": ConversationStringBufferMemory,
    "ReadOnlySharedMemory": ReadOnlySharedMemory,
}


## Chain
from langchain.chains.conversation.base import ConversationChain
from langchain.chains.loading import type_to_loader_dict

chain_type_to_cls_dict = type_to_loader_dict
# chain_type_to_cls_dict["conversation_chain"] = ConversationChain

## Tools
from langchain.tools.bing_search.tool import BingSearchRun
from langchain.tools.google_search.tool import GoogleSearchResults, GoogleSearchRun
from langchain.tools.python.tool import PythonREPLTool
from langchain.tools.requests.tool import RequestsGetTool
from langchain.tools.wikipedia.tool import WikipediaQueryRun
from langchain.tools.wolfram_alpha.tool import WolframAlphaQueryRun
from langchain.utilities.bash import BashProcess
from langchain.utilities.bing_search import BingSearchAPIWrapper
from langchain.utilities.google_search import GoogleSearchAPIWrapper
from langchain.utilities.google_serper import GoogleSerperAPIWrapper
from langchain.utilities.searx_search import SearxSearchWrapper
from langchain.utilities.serpapi import SerpAPIWrapper
from langchain.utilities.wikipedia import WikipediaAPIWrapper
from langchain.utilities.wolfram_alpha import WolframAlphaAPIWrapper

tool_type_to_cls_dict: dict[str, Any] = {
    "BingSearchRun": BingSearchRun,
    "GoogleSearchResults": GoogleSearchResults,
    "GoogleSearchRun": GoogleSearchRun,
    "PythonREPLTool": PythonREPLTool,
    "RequestsGetTool": RequestsGetTool,
    "WikipediaQueryRun": WikipediaQueryRun,
    "WolframAlphaQueryRun": WolframAlphaQueryRun,
    # "BashProcess": BashProcess,
    "BingSearchAPIWrapper": BingSearchAPIWrapper,
    "GoogleSearchAPIWrapper": GoogleSearchAPIWrapper,
    "GoogleSerperAPIWrapper": GoogleSerperAPIWrapper,
    "SearxSearchWrapper": SearxSearchWrapper,
    "SerpAPIWrapper": SerpAPIWrapper,
    "WikipediaAPIWrapper": WikipediaAPIWrapper,
    "WolframAlphaAPIWrapper": WolframAlphaAPIWrapper,
}
