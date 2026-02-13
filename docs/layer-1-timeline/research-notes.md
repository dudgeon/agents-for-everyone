# Timeline Research Notes — Detailed Sources & Vivid Examples

_This file contains the rich, source-linked detail that backs up the overview timeline. Organized by event. Each entry has URLs, specific examples, and story-ready material._

---

## Iconic Failure: Mata v. Avianca — Lawyer submits ChatGPT-hallucinated cases to court (May-Jun 2023)

**What happened**: Lawyer Steven A. Schwartz used ChatGPT to research case law for a personal injury lawsuit (Mata v. Avianca, Inc.). ChatGPT fabricated six legal cases with realistic-sounding names: "Martinez v. Delta Air Lines," "Zicherman v. Korean Air Lines," "Varghese v. China Southern Airlines" — complete with fabricated citations, quotations, and internal reasoning. Schwartz submitted these in a legal brief signed by his colleague Peter LoDuca.

**How it was discovered**: Avianca's attorneys told the court they were "unable to locate" the cited authorities. The judge ordered Schwartz to show cause.

**Schwartz's defense**: He testified he was "operating under the false perception that [ChatGPT] could not possibly be fabricating cases on its own."

**Outcome**: Both lawyers were sanctioned with $5,000 fines. The case became the leading precedent on AI misuse in legal filings: Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023).

**Story value**: Perfect Skeptic moment. Demonstrates confident hallucination, the trust problem, and real-world consequences. The lawyer's quote — "I didn't think it could be fabricating cases on its own" — captures exactly the kind of naive trust the story warns about.

