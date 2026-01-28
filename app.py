# -*- coding: utf-8 -*-
"""Gemma 3 27B IT 多模态图像文本生成 WebUI（前端展示，不加载模型）"""
import gradio as gr

def run_inference(image, text_input, system_prompt, max_tokens, temperature):
    """多模态推理占位：仅展示界面与结果区域，不执行模型推理。"""
    if image is None and not text_input:
        return "请上传一张图片或输入文本提示。\n\n加载模型后，将在此显示生成的文本结果。"
    
    result = "【演示模式】未加载模型，以下为示例输出格式：\n\n"
    
    if image is not None:
        result += "✓ 已接收图像输入\n"
    if text_input:
        result += f"✓ 已接收文本输入：{text_input[:50]}...\n"
    
    result += "\n---\n"
    result += "【示例输出】\n"
    result += "加载模型后，Gemma 3 27B IT 将分析输入的图像和文本，生成相应的文本回复。\n\n"
    result += "模型特点：\n"
    result += "• 支持图像和文本的多模态输入\n"
    result += "• 128K token 上下文窗口（27B 版本）\n"
    result += "• 支持超过 140 种语言\n"
    result += "• 图像分辨率：896 x 896\n"
    result += "• 最大输出：8192 tokens\n"
    
    return result

with gr.Blocks(title="Gemma 3 27B IT WebUI", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # Gemma 3 27B IT 多模态图像文本生成 WebUI
    
    Gemma 3 是 Google 开发的多模态大语言模型，支持图像和文本输入，生成文本输出。
    本界面用于加载 Gemma 3 27B IT（Instruction-Tuned）模型进行多模态推理与结果可视化。
    
    **模型信息**：
    - 模型类型：多模态（图像-文本到文本）
    - 参数量：27B
    - 上下文窗口：128K tokens
    - 支持语言：140+ 种语言
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 输入区域")
            input_image = gr.Image(
                label="上传图片（可选）",
                type="pil",
                height=300
            )
            text_input = gr.Textbox(
                label="文本提示",
                placeholder="例如：What animal is in this image? 或 Tell me about this picture.",
                lines=3
            )
            system_prompt = gr.Textbox(
                label="系统提示（可选）",
                placeholder="例如：You are a helpful assistant.",
                lines=2,
                value="You are a helpful assistant."
            )
            
            with gr.Row():
                max_tokens = gr.Slider(
                    label="最大生成 tokens",
                    minimum=1,
                    maximum=8192,
                    value=200,
                    step=1
                )
                temperature = gr.Slider(
                    label="Temperature",
                    minimum=0.1,
                    maximum=2.0,
                    value=0.7,
                    step=0.1
                )
            
            run_btn = gr.Button("生成文本", variant="primary", size="lg")
            clear_btn = gr.Button("清空", variant="secondary")
        
        with gr.Column(scale=1):
            gr.Markdown("### 输出区域")
            output_text = gr.Textbox(
                label="生成结果",
                lines=15,
                interactive=False
            )
            
            gr.Markdown("""
            ### 使用说明
            
            1. **上传图片**（可选）：支持 PNG、JPG 等格式，模型会将图像编码为 256 tokens
            2. **输入文本提示**：描述你想要模型完成的任务
            3. **设置参数**：调整最大生成 tokens 和 temperature
            4. **点击生成**：模型将分析输入并生成文本回复
            
            **注意**：当前为演示模式，实际使用时需要加载模型权重。
            """)
    
    # 绑定事件
    run_btn.click(
        fn=run_inference,
        inputs=[input_image, text_input, system_prompt, max_tokens, temperature],
        outputs=[output_text]
    )
    
    def clear_all():
        return None, "", "You are a helpful assistant.", 200, 0.7, ""
    
    clear_btn.click(
        fn=clear_all,
        outputs=[input_image, text_input, system_prompt, max_tokens, temperature, output_text]
    )
    
    gr.Markdown("""
    ---
    **模型说明**：Gemma 3 27B IT 是基于 Transformer 架构的多模态大语言模型，支持图像和文本的联合理解与生成。
    更多相关项目源码请访问：http://www.visionstudios.ltd
    """)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
