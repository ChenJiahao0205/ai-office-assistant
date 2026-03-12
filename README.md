---

# 项目名称

**AI Office Assistant (Local RAG Knowledge Base)**

---

# 项目简介

AI Office Assistant 是一个基于本地大模型构建的 **RAG（Retrieval-Augmented Generation）知识库系统**。
系统允许用户上传文档（如 PDF），自动解析文本、构建向量索引，并通过语义搜索和大语言模型生成智能回答。

该项目完全支持 **本地部署**，无需依赖云端 API，适合构建企业内部知识库、文档问答系统或 AI 办公助手。

核心目标：

* 将企业文档转化为可检索的 AI 知识库
* 使用语义搜索提升信息检索能力
* 结合大模型生成自然语言回答

---

# 核心功能

### 文档上传

用户可以上传 PDF 文件，系统会自动保存并进入知识库处理流程。

---

### 文档解析与切分

系统会解析文档内容，并将长文本切分为多个 **chunk（文本片段）**，以便进行语义检索。

---

### 向量化（Embedding）

每个 chunk 会通过本地 embedding 模型转换为向量表示，用于语义相似度搜索。

---

### 向量数据库索引

文本向量会存储在向量数据库中，实现高效的语义检索。

---

### 语义搜索

用户提问时：

1. 问题会被转换为向量
2. 系统在向量数据库中搜索最相似的文本片段
3. 返回相关上下文

---

### LLM 回答生成

检索到的上下文会提供给本地大模型生成最终回答，实现 **RAG 问答系统**。

---

# 技术架构

系统整体流程：

```
Document Upload
      │
      ▼
Document Parsing
      │
      ▼
Text Chunking
      │
      ▼
Embedding Model
      │
      ▼
Vector Database
      │
      ▼
Semantic Retrieval
      │
      ▼
LLM Answer Generation
```

---

# 使用技术

后端框架：

* FastAPI

本地大模型运行：

* Ollama

RAG框架：

* LlamaIndex

向量数据库：

* Qdrant

Embedding模型：

* nomic-embed-text

开发语言：

* Python 3

---

# 项目特点

### 本地部署

无需外部 API，所有模型和数据均运行在本地。

---

### 可扩展

系统架构支持扩展：

* 多文档知识库
* 企业内部文档问答
* AI 办公助手
* 自动化文档分析

---

### 模块化设计

项目模块包括：

```
upload        文件上传
indexer       文档索引
embedding     向量生成
rag           知识检索
api           接口服务
```

---

# 适用场景

该项目可用于：

* 企业知识库
* AI 文档问答系统
* 内部技术文档检索
* AI 办公助手
* RAG 系统学习与实践

---

# 开发目标

未来计划增加：

* Web UI
* 多文档管理
* 向量检索优化
* Hybrid Search（关键词 + 向量搜索）
* 多模型支持

---

如果你愿意，Wutiao，我可以再帮你写一版 **更高级一点的 GitHub README（更像开源项目）**，里面会包括：

* 项目架构图
* 安装步骤
* 快速启动
* API 示例

那一版基本就是 **可以直接放 GitHub 首页的完整 README**。
