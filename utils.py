from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from prompt_template import system_template_text, user_template_text
from langchain.output_parsers import PydanticOutputParser
from outputparser_model import GeneratedPrompt

#import os

def generate_prompt(domain,objective,style,special_requirements,openai_api_key):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_template_text),
            ("user", user_template_text)
        ]
    )
    model = ChatOpenAI(model="gpt-4o",api_key=openai_api_key)
    output_parser = PydanticOutputParser(pydantic_object=GeneratedPrompt)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "domain": domain,
        "objective": objective,
        "style": style,
        "special_requirements": special_requirements
    })
    return result

# print(generate_prompt("招聘求职",
#                       "模拟面试官",
#                       "严肃认真",
#                       "用Markdown格式输出",
#                       os.getenv("OPENAI_API_KEY")))