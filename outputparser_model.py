from pydantic import BaseModel, Field, field_validator
from typing import List
from typing_extensions import Annotated

PromptList = Annotated[
    List[str],
    Field(description="框架展示内容")
]

class GeneratedPrompt(BaseModel):
    analyse: str = Field(description="场景分析内容")
    prompts: PromptList

    @classmethod
    @field_validator("prompts")
    def validate_prompt_count(cls,v: List[str]) -> List[str]:
        if len(v) != 3:
            raise ValueError("prompts列表长度必须正好为 3 个模板")
        return v

#class GeneratedPrompt(BaseModel):
#    analyse: str = Field(description="场景分析内容")
#    prompts: List[str] = Field(description="框架展示内容",min_items=3, max_items=3)
