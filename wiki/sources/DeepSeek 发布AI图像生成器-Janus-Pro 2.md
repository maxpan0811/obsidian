---
title: "DeepSeek 发布AI图像生成器：Janus-Pro 2"
type: source
created: 2026-07-06
updated: 2026-07-06
source_path: 印象笔记管理工具/DeepSeek 发布AI图像生成器：Janus-Pro 2.md
tags: [evernote, impression, yinxiang]
---

# DeepSeek 发布AI图像生成器：Janus-Pro

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzk0NjY0MTc0NA==&mid=224748...](https://mp.weixin.qq.com/s?__biz=Mzk0NjY0MTc0NA==&mid=2247486644&idx=1&sn=4da825c45933b4b54546f4b651dd241d&chksm=c27a1b7c14a4582ccc35ceab23948d512a544f814539bd4630ca5228e802890492b03164b6e0&scene=132&exptype=timeline_recommend_article_extendread_extendread&show_related_article=1&subscene=169&ascene=0&devicetype=iOS18.3&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQmUrZwe1hsa+s7oqkH73VxRLWAQIE97dBBAEAAAAAACuoC4rdJBQAAAAOpnltbLcz9gKNyK89dVj0SxTWqWbwJK3EPa8IxdNFj8W7tqT2PnJmxgjILmICjs4EaHL1wH5nXGnonReRXuNerHAhyL3YdGcJtK0qf8W4YAGLeesppxXUauoRYUKU4LYr58svLupNimR7ZSjzUscxIMcfJ3ACC88HY3w+MYnI+2lJIHLfBzfedTUtHUy5iYfKOfojgbhAcPJJZR2xFXws/TDmCjJDUzPG0r2KExu3kNorOjCNQE96008TsZuhIRg=&pass_ticket=AsB8BpomGKIOU09UD4GyELghYxl3k/f7bmMckPvg+fb+CVO7He6oVi3BL6NLzo+o&wx_header=3)

原创 一叶扁舟 代码麻辣烫

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/A798DB5B-7EF8-4DFB-90F0-F774CE93AB30.png)

*使用 Flux Labs AI 生成的图像*

DeepSeek 的 R-1 模型最近几天在全球引起了广泛关注。它是一个开源且价格实惠的替代品，与 OpenAI 的 o1 模型性能相当。然而，在 R-1 的热度尚未消退之际，这家初创公司又发布了一款名为 **Janus-Pro** 的开源 AI 图像模型。

DeepSeek 表示，Janus-Pro 7B 在多个基准测试中表现优于 OpenAI 的 Dall-E 3 和 Stable Diffusion。但事实真的如此吗？它是否真的符合这些说法，还只是在蹭 AI 的热度？

让我们来一探究竟。

什么是 Janus-Pro？
--------------

简单来说，Janus-Pro 是一款强大的 AI 模型，能够理解图像和文本，并且可以根据文本描述生成图像。

Janus-Pro 是 Janus 模型的增强版本，专为统一的多模态理解和生成而设计。它采用了更好的训练方法、更多的数据以及更大的模型规模。此外，它还能够为简短的提示提供更稳定的输出，生成的图像视觉质量更高，细节更丰富，并且具备生成简单文本的能力。

以下是一些示例：

**提示：** 一位美丽女孩的面容

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/F9D4DC7C-D65D-4F00-B201-65CF361DF921.png)

*来自 DeepSeek 的图像*

新模型在渲染文本方面也更具能力。

**提示：** 一块清晰的黑板，表面为深绿色，中央用白色粉笔清晰、整齐地写着“Hello”。

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/63E9514C-97F4-4EC5-AAB7-5AF5A5B22199.png)

*来自 DeepSeek 的图像*

Janus-Pro 系列包括两种模型规模：10 亿和 70 亿，展示了视觉编码和解码方法的可扩展性。这两种模型生成的图像分辨率均为 384 × 384。

在商业许可方面，该模型可用于学术和商业用途。

Janus-Pro 的技术细节
---------------

Janus-Pro 使用不同的视觉编码方法来处理多模态理解和视觉生成任务。这种设计旨在减少这两种任务之间的冲突，从而提高整体性能。

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/9FD8AEEE-A14A-4B42-AA5C-3EC01A44AB13.png)

*来自 DeepSeek 的图像*

对于多模态理解，Janus-Pro 使用 SigLIP 编码器 从图像中提取高维语义特征，然后通过理解适配器将这些特征映射到 LLM 的输入空间。

对于视觉生成，该模型使用 VQ 分词器 将图像转换为离散 ID，然后通过生成适配器将这些 ID 映射到 LLM 的输入空间。

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/BB091761-F612-43F5-B830-620F8E3093F9.png)

*来自 DeepSeek 的图像*

在文本到图像的指令遵循方面，Janus-Pro-7B 在 GenEval 基准测试 中得分为 0.80，超过了其他模型，例如 OpenAI 的 Dall-E 3 和 Stability AI 的 Stable Diffusion 3 Medium。

