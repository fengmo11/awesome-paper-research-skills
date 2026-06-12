# 顶刊章节写作手法指南

这个指南把 Nature/Science/Cell/PNAS 风格论文中常见的章节推进方式，转成可以直接检查草稿的写作规则。计算机、机械、工程类论文可以沿用这里的逻辑，只需要根据 IEEE/ACM 或目标期刊格式调整小节标题。

参考来源包括 Nature 作者格式指南和 PLOS Computational Biology 的论文结构规则。Nature 强调摘要式 summary paragraph、跨学科可读性、Methods 可复现性和图注清晰度；PLOS 的 “Ten simple rules for structuring papers” 强调 C-C-C 结构，也就是 Context -> Content -> Conclusion。

## 总原则

每一层都用同一套逻辑：

```text
背景 / 问题语境 -> 本文内容 / 证据 -> 结论 / 边界
```

放到全文就是：

```text
引言 = 给问题语境
结果 = 给证据链
讨论 = 给解释、边界和意义
```

放到段落就是：

```text
第一句：本段问题、局部背景或要检验的点
中间句：方法、证据、比较、推理
最后一句：本段答案、局部结论或下一段桥梁
```

不要按“我做实验的时间顺序”写论文。顶刊读者关心的是论证顺序：为什么这个问题重要，已有方法缺什么，你的证据如何逐步支撑中心贡献。

## 摘要 / Summary Paragraph

顶刊风格下，摘要默认写成一个连续段落。不要把摘要拆成 Background/Methods/Results/Conclusion 这种小标题，除非目标期刊明确要求结构化摘要。

推荐推进：

```text
领域问题 -> 未解决缺口 -> 本文做什么 -> 关键结果
-> 结果解释 -> 更广意义 -> 边界条件
```

句子安排：

1. 第一句：让跨领域读者知道这个问题属于什么大背景。
2. 第二句：收窄到当前尚未解决的瓶颈。
3. 第三句：说明本文做了什么。
4. 第四句：给出最关键证据或核心定量结果。
5. 第五句：说明结果意味着什么，但只说结果真正支持的范围。
6. 可选末句：交代数据集、任务场景、适用边界或仍未解决的问题。

计算机 / 机械 / 工程类可用模板：

```text
problem context -> limitation of existing methods -> proposed method/system
-> benchmark or experiment result -> practical implication -> boundary
```

常见错误：

- 一上来就写 “This paper proposes...” 而没有先建立问题。
- 摘要里堆满缩写、公式和过多数字。
- 最后一句把意义夸大到结果之外。
- 写成广告语，例如 “revolutionary”, “groundbreaking”, “significantly advances all...”
- 为了显得高级而使用过多破折号、括号、引号和副词。

## 引言

顶刊引言通常是一条连续论证线，不适合拆成很多小节。IEEE/ACM 会议论文可以有 Introduction 章节标题，但 Introduction 内部也不建议再拆很多小标题，除非篇幅很长或期刊格式要求。

推荐推进：

```text
大背景 -> 当前进展 -> 未解决缺口 -> 缺口为什么重要
-> 本文做什么 -> 贡献预览
```

段落安排：

1. 第一段：说明领域问题为什么重要，不要过早进入细节。
2. 第二段：概括已有工作已经解决了什么。
3. 第三段：指出仍然存在的瓶颈，瓶颈要具体，例如鲁棒性、成本、尺度、可复现性、精度、泛化、安全性、工程部署限制。
4. 第四段：说明为什么现在有机会解决这个瓶颈。
5. 最后一段：紧凑说明本文贡献、证据类型和结果预览。

贡献预览可以这样写：

```text
Here, we develop/test/derive/measure X to address Y. We evaluate X using Z and
show that it achieves [scoped outcome] under [condition].
```

常见错误：

- 把引言写成作者顺序的流水账文献综述。
- 用 “few studies have...” 这种空泛表达，但不说具体缺口。
- 读者还不知道问题时就急着说 “we propose”。
- 过度使用 “first”, “novel”, “significant”。
- 对前人工作进行模糊批评，而不是指出清晰维度。

## Related Work

在 Nature 风格文章中，Related Work 常常融入引言；在 CS/工程论文中，单独 Related Work 很常见。是否单列要看目标期刊和会议格式。

推荐推进：

```text
研究方向 -> 代表性方法 -> 限制维度 -> 与本文关系
```

分组方式：

- 方法假设
- 模型家族
- 数据集或任务设置
- 尺度和成本
- 鲁棒性和安全性
- 可复现性
- 工程部署限制

常见错误：

