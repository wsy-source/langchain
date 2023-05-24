import env as env
from langchain.memory import ConversationTokenBufferMemory
from langchain.llms import AzureOpenAI
from langchain.chains import ConversationChain

llm = AzureOpenAI(deployment_name=env.deployment_name, model_name=env.model_name)

memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=1000)
chain = ConversationChain(llm=llm, verbose=True, memory=memory)
print(chain.predict(input="hi"))

