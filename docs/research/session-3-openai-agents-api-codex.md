# Raw Research: OpenAI Agents API Evolution & Codex 2025
## Session 3 — 2026-02-12
## Source: Research agent output (full preservation)

---

## Key Source URLs

### Assistants API
- [OpenAI DevDay Announcement](https://openai.com/index/new-models-and-developer-products-announced-at-devday/)
- [TechCrunch: OpenAI Launches API for Assistants](https://techcrunch.com/2023/11/06/openai-launches-api-that-lets-developers-build-assistants-into-their-apps/)
- [InfoQ: OpenAI DevDay Announcements](https://www.infoq.com/news/2023/11/openai-announcements-1stdevday/)
- [Amit Kothari: Assistants API — The Good, Bad, and Expensive](https://amitkoth.com/openai-assistants-api-review/)
- [OpenAI Developer Community: Challenges with Assistant API](https://community.openai.com/t/challenges-and-concerns-with-openais-assistant-api-a-researchers-perspective/562688)
- [OpenAI Help Center: Assistants API v2 FAQ](https://help.openai.com/en/articles/8550641-assistants-api-v2-faq)
- [Mamezou: File Search in Assistants API v2](https://developer.mamezou-tech.com/en/blogs/2024/04/21/openai-file-search-intro/)
- [Woyera: Assistants API v2 Improvements](https://medium.com/@woyera/openai-assistants-api-v2-whats-new-and-improved-a67c4f3936fc)

### Responses API & Agents SDK
- [OpenAI: New Tools for Building Agents](https://openai.com/index/new-tools-for-building-agents/)
- [OpenAI: New Tools and Features in the Responses API](https://openai.com/index/new-tools-and-features-in-the-responses-api/)
- [OpenAI Migration Guide: Assistants to Responses](https://platform.openai.com/docs/guides/migrate-to-responses)
- [VentureBeat: OpenAI Leader Admits Confusion](https://venturebeat.com/dev/openai-leader-admits-way-too-much-confusion-about-responses-api-posts-thread)
- [OpenAI Developer Community: Assistants API Deprecation](https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666)
- [Ragwalla: Assistants vs Responses Comparison](https://ragwalla.com/blog/openai-assistants-api-vs-openai-responses-api-complete-comparison-guide)
- [OpenAI Developer Community: Migration Is Not 1:1](https://community.openai.com/t/assistants-api-responses-api-this-is-not-a-1-1-migration/1371092)
- [Medium: Comparing OpenAI and Anthropic Agent Approaches](https://mectors.medium.com/agents-comparing-openais-operator-responses-api-agents-sdk-vs-anthropic-s-mcp-bd6bada18ba6)

### ChatGPT Plugins
- [OpenAI: ChatGPT Plugins Announcement](https://openai.com/index/chatgpt-plugins/)
- [Your Everyday AI: ChatGPT Is Killing Off Plugins](https://www.youreverydayai.com/chatgpt-is-killing-off-plugins-what-it-means/)
- [Toolify: The Demise of ChatGPT Plugins](https://www.toolify.ai/ai-news/the-demise-of-chatgpt-plugins-a-costly-mistake-and-your-next-move-2440241)
- [The Register: OpenAI Rolls Out ChatGPT Plugins](https://www.theregister.com/2023/03/26/openai_chatgpt_plugins/)
- [Medium: Why ChatGPT Plugins Failed But MCP Is Winning](https://bhavyansh001.medium.com/why-chatgpt-plugins-failed-but-mcp-is-winning-real-reasons-mcp-deepdive-02-abb9619b8c55)

### OpenAI Codex 2025
- [OpenAI: Introducing Codex (May 2025)](https://openai.com/index/introducing-codex/)
- [OpenAI: Introducing the Codex App (Feb 2026)](https://openai.com/index/introducing-the-codex-app/)
- [OpenAI Codex System Card (PDF)](https://cdn.openai.com/pdf/8df7697b-c1b2-4222-be00-1fd3298f351d/codex_system_card.pdf)
- [OpenAI Developers: Codex CLI](https://developers.openai.com/codex/cli)
- [GitHub: openai/codex](https://github.com/openai/codex)
- [TechCrunch: OpenAI Debuts Codex CLI](https://techcrunch.com/2025/04/16/openai-debuts-codex-cli-an-open-source-coding-tool-for-terminals/)
- [VentureBeat: Codex Desktop App for macOS](https://venturebeat.com/orchestration/openai-launches-a-codex-desktop-app-for-macos-to-run-multiple-ai-coding)
- [Builder.io: Codex vs Claude Code](https://www.builder.io/blog/codex-vs-claude-code)
- [build.ms: Codex vs Claude Code Today](https://build.ms/2025/12/22/codex-vs-claude-code-today/)
- [Graphite: Comparing Claude Code vs Codex](https://graphite.com/guides/claude-code-vs-codex)

### Narrative Arc Sources
- [Your Everyday AI: ChatGPT Killing Off Plugins](https://www.youreverydayai.com/chatgpt-is-killing-off-plugins-what-it-means/)
- [OpenAI: Introducing GPTs](https://openai.com/index/introducing-gpts/)
- [eesel.ai: Guide to Assistants API Deprecation](https://www.eesel.ai/blog/openai-assistants-api)
- [OpenAI: For Developers in 2025](https://developers.openai.com/blog/openai-for-developers-2025/)
- [Syntackle: OpenAI Assistants Deprecated](https://syntackle.com/blog/openai-assistants-to-responses-api/)
- [Medium: From Deprecated to Optimized](https://medium.com/@gjasula/from-deprecated-to-optimized-a-production-migration-from-openai-assistants-api-to-chat-completions-21d784036644)
- [Pento: A Year of MCP Review](https://www.pento.ai/blog/a-year-of-mcp-2025-review)

---

## Key Data Points Not in Final Entry

### Assistants API v1 Problems (detailed)
- State lived on OpenAI's servers — "guessing what the thread contains, what tools fired, why a run failed"
- Re-processed entire conversation thread with every message
- Developers couldn't optimize context management
- No streaming in v1
- Fixed assistant configurations, async run handling, multiple API calls per turn

### Assistants API v2 (Apr 2024)
- File Search: renamed from Retrieval, backed by Vector Store API
- Up to 10,000 files per assistant
- Automated parsing, chunking, embedding
- Multi-threaded searches, query rewriting, advanced reranking
- v1 sunset Dec 18, 2024
- Still didn't fix architectural complaints

### Responses API Key Differences
- Stateless by default (biggest change)
- No polling, no run objects, no thread management
- Optional statefulness via Conversations API or previous_response_id chaining
- Built-in tools: web search, file search, computer use, code interpreter, image generation, MCP support
- o3/o4-mini can call tools within chain-of-thought
- Assistants API deprecated Aug 26, 2025, sunset Aug 26, 2026
- Never left beta in its entire lifespan

### Plugins Details
- Launch partners: Expedia, FiscalNote, Instacart, KAYAK, Klarna, Milo, OpenTable, Shopify, Slack, Speak, Wolfram, Zapier
- ~1,000 plugins at peak
- Mar 19, 2024: no new conversations
- Apr 9, 2024: full shutdown

### Codex Details
- codex-1: specialized o3 fine-tune with RLHF for software engineering
- Cloud sandbox: internet disabled, can only access provided GitHub repos
- Multiple agents work in parallel
- Iteratively runs tests until they pass
- GPT-5.2-Codex: "most advanced agentic coding model"
- GPT-5.3-Codex-Spark: 1000+ tokens/sec, real-time
- Codex Desktop (Feb 2, 2026): native macOS, Apple Silicon, worktree support, Automations, Skills
- Windows expected late 2026
- Install: `npm i -g @openai/codex` or `brew install --cask codex`
- Apache 2.0 license, built in Rust
- $1M grant initiative

### Codex vs Claude Code Comparison Table
| Dimension | Claude Code | OpenAI Codex |
|-----------|------------|--------------|
| Philosophy | Developer-in-the-loop, local-first | Autonomous, cloud-based delegation |
| Metaphor | "Senior developer" | "Scripting-proficient intern" |
| Architecture | Interactive CLI + IDE | Cloud sandboxes + CLI + desktop |
| Strength | Complex single-task reasoning | Parallel task delegation |
| Cost | More expensive per token | More cost-efficient |
| Revenue | $1B ARR in 6 months (Nov 2025) | Included in ChatGPT subscription |

### The 6-Chapter Narrative Arc
1. Plugins (Mar 2023): "The App Store Fantasy" — bolting tools doesn't work
2. GPTs/Store (Nov 2023-Jan 2024): "The Creator Economy Fantasy" — marketplaces need economics
3. Assistants v1+v2 (Nov 2023-Apr 2024): "Let Us Handle Everything" — devs want control
4. Responses API (Mar 2025): "You Own the State" — primitives > platforms
5. MCP Adoption (Mar 2025): "If You Can't Beat Them, Join Them" — open > proprietary
6. Codex (Apr-May 2025+): "The Agent Era" — build agents, not platforms
