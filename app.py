# -*- coding: utf-8 -*-
"""Gemma 3 27B IT WebUI 演示界面（不加载真实模型权重）。"""
from __future__ import annotations

import gradio as gr


def fake_load_model():
    """模拟加载模型，实际不下载权重，仅用于界面演示。"""
    # 在真实环境中，这里会调用 transformers 加载 google/gemma-3-27b-it 模型。
    # 为避免耗时下载与计算，这里仅返回状态文本。
    return "模型状态：Gemma 3 27B IT 已就绪（演示模式，未加载真实权重）"


def fake_image_text_to_text(text: str, image=None) -> str:
    """模拟图像-文本到文本的生成任务。"""
    if not text or not text.strip():
        return "请输入文本提示。"
    if image is None:
        return (
            "[演示] 基于文本输入，模型已生成以下响应：\n\n"
            "Gemma 3 27B IT 是一个多模态大语言模型，能够处理图像和文本输入，"
            "并生成相应的文本输出。该模型在图像理解、视觉问答、图像描述生成等任务中表现优异。"
        )
    return (
        "[演示] 基于图像和文本输入，模型已生成以下响应：\n\n"
        "模型已成功分析输入图像，并结合文本提示生成了相应的描述。"
        "Gemma 3 27B IT 能够理解图像中的视觉内容，并基于用户的问题或指令生成准确的文本回复。"
        "该模型支持多种视觉理解任务，包括图像问答、图像描述、视觉推理等。"
    )


def fake_text_generation(text: str, max_tokens: int = 200) -> str:
    """模拟纯文本生成任务。"""
    if not text or not text.strip():
        return "请输入文本提示。"
    return (
        f"[演示] 基于输入文本，模型已生成以下内容（最大长度：{max_tokens} tokens）：\n\n"
        "Gemma 3 27B IT 是一个强大的指令调优模型，能够根据用户的输入生成连贯、"
        "相关且有用的文本响应。该模型在对话、问答、摘要、推理等多种文本生成任务中表现优异。"
        "模型支持多轮对话，能够理解上下文并生成符合语境的回复。"
    )


def build_ui():
    with gr.Blocks(title="Gemma 3 27B IT WebUI") as demo:
        gr.Markdown("## Gemma 3 27B IT 多模态大语言模型 · WebUI 演示")
        gr.Markdown(
            "本界面以交互方式展示 Gemma 3 27B IT 模型的典型使用流程，"
            "包括模型加载状态监控、图像-文本到文本生成以及纯文本生成等环节。"
        )

        # 模型加载区
        with gr.Row():
            load_btn = gr.Button("加载模型（演示）", variant="primary")
            status_box = gr.Textbox(label="模型状态", value="尚未加载", interactive=False)
        load_btn.click(fn=fake_load_model, outputs=status_box)

        with gr.Tabs():
            # 图像-文本到文本
            with gr.Tab("图像-文本到文本生成"):
                gr.Markdown(
                    "该功能模拟将图像和文本输入转换为文本输出，"
                    "适用于图像问答、图像描述、视觉推理等任务。"
                )
                with gr.Row():
                    image_input = gr.Image(label="输入图像", type="pil")
                    text_input = gr.Textbox(
                        label="文本提示",
                        placeholder="例如：请描述这张图片中的内容。",
                        lines=4,
                    )
                image_text_output = gr.Textbox(label="生成结果", lines=8, interactive=False)
                image_text_btn = gr.Button("生成（演示）", variant="primary")
                image_text_btn.click(
                    fn=fake_image_text_to_text,
                    inputs=[text_input, image_input],
                    outputs=image_text_output
                )

            # 纯文本生成
            with gr.Tab("纯文本生成"):
                gr.Markdown(
                    "该功能模拟基于文本输入生成文本输出，"
                    "适用于对话、问答、摘要、推理等任务。"
                )
                text_prompt = gr.Textbox(
                    label="文本提示",
                    placeholder="例如：请解释一下量子计算的基本原理。",
                    lines=6,
                )
                max_tokens_slider = gr.Slider(
                    minimum=50,
                    maximum=1000,
                    value=200,
                    step=50,
                    label="最大生成长度（tokens）"
                )
                text_output = gr.Textbox(label="生成结果", lines=10, interactive=False)
                text_btn = gr.Button("生成（演示）", variant="primary")
                text_btn.click(
                    fn=fake_text_generation,
                    inputs=[text_prompt, max_tokens_slider],
                    outputs=text_output
                )

        gr.Markdown("---\n*说明：当前为轻量级演示界面，未实际下载与加载任何大规模模型参数。*")

    return demo


def main():
    app = build_ui()
    app.launch(server_name="127.0.0.1", server_port=7860, share=False)


if __name__ == "__main__":
    main()
