import os

from langchain.chains import LLMChain
from langchain.chat_models import AzureChatOpenAI
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-05-15"
os.environ["OPENAI_API_BASE"] = "https://seanchatgptdemo01.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "96909d1b376646c78a49c0f95d13e4fc"

llm = AzureOpenAI(
    deployment_name="text-davinci-003",
    model_name="text-davinci-003"
)

template = """
you are a assistant to help human to resolve some questions
user question: {question}
solution:

"""
prompt_template = PromptTemplate(template=template, input_variables=["question"])
chain = LLMChain(llm=llm, prompt=prompt_template)
print(chain.run(question="what can you do for me ?"))
