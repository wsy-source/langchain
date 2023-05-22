from typing import Any

from langchain.prompts import PromptTemplate, StringPromptTemplate, load_prompt

template = """
you are a assistant to help human to resolve some questions
user question: {question}
solution:

"""

# case1
prompt_template = PromptTemplate(template=template, input_variables=["question"])
print(prompt_template.format(question="how old are you"))
prompt = load_prompt("demo.json")
print("below is loaded")
print(prompt)

# case2
template = PromptTemplate.from_template(template)
print(template.format(question="how old are you"))


# case3 CustomPrompt
class MyCustomPrompt(StringPromptTemplate):
    def format(self, **kwargs: Any) -> str:
        question = kwargs["question"]
        promt = f"""
you are a assistant to help human to resolve some questions
user question: {question}
solution:
        """
        return promt


print(MyCustomPrompt(input_variables=["question"]).format(question="how old are you?"))

# case4 load and serialize
template = """
you are a assistant to help human to resolve some questions
user question: {question}
solution:

"""
# serialize
prompt_template = PromptTemplate(template=template, input_variables=["question"])
prompt_template.save("demo.json")

# load
prompt = load_prompt("demo.json")
print("below is loaded")
print(prompt)
