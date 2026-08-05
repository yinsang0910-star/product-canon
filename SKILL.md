---
name: product-canon
description: "Initialize or explicitly re-found a project's durable product canon as exactly five fixed documents under docs/product: PRODUCT.md, ARCHITECTURE.md, ACCEPTANCE.md, ROADMAP.md, and CURRENT_STATE.md. Use only when the user asks to initialize a project and set its product direction, a completed grilling interview hands off confirmed product decisions, or the user explicitly asks to consolidate/rebuild the project's core vision, requirements, and user intent. Do not trigger for ordinary document reading, review, audit, cleanup, routine correction or status refresh, ROADMAP maintenance, Spec work, implementation, or acceptance checking."
---

# Product Canon

在项目定调初始化或用户明确要求重建核心意志时，把已确认的产品决定和当时可验证的起点事实归入固定五文件结构。它是低频的建制工具，不是日常文档维护器。

不要把当前项目已有的文件数量、文件名或历史结构复制成通用模板。

## 固定输出契约

执行初始化或显式归并重建时，只在 `docs/product/` 建立以下五个核心文件，文件名和职责不得变化：

| 文件 | 唯一职责 |
| --- | --- |
| `PRODUCT.md` | 产品承诺、用户、用户结果、可见行为、配置方式和永久边界 |
| `ARCHITECTURE.md` | 系统上下文、组件责任、单一状态/数据权威、关键路径和故障不变量 |
| `ACCEPTANCE.md` | “完成”的判定、声明所需证据、失败/恢复证据和不证明事项 |
| `ROADMAP.md` | 完整产品路线，以及用户批准的纵向交付结果、依赖、顺序、状态和 Spec 交接 |
| `CURRENT_STATE.md` | 源码与运行环境当前已验证、未验证、阻塞和证据指针 |

使用 `assets/core-docs/` 中的同名模板。模板只固定文件名、职责和最小骨架；不要把某个项目的业务章节变成所有项目都必须填写的通用章节。信息不足时保留 `UNKNOWN` 或 `NOT_VERIFIED`，不要猜测，也不要新增第六个核心文件。

“固定五文件”只限制**核心权威入口**，不限制仓库的文档总数。以下材料可以继续独立存在，并且不计入五个核心文件：

- 开发协作与实施材料，例如 `AGENTS.md`、Spec、plan 和 tasks；
- 合规、许可、第三方来源与 provenance（来源归属）记录；
- vendor（供应商）原文、API 参考、ADR、设计稿和研究资料；
- 测试、运行证据、发布回执、迁移说明和历史归档。

不要仅因为一个文件不属于五个核心文件就删除、合并或改名。它可以提供输入、证据或历史，但不能与五个核心文件争夺产品权威。

## 权威边界

- 采用用户本轮明确决定；它优先于旧聊天、旧报告、技能建议、测试和局部实现。
- 用 `PRODUCT.md`、`ARCHITECTURE.md` 和 `ACCEPTANCE.md` 记录稳定目标与规则；不要让当前代码反向缩小目标。
- 用 `CURRENT_STATE.md` 记录源码和运行证据；没有直接证据时写 `NOT_VERIFIED`。
- 用 `ROADMAP.md` 的产品路线保留已确认的阶段和顺序，用其中唯一的 Spec 交接表交付已批准的下一项；不要在 `CURRENT_STATE.md` 建立第二份下一步清单。
- 把同一声明放在一个文件；其它文件只链接，不复制正文。
- Git 中的 `M`、`U`、`??` 或“工作树有改动”只表示文件尚未进入当前提交，不表示内容正确、错误、过时或已获用户确认。
- diff（差异）的增加、删除和行数只描述文本变化。不要把删行、文件更短或时间更新推断为用户废止了某项决定；只有用户明确决定才能取代旧产品约束。

## 触发闸门

只允许以下入口：

1. **项目定调初始化**：用户明确要初始化项目、确定产品方向并输出核心文档。
2. **Grilling 交接**：连续追问已经结束，用户确认形成共同理解，且访谈主题是项目或产品的持久愿景与需求。
3. **显式归并重建**：用户明确要求把当前项目分散的核心、愿景、需求或用户核心意志重新归纳为权威文档。

