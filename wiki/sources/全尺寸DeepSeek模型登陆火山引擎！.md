---
title: 全尺寸DeepSeek模型登陆火山引擎！
type: source
created: 2026-06-17
updated: 2026-06-17
source: 印象笔记管理工具
source_path: 印象笔记管理工具/全尺寸DeepSeek模型登陆火山引擎！.html
tags: [AI技术, 教育]
updated: 2026-06-27
updated: 2026-06-27
updated: 2026-06-27
---

---
title: "全尺寸DeepSeek模型登陆火山引擎！"
source: evernote
type: note
export_date: 2026-06-24
guid: fecbc1e9-6253-4580-ac94-befc7ca9f346
---

# 全尺寸DeepSeek模型登陆火山引擎！

原文链接: [https://mp.weixin.qq.com/s?chksm=e9ace87cdedb616a1625a21d200ab97...](https://mp.weixin.qq.com/s?chksm=e9ace87cdedb616a1625a21d200ab97a0f7a5f2f35bca2acefb0b7efc2161de8d7c1528b28ac&exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1738681513_1&scene=169&mid=2247521724&sn=b55337b5aa3a2df4ae987f837f2bd703&idx=1&__biz=MzI0NzU1NzI5NQ==&sessionid=1738682876&subscene=200&clicktime=1738683122&enterid=1738683122&flutter_pos=23&biz_enter_id=5&ascene=56&devicetype=iOS18.3&version=1800382d&nettype=3G+&abtest_cookie=AAACAA==&lang=zh_CN&countrycode=CN&fontScale=115&exportkey=n_ChQIAhIQB2629GD72Tsl990G3gnQQhLWAQIE97dBBAEAAAAAADa3BKeHr30AAAAOpnltbLcz9gKNyK89dVj0Su1iel6g4C0Btl+LoQ5+qdQLNBl0HeFknMW0swFtdwyt7sFuWvemzysnT0QmXlGm/fmGRWba966sg5RUZN/RtbUTxrF0fwVqaY72cjOi4NyA0uOGdLCHlNmp7M72Q/pHq7cZcrNZyhHDMKxsd+1JDx3S1i3DwzkhHQrzAggk1kGX8rV7OqAWBPLSp680673K/fz5RMog+v6S6SbRYtJGH46yu9DBIhPVmA0GPXfy6vo=&pass_ticket=EwfWBElVO+zX8Q3Mtqiur4/5mDORQfuJBbx/7bMQ7bvRjGIPTrdFrsiC6ldoWGLH&wx_header=3)

原创 面向AI时代的 火山引擎

作为开放的云与 AI 服务提供商，除了豆包大模型之外，火山引擎还为企业提供各类主流三方大模型服务支持，满足企业不同场景的模型需求，目前已经支持月之暗面、智谱、Mistral 等多个系列模型。

今天，火山引擎将支持 V3/R1 等不同尺寸的 DeepSeek 开源模型，可以通过两种方式进行模型使用：

一是在火山引擎机器学习平台 veMLP 中部署，目前 veMLP 已经支持全尺寸 DeepSeek 模型， 并仔细对 SGLang 和 vLLM 做过性能调优和效果评测，火山引擎自研 PD 分离+EP 并行的推理引擎也即将推出，全面开放。适用于自己进行模型定制、部署、推理的企业。

二是在火山方舟中调用模型，适用于期望通过 API 快速集成预训练模型的企业，目前已经支持4个模型版本，并提供了全网最高的限流。

![](attachments/bab87f5ef9dececd.png)

**> 在火山引擎机器学习平台，3步部署全尺寸DeepSeek模型**

veMLP 已支持全尺寸 DeepSeek V3/R1。为客户加速试验，可以提供全尺寸 DeepSeek 预置模型权重文件，针对SGLang 和 vLLM 最新版本进行深度调优和算子优化。此外火山引擎自研 PD 分离+EP 并行的推理引擎也即将全面开放，届时将帮助您显著优化延时和成本，敬请期待。

3步助你打造属于自己的 DeepSeek 模型，以 DeepSeek-R1-Distill-Llama-70B 模型部署为例，更多细节请参考：https://www.volcengine.com/docs/6459/1449739。

Step1-模型下载

火山引擎提供 TOS 对象存储预置模型权重文件。在机器学习平台选择好队列计算资源配置、访问配置、共享存储配置后，即可创建开发机。登录到机器学习平台开发机的 WebIDE，打开终端，进行预置模型权重文件下载。

![](attachments/ce80d9d26e82e628.jpg)

Step2-服务配置

创建在线服务，并部署模型实例。在部署模型实例过程中，选择客户专属 VPC 网络环境、API 网关、镜像、配置入口命令、挂载模型权重文件的共享文件系统路径和计算资源即可一键实现模型部署。

![](attachments/9c898f6a4118cf69.jpg)

Step3-服务调用

在线服务详情页-部署页面获取实例的公网调用地址，配置调用参数，然后进入服务实例的 WebShell，发起服务调用测试。

![](attachments/ef3195efcd4138c1.jpg)

**> 通过火山方舟调用，价格限时优惠，支持更高并发**

通过全栈自研推理系统对 DeepSeek 的优化和降本，火山引擎为通过方舟调用 DeepSeek 模型 API 的企业提供有竞争力的价格，并提供全网最高的限流，方便业务快速落地。推理整个生命周期在安全沙箱中完成，确保用户 Prompt 会话数据无痕。此外，火山引擎还特别提供两周限时5折优惠，助力企业畅享满血版 DeepSeek-R1！

近期将陆续上线更多推理优化技术，推理延迟和承载能力会有持续优化和提升，敬请期待。

![](attachments/26a05cdb8393be19.png)

欢迎登录火山方舟、火山引擎机器学习平台体验并咨询 DeepSeek 模型：

![](attachments/b50794eff267f3f5.png)

火山方舟

![](attachments/ff74210bf9a50217.png)

火山引擎机器学习平台

https://www.volcengine.com/product/ark

https://www.volcengine.com/product/ml-platform

![](attachments/ab6d7aed6300739a.jpg)

![](attachments/47cc1645b1fff509.gif)

阅读原文
