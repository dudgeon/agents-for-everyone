# Unified AI Assistant Timeline

_Canonical chronological timeline: November 2022 → February 2026_
_Sources: OpenAI blog, Anthropic blog, web research, Every.to Vibe Check series, Ethan Mollick / Simon Willison commentary_

This is the raw, unified, chronological timeline. Epoch clustering will happen separately after user review.

Legend:
- **[OAI]** = OpenAI / ChatGPT ecosystem
- **[ANT]** = Anthropic / Claude ecosystem
- **[ECO]** = Broader ecosystem (Cursor, Devin, AutoGPT, etc.)
- **[META]** = Commentary, cultural moments, frameworks from trusted voices
- **[HARNESS]** = Primarily a tooling/harness improvement
- **[MODEL]** = Primarily a foundation model improvement
- **[BOTH]** = Model + harness change together

Confidence notes:
- Through May 2025: high confidence (training data + web research cross-referenced)
- May 2025 - Feb 2026: good confidence (web research, may be off by days)
- Exact day-of-month uncertain on some items, marked with ~

---

## 2022

### Nov 30 — ChatGPT launches [OAI] [MODEL]
- Free "research preview" built on GPT-3.5 (fine-tuned GPT-3.5 series)
- Multi-turn text conversation, code generation, creative writing, Q&A
- **Worked well**: Brainstorming, drafting emails, simple code snippets, explaining concepts, creative writing prompts
- **Failed at**: Math beyond basic arithmetic, factual accuracy (hallucinated freely and confidently), any task requiring current information (training cutoff Sep 2021), counting characters/tokens, citing sources, logical consistency across long conversations
- **Harness**: Web-only chat interface. No file upload, no tools, no external data, no persistent memory. System prompts existed but weren't user-configurable.
- **Cultural moment**: Fastest consumer app to 100M users. "Have you tried ChatGPT?" becomes ubiquitous.

---

## 2023

### Feb 1 — ChatGPT Plus launches ($20/mo) [OAI] [HARNESS]
- Faster responses, priority access during peak times. Still GPT-3.5.

### Mar 1 — ChatGPT API (gpt-3.5-turbo) [OAI] [HARNESS]
- Chat Completions endpoint. $0.002/1K tokens. Enabled third-party apps to build on ChatGPT-class models for the first time.

### Mar 14 — GPT-4 launches [OAI] [MODEL]
- Available to Plus subscribers and via API (waitlist)
- Dramatic reasoning improvement: ~90th percentile on bar exam (vs ~10th for 3.5)
- 8K and 32K context variants
- **Worked well**: Complex reasoning, nuanced writing, sophisticated code, multi-step problem solving
- **Failed at**: Still hallucinated (though less frequently). Slow (30-60+ sec for long responses). Expensive ($0.03/$0.06 per 1K tokens). Image input announced but not shipped. Knowledge still frozen at Sep 2021.

### Mar 14 — Claude 1.0 launches [ANT] [MODEL]
- Anthropic's first public model. API + limited chat access. 9K context (100K variant soon after).
- Constitutional AI approach (RLHF + RLAIF). Known for being more careful/less harmful.
- **Weaker than GPT-4** at math and coding. Strong at conversation, summarization, writing.

### Mar 23 — ChatGPT Plugins (Alpha) [OAI] [HARNESS]
- Plugin system: Wolfram Alpha, Kayak, Zapier, web browsing (Bing)
- **Iconic failure**: Plugins were notoriously unreliable — model chose wrong plugin, sent malformed requests, ignored results. Browsing was slow and frequently failed.
- Alpha-only, small group access.

### Mar 28-30 — AutoGPT + BabyAGI launch [ECO] [HARNESS]
- Open-source projects promising autonomous multi-step agents using GPT-4
- AutoGPT (GitHub, Mar 30) and BabyAGI (Yohei Nakajima, Mar 28)
- **Massive hype**: Fortune covers it, Andrej Karpathy calls it "next frontier of prompt engineering"
- **Spectacular failure**: Agents assumed powers they didn't have, made up information, got stuck in loops, contradicted instructions. GPT-3.5 was dramatically worse than GPT-4 as the "brain." Tom's Hardware: "They suck right now."
- **Significance**: Foreshadowed the agentic era but proved the models and harnesses weren't ready.