除此之外不要启用本 Skill。普通阅读、检查、审计、评审、整理、纠错、同步状态、维护 ROADMAP、核对 Spec、验收声明或实现工作，都由普通任务或对应专业流程处理。即使某份核心文档可能过时，也不能因此隐式触发。

本 Skill 只有两种执行形态：首次**建立**，或在用户明确要求下进行一次完整的**归并重建**。它不提供日常“修正模式”或独立“审计模式”。归并重建内部仍要做迁移覆盖检查，但该检查不能作为单独使用场景。

## 执行流程

### 1. 读取最小上下文

依次读取：

1. 项目的 `AGENTS.md` 或同等协作规则。
2. 用户本轮明确决定。
3. 项目声明为权威的产品、架构、路线图、验收和当前状态文档。
4. 仅在核对当前事实时读取最小范围源码、差异和运行证据。

不要为了完整而扫描无关源码、历史聊天、旧报告或全部 Spec。

### 2. 建立声明映射

先把每条内容映射到唯一目标：

| 内容 | 目标文件 |
| --- | --- |
| 产品是什么、为谁服务、用户获得什么、永久不做什么 | `PRODUCT.md` |
| 系统由谁负责什么、唯一权威路径、数据与故障边界 | `ARCHITECTURE.md` |
| 什么证据才能声称完成、哪些证据不能证明完成 | `ACCEPTANCE.md` |
| 完整产品路线、哪些用户结果获准交付、先后依赖和 Spec 状态 | `ROADMAP.md` |
| 当前源码/运行环境实际做到什么、还缺什么 | `CURRENT_STATE.md` |

无法唯一归类时，先判断它是否真是核心产品权威。不是则留在原有非核心文档，不新增核心文件。

### 3. 建立或归并重建

建立模式下，按模板一次创建五个文件；未知内容使用明确占位，不自行补全产品决定。

归并重建前先建立临时映射；把它放在本次执行记录或最终报告中，不创建第六个核心文件：

| 处理 | 含义 |
| --- | --- |
| `MERGE_CORE` | 内容属于五个核心职责之一，迁入对应文件 |
| `KEEP_NON_CANON` | 文件有独立的开发、合规、参考、证据或历史价值，原样保留 |
| `ARCHIVE_CANDIDATE` | 可能只剩历史价值；只报告，得到删除/移动授权后再处理 |
| `UNRESOLVED` | 无法判断是否仍有效；停止处理该部分并请求一个明确决定 |

归并重建时：

1. 为每个现有核心候选文档或相关章节记录处理方式、目标和依据。
2. 现有路线图中的阶段、顺序、依赖和未决事项默认 `MERGE_CORE` 到 `ROADMAP.md` 的产品路线；“不要自动生成 Spec”不能作为省略它们的理由。
3. 只合并 `MERGE_CORE`；保持 `KEEP_NON_CANON` 不变。旧 Spec 默认属于 `KEEP_NON_CANON`，不能仅因目录存在就绑定到新 ROADMAP ID。
4. 只有用户明确取代旧决定，或新位置已保留完全相同含义时，才删除重复声明。
5. 迁移映射仍有 `UNRESOLVED` 或任何旧核心决定尚无去向时，旧权威继续生效，固定五文件保持草案状态；不得改写权威链接或宣称迁移完成。
6. 映射归零后才更新本次范围内的权威链接；未经授权，不删除、重命名、移动或覆盖旧文件。

允许压缩重复措辞，但先确保每项明确产品决定、架构不变量、验收规则和当前事实都有目标或明确处理方式。文件变短、diff 删行或文本较新都不是“已经被取代”的证据。

## ROADMAP 与 Spec 工作流契约

`ROADMAP.md` 必须同时具有两个层次：

1. **产品路线**：保留已经确认的产品阶段、能力范围、先后顺序和未决事项。它描述完整的产品旅程，但本身不产生 Spec。
2. **Spec 交接表**：只放用户明确批准、可以独立演示和验收的近期交付结果。只有这一张表参与切片。

