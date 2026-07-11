# 微软又开源一个神级 skill 神器 。

---

原文链接: [https://mp.weixin.qq.com/s?\_\_biz=Mzg3NzU0NzIxMA==&mid=224751...](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247513164&idx=1&sn=292912928e729d8bc00e0498482f47d8&chksm=ce582ed62abbf3708b26c445eadc29bcb745d99891caf9b99a84861ed52cd04608e0cd00132b&scene=90&xtrack=1&req_id=1782292625192273&sessionid=1782291718&subscene=93&clicktime=1782292759&enterid=1782292759&flutter_pos=11&biz_enter_id=4&ranksessionid=1782292625&jumppath=WAWebViewController_1782292743351,WAWebViewController_1782292743857,20020_1782292753043,1104_1782292753755&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQVrdnb2q6VXdt8Gtf+MW3+BLTAQIE97dBBAEAAAAAAPaMF7rAs0QAAAAOpnltbLcz9gKNyK89dVj0Vs8wLfeRIUFbnN2zG7umzuwztHxHq8ftEjTppvujGcNAuEbNiciP/OUHF1wJTYT/wYfQ+kd7o/YEUtaBGzShgqPTdPaSu8vP0i75K/EfRkpJ+yMfnP8a/iFNBYPW6CEraOIaH77K37Y393kpw8KdAqWM8GuwwmCGJrSfEcJ0enCxEnmGiqKzCjaq23TsB/nPur9E8AbWu7wE5xUSwJlgDVCLa94Vf7Ht53rQUvY=&pass_ticket=LDNJrYMevRTChf0GPt3TeGrkwXoUD4iWRI5KCE0bygTy8FjO2Vz/qtrZOOAwv/VT&wx_header=3)

微软又开源一个神级 skill 神器 。
====================

Original开源日记开源日记

最近 SkillOpt 很火。

微软的这个开源项目已经拿下 9000+ Star。

![](.evernote-content/DAF9DBF1-FAF4-4532-9A9F-D5E48A641F74/E3E2FC9F-1F66-49F8-A3CD-89787574E6CB.png)

它把写Agent技能文档这件事也变成了一种真正的训练过程。

前向传播、反向传播、参数更新、门控验证等等全都用了上。

**简单来说，SkillOpt 就是专门帮 Agent 打磨 skill.md 的，把原本靠经验写的技能文档，变成像训练模型一样不断迭代优化。**

![](.evernote-content/DAF9DBF1-FAF4-4532-9A9F-D5E48A641F74/D2F1A8B4-B029-4A8F-9A19-FCC491EC40DB.png)

平时写技能文档就是这样的：

写了份技能文档之后就把它丢给了 Agent 去执行任务，结果不理想就又改了文档再运行一次，还是不行……

错误率高，并且没有系统的办法。

整个过程就是补课，但是没有考试、没有分数、不知道是对是错。

SkillOpt 把整个过程变成了一种真正的训练过程。
---------------------------

![](.evernote-content/DAF9DBF1-FAF4-4532-9A9F-D5E48A641F74/314BEC7C-AE38-45D5-B6A2-50D3211E0208.png)

假如你要写一本《做菜指南》来教会一个初学者学会做饭。

**01 先让他做一次，并且把整个过程都记录下来。**

新手拿着你的指南走进厨房，你得让他把整个过程都记录下来：用了哪些食材、加了多少调料、温度是多少度、最后的味道如何。

SkillOpt 也是这样：让 Agent 用现有的技能文档来运行一些任务，并且把整个执行的过程、工具调用、验证反馈和最终得分全部记录下来。

这就如同深度学习中的“前向传播”，运行一次，观察一下结果。

**02 查看记录，找到问题。**

你看他做的记录，好的菜都有放盐，不好的就没有放盐。

找到问题了，在指南中没有提到“要放盐”。

SkillOpt 也是一样的：用一个单独的模型来分析这些轨迹，并找到哪里是错的、哪里是对的。

也就是说，它把失败与成功的过程分开来处理——失败的过程用来找出“哪些规则要修改”，而成功的过程则用来确定“哪些规则是有效的，不能随便改动”。

这就相当于在计算“梯度方向”，知道要朝哪个方向去修改。

![](.evernote-content/DAF9DBF1-FAF4-4532-9A9F-D5E48A641F74/E82BE627-B229-468F-94D9-8B0FD5D3C232.png)

**03 改指南但是不要改太多。**

你要修改指南，但是每次只改一两个地方。

为什么不能一次性全部修改呢？因为改动太多，你就不知道是哪一个改动起了作用，如果改错了也无从得知哪里错了。

SkillOpt 也一样：提出具体的操作——增加新的规则、去掉无用的规则、修改要改正的规则。

有一个很重要的概念叫做“文本学习率”，默认值为4，表示每次最多修改4处。

这就如同在深度学习中使用的learning rate一样，避免一次改变过大而把之前学到的东西给覆盖掉了。

**04 试过了才知道，改对了才会留下。**

新手拿着新的指南再试一次，如果菜变好吃的话，就说明改对了；如果没有变好吃，那么这个改动就被否决了，你要把这一个方向错误记录下来。

SkillOpt 也一样：新技能文档要在验证集上严格提高性能之后才被接受。

![](.evernote-content/DAF9DBF1-FAF4-4532-9A9F-D5E48A641F74/1AB60C95-EFBC-4959-B5BD-8A1D09822EF7.png)

如果验证失败的话，那么这个编辑就会被拒绝并且记录在“拒绝编辑缓冲区”中，以防止下一次再出现相同的失败方向。

这就如同在深度学习中进行验证一样，保证修改的方向是正确的。

还有一个亮点：迁移能力。
------------

GPT-5.5 训练出的技能文档可以被直接应用到 GPT-5.4-mini 上；在 Codex 上训练出来的也可以用在 Claude Code 上。

![](.evernote-content/DAF9DBF1-FAF4-4532-9A9F-D5E48A641F74/AB62524F-1F40-41E6-B727-022513C7D8A9.png)

这就意味着你可以不用为每一个模型都重新编写技能文档了，只需要训练一次就可以重复使用。

测试结果怎么样？
--------

52 个测试场景中，全部都是最好或者并列最好的。GPT-5.5 平均提高了 23.5 个百分点，在 ALFWorld 上 GPT-5.4-mini 由原来的 70.9% 提升到了现在的 85.8%。

![](.evernote-content/DAF9DBF1-FAF4-4532-9A9F-D5E48A641F74/195384AD-C60F-4BAB-94B1-474EB025BE6B.png)

只用了 4 个被接受的编辑。

训练中分数逐渐提高，被拒的编辑也可以看到。

![](.evernote-content/DAF9DBF1-FAF4-4532-9A9F-D5E48A641F74/FEF4BC4F-F5E2-4D7E-A346-3E09C44ECE2D.png)

如果你也想试一下，可以参考下面的步骤。
-------------------

**01 安装。**

```
git clone https://github.com/microsoft/SkillOpt.git  
cd SkillOpt  
pip install -e .
```

**02 配置 API。**

把`.env.example` 复制一份到`.env`里，并把里面的API密钥填上：

```
# OpenAI  
export OPENAI_API_KEY="sk-..."  
  
# 或 Azure OpenAI  
export AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"  
export AZURE_OPENAI_API_KEY="your-key"  
  
# 或 Anthropic Claude  
export ANTHROPIC_API_KEY="sk-ant-..."
```

**03 准备数据。**

两种方式：

* **自动划分**：准备好原始数据，让 SkillOpt 自动划分训练集、验证集、测试集
* **手动划分**：自己准备好三个文件夹

**04 开始训练。**

```
python scripts/train.py --config configs/searchqa/default.yaml
```

可以指定teacher和student模型：

```
python scripts/train.py \  
  --config configs/searchqa/default.yaml \  
  --teacher_model gpt-5.5 \  
  --student_model gpt-5.5
```

**05 查看结果。**

训练完成后，输出目录结构：

```
outputs/<run_name>/  
├── best_skill.md #最后训练出的技能文档  
├── skills/       #每个步骤都对应一个技能快照  
├── steps/        #每个步骤都做了详细的记录  
└── history.json  #训练历史
```

**06 部署使用。**

把 best\_skill.md 文件的内容直接放入到Agent的system prompt中就可以使用了。

整个训练过程中没有增加额外的推理开销，在部署的时候也不需要调用优化器模型，只是多了一个Markdown文件。

写到最后
----

SkillOpt 让我重新思考了一个问题：

Agent 的能力上限，到底是受限于模型本身，还是技能文档的质量？

过去人们只重视模型的能力，而现在发现技能文档的质量也很重要。

即使模型很强，但是文档写得不好，那么Agent也无法很好地发挥作用。

SkillOpt 提供了一个系统化的方案，让技能文档可以像模型一样不断训练和优化。

这可能会成为 Agent 工具链发展的重要方向。

项目基于 MIT 协议开放，感兴趣的同学可以去 GitHub 仓库看看源码和文档。

开源地址：https://github.com/microsoft/SkillOpt

既然看到这了，欢迎随手点赞、在看、转发，也可以给我一个星标⭐，接收最新的文章，我们下期见！

---

[🌐 原始链接](https://mp.weixin.qq.com/s?__biz=Mzg3NzU0NzIxMA==&mid=2247513164&idx=1&sn=292912928e729d8bc00e0498482f47d8&chksm=ce582ed62abbf3708b26c445eadc29bcb745d99891caf9b99a84861ed52cd04608e0cd00132b&scene=90&xtrack=1&req_id=1782292625192273&sessionid=1782291718&subscene=93&clicktime=1782292759&enterid=1782292759&flutter_pos=11&biz_enter_id=4&ranksessionid=1782292625&jumppath=WAWebViewController_1782292743351,WAWebViewController_1782292743857,20020_1782292753043,1104_1782292753755&jumppathdepth=4&ascene=56&devicetype=iOS26.5&version=18004b2b&nettype=3G+&abtest_cookie=AAACAA==&lang=en&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQVrdnb2q6VXdt8Gtf+MW3+BLTAQIE97dBBAEAAAAAAPaMF7rAs0QAAAAOpnltbLcz9gKNyK89dVj0Vs8wLfeRIUFbnN2zG7umzuwztHxHq8ftEjTppvujGcNAuEbNiciP/OUHF1wJTYT/wYfQ+kd7o/YEUtaBGzShgqPTdPaSu8vP0i75K/EfRkpJ+yMfnP8a/iFNBYPW6CEraOIaH77K37Y393kpw8KdAqWM8GuwwmCGJrSfEcJ0enCxEnmGiqKzCjaq23TsB/nPur9E8AbWu7wE5xUSwJlgDVCLa94Vf7Ht53rQUvY=&pass_ticket=LDNJrYMevRTChf0GPt3TeGrkwXoUD4iWRI5KCE0bygTy8FjO2Vz/qtrZOOAwv/VT&wx_header=3)

[📎 在印象笔记中打开](evernote:///view/207087/s1/c4cacee4-a350-4065-8bcb-2029e98633a4/c4cacee4-a350-4065-8bcb-2029e98633a4/)