### May — Claude 1.3 (100K context) [ANT] [MODEL]
- 100K token context window — largest commercially available at the time
- Could process entire books or codebases in one prompt
- Major differentiator vs GPT-4's 8K/32K

### ~May — Cursor launches [ECO] [HARNESS]
- AI-first IDE by Anysphere. Embeds AI deeply into the coding workflow.
- 100,000+ developers adopt within first months.

### May — Browse with Bing rolls out (ChatGPT Plus) [OAI] [HARNESS]
- **Disabled in July** because it could bypass paywalls. Re-enabled Sep 27 in restricted form.

### Jun 13 — Function calling in OpenAI API [OAI] [HARNESS]
- `functions` parameter in Chat Completions API. Model returns structured JSON describing function calls.
- **Landmark moment for tool use.** Foundational building block for agent architectures. Replaced fragile prompt engineering for structured output.

### Jul 6 — Code Interpreter (ChatGPT Plus) [OAI] [HARNESS]
- Sandboxed Python execution within ChatGPT. File upload, data analysis, charts, downloadable files.
- **Worked well**: Data analysis, math, CSV/Excel processing, chart generation
- **Failed at**: Sessions were ephemeral (files disappeared). Sandboxed (no internet). Sometimes wrote buggy code and couldn't self-correct. Later renamed "Advanced Data Analysis."

### Jul 11 — Claude 2.0 + claude.ai launches [ANT] [BOTH]
- Major model upgrade. Public web interface. 100K context.
- Improved coding, math, reasoning. Bar exam: 76.5%.
- **Still no vision, no tool use.**

### Jul — Custom Instructions (ChatGPT) [OAI] [HARNESS]
- Persistent "About me" and "How should ChatGPT respond" settings across conversations.
- First step toward persistent personalization.

### Sep — ChatGPT voice + image input (Plus) [OAI] [BOTH]
- Voice conversations (speech-to-text → GPT-4 → text-to-speech) and image input (GPT-4V)
- First widely available multimodal AI assistant
- **Limitation**: Voice was NOT real-time — noticeable latency. Image understanding struggled with small text, spatial reasoning, refused to identify people.

### Sep — Claude Pro subscription ($20/mo) [ANT] [HARNESS]

### Sep 2023 — **[META] Mollick et al: "Navigating the Jagged Technological Frontier"**
- BCG study with 758 consultants using GPT-4
- Key finding: 40% higher quality results WITH AI on tasks inside the frontier. But 19 percentage points WORSE on tasks outside the frontier.
- Introduces the **"jagged frontier"** concept: AI capabilities are unpredictably uneven. Some hard-seeming tasks are easy for AI; some easy-seeming tasks are impossible.
- Introduces **"centaurs" vs "cyborgs"** — two patterns of human-AI collaboration.
- **Critical for our story**: This is the intellectual framework for the Skeptic's position. The frontier IS jagged. Trust IS dangerous when you don't know where the edges are.

### Oct — DALL-E 3 in ChatGPT [OAI] [HARNESS]
- Image generation through conversation. GPT-4 refines prompts before sending to DALL-E.
- **Better prompt understanding** but still refused real people, text rendering imperfect, content policy restrictions heavy.

### Nov 6 — OpenAI DevDay [OAI] [BOTH]
- **Arguably the single biggest capability expansion day in OpenAI's history:**
  - GPT-4 Turbo: 128K context, Apr 2023 knowledge cutoff, 3x cheaper
  - GPTs: No-code custom ChatGPT personas with knowledge files and actions
  - Assistants API: Agent-like API with persistent threads, file management, Code Interpreter, RAG
  - JSON mode, parallel function calling, Vision API, TTS API
- **Worked well**: 128K context was transformative. Cheaper pricing made GPT-4 practical.
- **Failed at**: GPT-4 Turbo was immediately "lazier" — shorter responses, cut corners, refused long code blocks. Assistants API was slow and expensive. GPTs could be trivially prompt-extracted.

### Nov — Cognition Labs founded [ECO]
- Scott Wu, Steven Hao, Walden Yan. Will later build Devin.

### Nov 21 — Claude 2.1 [ANT] [BOTH]
- 200K context (largest commercially available). Halved hallucination rates vs Claude 2.0.
- **Experimental tool use** (function calling) in API — beta.
- Better at admitting uncertainty ("I don't know").