- 按作者 A、B、C 逐个罗列。
- 每段只总结别人做了什么，不回到本文问题。
- 用 related work 替代引言的 gap-building。

## Methods

Methods 的核心目标是让研究可解释、可复现。顶刊可能把技术细节放到 Methods 或 Supplementary Information，但关键选择不能藏起来。

推荐推进：

```text
设计理由 -> 数据/材料/系统 -> 实验流程 -> 参数与实现
-> 评估/统计 -> 可复现细节
```

段落安排：

1. 设计理由：为什么这个方法适合回答本文问题。
2. 数据/材料/系统：用什么、来自哪里、筛选规则是什么。
3. 流程：按可复现顺序写清做了什么。
4. 参数与实现：哪些参数会影响结论。
5. 评估与统计：指标、基线、显著性、置信区间、随机种子、数据划分。
6. 质量控制：排除规则、失败处理、敏感性分析、验证策略。

常见错误：

- 在 Methods 里解释结果。
- 把关键假设塞进括号里。
- 省略 seeds、splits、baseline、preprocessing。
- 只写工具名，不写版本、配置、参数和数据来源。

## Results

Results 应该像一串被逐步回答的问题，而不是实验日记。每一段回答一个局部问题，每个图表支撑一个明确 claim。

推荐推进：

```text
问题 -> 测试/分析 -> 结果 -> 证据 -> 局部答案
```

段落安排：

1. 开头提出本段要检验的问题或 claim。
2. 说明用了什么分析或实验。
3. 给出主要证据。
4. 与 baseline、control、prior work 或预期比较。
5. 结尾给出局部答案，并自然过渡到下一段。

小标题规则：

- 结果小标题最好是陈述性结论或逻辑步骤。
- 不要只写 “Performance evaluation” 或 “Experimental results”。

更好的小标题：

```text
The proposed controller reduces tracking error under variable load
```

较弱的小标题：

```text
Experimental results
```

常见错误：

- 只描述图里有什么，而不解释证据说明了什么。
- 过早讨论宏大意义。
- 隐藏失败结果或负结果。
- 在 Results 里突然引入 Methods 没解释的新方法。

## 图表和图注

很多审稿人会先看摘要和图。图不是装饰，而是证据单元。

推荐推进：

```text
整图主张 -> 每个 panel 的问题 -> 数据来源 -> 统计/指标
-> 视觉编码 -> 图注边界
```

图注安排：

1. 开头说这张图显示什么。
2. 定义数据、组别、单位、样本量和统计方式。
3. 按 panel 顺序解释。
4. 只写图中数据支持的结论。
5. 如果是示意图，明确它是 schematic/conceptual。

常见错误：

- 图注比数据更夸张。
- 不同 panel 的颜色含义变化。
- 只靠颜色表达差异，没有 marker、line style、label 或 pattern。
- 图里有装饰性元素，却没有证据功能。

## Discussion

Discussion 不是第二个 Results。它要解释结果如何填补引言中建立的缺口，同时交代边界。

推荐推进：

```text
主要进展 -> 证据综合 -> 与已有工作的关系
-> 替代解释 -> 局限性 -> 未来方向
```

段落安排：

1. 第一段：总结最重要发现，并明确它如何回答引言中的 gap。
2. 中间段：解释机制、与前人工作比较、讨论替代解释。
3. 局限段：具体说明研究不能证明什么。
4. 末段：给出有边界的意义和下一步方向。

常见错误：

- 讨论中加入新数据。
- 只写 “there are limitations” 但不具体。
- 用 universal claims，比如 “always”, “fully”, “all scenarios”。
- 比 Results 更确定。

## Conclusion

很多顶刊文章不单列 Conclusion，而是在 Discussion 末段收束。如果目标期刊要求 Conclusion，要短而有边界。

推荐推进：

```text
中心贡献 -> 关键证据 -> 有边界的意义 -> 限制或未来方向
```

常见错误：

- 加入新数据或新引用。
- 写成宣传口号。
- 结尾超过结果支持范围。

## 自检清单

1. 摘要是否是一条完整故事，且默认单段。
2. 引言是否按背景、现状、缺口、意义、本文贡献推进。
3. Related Work 是否按问题维度分组，而不是作者流水账。
4. Methods 是否可复现，且不解释结果。
5. Results 是否是一串被回答的问题。
6. 图表是否每张都有单一主张和 panel 证据。
7. Discussion 是否解释、限定并连接到已有工作。
8. Conclusion 是否有边界，没有新增证据。
9. 全文是否去掉 AI 味表达：过多引号、破折号、括号、副词、夸大词和空泛过渡。