此外，Janus-Pro-7B 在 DPG-Bench 中得分为 84.19，超过了所有其他方法，展示了其在文本到图像生成中遵循密集指令的能力。

Janus-Pro 是否优于 Dall-E 3 或 Stable Diffusion？
-------------------------------------------

根据 DeepSeek 的内部基准测试，Dall-E 3 和 Stable Diffusion 模型在 GenEval 和 DPG-Bench 基准测试中的得分较低。

但我对这些信息持怀疑态度，因为样本图像看起来并不理想。最好的办法是亲自测试一下。让我们来看一些示例：

**提示：** 一片绿地上有一群红色的羊。

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/B5E23325-80FF-478D-BB50-E287E1331D31.png)

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/579E77FF-4D6B-43B4-97F4-793423F706F9.jpg)

*第一个图像（Janus-Pro），第二个图像（Dall-E 3）*

**提示：** 一位美丽的 35 岁女性，身材适中，穿着粉色薄纱连衣裙，坐在埃菲尔铁塔前的地上。柔和的光线照亮了她的脸，背景是巴黎，风格为香奈儿。她的肩长棕色头发以松散的波浪形垂落，偏向一侧。

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/66318E72-E70D-4C60-82FA-8E4A8E2FBCE9.png)

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/06EB6A68-2C26-4212-96C0-FFC313A75FA5.png)

*第一个图像（Janus-Pro），第二个图像（Dall-E 3）*

**提示：** 一个小男孩手里拿着一块白色板子，上面写着“AI 太棒了！”

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/B3CB0F44-9142-4B34-9F8C-8E1AA52F5FD1.png)

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/F4E5E1AB-1050-4203-8DC9-3ADAB1CD32DB.png)

*第一个图像（Janus-Pro），第二个图像（Dall-E 3）*

根据上述示例，Dall-E 3 的表现明显优于 Janus Pro。Janus Pro 输出的图像中人物面部和身体比例明显不协调，而且在文本渲染方面也显得力不从心。

当然，也许是我遗漏了某些内容——可能需要特定的参数或微调才能改善结果。然而，按照默认设置，输出结果确实让人有些失望。

如何获取 Janus-Pro？
---------------

DeepSeek 在 HuggingFace 上向公众发布了 Janus，以支持学术和商业社区内更广泛、更多样化的研究。

* Janus-1.3B：Hugging Face 链接
* JanusFlow-1.3B：Hugging Face 链接
* Janus-Pro-1B：Hugging Face 链接
* Janus-Pro-7B：Hugging Face 链接

需要注意的是，拥有 70 亿参数的 Janus-Pro 模型可能会占用你设备内存的近 15GB。

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/B6B0C984-51AF-4329-B554-01CEE2517752.png)

*由 Jim Clyde Monge 提供的图像*

如果你不想在自己的硬件上运行模型，可以直接在 HuggingFace 上运行 Gradio 演示。

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/C81866E2-79FA-4089-B19B-0FC215E7CB67.png)

*由 Jim Clyde Monge 提供的图像*

使用起来非常简单。只需描述你想要生成的图像，然后点击“生成图像”按钮即可。生成速度取决于同时使用该应用的用户数量。

你还可以通过上传图像并要求 AI 解释它来尝试多模态理解功能。以下是一个示例：

**提示：** 解释这张梗图

![](.evernote-content/77977D25-4781-411F-B3A2-85DE3CA06EA0/469B94A1-A86A-41AD-A583-32B22CE27286.png)

*来自 DeepSeek HuggingFace 应用的图像*

这张图是一个幽默的比较，展示了两种视觉编码方法，使用了流行的“buff Doge vs. Cheems”梗图格式。

它非常准确，我认为这是一个为照片添加自动字幕或替代文本的绝佳工具。

对于开发者来说，你可以下载模型并在本地磁盘上运行。以下是一个从文本生成图像的示例推理代码：

