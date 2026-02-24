# Agents for Everyone — Draft 003

_Package: `story/agent-unboxing`_ _Draft: 003_ _Date: 2026-02-23_ _Status: First draft of new story package_

---

## Chapter 1: "{~~You have to see what's in this box~>Agents are here!~~}{--.--}"

<!-- COMIC id: ch01-the-box characters: maven, declan, clawd aspect: 16:9 render: carousel-mobile, side-by-side-desktop

setting:{== Modern open-plan office kitchen/lounge area. A communal table with laptops and coffee mugs. Warm overhead pendant lights. A large cardboard box sits on the table, lid slightly ajar, with a faint warm glow coming from inside. Maven stands beside it, one hand on the box. Declan sits at the table across from her.==}{>>Declan should be sitting and maven should be walking in excitedly holding the box -- it says 'Agents' -- it is a slick, minimalist design -- like an apple product, with a small picture of Clawd on the top.<<}

frame_a: action: {==Maven stands beside the box, one hand resting on the lid, leaning forward with visible excitement. ==}{>>Maven should be holding it up initially, then sets it down in the second frame<<}Declan sits at the table, coffee in hand, leaning back in his chair with arms loosely crossed. expression_maven: excited, barely-contained energy expression_declan: unimpressed, bracing himself dialogue: ["{~~You need to stop what you're doing and look at this.~>The agents are here -- and it's time to put them to work!~~}", ""]

frame_b: action: Declan gestures dismissively with his coffee hand, not moving from his chair. Maven's hand tightens on the box lid, undeterred. expression_maven: determined, amused expression_declan: dry, eyebrow raised dialogue: ["", "If this is another AI demo, I'm going back to my Jira board."] -->

{==Maven has never been shy about new tools, but something about today is different. She walks into the office kitchen carrying a cardboard box, sets it on the communal table with a deliberate thunk. Declan is across the table, barely glancing up from his laptop.==}{>>Please stop directly referencing the box. This is not about the box. You should not use the word box.<<}{>>find some other introduction. it should be an optimistic statement that agents are here and they're poised to revolutionize knowledge work -- including product management; an earnest (but accurate) optimistic declaration -- that slams into the wall of declan's pessimism.<<}

{=="Coding agents," she says. "But not for coding."==}{>>Please stop directly referencing the box. This is not about the box. You should not use the word box.<<}{>>find some other introduction. it should be an optimistic statement that agents are here and they're poised to revolutionize knowledge work -- including product management; an earnest (but accurate) optimistic declaration -- that slams into the wall of declan's pessimism.<<}

Declan doesn't look up. He's a product manager, same as Maven, and he's sat through enough waves of "this changes everything" to have stopped counting. ChatGPT Enterprise in 2023. AutoGPT eating a whole weekend to infinite loops. Devin — the "first AI software engineer" — that quietly failed 85% of real-world tests.

"I don't code," he says. "I write PRDs. I wrangle stakeholders. I sit in meetings about meetings. Last quarter my team spent a sprint building from an AI-generated spec that {~~was~>seemed~~} plausible {~~and~>but was~~} completely wrong. If your magic {~~box~>agent~~} needs a terminal, I'm not interested."

Maven doesn't argue. He's not uninformed — he's informed and burned.

"Just — hold that thought for five minutes," she says. "Someone else is coming."

### Sources

1. **AutoGPT was the #1 GitHub repo of 2023 with 174,000+ stars — but users reported it getting stuck in infinite loops for entire nights.** AutoGPT and BabyAGI pioneered autonomous agents but proved the harness wasn't ready. ([Tom's Hardware](https://www.tomshardware.com/news/autonomous-agents-new-big-thing), [Wikipedia](https://en.wikipedia.org/wiki/AutoGPT))

