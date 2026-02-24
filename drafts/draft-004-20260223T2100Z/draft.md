# Agents for Everyone — Draft 004

_Package: `story/agent-unboxing`_
_Draft: 004_
_Date: 2026-02-23_
_Status: Feedback pass — CriticMarkup from draft-003 processed; writing edits applied broadly_

---

## Chapter 1: "Agents are here!"

<!-- COMIC
id: ch01-the-box
characters: maven, declan, clawd
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Modern open-plan office kitchen/lounge area. A communal table with laptops and coffee mugs. Warm overhead pendant lights. Maven has just set a sleek, minimalist white box on the table — labeled "Agents" in clean sans-serif type with a small printed image of Claw'd on the front, like a premium tech product. Declan sits across, coffee in hand.

frame_a:
  action: Maven holds the box up with both hands, presenting it. Barely-contained excitement. Declan sits across, coffee in hand, leaning back in his chair, arms loosely crossed — unimpressed.
  expression_maven: excited, barely-contained energy
  expression_declan: unimpressed, bracing himself
  dialogue: ["The agents are here — and it's time to put them to work!", ""]

frame_b:
  action: Maven has set the box on the table. Declan gestures dismissively with his coffee hand, not moving from his chair. Maven shifts to amused determination.
  expression_maven: determined, amused
  expression_declan: dry, eyebrow raised
  dialogue: ["", "If this is another AI demo, I'm going back to my Jira board."]
-->

The agents are here. That's how Maven puts it — not a prediction, not a hypothesis. A fact. She's been following what happened to software development over the past year: Claude Code, Windsurf, Cursor rewriting company codebases overnight. And now, she says, that same shift is starting to move through knowledge work. Including product management.

Declan doesn't look up. He's a product manager, same as Maven, and he's sat through enough waves of "this changes everything" to have stopped counting. ChatGPT Enterprise in 2023. AutoGPT eating a whole weekend to infinite loops. Devin — the "first AI software engineer" — that quietly failed 85% of real-world tests.

"I don't code," he says. "I write PRDs. I wrangle stakeholders. I sit in meetings about meetings. Last quarter my team spent a sprint building from an AI-generated spec that seemed plausible but was completely wrong. If your magic agent needs a terminal, I'm not interested."

Maven doesn't argue. He's not uninformed — he's informed and burned.

"Just — hold that thought for five minutes," she says. "Someone else is coming."

### Sources

1. **AutoGPT was the #1 GitHub repo of 2023 with 174,000+ stars — but users reported it getting stuck in infinite loops for entire nights.** AutoGPT and BabyAGI pioneered autonomous agents but proved the harness wasn't ready. ([Tom's Hardware](https://www.tomshardware.com/news/autonomous-agents-new-big-thing), [Wikipedia](https://en.wikipedia.org/wiki/AutoGPT))

