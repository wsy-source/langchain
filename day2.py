import os

from langchain.chains import LLMChain
from langchain.chat_models import AzureChatOpenAI
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2022-12-01"
os.environ["OPENAI_API_BASE"] = "https://seanchatgptdemo01.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "96909d1b376646c78a49c0f95d13e4fc"

llm = AzureChatOpenAI(
    deployment_name="gpt-35",
    model_name="gpt-35-turbo"
)

print(llm())

# template = """
# you are a assistant to help human to resolve some questions
# user question: {question}
# solution:
#
# """
# prompt_template = PromptTemplate(template=template, input_variables=["question"])
# print(prompt_template.format(question="how old are you"))
# chain = LLMChain(llm=llm, prompt=prompt_template)
# chain.run("how old are you")