```
import os  
import PIL.Image  
import torch  
import numpy as np  
from transformers import AutoModelForCausalLM  
from janus.models import MultiModalityCausalLM, VLChatProcessor  
  
model_path = "deepseek-ai/Janus-Pro-7B"  
vl_chat_processor: VLChatProcessor = VLChatProcessor.from_pretrained(model_path)  
tokenizer = vl_chat_processor.tokenizer  
vl_gpt: MultiModalityCausalLM = AutoModelForCausalLM.from_pretrained(  
    model_path, trust_remote_code=True  
)  
vl_gpt = vl_gpt.to(torch.bfloat16).cuda().eval()  
  
conversation = [  
    {  
        "role": "<|User|>",  
        "content": "一位来自喀布尔的美丽公主，穿着红色、白色的传统服装，蓝眼睛，棕色头发",  
    },  
    {"role": "<|Assistant|>", "content": ""},  
]  
sft_format = vl_chat_processor.apply_sft_template_for_multi_turn_prompts(  
    conversations=conversation,  
    sft_format=vl_chat_processor.sft_format,  
    system_prompt="",  
)  
prompt = sft_format + vl_chat_processor.image_start_tag  
  
@torch.inference_mode()  
def generate(  
    mmgpt: MultiModalityCausalLM,  
    vl_chat_processor: VLChatProcessor,  
    prompt: str,  
    temperature: float = 1,  
    parallel_size: int = 16,  
    cfg_weight: float = 5,  
    image_token_num_per_image: int = 576,  
    img_size: int = 384,  
    patch_size: int = 16,  
):  
    input_ids = vl_chat_processor.tokenizer.encode(prompt)  
    input_ids = torch.LongTensor(input_ids)  
    tokens = torch.zeros((parallel_size * 2, len(input_ids)), dtype=torch.int).cuda()  
    for i in range(parallel_size * 2):  
        tokens[i, :] = input_ids  
        if i % 2 != 0:  
            tokens[i, 1:-1] = vl_chat_processor.pad_id  
    inputs_embeds = mmgpt.language_model.get_input_embeddings()(tokens)  
    generated_tokens = torch.zeros((parallel_size, image_token_num_per_image), dtype=torch.int).cuda()  
    for i in range(image_token_num_per_image):  
        outputs = mmgpt.language_model.model(inputs_embeds=inputs_embeds, use_cache=True, past_key_values=outputs.past_key_values if i != 0elseNone)  
        hidden_states = outputs.last_hidden_state  
        logits = mmgpt.gen_head(hidden_states[:, -1, :])  
        logit_cond = logits[0::2, :]  
        logit_uncond = logits[1::2, :]  
        logits = logit_uncond + cfg_weight * (logit_cond - logit_uncond)  
        probs = torch.softmax(logits / temperature, dim=-1)  
        next_token = torch.multinomial(probs, num_samples=1)  
        generated_tokens[:, i] = next_token.squeeze(dim=-1)  
        next_token = torch.cat([next_token.unsqueeze(dim=1), next_token.unsqueeze(dim=1)], dim=1).view(-1)  
        img_embeds = mmgpt.prepare_gen_img_embeds(next_token)  
        inputs_embeds = img_embeds.unsqueeze(dim=1)  
    dec = mmgpt.gen_vision_model.decode_code(generated_tokens.to(dtype=torch.int), shape=[parallel_size, 8, img_size // patch_size, img_size // patch_size])  
    dec = dec.to(torch.float32).cpu().numpy().transpose(0, 2, 3, 1)  
    dec = np.clip((dec + 1) / 2 * 255, 0, 255)  
    visual_img = np.zeros((parallel_size, img_size, img_size, 3), dtype=np.uint8)  
    visual_img[:, :, :] = dec  
    os.makedirs('generated_samples', exist_ok=True)  
    for i in range(parallel_size):  
        save_path = os.path.join('generated_samples', f"img_{i}.jpg")  
        PIL.Image.fromarray(visual_img[i]).save(save_path)  
  
generate(  
    vl_gpt,  
    vl_chat_processor,  
    prompt,  
)
```

最终看法
----

我理解围绕这款新图像模型的炒作。人们声称它是 Dall-E 3 的一个不错的选择，但我不认同这种说法。我自己尝试了 Janus-Pro，但生成的图像质量并没有我想象中的那么令人印象深刻。

一个关键限制是其受限的输入分辨率，仅为 384 × 384。此外，文本到图像生成的分辨率较低，加上视觉分词器带来的重建损失，可能会导致生成的图像缺乏许多用户期望的细节。

尽管如此，像 Janus-Pro 这样的开源模型的快速出现表明，DeepSeek 已经在 AI 竞赛中定位自己为一个强大的搅局者。尽管目前存在质量限制，但他们推动开放创新的努力无疑让行业领导者们手忙脚乱。

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzk0NjY0MTc0NA==&mid=2247486644&idx=1&sn=4da825c45933b4b54546f4b651dd241d&chksm=c27a1b7c14a4582ccc35ceab23948d512a544f814539bd4630ca5228e802890492b03164b6e0&scene=132&exptype=timeline_recommend_article_extendread_extendread&show_related_article=1&subscene=169&ascene=0&devicetype=iOS18.3&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQmUrZwe1hsa+s7oqkH73VxRLWAQIE97dBBAEAAAAAACuoC4rdJBQAAAAOpnltbLcz9gKNyK89dVj0SxTWqWbwJK3EPa8IxdNFj8W7tqT2PnJmxgjILmICjs4EaHL1wH5nXGnonReRXuNerHAhyL3YdGcJtK0qf8W4YAGLeesppxXUauoRYUKU4LYr58svLupNimR7ZSjzUscxIMcfJ3ACC88HY3w+MYnI+2lJIHLfBzfedTUtHUy5iYfKOfojgbhAcPJJZR2xFXws/TDmCjJDUzPG0r2KExu3kNorOjCNQE96008TsZuhIRg=&pass_ticket=AsB8BpomGKIOU09UD4GyELghYxl3k/f7bmMckPvg+fb+CVO7He6oVi3BL6NLzo+o&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/8bd56482-426e-48a3-936e-8ff2bf5dcd1d/8bd56482-426e-48a3-936e-8ff2bf5dcd1d/)