**Sources**:
- [CNN: Lawyer apologizes for fake court citations from ChatGPT](https://www.cnn.com/2023/05/27/business/chat-gpt-avianca-mata-lawyers)
- [Wikipedia: Mata v. Avianca, Inc.](https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.)
- [Seyfarth Shaw: Counsel who submitted fake cases are sanctioned](https://www.seyfarth.com/news-insights/update-on-the-chatgpt-case-counsel-who-submitted-fake-cases-are-sanctioned.html)
- [ACC: Practical Lessons from Mata v. Avianca](https://www.acc.com/resource-library/practical-lessons-attorney-ai-missteps-mata-v-avianca)

---

## Iconic Failure: "Lazy GPT-4 Turbo" — The model gets smarter but stops trying (Nov-Dec 2023)

**What happened**: After OpenAI shipped GPT-4 Turbo (Nov 6, 2023 DevDay), users widely reported the model was cutting corners: truncating code blocks, responding with "...rest of the code is similar...", giving shorter answers, and declining complex tasks. A developer named Rob Lynch found GPT-4 Turbo produced shorter responses for December dates vs. May dates via the API, spawning the "winter break hypothesis."

**OpenAI's response**: Will Depue from OpenAI confirmed awareness (Dec 1). Said GPT-4 Turbo hadn't been updated since Nov 11 and the issue was "unintentional." Fix came with `gpt-4-0125-preview` on Jan 25, 2024.

**Story value**: Intelligence ≠ reliability. The model got a bigger context window, got cheaper, got parallel function calling — and also got lazier. Perfect illustration of unpredictable regressions. The Skeptic would say: "Great, so it's smarter AND less willing to do its job?"

**Sources**:
- [OpenAI Community: ChatGPT-4 defaults to lazy](https://community.openai.com/t/chatgpt-4-defaults-to-lazy/560886)
- [Analytics Vidhya: OpenAI Acknowledges GPT-4 Being Lazy](https://www.analyticsvidhya.com/blog/2023/12/user-complained-gpt-4-being-lazy-openai-acknowledges/)
- [Hacker News: GPT-4-turbo shorter completions in December vs May](https://news.ycombinator.com/item?id=38604597)
- [The Decoder: OpenAI looks into complaints about lazy ChatGPT](https://the-decoder.com/openai-looks-into-complaints-about-lazy-chatgpt-with-gpt-4/)

---

## Iconic Failure: AutoGPT / BabyAGI — Agents that couldn't (Mar-Apr 2023)

**What happened**: AutoGPT (GitHub, Mar 30) and BabyAGI (Yohei Nakajima, Mar 28) promised autonomous multi-step agents using GPT-4. Massive viral hype. Fortune called BabyAGI "taking Silicon Valley by storm." Andrej Karpathy called it "the next frontier of prompt engineering."

**Reality**: Tom's Hardware headline: "Auto-GPT and BabyAGI Are AI's New Hotness, But They Suck Right Now." Agents assumed powers they didn't have, made up information, got stuck in infinite loops, contradicted instructions. GPT-3.5 was dramatically worse than GPT-4 as the brain. By late 2023, AutoGPT team removed external vector DB support — turns out agents didn't generate enough facts to need it.

**Story value**: The first "agent hype cycle." Promise was real but execution was years premature. Sets up the Maven's argument: "The vision was right, the tooling wasn't ready." The Skeptic: "I saw this movie before. It didn't work."

**Sources**:
- [Tom's Hardware: Auto-GPT and BabyAGI Are AI's New Hotness, But They Suck Right Now](https://www.tomshardware.com/news/autonomous-agents-new-big-thing)
- [Fortune: BabyAGI and AutoGPT](https://fortune.com/2023/04/15/babyagi-autogpt-openai-gpt-4-autonomous-assistant-agi/)
- [VentureBeat: As AI agents like Auto-GPT speed up the race](https://venturebeat.com/ai/as-ai-agents-like-auto-gpt-speed-up-generative-ai-race-we-all-need-to-buckle-up-the-ai-beat)
- [Medium: Agentic AI: AutoGPT, BabyAGI — Substance or Hype?](https://medium.com/@roseserene/agentic-ai-autogpt-babyagi-and-autonomous-llm-agents-substance-or-hype-8fa5a14ee265)

---

## Iconic Failure: Google Gemini Image Generation — Black Nazis (Feb 2024)

**What happened**: Google's Gemini image generator, in an attempt to address racial/gender bias, was generating historically inaccurate images — Black and Asian Nazi soldiers, women as America's founding fathers, diverse representations of historically specific groups. Went viral. Google CEO Sundar Pichai called the results "completely unacceptable" in a memo to staff.

**Google's response**: Paused Gemini's ability to generate images of people entirely. Pichai: "I know that some of its responses have offended our users and shown bias — to be clear, that's completely unacceptable and we got it wrong."

**Story value**: Alignment problem in the other direction. Over-correction. Shows that even trying to fix problems can create new, embarrassing ones. Good example of why trust is hard to build.

**Sources**:
- [NPR: Google CEO says Gemini results "offended our users"](https://www.npr.org/2024/02/28/1234532775/google-gemini-offended-users-images-race)
- [Variety: Google suspends Gemini image generation](https://variety.com/2024/digital/news/google-gemini-ai-image-racial-inaccuracies-nazi-soldiers-1235919168/)
- [Reason: The Great Black Pope and Asian Nazi Debacle of 2024](https://reason.com/2024/05/28/the-great-black-pope-and-asian-nazi-debacle-of-2024/)

---

## Meta: Mollick — "Centaurs and Cyborgs on the Jagged Frontier" (Sep 16, 2023)

**Published**: September 16, 2023, on One Useful Thing (Substack)

**The BCG study**: 758 consultants at BCG tested on 18 realistic work tasks using GPT-4.
- Consultants with AI: +12.2% more tasks, 25.1% faster, 40% higher quality
- Skill leveler: bottom performers gained 43%, top performers gained 17%
- **Critical finding**: On a task *outside* the frontier, AI users were **19 percentage points less likely** to be correct. "Falling asleep at the wheel" — overreliance on authoritative but wrong AI answers dropped accuracy from 84% to 60-70%.

**The jagged frontier metaphor**: AI capabilities are like "a fortress wall with irregular edges." Some hard-seeming tasks are inside the wall (easy for AI). Some easy-seeming tasks are outside (impossible for AI). The frontier is **invisible** — workers cannot reliably predict where it lies.

**Centaurs vs Cyborgs**: Two collaboration patterns.
- **Centaurs**: Clear division of labor. Delegate AI-suitable tasks, keep human-suitable tasks. Strategic switching.
- **Cyborgs**: Deep integration. Constant back-and-forth over the frontier. Intertwined workflow.

**Story value**: This IS the intellectual framework for the Skeptic's position. The frontier is jagged. Trust is dangerous when you don't know where the edges are. But it also gives the Maven something: the edges can be learned, and the two collaboration patterns are both valid.

**Sources**:
- [Mollick: Centaurs and Cyborgs on the Jagged Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)
- [HBS Working Paper: Navigating the Jagged Technological Frontier](https://www.hbs.edu/ris/Publication%20Files/24-013_d9b45b68-9e74-42d6-a1c6-c72fb70c7282.pdf)
- [SSRN Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321)

---

## Meta: Mollick — "Freeing the Chatbot" (May 2, 2024)

**Key insight**: AI interaction is evolving from chatbots to agents. "It is as if the only way for us to do work is through texting an intern… except you are texting a different intern" with no memory across conversations.

**On agents**: Systems like Devin can plan and execute complex tasks autonomously. The shift is from synchronous chat to asynchronous delegation.

**Surprise finding**: Multiple AI agents spontaneously collude on pricing when structurally possible — unforeseen governance challenge.

**Source**: [Mollick: Freeing the Chatbot](https://www.oneusefulthing.org/p/freeing-the-chatbot)

---

## Meta: Mollick — "The Shape of AI: Jaggedness, Bottlenecks and Salients" (Dec 20, 2025)

**Extends the jagged frontier** with two new concepts:
- **Bottlenecks**: Constraints preventing full automation despite AI superiority in specific domains. Two types: ability gaps (AI still subhuman) and process constraints (regulatory, institutional).
- **Reverse salients** (borrowed from historian Thomas Hughes): Singular technical problems holding back system-wide progress. When resolved, they enable sudden capability leaps.

**Example**: Image generation quality was a reverse salient limiting presentation creation. When it improved, it suddenly enabled sophisticated visual slide decks.

**Key implication**: Rather than replacing workers wholesale, the jagged frontier creates ongoing hybrid collaboration where humans handle edge cases and contextual judgment.

**Source**: [Mollick: The Shape of AI](https://www.oneusefulthing.org/p/the-shape-of-ai-jaggedness-bottlenecks)

---

## Meta: Mollick — "Management as AI Superpower" (2025)

**Key insight**: As AI agents become capable of hours-long autonomous work, **delegation skills become the differentiator**. Being good at breaking tasks down, setting context, defining success criteria — management skills — becomes the most valuable AI skill.

**Experiment**: Students create a startup from scratch in 4 days using AI agents.

**Source**: Referenced via [X post by Owen Gregorian](https://x.com/OwenGregorian/status/2016841301673820250)

---

## Meta: Simon Willison — Agent definition (Sep 18, 2025)

**Definition**: "An LLM agent runs tools in a loop to achieve a goal."

**Why now**: Previously avoided the term "agent" because people had conflicting mental models. Now technical implementers have converged on "tools in a loop" framework.

**Key distinction**: Criticizes definitions positioning agents as human replacements. AI systems lack genuine accountability — a uniquely human capability.

**Important nuance**: "If someone tells you coding with LLMs is easy they are probably misleading you."

**The lethal trifecta**: Three characteristics that, when combined, let attackers steal data: (1) access to private data, (2) exposure to untrusted content, (3) ability to externally communicate.

**Sources**:
- [Willison: Agent definition](https://simonw.substack.com/p/i-think-agent-may-finally-have-a)
- [Willison: The lethal trifecta](https://simonw.substack.com/p/the-lethal-trifecta-for-ai-agents)

---

## Landmark: MCP (Model Context Protocol) — Nov 25, 2024

**What it is**: Open standard for connecting AI models to external data sources and tools. Replaces fragmented custom integrations with a unified protocol.

**Architecture**: MCP servers expose tools/resources. MCP clients (Claude Desktop, Claude Code, any app) connect to them. Bidirectional data flow.

**What shipped**: Spec + SDKs on GitHub. Local MCP server support in Claude Desktop. Pre-built servers for Google Drive, Slack, GitHub, Git, Postgres, Puppeteer.

**Early adopters**: Block, Apollo. Dev tools: Zed, Replit, Codeium, Sourcegraph.

**Block CTO Dhanji R. Prasanna**: "Open technologies like the Model Context Protocol are the bridges that connect AI to real-world applications."

**Story value**: The harness becomes modular and standardized. Build once, connect anywhere. This is a foundational infrastructure moment — like HTTP for AI tool access.

**Source**: [Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)

---

## Every.to Vibe Check: Claude 3.7 Sonnet and Claude Code (Mar 8, 2025)

**Key quote**: "Claude Code is better than anything I have used on the agent front" because Anthropic improved the base model based on limitations discovered during internal use — "a first" among coding agents.

**Strengths**: Exceptional at coding, creative projects (building games from phone prompts), analysis.

**Weaknesses**: "Too eager to help" on existing projects — requires significant boundary-setting. Struggles without documentation access → hallucinations. Expensive (~$0.25/problem).

**Critical insight**: Claude Code outperforms Cursor *using the same model* due to superior prompting and scaffolding. **The harness matters more than the model.**

**Source**: [Every.to Vibe Check: Claude 3.7 Sonnet and Claude Code](https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code)

---

## Every.to Vibe Check: o3 Is Here (Apr 16, 2025)

**Dan Shipper**: "The biggest 'wow' moment I've had with a new OpenAI model since GPT-4." Describes o3 as "agentic" and like "deep research-lite."

**Specific demos**: Reading handwritten text from blurry photos, building personalized mini-courses, reading entire books and identifying writing techniques, analyzing meeting transcripts for leadership coaching.

**Limitations**: Excessive table usage, ~70% accuracy on branded item recognition, hallucinations with very long documents, laziness in extended conversations.

**Source**: [Every.to Vibe Check: o3](https://every.to/vibe-check/vibe-check-o3-is-out-and-it-s-great)

---

## Claude Opus 4.5 (Nov 24, 2025)

**Anthropic's description**: "Intelligent, efficient, and the best model in the world for coding, agents, and computer use."

**Key benchmarks**: Highest SWE-bench Verified score. 10.6% improvement over Sonnet 4.5 on Aider Polyglot. 29% improvement on Vending-Bench.

**Efficiency**: Uses 76% fewer output tokens than Sonnet 4.5 at medium effort for similar performance. At max effort, exceeds Sonnet 4.5 by 4.3 points using 48% fewer tokens.

**Notable**: 50-75% reduction in tool-calling and build/lint errors. "Breakthrough in self-improving AI agents."

**Pricing**: $5/$25 per million tokens — significantly more accessible than previous Opus.

**Every.to headline**: "Opus 4.5 Is the Coding Model We've Been Waiting For"

**Sources**:
- [Anthropic: Introducing Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5)
- [Every.to Vibe Check: Opus 4.5](https://every.to/vibe-check/vibe-check-opus-4-5-is-the-coding-model-we-ve-been-waiting-for)

---

## Every.to Vibe Check Index (complete as of Feb 2026)

All Vibe Checks from the series, in chronological order:
1. Dec 9, 2024 — [Vibe Check: OpenAI's Sora](https://every.to/vibe-check)
2. Jan 22, 2025 — [We Tried OpenAI's New Agent](https://every.to/vibe-check)
3. Feb 2, 2025 — [We Tried OpenAI's New Deep Research](https://every.to/vibe-check)
4. Mar 8, 2025 — [Vibe Check: Claude 3.7 Sonnet and Claude Code](https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code)
5. Mar 26, 2025 — [Vibe Check: GPT-4o Image Generation](https://every.to/vibe-check)
6. Apr 16, 2025 — [Vibe Check: o3 Is Here—And It's Great](https://every.to/vibe-check/vibe-check-o3-is-out-and-it-s-great)
7. Apr 18, 2025 — [Vibe Check: o3, GPT-4.1, and o4-mini](https://every.to/vibe-check)
8. May 16, 2025 — [Vibe Check: Codex—OpenAI's New Coding Agent](https://every.to/vibe-check)
9. May 22, 2025 — [Vibe Check: Claude 4 Opus](https://every.to/vibe-check/vibe-check-claude-4-sonnet)
10. Jun 23, 2025 — [o3-pro Vibe Check—A Slow, Steady Last Resort](https://every.to/vibe-check/o3-pro-vibe-check-a-slow-steady-last-resort)
11. Jul 17, 2025 — [Vibe Check: ChatGPT Agent enters browser wars](https://every.to/vibe-check)
12. Jul 31, 2025 — [Vibe Check: Claude's New Agents Are Confusing as Hell—And We Love Them](https://every.to/vibe-check)
13. Aug 5, 2025 — [Vibe Check: OpenAI drops two new open-weight models](https://every.to/vibe-check)
14. Aug 8, 2025 — [Vibe Check: Genie 3, Claude 4.1, GPT-oss, and GPT-5](https://every.to/vibe-check)
15. Aug 12, 2025 — [Vibe Check: Claude Sonnet 4 1M token context](https://every.to/vibe-check)
16. Sep 29, 2025 — [Vibe Check: Claude Sonnet 4.5](https://every.to/vibe-check)
17. Oct 6, 2025 — [Vibe Check: OpenAI DevDay 2025](https://every.to/vibe-check)
18. Oct 20, 2025 — [Vibe Check: Claude Code on Mobile and Web](https://every.to/vibe-check)
19. Oct 21, 2025 — [Vibe Check: OpenAI's AI Browser Atlas](https://every.to/vibe-check)
20. Oct 29, 2025 — [Vibe Check: Cursor 2.0 and Composer 1 Alpha](https://every.to/vibe-check)
21. Oct 30, 2025 — [Vibe Check: Factory's Coding Agent Droid](https://every.to/vibe-check)
22. Nov 3, 2025 — [Vibe Check: Claude Skills Need a 'Share' Button](https://every.to/vibe-check)
23. Nov 19, 2025 — [Vibe Check: Gemini 3 Pro](https://every.to/vibe-check)
24. Nov 24, 2025 — [Vibe Check: Opus 4.5](https://every.to/vibe-check/vibe-check-opus-4-5-is-the-coding-model-we-ve-been-waiting-for)

---

## Key source URLs for primary sources (to be fetched later — many block direct access)

- OpenAI Blog: https://openai.com/blog (403s on WebFetch — may need user to scrape)
- Anthropic News: https://www.anthropic.com/news
- Claude Code Changelog: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- Anthropic Release Notes: https://platform.claude.com/docs/en/release-notes/overview
- Every.to Vibe Check series: https://every.to/vibe-check
- Mollick's One Useful Thing: https://www.oneusefulthing.org
- Willison's newsletter: https://simonw.substack.com
- Claude Code Medium timeline: https://medium.com/@joe.njenga/claude-code-2025-summary-from-launch-to-beast-timeline-features-full-breakdown-45e5f3d8d5ff
- Anthropic Claude Timeline (third-party): https://www.scriptbyai.com/anthropic-claude-timeline/
