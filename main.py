import streamlit as st
from utils import generate_prompt


st.header("提示词工程小助手✍🏻")
with st.sidebar:
    openai_api_key = st.text_input("请输入API密钥：", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

domain = st.text_input("输入应用领域（如招聘求职、运动健身、旅游出行、机械设计、AI大模型等）：")
objective = st.text_input("输入目标主题（如模拟面试官、健身教练、导游、设计师、程序员等）：")
style = st.text_input("指定生成风格（如严肃认真、轻松愉快、热情洋溢、幽默风趣等）：")
special_requirements = st.text_input("添加特殊请求（如使用Markdown格式输出等，没有则填无）：")
submit = st.button("生成✔️")

if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥！")
    st.stop()
if submit and not domain:
    st.info("请输入应用领域！")
    st.stop()
if submit and not objective:
    st.info("请输入目标主题！")
    st.stop()
if submit and not style:
    st.info("请指定生成风格！")
    st.stop()
if submit and not special_requirements:
    st.info("请添加特殊请求！")
    st.stop()
if submit:
    with st.spinner("AI正在努力创作中，请稍候..."):
        result = generate_prompt(domain,objective,style,special_requirements,openai_api_key)
    st.divider()
    st.markdown("#### 场景分析")
    st.write(result.analyse)
    with st.expander("模板1"):
        st.write(result.prompts[0])
    with st.expander("模板2"):
        st.write(result.prompts[1])
    with st.expander("模板3"):
        st.write(result.prompts[2])