### Dec — "Lazy GPT-4 Turbo" complaints peak [OAI]
- GPT-4 Turbo `1106-preview` widely reported as cutting corners, truncating code blocks, responding "...rest of the code is similar..."
- OpenAI acknowledges, promises fix.
- **Great Skeptic moment**: Model got "smarter" but also got "lazier." Intelligence ≠ reliability.

---

## 2024

### Jan 10 — GPT Store launches [OAI] [HARNESS]
- Discover and share custom GPTs. Revenue sharing announced.
- **Failed at**: Poor discovery, wildly varying quality, trivial wrappers. Revenue payouts tiny.

### Jan 25 — GPT-4 Turbo laziness fix [OAI] [MODEL]
- `gpt-4-0125-preview` addresses truncation/laziness issues.

### Feb 15 — Sora announced [OAI] [MODEL]
- Text-to-video, stunning demos. No public access for months.

### ~Feb — ChatGPT Memory feature (limited rollout) [OAI] [HARNESS]
- Remembers facts across conversations. Very slow rollout. Sometimes remembered wrong things.

### Mar 4 — Claude 3 family launches (Haiku / Sonnet / Opus) [ANT] [BOTH]
- Three-tier model family. Major generational leap.
  - Haiku: fast, cheap. Sonnet: balanced. Opus: flagship (topped MMLU, GPQA benchmarks).
- **New capabilities**: Vision (first for Claude), formal system prompts, improved tool use
- 200K context, near-perfect needle-in-haystack recall
- **Opus was widely regarded as the best available LLM** at launch for complex reasoning and writing
- Expensive: Opus at $15/$75 per million tokens

### Mar 12 — Devin AI announced [ECO] [HARNESS]
- Cognition Labs announces "first fully autonomous AI software engineer"
- Impressive demos. Generates massive hype. Skeptics question reproducibility.
- Public launch much later (Dec 2024).

### Apr — Claude tool use goes GA [ANT] [HARNESS]
- Function calling officially out of beta in Messages API.
- Enables building agentic applications through the Claude API.

### Apr 2 — **[META] Mollick publishes "Co-Intelligence: Living and Working with AI"**
- Book-length treatment of human-AI collaboration. Bestseller.
- Key themes: "Always invite AI to the table." The jagged frontier. Working with AI rather than having AI work for you.

### Apr 9 — GPT-4 Turbo with Vision GA [OAI] [MODEL]
- First unified text+vision GPT-4 Turbo model (not separate `-vision-preview`).

### May 13 — GPT-4o launches [OAI] [BOTH]
- "Omni" model: natively multimodal (text, image, audio). 2x faster, 50% cheaper than GPT-4 Turbo.
- **Available to ChatGPT FREE tier** — huge democratization moment. Every free user gets GPT-4 class intelligence.
- Live voice demo (real-time, emotional) was the highlight — **but did not ship yet**. Took months.
- **Limitation**: Some users reported GPT-4o was worse than GPT-4 Turbo for complex reasoning.

### ~May — ChatGPT Plugins officially sunset [OAI] [HARNESS]
- Plugins never achieved product-market fit. Replaced by GPTs with Actions.
- **Significant for our story**: A major bet on tool use that failed. The harness wasn't right yet.

### Jun 20 — Claude 3.5 Sonnet [ANT] [MODEL]
- **Surpassed Claude 3 Opus** on most benchmarks while being faster and cheaper.
- Topped MMLU, HumanEval, graduate-level reasoning benchmarks.
- Became known as one of the best coding models available.
- **Pivotal**: Many users switched from Opus to Sonnet because it was both better AND cheaper.

### Jun — Artifacts launch (claude.ai) [ANT] [HARNESS]
- Rich interactive content in a side panel: code previews, HTML/CSS/JS, SVGs, React components.
- Transformed Claude from chat-only to collaborative workspace.

### Jul 18 — GPT-4o mini [OAI] [MODEL]
- Small, cheap, fast. $0.15/$0.60 per 1M tokens. 128K context.
- Effectively killed GPT-3.5 Turbo. New default for free tier.

### Aug — Structured Outputs (OpenAI API) [OAI] [HARNESS]
- JSON Schema enforcement via constrained decoding. Guaranteed schema compliance.