2. **Answer.AI tested Devin on 20 real-world tasks and found a 15% success rate — "we couldn't discern any pattern to predict which tasks would work."** The first "AI software engineer" struggled with basic reliability. ([Answer.AI](https://www.answer.ai/posts/2025-01-08-devin.html))

3. **A lawyer who trusted ChatGPT's legal research submitted six entirely fabricated cases to federal court, resulting in sanctions.** Mata v. Avianca became the cautionary tale for uncritical AI trust. ([CNN](https://www.cnn.com/2023/05/27/business/chat-gpt-avianca-mata-lawyers))

4. **"If someone tells you coding with LLMs is easy they are probably misleading you."** — Simon Willison, who has built 150+ tools with LLMs and still emphasizes intellectual honesty about their limitations. ([Willison](https://simonw.substack.com/p/i-think-agent-may-finally-have-a))

---

## Chapter 2: "I tried AI; it was fine. But it didn't change my work."

<!-- COMIC
id: ch02-emery-enters
characters: maven, declan, emery
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office kitchen/lounge. The "Agents" box sits on the table, lid closed. Maven stands beside it. Declan still seated. Emery has just walked in, tablet tucked under one arm, stylus behind their ear, teal cardigan over a gray tee.

frame_a:
  action: Emery pulls out a chair and sits down, placing their tablet on the table. Maven turns to greet them warmly. Declan watches with mild interest.
  expression_maven: welcoming, gesturing Emery in
  expression_emery: curious, glancing at the box
  expression_declan: neutral, observing
  dialogue: ["How are you using AI in your work today?", ""]

frame_b:
  action: Emery shrugs casually, one hand on their tablet. They're comfortable, not defensive.
  expression_emery: self-aware, slightly amused
  expression_declan: leaning forward slightly, interested despite himself
  dialogue: ["", "I mean, I use Gemini? Like, every day. It's basically replaced Google for me."]
-->

Emery is a PM on the platform team. They use AI. It's fine.

They describe their current setup: Gemini for quick questions instead of search. A writing assistant for first drafts of customer-facing docs. A text file on their desktop — "prompts.txt" — with their twenty most-used prompts, organized by task. On a recent weekend, they tried Lovable to prototype a feature tracker app. It almost worked. But that was for fun — it didn't seem related to their actual work.

"The thing is," Emery says, "it's all disconnected. I copy-paste context into a chat window every time. It doesn't know my project. It doesn't remember yesterday. Last week I pasted our PRD into Gemini for the third time and it still asked me what our target audience was."

Maven nods. "That's exactly right."

"And I heard about coding agents — Claude Code, Windsurf, whatever. But I don't code. So I figured that's a developer thing."

### Sources

1. **Google Gems let users save custom instructions for Gemini — personal productivity tools embedded in the Google ecosystem.** Unlike GPTs, Gems are practical but siloed: no file access, no tool integrations, no persistence beyond the instruction set. ([Google Blog](https://blog.google/products-and-products/products/gemini/google-gemini-update-august-2024/))

2. **Teresa Torres broke her context into dozens of tiny focused markdown files so simple prompts produce rich output — she calls it "lazy prompting."** The key insight: pre-loading context into files eliminates the copy-paste burden of chat interfaces. ([ChatPRD](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management))

3. **Helen Lee Kupp voice-records ideas on stroller walks, drops transcripts into a folder, and Claude Code organizes them into research themes, articles, and LinkedIn posts.** The filesystem replaces the chat window as the primary interface. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

4. **ChatGPT Plugins, OpenAI's first attempt at giving AI access to external tools, never achieved product-market fit and were shut down in April 2024** — proving that tool use needs to be embedded, not bolted on. ([OpenAI](https://openai.com/index/chatgpt-plugins/))

---

## Chapter 3: "So what's the difference between a chatbot and an agent?"

<!-- COMIC
id: ch03-the-unboxing
characters: maven, declan, emery, clawd
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office kitchen/lounge. The "Agents" box is fully open on the table, lid back. Maven stands beside it. Emery leans forward in their chair. Declan watches from across the table.

frame_a:
  action: Maven gestures to Claw'd sitting on the table next to the open box — notebook open, tiny pencil in hand, looking up at the humans. Emery's eyes go wide. Declan's coffee cup freezes halfway to his mouth.
  expression_maven: proud, presenting
  expression_emery: delighted, eyes wide
  expression_declan: caught off guard, frozen mid-sip
  dialogue: ["That was a chatbot. This is an agent — and you're going to love working with one.", ""]

frame_b:
  action: Claw'd sits at the center of the table, notebook open. Emery reaches a hand toward it instinctively. Maven gestures warmly.
  expression_maven: warm, gesturing at Claw'd
  expression_emery: reaching out, curious
  expression_declan: skeptical but looking at Claw'd
  dialogue: ["", "It has a notebook?"]
-->

"That was a chatbot," Maven says. "This is an agent — and you're going to love working with one."

"A chatbot is a text box. You type a question, it types an answer. It doesn't know your files, it can't use your tools, and it forgets things unpredictably — some sessions remember more than others, but you can't know what, and you can't control it."

"An agent is different. It reads your project folder. It connects to your tools — Jira, Slack, Google Drive. It follows rules you write for it. And it doesn't just answer — it plans, tries something, checks if it worked, and adjusts. Like a junior teammate who actually listens."

Emery gets it immediately. "So instead of pasting my PRD into a chat window..."

"The agent reads your PRD directly. It reads your CLAUDE.md — a persistent instruction file that tells it who you are, what your project is, how you like things done. Your whole repo is its context."

Declan sets down his coffee. "Plan, try, check, adjust. That's what AutoGPT promised. It got stuck in loops."

"AutoGPT was the right idea two years early," Maven says. "The models weren't good enough and the harness wasn't smart enough. Models learned to recognize when they were stuck. The harness learned to checkpoint progress, compact context, and ask for help instead of looping."

### Sources

1. **Simon Willison defined an agent as "an LLM that runs tools in a loop to achieve a goal"** — widely quoted, but agency requires more: the ability to act on the world, read files, call APIs, take consequential steps. The loop is the mechanism; the actions are the substance. ([Willison](https://simonw.substack.com/p/i-think-agent-may-finally-have-a))

2. **Claude Code launched in February 2025 as a terminal-based agent that could search code, edit files, run tests, commit to GitHub, and execute CLI tools** — the moment the agent left the browser and entered the file system. ([Anthropic](https://www.anthropic.com/news/claude-3-7-sonnet))

3. **@mernit (Openclaw): "The architecture of an AI agent can be reduced to two components: the filesystem as state, and Claude as the orchestrator."** When you connect Gmail, the emails become files. The filesystem IS the state. ([X](https://x.com/mernit/status/2021324284875153544))

4. **By February 2026, Claude Code authored 4% of all public GitHub commits (~135,000/day), projected to reach 20%+ by year-end.** The agent didn't stay in the lab. ([Anthropic](https://www.anthropic.com/news/claude-opus-4-6))

---

## Chapter 4: "It works with your actual files — not a chat window."

<!-- COMIC
id: ch04-files-context
characters: maven, emery, declan, clawd
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office area, but now someone has pulled up a laptop screen showing a file explorer with folders: /docs, /specs, /research, /decisions. Claw'd sits on the table next to the laptop, notebook open, actively scribbling. Maven points at the screen. Emery leans in with their tablet propped beside the laptop.

frame_a:
  action: Maven points at the folder structure on the laptop screen. Claw'd is flipping through its notebook, mirroring the file browsing. Emery leans forward, tablet forgotten.
  expression_maven: explaining, pointing at screen
  expression_emery: leaning in, aha moment dawning
  expression_declan: watching from behind, arms still crossed but closer to the group
  dialogue: ["See this file? CLAUDE.md. The agent reads it every time you start a session. Your project context, your preferences, your conventions — all in one place.", ""]

frame_b:
  action: Emery looks down at their tablet, then back at the screen, making a connection.
  expression_emery: excited, the lightbulb moment
  expression_maven: pleased, watching Emery get it
  dialogue: ["", "Wait — so my prompts.txt on the desktop... that could just BE the instruction file? And it would read it automatically?"]
-->

Emery's prompts.txt file has twenty saved prompts. Every time they start a conversation with Gemini, they open the file, find the right prompt, copy it, paste it, then add whatever context is specific to today's task. It works. Barely.

"Here's what that looks like with an agent," Maven says. She opens a project folder on the laptop. Inside: /docs, /specs, /research, /decisions, and at the root, a file called CLAUDE.md.

"This file is your prompts.txt — but permanent. The agent reads it automatically every time you start working. You put your project context here, your conventions, your preferences. 'When I ask for a PRD, use this format. Our users are mid-market SaaS buyers. Always check the /research folder before answering questions about competitors.'"

Emery stares. "And it... just reads my files?"

"All of them. Your specs, your meeting notes, your decision log. It doesn't need you to paste anything. It lives in your project."

This is the first primitive: **filesystem access**. The agent doesn't operate in a chat window — it operates in your project folder. It reads what's there. It creates new files. It updates existing ones. The difference between describing your kitchen over the phone and letting the chef walk in.

Teresa Torres, a product discovery coach, broke her entire workflow into small markdown files — one per topic, one per client, one per research theme. Instead of crafting elaborate prompts, she just works. The agent reads what it needs. She calls it "lazy prompting."

Declan, from behind them: "So it reads everything. Including the stuff that's wrong?"

Maven: "Yes. Which is why the files matter. Garbage context, garbage output. Investing in good project documentation helps your human teammates AND the agent — the same investment paying off twice."

### Sources

1. **Teresa Torres built her context into dozens of focused markdown files — at the end of each session she asks "Claude, what did you learn today that we should document?"** The context library grows as a side effect of working. ([ChatPRD](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management))

2. **CLAUDE.md files provide persistent project instructions loaded into every conversation — root, parent directories, home folder, child directories.** The `/init` command auto-generates one. ([Claude Code Docs](https://code.claude.com/docs/en/overview))

3. **"Chat is describing your kitchen to a chef over the phone. Filesystem access is letting the chef into your kitchen."** Framing from Session 6 research on the non-SWE capability stack.

4. **Abhi Chandwani maintains verbose git commits specifically to create context for future agent workflows — the commit history becomes the agent's memory.** Good documentation practices compound. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

---

## Chapter 5: "You teach it how you work — and it remembers."

<!-- COMIC
id: ch05-rules-skills
characters: maven, emery, clawd
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Closer angle on the table. Claw'd is sitting between Maven and Emery, notebook open to a page with a neat checklist. Maven has pulled up a text file on the laptop showing structured markdown — a skill definition. Emery is taking notes on their tablet with the stylus from behind their ear. Declan is visible in the background, chair pushed back slightly, listening but not participating.

frame_a:
  action: Maven points at a section of the skill file on screen. Claw'd looks up attentively, pencil poised. Emery has pulled the stylus from behind their ear and is sketching on their tablet.
  expression_maven: teaching, animated
  expression_emery: focused, taking notes
  dialogue: ["This is a skill file. It tells the agent exactly how to do a specific task — your format, your criteria, your workflow. Write it once, use it forever.", ""]

frame_b:
  action: Emery looks up from their tablet, connecting dots.
  expression_emery: excited, something clicking
  expression_maven: nodding, affirming
  dialogue: ["", "So it's like onboarding documentation... but the documentation actually gets read?"]
-->

Every PM has a way they do things. Format for PRDs, launch checklists, interview questions. Usually it lives in their head or a Google Doc nobody reads — tribal knowledge that evaporates when someone changes teams.

"Skills," Maven says, opening a file on the laptop, "are how you teach the agent your way of working."

A skill file is structured text — markdown, not code — that describes a specific task: what inputs it needs, what steps to follow, what format to produce. Write one skill file for "draft a PRD," and every time the agent does that task, it follows your format, your conventions, your quality bar.

"It's like onboarding a new hire," Emery says slowly, "except they actually retain what you told them."

"And you don't have to write skill files from scratch. You can teach them in conversation — work a task with the agent, give feedback as you go, then ask: 'What did you learn today? Write it as a skill file.' The agent can author its own instructions from your corrections."

"Agents are also unusually good at introspection. After a working session, ask it to retro: what went well, what didn't, how should the skill file change? The output is specific — not 'improve communication' but 'always check the /research folder before making claims about competitors.'"

"Once you update the skill, it holds. Every time after that, the agent follows the new instructions reliably. The investment compounds. And when you nail a skill, you can share it — drop the file in a shared repo and your whole team has it. Someone else's expertise, running in your workflow."

This is the second primitive: **persistent instructions**. CLAUDE.md gives the agent project context. Skills give it task-specific expertise. The model is the same for everyone — the instructions make it behave like YOUR expert.

Declan, from the background: "So you're encoding your preferences in text files and hoping the AI follows them?"

Maven: "Not hoping. Testing. You run it, review the output, adjust the instructions. Same way you'd manage anyone."

### Sources

1. **Hilary Gridley reverse-engineered her implicit quality standards from before/after slide examples into a "Deck Doctor" GPT — key prompt: "Be 100 times more specific."** This turns tacit expertise into explicit, scalable evaluation. ([ChatPRD](https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts))

2. **Lazar Jovanovic: "After solving a problem, ask the AI how to prompt it better next time, then add that guidance to your rules file."** A single rules file achieves compounding improvement across sessions. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code))

3. **Claire Vo built a meta-skill — a "skill that builds skills" — demonstrating that agent capabilities are composable, not flat.** One factory skill generates domain-specific skills consistently. ([ChatPRD](https://www.chatprd.ai/how-i-ai/claude-skills-explained))

4. **The Cowork legal plugin is ~200 lines of structured markdown — NDA triage against 13 criteria, contract review with clause-by-clause analysis.** It triggered a $285 billion stock selloff. The harness is markdown. ([Nate's Newsletter](https://natesnewsletter.substack.com/p/200-lines-of-markdown-just-triggered))

---

## Chapter 6: "It doesn't just answer — it does things."

<!-- COMIC
id: ch06-tools-actions
characters: maven, emery, clawd
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: The laptop screen now shows a terminal/command output with a list of completed actions: "Searched 4 databases... Updated Jira ticket... Created summary.md..." Claw'd is sitting near the laptop, notebook filled with checkmarks. Maven leans against the table. Emery is on the edge of their seat. Declan is visible in background, having moved his chair slightly closer.

frame_a:
  action: Maven gestures at the terminal output. Claw'd's notebook page is full of completed checkmarks. Emery reads the output, mouth slightly open.
  expression_maven: matter-of-fact, letting the output speak
  expression_emery: impressed, reading the screen
  dialogue: ["It didn't just tell me what to do. It did it. Searched the web, pulled the data, updated the ticket, wrote the summary.", ""]

frame_b:
  action: Emery turns to look at Maven directly, something shifting in how they think about this.
  expression_emery: recalibrating, serious
  expression_maven: steady, waiting for it to land
  dialogue: ["", "That's... not what I thought this was."]
-->

Emery has used AI to draft emails, brainstorm feature names, and summarize meeting notes. In every case, the output was text. Suggestions. Ideas. Things they had to copy-paste into the actual tool and then do the work themselves.

"Watch this," Maven says. She types: *Analyze Q4 usage data, find the three features with the highest signup-to-week-2 drop-off, cross-reference our backlog, and draft priorities for planning.*

The agent reads the CSV files. It writes and runs an analysis script. It searches the backlog folder for related issues. It produces a markdown summary with three feature recommendations, each grounded in specific data points and linked to existing tickets.

"It didn't give me a suggestion," Maven says. "It did the work."

This is the third primitive: **tool use and actions.** Through MCP — think of it as USB ports for AI, letting you plug your existing tools in — agents connect to Jira, Slack, Google Drive, databases, web search, APIs. The agent doesn't just generate text. It queries, updates, creates, and organizes. And for tools that don't yet have MCP servers, agents can use the CLI or operate a browser directly — navigating, clicking, extracting — without waiting for anyone to build an integration.

Reid Robinson, a PM at Zapier, connected his agent to HubSpot, Coda, and Fireflies via MCP. After every customer call, the agent reads the transcript, searches his CRM for the contact, enriches the record, and creates a follow-up task. A fifteen-minute manual workflow reduced to one step.

Declan, now closer to the group than before: "And when it does something wrong? When it updates the wrong ticket?"

Maven: "You review before it acts. Most agents have approval gates — they show you what they're about to do and wait for a thumbs up. Same as reviewing a junior's PR."

### Sources

1. **Reid Robinson (Zapier PM): Post-meeting transcript → agent searches CRM via MCP → enriches contact record → creates follow-up task.** A 15-minute manual workflow became automated. ([ChatPRD](https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep))

2. **Dennison Bertram built "Claude CEO" — connecting Gmail, Brex, Mercury, and Linear via MCP.** A single morning prompt produces a cross-tool executive summary of what to focus on today. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

3. **MCP (Model Context Protocol), announced November 2024, is an open standard for connecting AI to external tools** — replacing the fragmented, proprietary integrations that doomed ChatGPT Plugins. ([Anthropic](https://www.anthropic.com/news/model-context-protocol))

4. **The Anthropic Growth Marketing team built an agent that processes a CSV of hundreds of ads, identifies underperformers, and generates new variations — reducing hours of copy-pasting to "half a second per batch."** ([Anthropic](https://claude.com/blog/how-anthropic-teams-use-claude-code))

---

## Chapter 7: "Show me what this looks like for a PM."

<!-- COMIC
id: ch07-pm-lifecycle
characters: maven, emery, clawd
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: The table now has multiple items spread across it — the laptop, Emery's tablet with sketches, printouts of a feature spec. Claw'd is walking between items like a tiny project manager, notebook open. Maven and Emery are deep in conversation. Declan is in the background, chair turned toward them, listening with an expression that's more thoughtful than dismissive.

frame_a:
  action: Maven counts on her fingers as she lists use cases. Claw'd follows along, flipping notebook pages. Emery's tablet shows what looks like a rough workflow diagram they've been sketching.
  expression_maven: animated, ticking off examples
  expression_emery: engaged, sketching on tablet
  dialogue: ["Discovery research synthesis. PRD drafting grounded in customer data. Spec review against acceptance criteria. Competitive analysis. Stakeholder updates. Release notes from commit history.", ""]

frame_b:
  action: Emery stops sketching and looks up, stylus in hand, connecting it to their own work.
  expression_emery: recognizing their own workflow, excited
  expression_maven: watching Emery connect the dots
  dialogue: ["", "Half my week is synthesizing information that already exists in four different places. That's what this does?"]
-->

Emery's calendar is mostly synthesis: customer notes into themes, specs against acceptance criteria, Jira and Slack into a stakeholder update. Structured information taken from here, filtered through judgment, produced over there.

"Discovery," Maven says. "Your agent reads every call transcript in the /calls folder, identifies recurring themes, and produces a summary with supporting quotes. Derek DeHart does this — his agent synthesizes evidence for and against product hypotheses across dozens of calls."

"PRD drafting. It pulls your product brief, your research, your existing template from the skills folder, and produces a first draft that follows YOUR format, grounded in YOUR data."

"Spec review. It compares the engineering spec against your acceptance criteria and flags gaps — missing edge cases, untested scenarios, ambiguous requirements — with specific questions."

Emery has stopped sketching. They're doing math in their head.

"The cross-referencing alone," they say. "That's half my time. Checking the spec against the PRD against the acceptance criteria against what customers actually said."

"And the agent does it in minutes because it can hold all those files in context simultaneously."

Declan, from his chair: "How good is it, actually? You're describing perfection."

Maven: "It's not perfect — it misses things, gets confused by ambiguity. But it shifts the job from 'synthesize six documents from scratch' to 'review and refine one summary.' That's different. Faster."

### Sources

1. **Derek DeHart: "Given MCPs to interact with Fireflies, Linear, Notion — it's become my hub for ongoing product research and development."** He synthesizes customer call transcripts, compiles evidence for/against hypotheses, and creates tickets. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

2. **Trist Adlington: "I talk to Claude more than anyone else" — using it for continuous PRD iteration, competitive analysis, and roadmap planning.** ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

3. **The Cowork product-management plugin connects to Figma, Amplitude, and Pendo** — pre-wired for the tools PMs already use, with skills for discovery, spec writing, and release planning. ([GitHub](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management))

4. **Ethan Mollick's BCG study: Consultants with AI completed 12.2% more tasks, 25.1% faster, at 40% higher quality — but were 19 percentage points WORSE on tasks outside AI's capability frontier.** The jagged frontier is real: you have to learn where the edges are. ([One Useful Thing](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged))

---

## Chapter 8: "Your dev team is about to move a lot faster."

<!-- COMIC
id: ch08-agentic-teams
characters: maven, emery, declan, clawd
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Maven has drawn a simple diagram on a whiteboard in the background: a flow chart showing "PM intent" → "Structured context" → "Agent" → "Code/Output" → "Review". Claw'd sits near the whiteboard, having contributed a small doodle. Emery and Declan are both now facing the whiteboard.

frame_a:
  action: Maven taps the "PM intent → Structured context" part of the diagram. Both Emery and Declan are looking at it. Declan has uncrossed his arms for the first time.
  expression_maven: serious, this is the key point
  expression_emery: focused, thinking about implications
  expression_declan: arms uncrossed, brow furrowed in thought
  dialogue: ["Your dev team is already using agents. The question is whether you're giving them what they need — or becoming the bottleneck.", ""]

frame_b:
  action: Declan speaks up for the first time in several chapters, not objecting but thinking through a real problem.
  expression_declan: engaged, working through an idea
  expression_maven: nodding, inviting him in
  dialogue: ["", "So if engineering is using agents to turn specs into code faster... and the specs are unclear... the agent just builds the wrong thing faster."]
-->

This chapter isn't about the PM using agents. It's about what happens when the engineering team does.

Andrej Karpathy coined "vibe coding" in February 2025 — developers describe intent and let AI write code. By late 2025, he updated it to "agentic engineering." At Anthropic, Claude Code writes 70-90% of code with human review. Their CPO said that for most products, "it's effectively 100 percent just Claude writing." Amodei clarified: "If Claude is writing 90% of the code, you still need just as many software engineers." The point isn't fewer people — it's faster intent-to-output.

If agents can turn a clear spec into a working feature in hours instead of days, the quality of the spec becomes the rate-limiting factor. Ambiguous requirements don't just slow down developers — they slow down agents who follow them literally.

"So if the agent builds from my spec," Declan says, "and the spec is vague... it doesn't push back like a developer would. It just builds the wrong thing, confidently and quickly."

"Yes," Maven says. "Your PRD, your acceptance criteria, your decision log — these are machine-readable now. Clear specs aren't just good practice. They're an input to a system."

This is the fourth primitive: **legibility.** Teams that adopt agents don't just go faster — they become hungry for intent. The throughput is there; the bottleneck moves upstream. PMs who express intent clearly, in structured repos with good context, become force multipliers.

The risk isn't that agents replace PMs. It's that a team running agents starves for clear direction — and unclear PMs become the constraint in a system that just got three times faster.

The skill isn't coding. It's clarity.

### Sources

1. **Andrej Karpathy coined "vibe coding" in February 2025 and updated it to "agentic engineering" by late 2025** — a terminology shift from novelty to professional default in under a year. ([Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding))

2. **At Anthropic, Claude Code writes 70-90% of code, with CPO Mike Krieger stating "for most products it's effectively 100 percent just Claude writing."** Amodei clarified: "if Claude is writing 90% of the code, you need just as many software engineers." ([Anthropic](https://www.anthropic.com/news/claude-opus-4-6))

3. **SemiAnalysis: "Claude Code is the Inflection Point" — documenting how agent-native development changes the role of everyone on the team, not just developers.** ([SemiAnalysis](https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point))

4. **Ethan Mollick: "As AI agents become capable of hours-long autonomous work, delegation skills become the differentiator."** Management — not prompting — is the AI superpower. ([X/Owen Gregorian](https://x.com/OwenGregorian/status/2016841301673820250))

---

## Chapter 9: "Okay — how do I actually start?"

<!-- COMIC
id: ch09-getting-started
characters: maven, emery, clawd
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: The office kitchen is quieter now. The box is empty on the table. Claw'd sits at the table's edge, notebook full of notes, pencil resting. Maven and Emery sit across from each other, tablets and laptops aside, talking directly. Declan's chair is empty — he left at some point. Warm, late-afternoon light.

frame_a:
  action: Emery has their tablet in hand, listing things on the screen. Maven sits back, relaxed, letting Emery lead. Claw'd watches them, attentive.
  expression_maven: relaxed, supportive
  expression_emery: determined, making a plan
  dialogue: ["", "Okay. Markdown. GitHub. A project folder with a CLAUDE.md. Start with the drudgery."]

frame_b:
  action: Claw'd hops closer to Emery on the table and holds up its notebook, showing a page with neat notes. Emery smiles at it.
  expression_emery: warm, looking at Claw'd
  expression_maven: pleased, watching the connection form
  dialogue: ["It gets better the more you invest in it. The context, the skills, the corrections — they compound.", ""]
-->

Declan's chair is empty — he slipped out somewhere around Chapter 7, unconverted but no longer arguing.

Emery has their tablet out, making a list.

"Here's what I'd actually tell you to do," Maven says.

**Learn markdown.** Most chat interfaces display everything as plain text — they don't render headings or links, so there's no reason to use them there. But markdown lets you convey the structure and intent of your formatting in a language agents actually understand. It's the native format of skill files, CLAUDE.md, project docs, and decision logs. markdowntutorial.com takes twenty minutes.

**Get on GitHub.** Not to code — to have a shared workspace that agents can also access. Think of it as Dropbox where every change is tracked and every collaborator (human or AI) can see the full history. Your decision logs, your specs, your research — put them in a repo.

**Build context into your repos.** Write a README for your project. Start a decision log. Add a CLAUDE.md with your preferences and conventions. This investment pays off twice: once for your human teammates, once for the agent.

**Experiment safely.** Pick a low-stakes task — a weekly status update, a competitive analysis, an FAQ draft. Try it with an agent. See where it succeeds and where it fails. AI is unpredictably good and unpredictably bad — you can't guess where the edges are. You have to discover them empirically.

**Audit your drudgery.** Which recurring tasks drain you? The ones that are structured, repetitive, and information-heavy are your first candidates. Not the creative strategy work — the synthesis, formatting, and cross-referencing that consumes your Tuesday afternoons.

"Does it really get better over time?"

Maven: "Every correction, every skill, every piece of context compounds. In a month the agent is better — not because the model changed, but because you did. That's the real unlock."

### Sources

1. **James Pember built "self-driving documentation" — an agent with browser access that explores software independently, identifies knowledge gaps, and creates documentation.** Autonomous, end-to-end, zero manual effort. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

2. **Gang Rui's slash command analyzes journal entries and git commits for the past 7 days, spots gaps between intentions and actions, and suggests system improvements — "like having a COO that learns from my patterns."** ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

3. **Claude Cowork, launched January 2026, brought Claude Code's agentic capabilities to non-developers via a desktop app — "Claude Code for the rest of your work."** Built in ~10 days using Claude Code itself. ([TechCrunch](https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/))

4. **Boris Cherny, Claude Code's creator: "An AI model like Claude is the horse, and a coding assistant like Claude Code is the harness."** Two critical factors: sufficient model capability AND adequate scaffolding. Both must be excellent simultaneously. ([OfficeChai](https://officechai.com/ai/claude-is-like-the-horse-and-claude-code-is-the-harness-anthropics-boris-cherny/))

---

## Epilogue

I wrote this story, with plenty of help from Claude, to get people thinking about the agentic moment that has rocked software development over the past year, and is now beginning to sweep through other knowledge work.

In some ways it is similar to the ChatGPT moment — in other ways it is much, much bigger. This story is a conversation starter and probably offers more questions and avenues to explore than it does answers.

But the goal is to make agents feel different, tangible, and like something you can understand and excel at — because I know you will.

_— [Geoff Dudgeon](https://x.com/geoffdudgeon) ([GitHub](https://github.com/dudgeon/agents-for-everyone)) + Claude_
