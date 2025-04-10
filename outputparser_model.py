from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class GeneratedPrompt(BaseModel):
    analyse: str = Field(description="场景分析内容")
    prompts: List[str] = Field(description="框架展示内容",min_items=3, max_items=3)