### Aug — Prompt Caching (Claude API) [ANT] [HARNESS]
- Up to 90% cost reduction for repeated long contexts. Essential for agentic/RAG workloads.

### Aug-Sep — Claude Projects launch (claude.ai) [ANT] [HARNESS]
- Persistent project spaces with uploaded documents and custom instructions across conversations.
- Knowledge-base-style workflows.

### Sep 12 — o1-preview and o1-mini launch [OAI] [MODEL]
- First "reasoning" models. Chain-of-thought at inference time ("test-time compute scaling").
- o1-preview: 83% on AIME (vs GPT-4o's ~13%). PhD-level science.
- **Revolutionary concept, crippled harness**: No streaming, no image input, no system messages, no function calling, no tools, no browsing, no code interpreter. 30-120 second responses. 30 messages/week limit. Overthought simple questions.
- **Great Skeptic moment**: Smartest model ever, but couldn't use any tools and was painful to actually use.

### Oct 22 — Updated Claude 3.5 Sonnet + Claude 3.5 Haiku [ANT] [MODEL]
- Further improved coding, instruction following, tool use.
- Updated Sonnet becomes the workhorse model.

### Oct 29 — Computer Use (Claude, public beta) [ANT] [BOTH]
- Claude can control a computer: view screenshots, move mouse, click, type, navigate apps.
- **Landmark for AI agents**: Can interact with any GUI application.
- **Beta quality**: Slow screenshot-action loops, error-prone on complex multi-step tasks.

### ~Oct — ChatGPT Canvas [OAI] [HARNESS]
- Side panel for collaborative document/code editing. Inline edits, targeted revisions.
- Moves ChatGPT beyond pure chat toward IDE/editor feel.

### ~Oct — ChatGPT Search launches [OAI] [HARNESS]
- Replaces "Browse with Bing." Inline citations, cleaner UX. Positions ChatGPT vs Google.

### Nov 25 — MCP (Model Context Protocol) announced [ANT] [HARNESS]
- **Open protocol for connecting AI models to external tools and data sources.**
- Client-server architecture: MCP servers expose tools/resources, MCP clients connect to them.
- Build an MCP server once → works with any MCP-compatible client.
- **Huge for our story**: This is the beginning of standardized, composable tool ecosystems. The harness becomes modular.

### Dec 5 — o1 full + ChatGPT Pro ($200/mo) [OAI] [BOTH]
- o1 full: now with vision, function calling, developer messages. Major upgrade over preview.
- o1 Pro mode: even more compute, extremely slow (minutes per response).
- **$200 price point controversial.** Many questioned value vs Plus.

### Dec — "12 Days of OpenAI" / Shipmas [OAI] [HARNESS]
- Sora public launch (~Dec 9), Canvas GA, ChatGPT Projects, Advanced Voice with vision, video/screen sharing, Search to free users, o1 in API, WebRTC for Realtime API
- **Massive harness expansion in rapid succession.**

### Dec 9, 2024 — **[META] Every.to Vibe Check: OpenAI's Sora**

### Dec 10 — Devin public launch [ECO] [HARNESS]
- Cognition's autonomous coding agent. Public access after 9 months of limited preview.

---

## 2025

### ~Jan — Extended thinking (Claude) [ANT] [MODEL]
- Visible chain-of-thought reasoning before answering. `thinking` block in API.
- Improved math, logic, complex analysis. Users can see reasoning → improved trust.

### ~Jan — Operator (OpenAI) [OAI] [HARNESS]
- Web-browsing agent for tasks (booking, shopping, forms). Pro subscribers.
- Slow, expensive, required human oversight. Made mistakes on complex tasks.

### Jan 22 — **[META] Every.to: "We Tried OpenAI's New Agent"**

### Jan 30 — o3-mini [OAI] [MODEL]
- Smaller, faster, cheaper reasoning model. Three "effort" levels (low/medium/high).
- Made reasoning models practical for everyday use.

### Feb — Claude Code preview [ANT] [HARNESS]
- **Agentic CLI tool**: Terminal access, file system read/write, execute commands, search codebases, git, run tests, MCP server connections.
- Runs in the user's actual terminal, not a separate IDE.
- **This is a pivotal moment for our story.** The agent leaves the browser and enters the file system.

### Feb 2 — **[META] Every.to: "We Tried OpenAI's New Deep Research"**

### ~Feb — Deep Research (ChatGPT) [OAI] [HARNESS]
- Model spends minutes autonomously browsing, reading, synthesizing research reports.
- Uses o3-class reasoning. First real "agentic" feature in ChatGPT.

### ~Feb 27 — GPT-4.5 research preview [OAI] [MODEL]
- Largest non-reasoning model. Improved "EQ," reduced hallucinations, better creative writing.
- Extremely expensive. Research preview positioning.

### Mar 8 — Claude 3.7 Sonnet + Claude Code updates [ANT] [BOTH]
- Claude 3.7 Sonnet with extended thinking.

### Mar 8 — **[META] Every.to Vibe Check: Claude 3.7 Sonnet and Claude Code**

### ~Mar — Citations (Claude API) [ANT] [HARNESS]
- Character-level source attribution from provided documents. Critical for RAG.

### ~Mar — Batches API (Claude) [ANT] [HARNESS]
- Async processing at 50% discount. For evaluation runs and high-volume workloads.

### Mar 26 — **[META] Every.to Vibe Check: GPT-4o Image Generation**
- GPT-4o image generation goes viral (Ghibli-style images). Major cultural moment.

### Apr 16 — o3 and o4-mini [OAI] [BOTH]
- Reasoning + native tool use: code execution, web search, file analysis, image generation IN the reasoning chain.
- o4-mini: best benchmarked model on AIME 2024 and 2025.
- **Convergence of reasoning and tools.** The harness and the model start merging.

### Apr 16 — **[META] Every.to Vibe Check: o3 Is Here—And It's Great**
### Apr 18 — **[META] Every.to Vibe Check: o3, GPT-4.1, and o4-mini**

### May 16 — **[META] Every.to Vibe Check: Codex—OpenAI's New Coding Agent**
- OpenAI ships Codex as a coding agent product.

### May 22 — Claude 4 (Sonnet 4, Opus 4) + Claude Code GA [ANT] [BOTH]
- Major model generation leap. Claude Code moves from preview to GA.
- **CLAUDE.md framework**: Project-level and user-level instruction files. Claude Code reads them automatically.
- **This is the moment persistent alignment becomes a product feature.**

### May 22 — **[META] Every.to Vibe Check: Claude 4 Opus**

### ~May — Claude Agent SDK [ANT] [HARNESS]
- Programmatic control over Claude agents. Build custom agentic applications.

### Jun 23 — **[META] Every.to: o3-pro Vibe Check—A Slow, Steady Last Resort**

### ~Jul — Cognition acquires Windsurf [ECO]

### Jul 17 — **[META] Every.to Vibe Check: ChatGPT Agent enters browser wars**

### Jul 31 — **[META] Every.to Vibe Check: Claude's New Agents Are Confusing as Hell—And We Love Them**

### Aug 5 — Claude Opus 4.1 [ANT] [MODEL]
- Most powerful Claude model to date at time of release.

### ~Aug — GPT-5 launches [OAI] [BOTH]
- New default in ChatGPT. Replaces GPT-4o, o3, o4-mini, GPT-4.1, and GPT-4.5.
- 94.6% on AIME 2025 (without tools). 74.9% on SWE-bench Verified.
- Thinking mode: 6x fewer hallucinations than o3. 50-80% fewer output tokens.
- Rolls out to Plus, Pro, Team, Free; Enterprise/Edu the following week.

### Aug 5 — **[META] Every.to Vibe Check: OpenAI drops two new open-weight models**
### Aug 8 — **[META] Every.to Vibe Check: Genie 3, Claude 4.1, GPT-oss, and GPT-5**
### Aug 12 — **[META] Every.to Vibe Check: Claude Sonnet 4 Now Has a 1-million Token Context Window**

### Sep 29 — Claude Sonnet 4.5 [ANT] [MODEL]

### Sep 29 — **[META] Every.to Vibe Check: Claude Sonnet 4.5**

### Oct 2 — Agent Skills beta [ANT] [HARNESS]
- **Skills**: Organized folders of instructions, scripts, and resources that Claude loads dynamically.
- Initial release: Anthropic-managed Skills for PowerPoint, Excel, Word, PDF.
- Custom Skills via Skills API.
- **Recursive self-improvement begins**: Skills can be refined through use. This is the "nurturing" thesis.

### Oct 6 — **[META] Every.to Vibe Check: OpenAI DevDay 2025**

### Oct 20 — Claude Code on the web [ANT] [HARNESS]
- Claude Code's agentic capabilities available in the browser, not just CLI.

### Oct 20 — **[META] Every.to Vibe Check: Claude Code Now Works on Mobile and the Web**

### Oct 29 — Cursor 2.0 + Composer [ECO] [HARNESS]
- Cursor ships agentic coding model. Cursor ARR reaches $500M.

### Oct 29 — **[META] Every.to Vibe Check: Cursor 2.0 and Composer 1 Alpha**
### Oct 30 — **[META] Every.to Vibe Check: Factory's Coding Agent Droid**

### ~Oct — Claude Haiku 4.5 [ANT] [MODEL]
- Fastest, most intelligent Haiku. Near-frontier performance at lowest cost.

### Nov 3 — **[META] Every.to Vibe Check: Claude Skills Need a 'Share' Button**
- Skills are powerful but sharing/distribution needs work.

### Nov 19 — **[META] Every.to Vibe Check: Gemini 3 Pro**

### Nov 24 — Claude Opus 4.5 [ANT] [BOTH]
- Best model in the world for coding, agents, and computer use (per Anthropic).
- Also better at everyday tasks: deep research, slides, spreadsheets.

### Nov 24 — **[META] Every.to Vibe Check: Opus 4.5 Is the Coding Model We've Been Waiting For**

### ~Dec — Claude Code: background agents, named sessions, .claude/rules/, model switching [ANT] [HARNESS]

### 2025 — **[META] Mollick: "Management as AI Superpower"**
- "Thriving in a world of agentic AI." As AIs become capable of hours-long human tasks, the value of delegation skills increases.
- Taught experimental class: students create a startup from scratch in 4 days using AI agents.

### 2024-2025 — **[META] Simon Willison key contributions**
- Defines agents clearly: **"An LLM agent runs tools in a loop to achieve a goal."**
- Warns about **"the lethal trifecta"** for agent security: access to private data + exposure to untrusted content + ability to externally communicate.
- Built 150+ HTML tools using LLMs. Demonstrates practical LLM coding.
- Honest about difficulty: "If someone tells you coding with LLMs is easy they are probably misleading you."

---

## 2026

### ~Jan — Claude Code: SKILL.md support, session forking, cloud handoff [ANT] [HARNESS]
- SKILL.md: Structured skill definitions alongside CLAUDE.md and AGENTS.md.

### Feb 4 — GPT-5.2 thinking level restored [OAI]

### Feb 5 — Claude Opus 4.6 [ANT] [MODEL]
- Improved coding, more careful planning, longer agentic task sustain, 1M token context (beta).

### ~Feb — Cowork [ANT] [HARNESS]
- Claude Code's agentic capabilities brought to the Claude desktop app for knowledge work beyond coding. Runs locally in an isolated VM.
- **The agent leaves the developer's terminal and enters general knowledge work.**

### Feb — Claude for Excel (beta) [ANT] [HARNESS]
- Pivot tables, charts, file uploads. Available to Max, Team, Enterprise.

---

## Recurring Themes for Epoch Analysis

When clustering into epochs, consider these patterns:

1. **Model jumps vs harness jumps**: Sometimes the model got smarter (GPT-3.5→4, o1). Sometimes the harness got better (plugins, function calling, Code Interpreter, Claude Code). The most transformative moments were often harness changes.

2. **Promise → failure → refinement**: Plugins promised tool use but failed. AutoGPT promised agents but failed. o1 promised reasoning but shipped without tools. Each failure taught the next iteration what was needed.

3. **The file system transition**: Chat bubble → file upload/download → Code Interpreter → Claude Code (full file system access). This is a multi-year arc from the model being isolated to the model being embedded in your work.

4. **The alignment progression**: No customization → system prompts → custom instructions → GPTs → CLAUDE.md → skills → recursive skill improvement. A multi-year arc toward persistent, user-defined alignment.

5. **Democratization waves**: GPT-4 was expensive/restricted → GPT-4o made it free → reasoning models were restricted → o3-mini made them accessible → GPT-5 unified everything.

6. **The trust problem**: Mollick's jagged frontier is the through-line. At every stage, users had to learn where the edges were. The Skeptic is right to be cautious — the edges keep moving.