2. **Answer.AI tested Devin on 20 real-world tasks and found a 15% success rate — "we couldn't discern any pattern to predict which tasks would work."** The first "AI software engineer" struggled with basic reliability. ([Answer.AI](https://www.answer.ai/posts/2025-01-08-devin.html))

3. **A lawyer who trusted ChatGPT's legal research submitted six entirely fabricated cases to federal court, resulting in sanctions.** Mata v. Avianca became the cautionary tale for uncritical AI trust. ([CNN](https://www.cnn.com/2023/05/27/business/chat-gpt-avianca-mata-lawyers))

4. **"If someone tells you coding with LLMs is easy they are probably misleading you."** — Simon Willison, who has built 150+ tools with LLMs and still emphasizes intellectual honesty about their limitations. ([Willison](https://simonw.substack.com/p/i-think-agent-may-finally-have-a))

---

## Chapter 2: "I tried AI{--.--}{++;++}{-- I--}t was fine.{++ But it didn't change my work.++}"

<!-- COMIC id: ch02-emery-enters characters: maven, declan, emery aspect: 16:9 render: carousel-mobile, side-by-side-desktop

setting: Same office kitchen/lounge. The box still sits on the table{--, lid ajar with a faint glow--}. Maven stands beside it. Declan still seated. Emery has just walked in, tablet tucked under one arm, stylus behind their ear, teal cardigan over a gray tee.

frame_a: action: Emery pulls out a chair and sits down, placing their tablet on the table. They glance at the box curiously. Maven turns to greet them warmly. Declan watches with mild interest. expression_maven: welcoming, gesturing Emery in expression_emery: curious, glancing at the box expression_declan: neutral, observing dialogue: ["Perfect timing. {~~Tell him how you use AI.~>How are you using AI in your work today?~~}", ""]

frame_b: action: Emery shrugs casually, one hand on their tablet. They're comfortable, not defensive. expression_emery: self-aware, slightly amused expression_declan: leaning forward slightly, interested despite himself dialogue: ["", "I mean, I use Gemini? Like, every day. It's basically replaced Google for me."] -->

Emery is a PM on the platform team. They use AI. It's fine.

They describe their current setup: Gemini for quick questions instead of search. A writing assistant for first drafts of customer-facing docs. A text file on their desktop — "prompts.txt" — with their twenty most-used prompts, organized by task. On a recent weekend, they tried Lovable to prototype a feature tracker app. It almost worked.{++ But that was for fun -- it didn't seem related to their work.++}

"The thing is," Emery says, "it's all disconnected. I copy-paste context into a chat window every time. It doesn't know my project. It doesn't remember yesterday. Last week I pasted our PRD into Gemini for the third time and it still asked me what our target audience was."

Maven nods. "That's exactly right."

"And I heard about coding agents — Claude Code, {~~Cursor~>Windsurf~~}, whatever. But I don't code. So I figured that's a developer thing."

{--Maven's hand drifts back to the box on the table.--}

{--"That," she says, "is what's in the box."--}

### Sources

1. **Google Gems let users save custom instructions for Gemini — personal productivity tools embedded in the Google ecosystem.** Unlike GPTs, Gems are practical but siloed: no file access, no tool integrations, no persistence beyond the instruction set. ([Google Blog](https://blog.google/products-and-products/products/gemini/google-gemini-update-august-2024/))

2. **Teresa Torres broke her context into dozens of tiny focused markdown files so simple prompts produce rich output — she calls it "lazy prompting."** The key insight: pre-loading context into files eliminates the copy-paste burden of chat interfaces. ([ChatPRD](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management))

3. **Helen Lee Kupp voice-records ideas on stroller walks, drops transcripts into a folder, and Claude Code organizes them into research themes, articles, and LinkedIn posts.** The filesystem replaces the chat window as the primary interface. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

4. **ChatGPT Plugins, OpenAI's first attempt at giving AI access to external tools, never achieved product-market fit and were shut down in April 2024** — proving that tool use needs to be embedded, not bolted on. ([OpenAI](https://openai.com/index/chatgpt-plugins/))

---

## Chapter 3: "So what's the difference between a chatbot and an agent?"

<!-- COMIC id: ch03-the-unboxing characters: maven, declan, emery, clawd aspect: 16:9 render: carousel-mobile, side-by-side-desktop

setting: Same office kitchen/lounge. Maven has her hands on the box lid. Emery leans forward in their chair. Declan watches from across the table. The warm glow from inside the box is brighter now.

frame_a: action: Maven lifts the box lid. Warm light spills out. Claw'd is visible inside — a small boxy terracotta creature with dark square eyes, a leaf sprout on its head, and a tiny notebook. Emery's eyes go wide. Declan's coffee cup freezes halfway to his mouth. expression_maven: proud, presenting expression_emery: delighted, eyes wide expression_declan: caught off guard, frozen mid-sip dialogue: ["A chatbot answers questions in a window. An agent operates in your world.", ""]

frame_b: action: Claw'd has climbed out of the box and sits on the table, notebook open, tiny pencil in hand, looking up at the three humans. Emery reaches a hand toward it instinctively. Maven gestures at Claw'd. expression_maven: warm, gesturing at Claw'd expression_emery: reaching out, curious expression_declan: skeptical but looking at Claw'd dialogue: ["", "It has a notebook?"] -->

{--Maven lifts the lid. Something small and warm-colored climbs out onto the table, notebook open.--}{>>Something more like -- "that was a chatbot -- this is an agent. and you're going to love working with agents"<<}

"A chatbot," Maven says, "is a text box. You type a question, it types an answer. It doesn't know your files, it can't use your tools, {==and it forgets everything the moment you close the tab.==}{>>some chatbots remember som things, but it's hard to know what and impossible to control<<}"

"An agent is different. It reads your project folder. It connects to your tools — Jira, Slack, Google Drive. It follows rules you write for it. And it doesn't just answer — it plans, tries something, checks if it worked, and adjusts. Like a junior teammate who actually listens."

Emery gets it immediately. "So instead of pasting my PRD into a chat window..."

"The agent reads your PRD directly. It reads your CLAUDE.md — a persistent instruction file that tells it who you are, what your project is, how you like things done. Your whole repo is its context."

Declan sets down his coffee. "Plan, try, check, adjust. That's what AutoGPT promised. It got stuck in loops."

"AutoGPT was the right idea two years early," Maven says. "The models weren't good enough and the harness wasn't smart enough. Models learned to recognize when they were stuck. The harness learned to checkpoint progress, compact context, and ask for help instead of looping."

### Sources

1. **Simon Willison defined an agent as "an LLM that runs tools in a loop to achieve a goal"** — {==the simplest, most precise definition in the industry==}{>>I think this is an incomplete definition; loops are one aspect; but agency requires the ability to act; are there quotes that include this?<<}. ([Willison](https://simonw.substack.com/p/i-think-agent-may-finally-have-a))

2. **Claude Code launched in February 2025 as a terminal-based agent that could search code, edit files, run tests, commit to GitHub, and execute CLI tools** — the moment the agent left the browser and entered the file system. ([Anthropic](https://www.anthropic.com/news/claude-3-7-sonnet))

3. **@mernit (Openclaw): "The architecture of an AI agent can be reduced to two components: the filesystem as state, and Claude as the orchestrator."** When you connect Gmail, the emails become files. The filesystem IS the state. ([X](https://x.com/mernit/status/2021324284875153544))

4. **By February 2026, Claude Code authored 4% of all public GitHub commits (~135,000/day), projected to reach 20%+ by year-end.** The agent didn't stay in the lab. ([Anthropic](https://www.anthropic.com/news/claude-opus-4-6))

---

## Chapter 4: "It works with your actual files — not a chat window."

<!-- COMIC id: ch04-files-context characters: maven, emery, declan, clawd aspect: 16:9 render: carousel-mobile, side-by-side-desktop

setting: Same office area, but now someone has pulled up a laptop screen showing a file explorer with folders: /docs, /specs, /research, /decisions. Claw'd sits on the table next to the laptop, notebook open, actively scribbling. Maven points at the screen. Emery leans in with their tablet propped beside the laptop.

frame_a: action: Maven points at the folder structure on the laptop screen. Claw'd is flipping through its notebook, mirroring the file browsing. Emery leans forward, tablet forgotten. expression_maven: explaining, pointing at screen expression_emery: leaning in, aha moment dawning expression_declan: watching from behind, arms still crossed but closer to the group dialogue: ["See this file? CLAUDE.md. The agent reads it every time you start a session. Your project context, your preferences, your conventions — all in one place.", ""]

frame_b: action: Emery looks down at their tablet, then back at the screen, making a connection. expression_emery: excited, the lightbulb moment expression_maven: pleased, watching Emery get it dialogue: ["", "Wait — so my prompts.txt on the desktop... that could just BE the instruction file? And it would read it automatically?"] -->

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

## {==Chapter 5: "You teach it how you work — and it remembers."==}{>>I want you to add a couple concepts to this section:

1- you can write skills and rules by hand -- or you can do it interactively like if you were teaching someone

2- agents are _really_ good at introspection;  if you ask them to retro based on the feedback you gave during a session, they will precisely identify ways to improve

3- retention; once you upgrade a skill, you can count on the agent following the new procedures

4- diffusion; once you nail a rule or skill you can easily share it across your team -- or discover skills others have created<<}

<!-- COMIC id: ch05-rules-skills characters: maven, emery, clawd aspect: 16:9 render: carousel-mobile, side-by-side-desktop

setting: Closer angle on the table. Claw'd is sitting between Maven and Emery, notebook open to a page with a neat checklist. Maven has pulled up a text file on the laptop showing structured markdown — a skill definition. Emery is taking notes on their tablet with the stylus from behind their ear. Declan is visible in the background, chair pushed back slightly, listening but not participating.

frame_a: action: Maven points at a section of the skill file on screen. Claw'd looks up attentively, pencil poised. Emery has pulled the stylus from behind their ear and is sketching on their tablet. expression_maven: teaching, animated expression_emery: focused, taking notes dialogue: ["This is a skill file. It tells the agent exactly how to do a specific task — your format, your criteria, your workflow. Write it once, use it forever.", ""]

frame_b: action: Emery looks up from their tablet, connecting dots. expression_emery: excited, something clicking expression_maven: nodding, affirming dialogue: ["", "So it's like onboarding documentation... but the documentation actually gets read?"] -->

Every PM has a way they do things. Format for PRDs, launch checklists, interview questions. Usually it lives in their head or a Google Doc nobody reads — tribal knowledge that evaporates when someone changes teams.

"Skills," Maven says, opening a file on the laptop, "are how you teach the agent your way of working."

A skill file is structured text — markdown, not code — that describes a specific task: what inputs it needs, what steps to follow, what format to produce. Write one skill file for "draft a PRD," and every time the agent does that task, it follows your format, your conventions, your quality bar.

"It's like onboarding a new hire," Emery says slowly, "except they actually retain what you told them."

"Exactly. And it compounds. You correct the agent — say, the way you prefer acceptance criteria written — and update the skill file. Next time, it gets it right without being told."

This is the second primitive: **persistent instructions**. CLAUDE.md gives the agent project context. Skills give it task-specific expertise. Before: you tell Gemini "write a PRD" and get generic output. After: the agent reads your PRD skill, follows your format, checks against your acceptance criteria template, and grounds claims in data from the /research folder. The model is the same for everyone — the instructions make it behave like YOUR expert.

{--Hilary Gridley, a product exec at WHOOP, took this further. She reverse-engineered her own judgment by feeding before/after examples of her slide feedback to a custom GPT, then told it "be 100 times more specific." The result was a "Deck Doctor" that evaluates presentations using HER standards — consistently, at scale, without her reviewing every deck.--}

Declan, from the background: "So you're encoding your preferences in text files and hoping the AI follows them?"

Maven: "Not hoping. Testing. You run it, review the output, adjust the instructions. Same way you'd manage anyone."

### Sources

1. **Hilary Gridley reverse-engineered her implicit quality standards from before/after slide examples into a "Deck Doctor" GPT — key prompt: "Be 100 times more specific."** This turns tacit expertise into explicit, scalable evaluation. ([ChatPRD](https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts))

2. **Lazar Jovanovic: "After solving a problem, ask the AI how to prompt it better next time, then add that guidance to your rules file."** A single rules file achieves compounding improvement across sessions. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code))

3. **Claire Vo built a meta-skill — a "skill that builds skills" — demonstrating that agent capabilities are composable, not flat.** One factory skill generates domain-specific skills consistently. ([ChatPRD](https://www.chatprd.ai/how-i-ai/claude-skills-explained))

4. **The Cowork legal plugin is ~200 lines of structured markdown — NDA triage against 13 criteria, contract review with clause-by-clause analysis.** It triggered a $285 billion stock selloff. The harness is markdown. ([Nate's Newsletter](https://natesnewsletter.substack.com/p/200-lines-of-markdown-just-triggered))

---

## Chapter 6: "It doesn't just answer — it does things."

<!-- COMIC id: ch06-tools-actions characters: maven, emery, clawd aspect: 16:9 render: carousel-mobile, side-by-side-desktop

setting: The laptop screen now shows a terminal/command output with a list of completed actions: "Searched 4 databases... Updated Jira ticket... Created summary.md..." Claw'd is sitting near the laptop, notebook filled with checkmarks. Maven leans against the table. Emery is on the edge of their seat. Declan is visible in background, having moved his chair slightly closer.

frame_a: action: Maven gestures at the terminal output. Claw'd's notebook page is full of completed checkmarks. Emery reads the output, mouth slightly open. expression_maven: matter-of-fact, letting the output speak expression_emery: impressed, reading the screen dialogue: ["It didn't just tell me what to do. It did it. Searched the web, pulled the data, updated the ticket, wrote the summary.", ""]

frame_b: action: Emery turns to look at Maven directly, something shifting in how they think about this. expression_emery: recalibrating, serious expression_maven: steady, waiting for it to land dialogue: ["", "That's... not what I thought this was."] -->

Emery has used AI to draft emails, brainstorm feature names, and summarize meeting notes. In every case, the output was text. Suggestions. Ideas. Things they had to copy-paste into the actual tool and then do the work themselves.

"Watch this," Maven says. She types: *Analyze Q4 usage data, find the three features with the highest signup-to-week-2 drop-off, cross-reference our backlog, and draft priorities for planning.*

The agent reads the CSV files. It writes and runs an analysis script. It searches the backlog folder for related issues. It produces a markdown summary with three feature recommendations, each grounded in specific data points and linked to existing tickets.

"It didn't give me a suggestion," Maven says. "It did the work."

{==This is the third primitive: **tool use and actions.** Through MCP — think of it as USB ports for AI, letting you plug your existing tools in — agents connect to Jira, Slack, Google Drive, databases, web search, APIs. The agent doesn't just generate text. It queries, updates, creates, and organizes.==}{>>even for tools that don't have MCP servers (yet!), agents can use CLI (so you don't have to) or operate browsers to execute a wide variety of tasks<<}

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

<!-- COMIC id: ch07-pm-lifecycle characters: maven, emery, clawd aspect: 16:9 render: carousel-mobile, side-by-side-desktop

setting: The table now has multiple items spread across it — the laptop, Emery's tablet with sketches, printouts of a feature spec. Claw'd is walking between items like a tiny project manager, notebook open. Maven and Emery are deep in conversation. Declan is in the background, chair turned toward them, listening with an expression that's more thoughtful than dismissive.

frame_a: action: Maven counts on her fingers as she lists use cases. Claw'd follows along, flipping notebook pages. Emery's tablet shows what looks like a rough workflow diagram they've been sketching. expression_maven: animated, ticking off examples expression_emery: engaged, sketching on tablet dialogue: ["Discovery research synthesis. PRD drafting grounded in customer data. Spec review against acceptance criteria. Competitive analysis. Stakeholder updates. Release notes from commit history.", ""]

frame_b: action: Emery stops sketching and looks up, stylus in hand, connecting it to their own work. expression_emery: recognizing their own workflow, excited expression_maven: watching Emery connect the dots dialogue: ["", "Half my week is synthesizing information that already exists in four different places. That's what this does?"] -->

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

<!-- COMIC id: ch08-agentic-teams characters: maven, emery, declan, clawd aspect: 16:9 render: carousel-mobile, side-by-side-desktop

{==setting: Maven has drawn a simple diagram on a whiteboard in the background: a flow chart showing "PM intent" → "Structured context" → "Agent" → "Code/Output" → "Review". Claw'd sits near the whiteboard, having contributed a small doodle. Emery and Declan are both now facing the whiteboard.==}{>>a big take away should be that dev teams will accelerate and become starved for intent -- so not only do agents represent an opportunity, failing to adopt them can be a big risk for organizations; we don't want to fear monger -- but this should be a take-away<<}

{==frame_a: action: Maven taps the "PM intent → Structured context" part of the diagram. Both Emery and Declan are looking at it. Declan has uncrossed his arms for the first time. expression_maven: serious, this is the key point expression_emery: focused, thinking about implications expression_declan: arms uncrossed, brow furrowed in thought dialogue: ["Your dev team is already using agents. The question is whether you're giving them what they need — or becoming the bottleneck.", ""]==}{>>a big take away should be that dev teams will accelerate and become starved for intent -- so not only do agents represent an opportunity, failing to adopt them can be a big risk for organizations; we don't want to fear monger -- but this should be a take-away<<}

{==frame_b: action: Declan speaks up for the first time in several chapters, not objecting but thinking through a real problem. expression_declan: engaged, working through an idea expression_maven: nodding, inviting him in dialogue: ["", "So if engineering is using agents to turn specs into code faster... and the specs are unclear... the agent just builds the wrong thing faster."] -->==}{>>a big take away should be that dev teams will accelerate and become starved for intent -- so not only do agents represent an opportunity, failing to adopt them can be a big risk for organizations; we don't want to fear monger -- but this should be a take-away<<}

{==This chapter isn't about the PM using agents. It's about the PM's team using agents — and what that means for how PMs work.==}{>>a big take away should be that dev teams will accelerate and become starved for intent -- so not only do agents represent an opportunity, failing to adopt them can be a big risk for organizations; we don't want to fear monger -- but this should be a take-away<<}

{==Andrej Karpathy coined "vibe coding" in February 2025 — developers describe intent and let AI write code. By late 2025, he updated it to "agentic engineering." At Anthropic, Claude Code writes 70-90% of code with human review. Their CPO said that for most products, "it's effectively 100 percent just Claude writing." Amodei clarified: "If Claude is writing 90% of the code, you still need just as many software engineers." The point isn't fewer people — it's faster intent-to-output.==}{>>a big take away should be that dev teams will accelerate and become starved for intent -- so not only do agents represent an opportunity, failing to adopt them can be a big risk for organizations; we don't want to fear monger -- but this should be a take-away<<}

{==If agents can turn a clear spec into a working feature in hours instead of days, the quality of the spec becomes the rate-limiting factor. Ambiguous requirements don't just slow down developers — they slow down agents who follow them literally.==}{>>a big take away should be that dev teams will accelerate and become starved for intent -- so not only do agents represent an opportunity, failing to adopt them can be a big risk for organizations; we don't want to fear monger -- but this should be a take-away<<}

{=="So if the agent builds from my spec," Declan says, "and the spec is vague... it doesn't push back like a developer would. It just builds the wrong thing, confidently and quickly."==}{>>a big take away should be that dev teams will accelerate and become starved for intent -- so not only do agents represent an opportunity, failing to adopt them can be a big risk for organizations; we don't want to fear monger -- but this should be a take-away<<}

{=="Yes," Maven says. "Your PRD, your acceptance criteria, your decision log — these are machine-readable now. Clear specs aren't just good practice. They're an input to a system."==}{>>a big take away should be that dev teams will accelerate and become starved for intent -- so not only do agents represent an opportunity, failing to adopt them can be a big risk for organizations; we don't want to fear monger -- but this should be a take-away<<}

{==This is the fourth primitive: **legibility.** PMs who express intent clearly — in markdown, in structured repos, with good context — become force multipliers. PMs who write ambiguous requirements in unstructured wikis become the bottleneck in an increasingly fast pipeline.==}{>>a big take away should be that dev teams will accelerate and become starved for intent -- so not only do agents represent an opportunity, failing to adopt them can be a big risk for organizations; we don't want to fear monger -- but this should be a take-away<<}

{==The skill isn't coding. It's clarity.==}{>>a big take away should be that dev teams will accelerate and become starved for intent -- so not only do agents represent an opportunity, failing to adopt them can be a big risk for organizations; we don't want to fear monger -- but this should be a take-away<<}

### Sources

1. **Andrej Karpathy coined "vibe coding" in February 2025 and updated it to "agentic engineering" by late 2025** — a terminology shift from novelty to professional default in under a year. ([Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding))

2. **At Anthropic, Claude Code writes 70-90% of code, with CPO Mike Krieger stating "for most products it's effectively 100 percent just Claude writing."** Amodei clarified: "if Claude is writing 90% of the code, you need just as many software engineers." ([Anthropic](https://www.anthropic.com/news/claude-opus-4-6))

3. **SemiAnalysis: "Claude Code is the Inflection Point" — documenting how agent-native development changes the role of everyone on the team, not just developers.** ([SemiAnalysis](https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point))

4. **Ethan Mollick: "As AI agents become capable of hours-long autonomous work, delegation skills become the differentiator."** Management — not prompting — is the AI superpower. ([X/Owen Gregorian](https://x.com/OwenGregorian/status/2016841301673820250))

---

## Chapter 9: "Okay — how do I actually start?"

<!-- COMIC id: ch09-getting-started characters: maven, emery, clawd aspect: 16:9 render: carousel-mobile, side-by-side-desktop

setting: The office kitchen is quieter now. The box is empty on the table. Claw'd sits at the table's edge, notebook full of notes, pencil resting. Maven and Emery sit across from each other, tablets and laptops aside, talking directly. Declan's chair is empty — he left at some point. Warm, late-afternoon light.

frame_a: action: Emery has their tablet in hand, listing things on the screen. Maven sits back, relaxed, letting Emery lead. Claw'd watches them, attentive. expression_maven: relaxed, supportive expression_emery: determined, making a plan dialogue: ["", "Okay. Markdown. GitHub. A project folder with a CLAUDE.md. Start with the drudgery."]

frame_b: action: Claw'd hops closer to Emery on the table and holds up its notebook, showing a page with neat notes. Emery smiles at it. expression_emery: warm, looking at Claw'd expression_maven: pleased, watching the connection form dialogue: ["It gets better the more you invest in it. The context, the skills, the corrections — they compound.", ""] -->

The box is empty. Declan's chair is empty too — he left quietly somewhere around Chapter 7. Not converted, but no longer arguing.

Emery has their tablet out, making a list.

"Here's what I'd actually tell you to do," Maven says.

{==**Learn markdown.** It's formatting, not programming. Bold, headers, bullet points, links — you probably use most of it already in Slack. Markdown is how agents read and write. It's the native language of project files, skills, and documentation. markdowntutorial.com takes twenty minutes.==}{>>you've probably noticed that most chatbots seem like they don't accept rich text like headings and links -- but markdown let's you convey the context of formatting in a language agents understand<<}{>>add a link to a canonical markdown reference<<}

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

## Self-Review Summary

This draft introduces the new story package — three characters, the unboxing metaphor, PM-focused examples. The arc follows the seed closely: 10% setup (Ch 1), 20% Emery's current state (Ch 2-3), 60% primitives (Ch 4-8), 10% on-ramp (Ch 9).

**What's working:** - Three-character dynamic feels natural. Emery as audience surrogate works — their questions ARE the reader's questions. - The unboxing metaphor gives the story a physical anchor. Claw'd on the table is visual and memorable. - Declan fading out (present but increasingly silent) feels more realistic than a conversion arc. - COMIC specs include all four characters with distinct expressions and actions.

**Gaps from self-review (all 9 addressed in revision pass):** - GAP-01: Added specific bad experience (AI-generated spec that was plausible and wrong) - GAP-02: Added vivid copy-paste example (pasted PRD three times, still asked about audience) - GAP-03: Named specific harness innovations (checkpoints, context compaction, asking for help) - GAP-04: Kept Torres — still the best example; removed GAP marker - GAP-05: Added before/after for PRD drafting inline - GAP-06: Added USB analogy for MCP - GAP-07: Varied verb structure across PM tasks (reads, pulls, compares) - GAP-08: Added Amodei clarification ("still need just as many software engineers")

---

## Epilogue

{~~Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.~>~~}

{~~Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.~>~~}

{~~At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.~>~~}I wrote this story, with plenty of help from Claude, to get people thinking about the agentic moment that has rocked software development over the past ~year, and is now beginning to sweep through other knowledge work. in some ways it is similar to the chatgpt moment -- in other ways it is much much bigger. this story is a conversation starter and probably offers more questions and avenues to explore than it does answers. but the goal is to make agents feel different, tangible, and like something you can understand and -- because I know you will.{++excel at++}

_— {==Geoff Dudgeon==}{++ (X, Github)++}{>>add links to twitter bio @geoffdudgeon, github link to this repo<<} + Claude_ - GAP-09:{== ==}Added markdowntutorial.com resource