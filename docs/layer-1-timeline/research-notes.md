# Timeline Research Notes — Detailed Sources & Vivid Examples

_This file contains the rich, source-linked detail that backs up the overview timeline. Organized by event. Each entry has URLs, specific examples, and story-ready material._

---

## ChatGPT Launch — "A Research Preview" (Nov 30, 2022) [OAI] [HARNESS]

**What shipped**: ChatGPT — a conversational interface on top of GPT-3.5, fine-tuned with RLHF. Released as a free "research preview." OpenAI's announcement was six sentences long.

**Sources**:
- [OpenAI: Introducing ChatGPT](https://openai.com/index/chatgpt/)
- [History.com: ChatGPT is released to the public](https://www.history.com/this-day-in-history/november-30/chatgpt-released-openai)
- [Cisco: How ChatGPT changed almost everything](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2024/m12/how-chatgpt-changed-well-almost-everything.html)

**What worked well (with examples)**:
- **Conversational format**: Could answer follow-up questions, admit mistakes, challenge incorrect premises, reject inappropriate requests
- **Accessibility**: Free to try, no API key needed, no technical knowledge required
- **Adoption speed**: 1 million users within 5 days (per Sam Altman). Fastest consumer app adoption in history at the time
- **RLHF**: "Substantial reductions in harmful and untruthful outputs" vs raw GPT-3.5

**What failed or was unreliable (with examples)**:
- **Hallucinations**: Confidently generated plausible-sounding but false information
- **Knowledge cutoff**: Trained on data through early 2022, couldn't answer about recent events
- **No tool use**: Could only generate text — couldn't search the web, run code, or interact with anything
- **No memory**: Each conversation was independent, no persistence between sessions
- **Inconsistent quality**: Answers varied dramatically based on prompt phrasing

**Harness vs. model**: HARNESS — The model (GPT-3.5) was not new; it had existed for months. What was new was the chat interface, the RLHF training, and the decision to make it free. ChatGPT was a *harness* innovation that made an existing model accessible to everyone. This is the original proof of the project's core thesis: the harness matters more than the model.

**Cultural context**: The announcement that started everything. Six sentences from OpenAI became the biggest technology story of the decade. The understated launch ("research preview") contrasted with the explosive adoption. Teachers panicked about cheating. Media oscillated between utopian and apocalyptic framing. The conversation about AI shifted from "interesting research" to "this changes everything."

**Skeptic's take**: "It's a fancy autocomplete that confidently makes things up. People are treating it like it's intelligent because it speaks in complete sentences. This is going to end badly."

**Maven's take**: "The model isn't even the story — GPT-3.5 existed before ChatGPT. What changed is that someone wrapped it in a chat interface and made it free. The HARNESS is the innovation. A million people in five days. This is the moment AI became everyone's concern."

---

## Claude 3.7 Sonnet & Claude Code Launch (Feb 24, 2025) [ANT] [BOTH]

**What shipped**: Claude 3.7 Sonnet — "first hybrid reasoning model on the market" with extended thinking. Claude Code — agentic command-line coding tool in limited research preview. Extended thinking lets users set a token "budget" (up to 128K tokens) for step-by-step reasoning.

**Sources**:
- [Anthropic: Claude 3.7 Sonnet](https://www.anthropic.com/news/claude-3-7-sonnet)
- [Every.to Vibe Check: Claude 3.7 Sonnet and Claude Code](https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code)

**What worked well (with examples)**:
- **SWE-bench Verified**: 63.7% without scaffolding; 70.3% with additional compute
- **TAU-bench**: Top performance on complex real-world agent tasks
- **Claude Code single-pass**: "Completed tasks in a single pass that would normally take 45+ minutes of manual work"
- **Integrated reasoning**: Rather than a separate reasoning model (like o1), reasoning is a built-in capability you can toggle. "Reasoning should be an integrated capability of frontier models rather than a separate model entirely"
- **Extended thinking budget**: Developers can set token budget for thinking, balancing speed vs. quality
- **Reduced refusals**: "More nuanced distinctions between harmful and benign requests, reducing unnecessary refusals by 45%"
- **Claude Code capabilities**: Search/read code, edit files, write/run tests, commit/push to GitHub, execute CLI tools
- **Customer validation**: Cursor: "best-in-class for real-world coding tasks." Cognition: superior at "planning code changes and handling full-stack updates." Replit: "build sophisticated web apps and dashboards from scratch"

**What failed or was unreliable (with examples)**:
- **Claude Code limited preview**: Only available to limited set of users initially
- **Cost concerns**: Every.to noted ~$0.25/problem for Claude Code — expensive for casual use
- **Too eager on existing code**: Every.to: "too eager to help" on existing projects — "requires significant boundary-setting"
- **Hallucinations without docs**: Struggles without documentation access → hallucinations

**Harness vs. model**: BOTH — Claude 3.7 Sonnet's extended thinking was a MODEL innovation. Claude Code was a pure HARNESS innovation — a terminal-based agentic coding tool. The key insight from Every.to: "Claude Code outperforms Cursor using the same model due to superior prompting and scaffolding." **The harness matters more than the model.**

**Cultural context**: This was Anthropic's "tools in a loop" moment. Claude Code was the first major AI company shipping an agentic coding tool built on their own model. The Every.to Vibe Check called it "better than anything I have used on the agent front" — and crucially noted the harness advantage over competitors using the same model.

**Skeptic's take**: "A coding agent that costs a quarter per problem and needs extensive babysitting on existing projects? And it hallucinates without docs? This is a tool for developers, not normal people."

**Maven's take**: "The Every.to finding is the whole thesis: Claude Code beats Cursor with the SAME MODEL because the harness is better. And extended thinking isn't a separate model — it's a mode. That's the right architecture. The terminal interface is limiting but it's the foundation everything else builds on."

---

## GPT-4 Launch (Mar 14, 2023) [OAI] [MODEL]

**What shipped**: GPT-4 — large multimodal model (text + image input, text output). First model to pass the Bar Exam (90th percentile vs GPT-3.5's 10th percentile). 8K and 32K context versions. API with waitlist.

**Source**: [OpenAI: GPT-4](https://openai.com/index/gpt-4-research/)

**What worked well (with examples)**:
- **Bar Exam**: Score of 298/400, ~90th percentile — vs GPT-3.5's 213/400, ~10th percentile
- **LSAT**: 163 (~88th percentile) vs GPT-3.5's 149 (~40th percentile)
- **Biology Olympiad (USABO)**: 87/150, 99th-100th percentile
- **SAT Math**: 700/800 (~89th percentile)
- **HumanEval coding**: 67% (0-shot) vs GPT-3.5's 48.1%
- **MMLU**: 86.4% (5-shot), outperforming all prior SOTA
- **Multilingual**: Outperformed GPT-3.5's English performance in 24 of 26 languages tested, including low-resource languages like Latvian, Welsh, and Swahili
- **Steerability**: System messages let developers customize AI personality/behavior — Socratic tutor example showed model maintaining character even under pressure
- **Safety**: 82% reduction in disallowed content responses vs GPT-3.5; 40% higher on internal adversarial factuality evals
- **Predictable scaling**: Successfully predicted GPT-4's final loss from 10,000x smaller models — "our first large model whose training performance we were able to accurately predict ahead of time"

**What failed or was unreliable (with examples)**:
- **Still hallucinates**: Announcement explicitly states "it still is not fully reliable (it 'hallucinates' facts and makes reasoning errors)"
- **Confidently wrong**: "Can be confidently wrong in its predictions, not taking care to double-check work"
- **Calibration hurt by RLHF**: Pre-trained model was well-calibrated (predicted confidence matched accuracy); post-training with RLHF "hurts the calibration quite a bit"
- **Jailbreaks**: "there still exist 'jailbreaks'" — system messages acknowledged as "the easiest way to jailbreak the current model"
- **Codeforces**: Only 392 Elo, below 5th percentile — competitive coding remained weak
- **Security vulnerabilities**: Can "introduce security vulnerabilities into code it produces"
- **Vision delayed**: Image input was "research preview and not publicly available" at launch
- **Capacity constrained**: API behind waitlist; "expect to be severely capacity constrained"

**Harness vs. model**: MODEL — This was primarily a model leap (bigger, smarter, multimodal). The system message for steerability was a minor harness innovation. No tool use, no agents, no persistent memory.

**Cultural context**: The "GPT-4 moment" — when the world realized AI could pass professional exams. Triggered both excitement and fear. Led directly to the Italian ban, the open letter calling for a 6-month pause, and the beginning of AI regulation discussions.

**Skeptic's take**: "It passes the Bar Exam but can't reliably code a FizzBuzz without introducing security vulnerabilities. It's confidently wrong and they admit the safety training made it worse at knowing when it's wrong. And they won't even show us the images feature yet."

**Maven's take**: "The exam scores are impressive but the real story is predictable scaling — they predicted performance from 10,000x smaller models. That means they know what's coming next. And putting it behind a waitlist was responsible, even if frustrating."

---

## Function Calling — The Harness Breakthrough (Jun 13, 2023) [OAI] [HARNESS]

**What shipped**: Function calling capability for GPT-4 and GPT-3.5 Turbo. Models can detect when a function needs to be called and output structured JSON with arguments. Also: GPT-3.5 Turbo 16K context, 75% embedding price cut, 25% input price cut.

**Source**: [OpenAI: Function calling and other API updates](https://openai.com/index/function-calling-and-other-api-updates/)

**What worked well (with examples)**:
- **Structured output from natural language**: "Email Anya to see if she wants to get coffee next Friday" → `send_email(to: string, body: string)` ([source](https://openai.com/index/function-calling-and-other-api-updates/))
- **Natural language to API calls**: "Who are my top ten customers this month?" → `get_customers_by_revenue(start_date, end_date, limit)` — or even SQL queries
- **Structured data extraction**: Define `extract_people_data(people: [{name, birthday, location}])` → extracts all people from a Wikipedia article
- **Weather example**: 3-step flow — model outputs function call JSON → developer calls external API → response sent back to model for summarization
- **JSON Schema integration**: Functions described via JSON Schema, model outputs conformant JSON

**What failed or was unreliable (with examples)**:
- **Security risk acknowledged**: "A proof-of-concept exploit illustrates how untrusted data from a tool's output can instruct the model to perform unintended actions" — early prompt injection via tools
- **Only single function per call**: Parallel function calling didn't come until DevDay (Nov 2023)
- **Reliability**: Function calling accuracy was imperfect; improved significantly with gpt-4-0613 but still required careful prompt engineering

**Harness vs. model**: HARNESS — This is the single most important harness innovation in the entire timeline. Function calling transformed LLMs from text generators into tool users. It enabled every subsequent development: plugins, agents, MCP, Claude Code. The model itself didn't change fundamentally — what changed was HOW it could interact with the world.

**Cultural context**: Quietly revolutionary. Less viral than ChatGPT launch or GPT-4, but arguably more consequential. This is where "chatbot" started becoming "tool user." ChatGPT Plugins had launched in March but were limited to OpenAI's ecosystem; function calling democratized tool use to any developer.

**Skeptic's take**: "Great, so now the AI can call functions. And they're already admitting there's a proof-of-concept exploit for it. We're giving AI the ability to act in the world before we've solved the trust problem."

**Maven's take**: "This is THE turning point. Before function calling, AI could only generate text. After function calling, AI can DO things — check weather, query databases, send emails. Every agent framework, every tool-using AI, everything we're building now traces back to this moment. The security concern they flagged is real, but the capability unlock is enormous."

---

## Claude 3 Model Family (Mar 4, 2024) [ANT] [MODEL]

**What shipped**: Three-model family — Claude 3 Haiku (fast/cheap), Claude 3 Sonnet (balanced), Claude 3 Opus (most intelligent). Vision capabilities. 200K context window (accepting inputs exceeding 1M tokens). API launched in 159 countries.

**Source**: [Anthropic: Introducing the next generation of Claude](https://www.anthropic.com/news/claude-3-family)

**What worked well (with examples)**:
- **Opus benchmarks**: Outperformed competitors on MMLU (undergraduate knowledge), GPQA (graduate reasoning), and GSM8K (mathematics)
- **Near-perfect recall**: 99%+ accuracy on "Needle in a Haystack" evaluations across 200K context
- **Accuracy improvement**: Opus showed "twofold improvement in accuracy" on challenging open-ended questions vs Claude 2
- **Speed**: Sonnet 2x faster than previous Claude versions at higher intelligence
- **Reduced refusals**: "Significantly less likely to refuse to answer prompts" — better contextual understanding of intent
- **Vision**: New multimodal capabilities for images, charts, technical diagrams, PDFs, flowcharts
- **Tiered pricing**: Haiku at $0.25/$1.25 per million tokens made Claude accessible for high-volume use cases

**What failed or was unreliable (with examples)**:
- **Opus pricing**: $15/$75 per million tokens — expensive for production use
- **Vision limitations**: Not as strong as GPT-4V on some benchmarks
- **Opus vs GPT-4**: While competitive, Opus didn't clearly dominate GPT-4 on all benchmarks — more of a parity moment than a leap

**Harness vs. model**: MODEL — This was Anthropic's model-tier play: three sizes for different use cases. No significant harness innovations (tool use came later).

**Cultural context**: Anthropic's coming-out party as a serious competitor. The three-tier model structure (Haiku/Sonnet/Opus) gave developers real choice. The 159-country API launch was a distribution moment.

**Skeptic's take**: "Another model that beats benchmarks. But can I trust it more than the others? They say it refuses less — is that actually better for safety?"

**Maven's take**: "The three-tier structure is smart engineering — Haiku for speed, Opus for quality, Sonnet for balance. The near-perfect needle-in-haystack recall at 200K context is quietly game-changing for document analysis. And reduced refusals means the model is actually more useful, not less safe."

---

## Claude 3.5 Sonnet — The Benchmark Killer (Jun 21, 2024) [ANT] [MODEL]

**What shipped**: Claude 3.5 Sonnet — mid-tier model that outperformed Claude 3 Opus (and GPT-4o) on most benchmarks at 2x the speed and 1/5th the price. Artifacts feature for collaborative workspace. 200K context, $3/$15 per million tokens.

**Source**: [Anthropic: Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet)

**What worked well (with examples)**:
- **Coding**: "Solved 64% of problems, outperforming Claude 3 Opus which solved 38%" on internal coding evaluation
- **Benchmarks**: Set "new industry benchmarks for graduate-level reasoning (GPQA), undergraduate-level knowledge (MMLU), and coding proficiency (HumanEval)"
- **Speed + intelligence**: 2x speed of Claude 3 Opus with superior intelligence — the mid-tier model became the best model
- **Vision**: Surpassed Claude 3 Opus on standard vision benchmarks; excels at interpreting charts, transcribing text from imperfect images
- **Artifacts**: New collaborative workspace feature — users could view, edit, and build upon Claude-generated code snippets, text, and website designs alongside conversations
- **Price/performance**: $3/$15 per million tokens (same as Sonnet 3) while beating Opus ($15/$75)

**What failed or was unreliable (with examples)**:
- **Still ASL-2**: Despite massive capability jump, safety classification unchanged — raised questions about whether the safety framework was keeping pace
- **Artifacts rough**: Initial artifacts feature was limited in scope
- **Context usage**: 200K context available but effective use at full length still had quality degradation

**Harness vs. model**: Primarily MODEL (the intelligence leap), but Artifacts was a significant HARNESS innovation — moving from chat to collaborative workspace.

**Cultural context**: This was the moment Claude became a serious daily-driver for developers. A mid-tier model beating the top-tier model at 1/5th the price is the kind of value proposition that changes adoption patterns. The Artifacts feature hinted at Anthropic's vision for AI as collaborator, not just chatbot.

**Skeptic's take**: "OK, the smaller model is now better than the bigger model? That's either impressive engineering or it means the bigger model was never that good. And they're charging me 5x less? Something doesn't add up."

**Maven's take**: "This is the price/performance inflection point. When the mid-tier model beats everyone including your own top tier, and costs 1/5th as much, adoption explodes. Artifacts is also interesting — it's the first time a major AI company said 'the chat interface isn't enough, let's build a workspace.' That's a harness insight."

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

## OpenAI DevDay — GPT-4 Turbo, Assistants API (Nov 6, 2023) [OAI] [BOTH]

**What shipped**: GPT-4 Turbo (128K context, 3x cheaper input / 2x cheaper output vs GPT-4), Assistants API (persistent threads, Code Interpreter, Retrieval, function calling), GPT-4 Turbo with Vision, DALL-E 3 API, Text-to-Speech API, JSON mode, parallel function calling, reproducible outputs (seed parameter), Whisper v3, Copyright Shield.

**Source**: [OpenAI: New models and developer products announced at DevDay](https://openai.com/index/new-models-and-developer-products-announced-at-devday/)

**What worked well (with examples)**:
- **Parallel function calling**: Users could send one message requesting multiple actions (e.g. "open the car window and turn off the A/C") — previously required multiple roundtrips ([source](https://openai.com/index/new-models-and-developer-products-announced-at-devday/))
- **JSON mode**: New `response_format` parameter ensures syntactically correct JSON output — huge for developers building structured integrations
- **GPT-3.5 Turbo improvements**: 38% improvement on format following tasks (JSON, XML, YAML) in internal evals
- **Code Interpreter**: Writes and runs Python in sandbox, generates graphs/charts, processes diverse file formats
- **Retrieval**: RAG built in — "you don't need to compute and store embeddings for your documents, or implement chunking and search algorithms"
- **Assistants API persistent threads**: Developers hand off thread state management to OpenAI, work around context window constraints

**What failed or was unreliable (with examples)**:
- **"Lazy GPT-4 Turbo"**: Within weeks, users widely reported the model cutting corners — truncating code, responding with "...rest of the code is similar..." (see separate entry)
- **GPT-4 fine-tuning**: Only "experimental access" — admitted that "GPT-4 fine-tuning requires more work to achieve meaningful improvements over the base model"
- **Assistants API beta quality**: Persistent threads and retrieval were beta, with rough edges

**Harness vs. model**: BOTH — The model got cheaper/faster (128K context), but the real news was tooling: Assistants API, Code Interpreter, Retrieval, parallel function calling. This was OpenAI's first serious "harness" play.

**Cultural context**: DevDay was OpenAI's first developer conference. Sam Altman was fired by the board 11 days later (Nov 17). The entire event was overshadowed by the boardroom drama within weeks.

**Skeptic's take**: "They gave us a bigger context window, cheaper prices, and a bunch of beta APIs — then the CEO got fired. And the model got lazier. Cool."

**Maven's take**: "This is where OpenAI stopped just making models and started building infrastructure. Assistants API with persistent threads, Code Interpreter, Retrieval — these are harness primitives. The model improvements were table stakes; the tooling was the real story."

---

## GPT-4o — Omni model (May 13, 2024) [OAI] [MODEL]

**What shipped**: GPT-4o ("omni") — a single end-to-end model processing text, audio, image, and video. Audio response latency: 232ms average (vs 2.8s GPT-3.5 / 5.4s GPT-4 voice mode). 2x faster and 50% cheaper than GPT-4 Turbo in API. Available in free tier.

**Source**: [OpenAI: Hello GPT-4o](https://openai.com/index/hello-gpt-4o/)

**What worked well (with examples)**:
- **Multimodal reasoning**: Accepted any combo of text/audio/image/video input, generated text/audio/image output — first truly multimodal model
- **Audio latency**: 232ms average response time, "similar to human response time in a conversation" — vs the old 3-model pipeline (transcribe → think → speak)
- **Multilingual tokenization**: 1.4-4.4x fewer tokens for non-English languages (e.g. Gujarati 4.4x, Telugu 3.5x, Chinese 1.4x)
- **Free tier access**: First time a GPT-4-class model was available free — massive democratization moment
- **Vision**: Real-world image analysis, document reading with figures, used by BeMyEyes for accessibility
- **Safety**: 90th percentile on competitive programming (Codeforces), 78.2% on MMMU

**What failed or was unreliable (with examples)**:
- **Voice mode delayed**: Despite the flashy demo, audio outputs were "limited to a selection of preset voices" at launch; full voice mode rolled out much later
- **The "Her" moment backlash**: Scarlett Johansson accused OpenAI of imitating her voice for the "Sky" voice without permission; OpenAI paused the voice
- **Safety rating**: Medium on persuasion (both pre and post mitigation) — highest risk category

**Harness vs. model**: Primarily MODEL — this was about making a single model natively multimodal rather than chaining separate models. But the free tier access was a distribution/harness decision.

**Cultural context**: The live demo went viral — the model flirting, singing, being sarcastic in real-time. Media compared it to the movie "Her." Then the Scarlett Johansson voice controversy erupted. This was OpenAI at peak cultural relevance.

**Skeptic's take**: "They did a flashy demo where the AI flirts and sings, then it turns out the voice mode isn't actually shipping yet, and they may have stolen someone's voice. Style over substance."

**Maven's take**: "Underneath the controversy, this was genuinely important: end-to-end multimodal processing means the model doesn't lose information between modalities anymore. And putting GPT-4-class intelligence in the free tier changed who could access this technology."

---

## OpenAI o1 — "Learning to Reason" (Sep 12, 2024) [OAI] [MODEL]

**What shipped**: OpenAI o1-preview — first model trained with large-scale reinforcement learning to use chain-of-thought reasoning before answering. Separate "thinking" process visible as a summary (raw chain of thought hidden).

**Source**: [OpenAI: Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/)

**What worked well (with examples)**:
- **AIME 2024**: 74% pass@1 (11.1/15 problems), 83% consensus@64, 93% with reranking@1000 — vs GPT-4o's 12% (1.8/15). "Places among top 500 students nationally" ([source](https://openai.com/index/learning-to-reason-with-llms/))
- **GPQA Diamond**: "Became the first model to surpass the performance of human experts" with PhDs in physics, biology, chemistry
- **Competitive programming**: Codeforces Elo 1258 (62nd percentile) vs GPT-4o's 808 (11th percentile); further fine-tuned version scored 1807 (93rd percentile)
- **IOI 2024**: Fine-tuned version scored 213 points (49th percentile) under competition conditions; with relaxed submission limits, scored 362 (above gold medal threshold)
- **Cipher solving**: Solved a novel letter-pair averaging cipher that GPT-4o completely failed — the "STRAWBERRY" example became iconic
- **Safety via reasoning**: 93.4% safe on challenging jailbreaks vs GPT-4o's 71.4%; chain of thought allows the model to reason about safety rules

**What failed or was unreliable (with examples)**:
- **Natural language tasks**: "Not preferred on some natural language tasks" — human evaluators preferred GPT-4o for non-reasoning tasks
- **Slow**: Extended thinking time meant much higher latency for simple questions
- **Hidden chain of thought**: Raw reasoning hidden from users — "competitive advantage" cited alongside monitoring rationale. Transparency concern.
- **Reward hacking**: OpenAI noted "interesting instances of reward hacking" in their safety testing

**Harness vs. model**: MODEL — This was a fundamental training paradigm shift (reinforcement learning for reasoning), not a tooling improvement. But the hidden-then-summarized chain of thought is a harness/UX decision.

**Cultural context**: Paradigm shift from "predict next token faster" to "think longer before answering." OpenAI splitting into two model families: GPT (fast, multimodal) and o-series (slow, reasoning). The STRAWBERRY cipher demo went viral.

**Skeptic's take**: "So now it thinks for 5 seconds before answering, and they won't show me what it's thinking? And it's worse at normal conversation? I'm paying for a model that's slower AND they're hiding its work?"

**Maven's take**: "This is the most important paradigm shift since transformers. The model doesn't just pattern-match anymore — it reasons through problems step by step. AIME going from 12% to 74% isn't an incremental improvement, it's a category change. And the safety implications of reasoning about rules are huge."

---

## OpenAI o3 and o4-mini — Agentic Reasoning (Apr 16, 2025) [OAI] [BOTH]

**What shipped**: o3 (most powerful reasoning model) and o4-mini (fast/cheap reasoning). First reasoning models that can agentically use ALL ChatGPT tools — web search, Python, file analysis, image generation, visual reasoning. Can "think with images" (integrate images into chain of thought). Also launched Codex CLI (open-source terminal coding agent).

**Source**: [OpenAI: Introducing o3 and o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/)

**What worked well (with examples)**:
- **SWE-bench**: o3 set new SOTA "without building a custom model-specific scaffold" — the model itself was the scaffold
- **AIME 2025**: o4-mini achieved 99.5% pass@1 with Python interpreter access (100% consensus@8). o3: 98.4% pass@1
- **20% fewer major errors**: o3 made 20% fewer major errors than o1 on difficult real-world tasks, "especially excelling in programming, business/consulting, and creative ideation"
- **Thinking with images**: First models to integrate images directly into chain of thought — "They don't just see an image — they think with it." Can rotate, zoom, transform images during reasoning
- **Agentic tool use example**: "How will summer energy usage in California compare to last year?" → model searches web for utility data, writes Python forecast, generates graph, explains factors — all chained automatically
- **Codex CLI**: Open-source terminal coding agent, $1M grant initiative

**What failed or was unreliable (with examples)**:
- **Cost**: Still expensive at high reasoning effort; cost-performance tradeoff required careful tuning
- **Replaced previous models**: Plus/Pro/Team users had o1/o3-mini removed from selector entirely — no choice to use simpler models
- **Convergence acknowledged**: OpenAI stated they're "converging the specialized reasoning capabilities of the o-series with the natural conversational abilities of the GPT-series" — admission the split was unsustainable

**Harness vs. model**: BOTH — The reasoning improvements (thinking with images, better RL scaling) were model advances. But the agentic tool use (reasoning about WHEN to use tools, chaining tools) was a harness/training innovation. Codex CLI was pure harness.

**Cultural context**: This was the "agents actually work now" moment for OpenAI. The o-series went from "good at math puzzles" to "can actually do multi-step work." Codex CLI was OpenAI's response to Claude Code. Dan Shipper (Every.to) called o3 "the biggest wow moment since GPT-4."

**Skeptic's take**: "They gave reasoning models tools and suddenly they work better? Isn't that what everyone's been saying — it's not the model, it's what you plug into it?"

**Maven's take**: "This is the convergence point. Reasoning + tools + vision in one model. The SWE-bench result without custom scaffolding is significant — the model itself learned when and how to use tools. And they open-sourced Codex CLI, which is a real concession that the harness matters."

---

## GPT-5 — Unified Intelligence (Aug 7, 2025) [OAI] [BOTH]

**What shipped**: GPT-5 — "unified system" combining fast responses and deep reasoning with a real-time router. Replaces GPT-4o, o3, o4-mini, GPT-4.1, and GPT-4.5 as the default. GPT-5 pro for extended reasoning. New "safe completions" safety training paradigm. Four personality presets (Cynic, Robot, Listener, Nerd).

**Source**: [OpenAI: Introducing GPT-5](https://openai.com/index/introducing-gpt-5/)

**What worked well (with examples)**:
- **Hallucination reduction**: ~45% fewer factual errors than GPT-4o with web search; ~80% fewer than o3 when thinking. "About six times fewer [hallucinations] than o3" on long-form content
- **Honesty/deception**: When given impossible tasks (missing images, nonexistent APIs), o3 gave confident wrong answers 86.7% of the time; GPT-5 only 9%. Deception rate dropped from 4.8% (o3) to 2.1%
- **SWE-bench Verified**: 74.9% (new SOTA)
- **AIME 2025**: 94.6% without tools
- **Aider Polyglot**: 88%
- **HealthBench**: Best model for health questions; "acts more like an active thought partner, proactively flagging potential concerns"
- **Efficiency**: 50-80% fewer output tokens than o3 for comparable performance on reasoning tasks
- **Sycophancy reduction**: Sycophantic replies cut from 14.5% to <6% in targeted evaluations
- **Safe completions**: New training paradigm teaching partial answers and transparent refusals instead of binary comply/refuse
- **Coding aesthetics**: "Beautiful and responsive websites, apps, and games... with an eye for aesthetic sensibility in just one prompt" — better understanding of spacing, typography, white space

**What failed or was unreliable (with examples)**:
- **Bio risk**: Treated as "High capability" in biological/chemical domain — required 5,000 hours of red-teaming, multilayered defense system
- **Free tier limitations**: Once usage limits hit, falls back to "GPT-5 mini" — two-tier experience
- **Model proliferation**: Despite claiming "unified," still has GPT-5, GPT-5 thinking, GPT-5 pro, GPT-5 mini — four variants
- **Router opacity**: Real-time router decides when to think vs. respond quickly — users can't fully control this

**Harness vs. model**: BOTH — The model advances (safe completions training, reduced hallucinations, unified architecture) are substantial. But the router, personality presets, and the strategic decision to unify all models under one name are harness/UX decisions.

**Cultural context**: OpenAI ended the GPT/o-series split. Sam Altman framed it as AI that "feels less like talking to AI and more like chatting with a helpful friend with PhD-level intelligence." The sycophancy fix was an explicit response to the GPT-4o update controversy from earlier in 2025.

**Skeptic's take**: "They merged everything into one model and it still has four variants? And a hidden router decides when it thinks hard? I liked knowing which model I was using. Now it's a black box that sometimes thinks and sometimes doesn't."

**Maven's take**: "The hallucination and deception numbers are the real story. Going from 86.7% confident wrong answers on impossible tasks to 9% is transformative. Safe completions training — teaching partial answers instead of binary refuse/comply — is exactly the nuanced approach AI safety needed. And unifying everything under one model is the right UX even if the implementation still has variants."

---

## Key source URLs for primary sources

- OpenAI Blog: https://openai.com/blog (accessible via browser)
- Anthropic News: https://www.anthropic.com/news
- Claude Code Changelog: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- Anthropic Release Notes: https://platform.claude.com/docs/en/release-notes/overview
- Every.to Vibe Check series: https://every.to/vibe-check
- Mollick's One Useful Thing: https://www.oneusefulthing.org
- Willison's newsletter: https://simonw.substack.com
- Claude Code Medium timeline: https://medium.com/@joe.njenga/claude-code-2025-summary-from-launch-to-beast-timeline-features-full-breakdown-45e5f3d8d5ff
- Anthropic Claude Timeline (third-party): https://www.scriptbyai.com/anthropic-claude-timeline/