两个层次不能互相代替。可以压缩重复文字，但不得把已有产品路线缩成当前一条 Spec；也不得把完整产品愿景自动展开成一长串推测性的 Spec 条目。

只有 Spec 交接表参与切片。保持恰好一个交接表，列固定为：

```text
ID | User outcome | Boundary | Dependencies | Acceptance | Status | Spec
```

遵守以下规则：

- 只记录纵向、可独立演示和验收的用户结果；不按前端、后端、API、数据库或团队拆条目。
- 只有用户明确批准了准确的 `User outcome`、`Boundary` 和 `Acceptance`，条目才能进入 `APPROVED`；交接表为空是合法状态。
- “不要根据产品终局自动生成完整实施清单”只约束 Spec 交接表，不允许借此删除、压缩或漏掉产品路线。
- 默认一个 `APPROVED` 条目对应一个 Spec；拆分或合并必须先修改 ROADMAP 并获得用户批准，Spec 工作流不得自行扩张数量。
- 产品阶段、能力分组和普通标题不产生 Spec。下一条只是交接表中依赖均为 `ACCEPTED` 的首个 `APPROVED` 条目。
- Spec 工作流只能填写 `Spec` 并推进 `Status`；不得改写 `User outcome`、`Boundary` 或 `Acceptance`。
- ROADMAP ID 是产品交付 ID，必须在绑定 Spec 前由产品讨论确定；`011-*` 一类目录序号只是 Spec 标识，不得反向生成或替代 ROADMAP ID。
- 迁移期间，不得仅凭旧 Spec 已存在就新建交接条目，或把条目推进到 `SPECIFIED`、`IMPLEMENTING`、`BLOCKED`、`ACCEPTED`；必须先取得上述产品结果的明确批准和绑定批准。
- `CURRENT_STATE.md` 可以引用正在处理的 ROADMAP ID，但不能另外选择或排序下一条。

允许的状态只有：`PROPOSED`、`APPROVED`、`SPECIFIED`、`IMPLEMENTING`、`BLOCKED`、`ACCEPTED`。

本 Skill 只在建立或显式归并重建时生成 ROADMAP 结构并记录当次已确认决定；它不负责日常维护 ROADMAP，不创建或修改 Spec、plan、tasks，不执行切片，也不充当调度器。Speckit 等规格流程消费一个合格的 `APPROVED` 条目。

## 验证

写入后执行 `python <skill>/scripts/validate_core_docs.py <project>/docs/product`；归并重建时增加 `--migration`。然后完成一次最小语义检查：

1. `docs/product/` 中五个固定核心文件全部存在，名称和大小写正确。
2. 非核心开发、合规、参考、证据和历史文档没有因“五文件”规则被擅自删除或吞并。
3. 每个迁移输入和每项旧核心决定都有处理方式；`UNRESOLVED` 没有被静默丢弃、写成已取代或在切换权威后继续悬空。
4. 已有产品路线完整进入 `Product route`；交接表的列名、状态值和 ID 唯一性符合契约，且没有未获批准的旧 Spec 绑定。
5. `CURRENT_STATE.md` 的完成声明有直接证据或 `NOT_VERIFIED`，且本次没有越界修改 Spec、源码、数据库或运行系统。

## 停止条件

遇到以下情况时停止扩大修改并指出一个具体缺口：

- 两个当前用户决定互相冲突，且会改变产品方向或永久边界。
- 缺少会改变核心用户结果、安全边界、真实账户、实盘、数据迁移或主流程的决定。
- 无法判断被删除、缩短或改写的内容是否由用户明确取代。
- 请求已进入 Spec 拆分、实施、排期或运行验收执行。
- 迁移需要删除、重命名或覆盖受保护文件，但用户尚未授权该动作。

## 最终输出

最多输出五项：

1. 使用的入口：项目定调初始化、Grilling 交接或显式归并重建。
2. 固定五个核心文件及非核心文档的保留状态。
3. 实际修改或迁移位置。
4. 未解决的用户决定；没有则写“无”。
5. 当前仍未由源码或运行证据证明的事项。
