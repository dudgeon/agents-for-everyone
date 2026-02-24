# Agents for Everyone — Draft 005

_Package: `story/agent-unboxing`_ _Draft: 005_ _Date: 2026-02-24_ _Status: Self-reviewed — 7 GAP annotations inline; all draft-004 CriticMarkup feedback applied_

**Subtitle**: The agents are here — and they're not just for developers.

---

## Chapter 1: "You have to see what's in this box."

<!-- COMIC
id: ch01-the-box
characters: maven, declan
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Modern open-plan office kitchen/lounge. A communal table with laptops and coffee mugs. Warm pendant lights. Maven has just set a sleek white box on the table — labeled "Agents" in clean sans-serif type with a small printed illustration of Claw'd (a boxy terracotta creature) on the front panel. Declan sits across from Maven, coffee mug in hand.

frame_a:
  action: Maven holds the box up with both hands, presenting it to Declan. Her expression barely contains excitement. Declan leans back in his chair, arms loosely crossed, coffee mug resting on the table in front of him — unimpressed.
  expression_maven: excited, barely-contained energy
  expression_declan: unimpressed, bracing himself
  dialogue: ["The agents are here — and it's time to put them to work!", ""]

frame_b:
  action: Maven has set the box on the table, lid still closed. The Claw'd illustration is clearly visible on the front panel. Declan gestures dismissively with his coffee mug hand toward the box, not moving from his chair. Maven shifts to amused determination.
  expression_maven: determined, amused
  expression_declan: dry, eyebrow raised
  dialogue: ["", "If this is another AI demo, I'm going back to my Jira board."]
-->

The agents are here. That's how Maven puts it — not a prediction, not a hypothesis. A fact. She's spent the last year watching what happened to software development: Claude Code, Windsurf, Cursor rewriting company codebases overnight. That same shift, she says, is starting to move through knowledge work. Including product management.

Declan doesn't look up from his laptop. He's a PM, same as Maven, and he's sat through enough waves of "this changes everything" to have stopped counting. Early-2023 models that confidently hallucinated citations, statistics, and legal cases — one lawyer submitted six fabricated court cases to a federal judge because he trusted ChatGPT's research. AutoGPT, the autonomous agent that was going to run your errands forever, mostly burned through nights running in circles. Devin — launched with a demo showing it solving real engineering problems — quietly failed 85% of real-world tasks when researchers actually tested it.{>>GAP-01 (Devin specificity): The 15% number lands, but a vivid detail would sharpen it — Devin's showcase demo turned out to be on a pre-configured frozen repository, not a live codebase. One sentence of "the demo was staged" would make Declan's skepticism feel more earned than a percentage alone.<<}

"I don't code," Declan says. "I write PRDs. I wrangle stakeholders. I sit in meetings about meetings. Last quarter my team spent a sprint building from an AI-generated spec that seemed plausible but was completely wrong. If your magic agent needs a terminal, I'm not interested."

Maven doesn't argue. He's not uninformed — he needs to update his priors.

"Just — hold that thought for five minutes," she says. "Someone else is coming."

### Sources

1. **AutoGPT was the #1 GitHub repo of 2023 with 174,000+ stars — but users reported it getting stuck in infinite loops for entire nights.** The harness wasn't ready for the ambition. ([Tom's Hardware](https://www.tomshardware.com/news/autonomous-agents-new-big-thing), [Wikipedia](https://en.wikipedia.org/wiki/AutoGPT))

2. **Answer.AI tested Devin on 20 real-world tasks and found a 15% success rate — "we couldn't discern any pattern to predict which tasks would work."** The first "AI software engineer" struggled with basic reliability. ([Answer.AI](https://www.answer.ai/posts/2025-01-08-devin.html))

3. **A lawyer who trusted ChatGPT's legal research submitted six entirely fabricated cases to federal court, resulting in sanctions.** Mata v. Avianca became the cautionary tale for uncritical AI trust. ([CNN](https://www.cnn.com/2023/05/27/business/chat-gpt-avianca-mata-lawyers))

4. **"If someone tells you coding with LLMs is easy they are probably misleading you."** — Simon Willison, who has built 150+ tools with LLMs and still emphasizes intellectual honesty about their limitations. ([Willison](https://simonw.substack.com/p/i-think-agent-may-finally-have-a))

---

## Chapter 2: "I tried AI. It was fine."

<!-- COMIC
id: ch02-emery-enters
characters: maven, declan, emery
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office kitchen/lounge. The "Agents" box sits on the table, lid closed, Claw'd illustration visible on the front panel. Maven stands beside the table. Declan still seated with his coffee mug. Emery has just walked in — tablet tucked under one arm, stylus behind their right ear, open muted-teal cardigan over a heather-gray tee with a small lightning bolt logo on the left chest, dark chinos, clean white sneakers.

frame_a:
  action: Emery pulls out a chair and sits, placing their tablet flat on the table. Maven turns toward them with a warm welcoming gesture. Declan watches with mild interest, coffee mug in hand.
  expression_maven: welcoming, gesturing toward empty chair
  expression_emery: curious, glancing at the box on the table
  expression_declan: neutral, observing
  dialogue: ["How are you actually using AI in your work right now?", ""]

frame_b:
  action: Emery shrugs casually, one hand resting on their tablet. They're comfortable, not defensive. Declan has leaned slightly forward despite himself. Maven listens, waiting.
  expression_emery: self-aware, slightly amused
  expression_declan: leaning forward, interested despite himself
  expression_maven: attentive, listening
  dialogue: ["", "I mean, I use Gemini every day. It's basically replaced Google for me. But..."]
-->

Emery is a PM on the platform team. They use AI. It's fine.

Gemini, every day — as a search replacement, a writing helper, a brainstorming partner. A text file on their desktop, "prompts.txt," with their twenty most-used prompts organized by task. They tried building Gems — Google's version of a saved assistant — but they're annoying to update and hard to share. Made one, got excited, then couldn't figure out how to tweak it without rebuilding the whole thing. On a recent weekend, they tried Lovable to prototype a feature tracker. It almost worked. That was for fun. It didn't feel related to actual work.

"The thing is," Emery says, "it's all disconnected. I copy-paste context into a chat window every time. It doesn't know my project. It doesn't remember yesterday. Last week I pasted our PRD into Gemini for the third time and it still asked me what our target audience was. I'm sure I could be using it more — but honestly, it sometimes just feels like more work."

Maven nods. "That's exactly right — and you're not doing it wrong. What you've described is the ceiling of the chatbot paradigm."

"And I heard about coding agents — Claude Code, Windsurf, whatever. But I don't code. So I figured that was a developer thing."

Maven smiles. "That's exactly what we need to talk about."

### Sources

1. **Google Gems let users save custom instructions for Gemini — but they're siloed to individual accounts with no file access, no tool integrations, and no way to share them across a team.** The friction of updating and sharing Gems is exactly the limitation Emery is hitting. ([Google Blog](https://blog.google/products-and-products/products/gemini/google-gemini-update-august-2024/)){>>GAP-02 (Gems source tone): The source description is still architectural ("no file access, no tool integrations"). The story-ready version would echo Emery's voice — "can't share them, can't update them without rebuilding, knows nothing about your project." Consider revising to match Emery's frustration rather than a feature-comparison framing.<<}

2. **Teresa Torres broke her context into dozens of focused markdown files — at the end of each session she asks "Claude, what did you learn today that we should document?"** The key insight: pre-loading context into files eliminates the copy-paste burden entirely. ([ChatPRD](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management))

3. **Helen Lee Kupp voice-records ideas on stroller walks, drops transcripts into a folder, and Claude Code organizes them into research themes, articles, and LinkedIn posts.** The filesystem replaces the chat window as the primary interface. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

4. **ChatGPT Plugins, OpenAI's first attempt at giving AI access to external tools, never achieved product-market fit and were shut down in April 2024** — proving that tool use needs to be embedded in the architecture, not bolted on as an afterthought. ([OpenAI](https://openai.com/index/chatgpt-plugins/))

---

## Chapter 3: "So what's the difference between a chatbot and an agent?"

<!-- COMIC
id: ch03-the-unboxing
characters: maven, declan, emery, clawd
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office kitchen/lounge. The "Agents" box is fully open on the table, lid folded back. Claw'd — a small, boxy terracotta creature with dark square pixel-art eyes, a tiny leaf sprout on its head, and four stubby legs — sits beside the open box. Claw'd's leather-bound notebook is open, tiny pencil in hand, eyes looking up at the humans. Maven stands beside the box. Emery leans forward in their chair, tablet flat on table. Declan watches from across the table, coffee cup frozen halfway to his mouth.

frame_a:
  action: Maven gestures toward Claw'd sitting beside the open box — Claw'd's notebook is open to a fresh page, pencil raised. Emery stares with wide eyes. Declan has stopped mid-sip, coffee cup frozen in the air.
  expression_maven: proud, presenting
  expression_emery: delighted, eyes wide
  expression_declan: caught off guard, frozen mid-sip
  dialogue: ["That was a chatbot. This is an agent — and the difference matters.", ""]

frame_b:
  action: Claw'd has moved to the center of the table, notebook still open. Emery reaches a hand toward Claw'd instinctively, leaning in with curiosity. Maven gestures warmly. Declan watches Claw'd with skeptical attention.
  expression_maven: warm, gesturing at Claw'd
  expression_emery: reaching out, curious and delighted
  expression_declan: skeptical, but watching Claw'd intently
  dialogue: ["", "It has a notebook?"]
-->

"That was a chatbot," Maven says, as Claw'd settles on the table and opens its notebook. "This is an agent — and the difference matters."

A chatbot is a text box. You type a question, it types an answer. It doesn't know your files. It can't connect to your tools. It forgets things unpredictably — some sessions remember more than others, but you can't know what, and you can't control it.

An agent is different. It reads your project folder. It connects to your tools — Jira, Slack, Google Drive. It follows rules you write for it. And it doesn't just answer — it plans, tries something, checks if it worked, and adjusts. Like a junior teammate who actually listens.

"So there's the AI — the model itself," Declan says. "And then there's all the stuff around it. The files it reads, the tools it connects to, the rules it follows."

"That's the harness," Maven says. "The model is the engine. The harness is everything else — file access, instruction sets, tool connections. Claude Code and Windsurf are harnesses: they take a model and connect it to your codebase, your tools, your data. Without a harness, it's just a chat window."

"Like AutoGPT," Declan says. "Plan, try, check, adjust — that was the pitch. And it spent the whole night in an infinite loop."

"AutoGPT was the right idea two years early. The models weren't capable enough and the harness wasn't smart enough. It got stuck because it couldn't recognize failure. Models now recognize when they're stuck. The harness learned to checkpoint progress, compact context, and ask for help instead of looping. What AutoGPT attempted, today's agents do reliably."

Emery reaches out toward Claw'd. It tilts its head and opens to a fresh page.

### Sources

1. **Simon Willison defined an agent as "an LLM that runs tools in a loop to achieve a goal"** — and noted that agency requires more: the ability to act on the world, read files, call APIs, take consequential steps. The loop is the mechanism; the actions are the substance. ([Willison](https://simonw.substack.com/p/i-think-agent-may-finally-have-a))

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

setting: Same office area. Someone has pulled up a laptop screen showing a file explorer with folders: docs/, specs/, research/, decisions/ — each with a trailing slash visible in the path labels. A CLAUDE.md file is visible at the root level. Claw'd sits on the table next to the laptop, notebook open, actively scribbling. Maven points at the screen. Emery leans in close, their tablet propped beside the laptop. Declan stands slightly behind them, watching.

frame_a:
  action: Maven points at the CLAUDE.md file in the file explorer on the laptop screen. Claw'd flips through its notebook, mirroring the file browsing. Emery leans forward with both hands on the table, stylus still tucked behind their right ear, completely absorbed.
  expression_maven: explaining, pointing at screen
  expression_emery: leaning in, aha moment starting to dawn
  expression_declan: watching from behind, arms still crossed but standing closer
  dialogue: ["See this file? CLAUDE.md. The agent reads it every time you start a session — your project context, your preferences, your conventions.", ""]

frame_b:
  action: Emery looks down at their tablet (showing their own prompts.txt on the screen), then back at the laptop, making a connection. Emery pulls the stylus from behind their ear, ready to take a note.
  expression_emery: excited, lightbulb moment
  expression_maven: pleased, watching Emery make the connection
  dialogue: ["", "Wait — so my prompts.txt on the desktop... that could just BE the instruction file? And it would read it automatically?"]
-->

Emery's prompts.txt has twenty saved prompts. Every time they start a conversation with Gemini, they open the file, find the right prompt, copy it, paste it, then add whatever context is specific to today's task. It works. Barely.

"Here's what that looks like with an agent," Maven says. She opens a project folder on the laptop. Inside: docs/, specs/, research/, decisions/ — and at the root, a file called CLAUDE.md.

"This file is your prompts.txt — but permanent. The agent reads it automatically every time you start working. You put your project context here, your conventions, your preferences. 'When I ask for a PRD, use the template in the specs/ folder. Our users are developer teams at B2B software companies. Always check the research/ folder before answering questions about competitors.'"

Emery stares. "And it just... reads my files?"

"All of them — your specs, your meeting notes, your decision log. It searches the web and connects to other tools when you ask, but it starts with your project folder. It lives there. You don't paste anything."

This is the first primitive: **filesystem access**. The agent isn't trapped in a chat window — it operates in your project folder. It reads what's there, creates new files, updates existing ones. The difference between describing your kitchen over the phone and letting the chef walk in.

Teresa Torres, a product discovery coach, broke her entire workflow into small markdown files — one per topic, one per client, one per research theme. Instead of crafting elaborate prompts, she just works. The agent reads what it needs. She calls it "lazy prompting."

Declan, from behind them: "So it reads everything. Including the stuff that's wrong?"

Maven: "Yes. Which is why the files matter. Garbage context, garbage output. Investing in good project documentation pays off twice — once for your human teammates, once for the agent. Same investment, two payoffs."

### Sources

1. **Teresa Torres built her context into dozens of focused markdown files — at the end of each session she asks "Claude, what did you learn today that we should document?"** The context library grows as a side effect of working. ([ChatPRD](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management))

2. **CLAUDE.md files provide persistent project instructions loaded into every conversation — root, parent directories, home folder, child directories.** The `/init` command auto-generates one from your existing project. ([Claude Code Docs](https://code.claude.com/docs/en/overview))

3. **"Chat is describing your kitchen to a chef over the phone. Filesystem access is letting the chef into your kitchen."** Framing from Session 6 research on the non-SWE capability stack.

4. **Abhi Chandwani maintains verbose git commits specifically to create context for future agent workflows — the commit history becomes the agent's memory.** Good documentation practices compound. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

---

## Chapter 5: "You teach it how you work — and it remembers."

<!-- COMIC
id: ch05-rules-skills
characters: maven, emery, clawd
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Closer angle on the same table. Claw'd sits between Maven and Emery, notebook open to a page with a neat checklist. Maven has pulled up a text file on the laptop showing structured markdown — a skill definition with visible if/then conditional lines and a broader "think like" instruction below it. Emery has pulled the stylus from behind their right ear and is taking notes on their tablet. Declan is visible in the background, chair pushed back slightly, listening but not participating.

frame_a:
  action: Maven points at the if/then section of the skill file on screen. Claw'd looks up from its notebook, pencil poised mid-stroke. Emery sketches rapidly on their tablet, stylus moving.
  expression_maven: teaching, animated
  expression_emery: focused, taking notes
  dialogue: ["This is a skill file. You write it once — your format, your criteria, your workflow. Every time the agent does that task, it follows your rules.", ""]

frame_b:
  action: Emery looks up from their tablet, stylus hovering, connecting what Maven said to something they already do.
  expression_emery: excited, something clicking
  expression_maven: nodding, affirming
  dialogue: ["", "So it's like onboarding documentation... except the documentation actually gets read?"]
-->

Every PM has a way they do things. A format for PRDs, a launch checklist, a set of discovery interview questions. Usually it lives in their head or a Google Doc nobody reads — tribal knowledge that evaporates when someone changes teams.

"Skills," Maven says, opening a file on the laptop, "are how you teach the agent your way of working."

A skill file is structured text — markdown, not code — that describes a specific task: what inputs it needs, what steps to follow, what format to produce. They range from extremely specific to broad and conceptual. Specific end: *"If the user provides customer interview data, cite it inline. If the spec is missing acceptance criteria, flag it before proceeding."* Conceptual end: *"When reviewing a technical spec, think like a skeptical engineer who has seen requirements change at the last minute."* The same format handles both — precise checklists and general judgment.

"It's like onboarding a new hire," Emery says slowly, "except they actually retain what you told them."

"And you don't have to write skill files from scratch. Work a task with the agent, give feedback as you go, then ask: 'What did you learn today? Write it as a skill file.' The agent authors its own instructions from your corrections. After a working session, ask it to retro: what went well, what didn't, how should the skill change? The output is specific — not 'improve communication' but 'always check the research/ folder before making claims about competitors.'"

The investment compounds. And when you nail a skill, share it: drop the file in a shared repository{>>GAP-03 (repository undefined): "Repository" appears here before it's explained in Ch9 (where GitHub is introduced as "think of it as Dropbox"). For a non-developer reader in Ch5, "shared repository" is undefined jargon. Either add a brief parenthetical here ("a shared project folder online, more on this in Ch9") or restructure so Ch9 precedes this usage — or just say "shared project folder" here.<<} and your whole team has it. Someone else's expertise, running in your workflow.

This is the second primitive: **persistent instructions**. CLAUDE.md gives the agent project context. Skills give it task-specific expertise. The model is the same for everyone — the instructions make it behave like YOUR expert.

Declan, from the background: "So you're encoding your preferences in text files and hoping the AI follows them?"

Maven: "Not hoping. Testing. You run it, review the output, adjust the instructions. Same way you'd manage anyone."

### Sources

1. **Hilary Gridley reverse-engineered her implicit quality standards from before/after slide examples into a "Deck Doctor" skill — key prompt: "Be 100 times more specific."** This turns tacit expertise into explicit, scalable evaluation. ([ChatPRD](https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts))

2. **Lazar Jovanovic: "After solving a problem, ask the AI how to prompt it better next time, then add that guidance to your rules file."** A single rules file achieves compounding improvement across sessions. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code))

3. **Claire Vo built a meta-skill — a "skill that builds skills" — demonstrating that agent capabilities are composable, not flat.** One factory skill generates domain-specific skills consistently. ([ChatPRD](https://www.chatprd.ai/how-i-ai/claude-skills-explained))

4. **The Cowork legal plugin is ~200 lines of structured markdown — NDA triage against 13 criteria, contract review with clause-by-clause analysis.** It triggered a $285 billion stock selloff in the legal SaaS sector. The harness is markdown. ([Nate's Newsletter](https://natesnewsletter.substack.com/p/200-lines-of-markdown-just-triggered))

---

## Chapter 6: "It doesn't just answer — it does things."

<!-- COMIC
id: ch06-tools-actions
characters: maven, emery, clawd
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: The laptop screen now shows a terminal/command output with a list of completed actions: "Searched 4 databases... Updated Jira ticket... Created summary.md..." Claw'd sits near the laptop, its open notebook page completely filled with small checkmarks. Maven leans against the table, relaxed, arms at her sides. Emery is on the edge of their seat, leaning toward the screen. Declan is visible in the background, having moved his chair noticeably closer to the group.

frame_a:
  action: Maven gestures at the terminal output on the screen, palm open. Claw'd's notebook is full of checkmarks — it holds up the page briefly. Emery reads the output, mouth slightly open.
  expression_maven: matter-of-fact, letting the output speak
  expression_emery: impressed, reading the screen intently
  dialogue: ["It didn't tell me what to do. It did it. Searched the web, pulled the data, updated the ticket, wrote the summary.", ""]

frame_b:
  action: Emery turns away from the screen to look directly at Maven. Something has shifted in how they're thinking about this.
  expression_emery: recalibrating, serious
  expression_maven: steady, letting it land
  dialogue: ["", "That's... not what I thought this was."]
-->

Emery has used AI to draft emails, brainstorm feature names, and summarize meeting notes. In every case, the output was text. Suggestions. Ideas. Things they had to copy-paste into the actual tool and then do the work themselves.

"Watch this," Maven says. She types: *Analyze Q4 usage data, find the three features with the highest signup-to-week-2 drop-off, cross-reference our backlog, and draft priorities for planning.*

The agent reads the CSV files. It writes and runs an analysis script. It searches the backlog folder for related issues. It produces a markdown summary with three feature recommendations, each grounded in specific data points and linked to existing tickets.

"It didn't give me a suggestion," Maven says. "It did the work."

This is the third primitive: **tool use and actions**. Through MCP — think of it as USB ports for AI, letting you plug your existing tools in — agents connect to Jira, Slack, Google Drive, databases, web search, and APIs. The agent doesn't just generate text. It queries, updates, creates, and organizes. And for tools that don't yet have MCP connections, agents can use the command line{>>GAP-04 (command line jargon): "Command line" is undefined jargon for non-developers. A brief parenthetical would help: "the command line (text-based computer instructions, like the terminal on your Mac)." Or just cut this clause — the MCP story is the key point, and the browser-navigation capability is a bonus detail that might distract from the main message.<<} or operate a browser directly — navigating, clicking, extracting — without waiting for anyone to build an integration.

Reid Robinson, a PM at Zapier, connected his agent to HubSpot, Coda, and Fireflies via MCP. After every customer call, the agent reads the transcript, searches his CRM for the contact, enriches the record, and creates a follow-up task. A fifteen-minute manual workflow reduced to one step.

Declan, now noticeably closer: "And when it does something wrong? When it updates the wrong ticket?"

Maven: "You review before it acts. Most agents have approval gates — they show you what they're about to do and wait for a thumbs up. Same as reviewing a junior's PR. The agent's initiative, your oversight."

### Sources

1. **Reid Robinson (Zapier PM): Post-meeting transcript → agent searches CRM via MCP → enriches contact record → creates follow-up task.** A 15-minute manual workflow became one step. ([ChatPRD](https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep))

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

setting: The table now has multiple items spread across it — the laptop showing a discovery research summary on screen, Emery's tablet flat on the table with a rough workflow diagram sketched on it, printed pages of a feature spec. Claw'd moves between the items like a tiny project manager, notebook open. Maven and Emery are deep in conversation. Declan is in the background, chair turned toward them, listening with an expression more thoughtful than dismissive.

frame_a:
  action: Maven counts on her fingers as she lists use cases. Claw'd follows along, flipping to a new notebook page with each item. Emery's stylus moves quickly across their tablet, sketching a workflow diagram.
  expression_maven: animated, ticking off examples on her fingers
  expression_emery: engaged, sketching rapidly
  dialogue: ["Discovery synthesis. PRD drafting grounded in actual customer data. Spec review against acceptance criteria. Competitive analysis. Stakeholder updates. Release notes from commit history.", ""]

frame_b:
  action: Emery stops sketching and looks up, stylus frozen mid-stroke, connecting what Maven described to their own Tuesday afternoon.
  expression_emery: recognizing their own workflow, excited
  expression_maven: watching Emery connect the dots, patient
  dialogue: ["", "Half my week is synthesizing information that already exists in four different places. That's what this does?"]
-->

Emery's calendar is mostly synthesis. Customer notes into themes. Specs against acceptance criteria. Jira and Slack into a stakeholder update. Structured information taken from here, filtered through judgment, produced over there.

"Discovery," Maven says. "Your agent reads every call transcript in the calls/ folder, identifies recurring themes, and produces a summary with supporting quotes. Derek DeHart does this — his agent synthesizes evidence for and against product hypotheses across dozens of calls."

"PRD drafting. It pulls your product brief, your research, your existing PRD template from the skills/ folder, and produces a first draft that follows your format, grounded in your data."

"Spec review. It compares the engineering spec against your acceptance criteria and flags gaps — missing edge cases, untested scenarios, ambiguous requirements — with specific questions."

Emery has stopped sketching. They're doing math in their head.

"The cross-referencing alone," they say. "That's half my time. Checking the spec against the PRD against the acceptance criteria against what customers actually said."

"The agent does it in minutes because it can hold all of those files in context simultaneously. You can't. No human can keep six documents in their head at once."

Declan, from his chair: "How good is it, actually? You're describing perfection."

Maven: "It's not perfect. It misses things, gets confused by ambiguity, and sometimes confidently synthesizes what looks like a pattern but isn't. The job shifts from 'synthesize six documents from scratch' to 'review and refine one summary.' That's the improvement — not perfection, but a meaningful change in where you spend your time."

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

setting: Maven has drawn a diagram on a whiteboard: a horizontal flow "PM intent → Structured context → Agent → Code/Output → Review". Below it, a second line with an upward arrow: "Agent → PM intent (faster)". Claw'd sits near the whiteboard base, having contributed a small doodle. Emery and Declan are both facing the whiteboard from the table.

frame_a:
  action: Maven taps the left side of the diagram — "PM intent → Structured context" — with her finger. Both Emery and Declan look at the whiteboard. Declan's arms are uncrossed for the first time, hanging at his sides.
  expression_maven: serious, making the key point
  expression_emery: focused, thinking about implications
  expression_declan: arms uncrossed, brow furrowed in thought
  dialogue: ["Your dev team is already using agents. The question is whether you're giving them what they need — or becoming the bottleneck.", ""]

frame_b:
  action: Declan speaks up — not objecting, but working through a real problem. He leans forward, elbows on his knees. Maven nods, inviting him to continue.
  expression_declan: engaged, working through an idea
  expression_maven: nodding, inviting him in
  dialogue: ["", "So if engineering is using agents to turn specs into code faster... and the specs are unclear... the agent just builds the wrong thing faster."]
-->

Andrej Karpathy coined "vibe coding" in February 2025 — developers describe intent and let AI write code. By late 2025, he updated it to "agentic engineering." At Anthropic, Claude Code writes 70-90% of code with human review. Speed is the first effect.

The second effect is less obvious. If agents can turn a clear spec into a working feature in hours instead of days, the quality of the spec becomes the rate-limiting factor. Agents follow specs literally. They don't push back the way an experienced developer would. They don't check their interpretation against your unstated intent.

"So if the agent builds from my spec," Declan says, "and the spec is vague — it doesn't ask for clarification. It just goes."

"Yes. Your PRD, your acceptance criteria, your decision log — these are machine-readable inputs now. Clear specs aren't just good practice. They're an input to a system."

But here's what most PMs haven't heard yet: the same agents that accelerate engineering can accelerate intent production. A PM who used to spend Tuesday synthesizing four documents before writing a first PRD draft can now do it in an hour. Some teams have already flipped the script — PMs have stopped waiting on engineering to finish one sprint before starting the next. Engineering is now waiting on the PM.

"The bottleneck moves upstream," Declan says. "But you have tools to move faster at the new constraint."

Maven: "Exactly. The agents help both ends. Clear intent becomes a force multiplier. And now you can produce that intent faster than ever before."

Teams that adopt agents don't just go faster — they become hungry for clarity. PMs who can express intent clearly in structured repos with good context become force multipliers. PMs who can't become the constraint in a system that just got three times faster. The skill isn't coding. It's clarity.{>>GAP-05 (primitive label absent): This chapter no longer has a "fourth primitive: X" label (removed because it felt forced). But the throughput argument also makes the chapter feel like TWO points (quality-of-spec + speed-of-producing-specs) rather than one unified idea. Consider whether a unifying frame would help — something like: the real primitive here is "intent legibility," and the chapter is making two sides of the same argument (quality AND throughput). Or lean into it being two points and trust that both land. Current structure is actually clean — this is a soft gap, not a hard fix.<<}

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

setting: The office kitchen is quieter now. The white "Agents" box sits empty and open on the table, lid folded back, the Claw'd illustration visible on the inside of the lid. Claw'd sits at the table's edge, notebook full of notes from the entire conversation, tiny pencil resting on top. Maven and Emery sit across from each other, tablets and laptops set aside, talking directly. Declan's chair is empty — he left at some point. Warm late-afternoon light through the windows.

frame_a:
  action: Emery has their tablet in hand, finger moving across the screen as they make a list. Maven sits back in her chair, relaxed, letting Emery lead the conversation now. Claw'd watches them both, attentive.
  expression_maven: relaxed, supportive
  expression_emery: determined, making a plan
  dialogue: ["", "Okay. Markdown. GitHub. A project folder with a CLAUDE.md. Where do I actually start?"]

frame_b:
  action: Claw'd hops closer to Emery along the table and holds up its notebook — the page shows neat notes from the entire conversation, organized into five clear steps. Emery looks at Claw'd and smiles.
  expression_emery: warm, looking at Claw'd
  expression_maven: pleased, watching the connection form
  dialogue: ["It gets better the more you invest in it. The context, the skills, the corrections — they compound.", ""]
-->

Emery has their tablet out, ready to make a list.

"Here's what I'd actually tell you to do," Maven says.

**Learn markdown.** Agents can't interpret visual formatting — bold in a Word doc, color-coding in a spreadsheet, indentation in a Google Doc. They read text. Markdown is how you add structure to text in a format agents actually understand: # headers, **bold**, bullet lists, [links](https://example.com). It's not a programming language — it's closer to punctuation for meaning. The native format of skill files, CLAUDE.md, project docs, and decision logs. [markdowntutorial.com](https://www.markdowntutorial.com) takes twenty minutes.

**Get on GitHub.** Not to code — to have a shared workspace that agents can also access. Think of it as Dropbox where every change is tracked and every collaborator (human or AI) can see the full history. Your decision logs, your specs, your research — put them in a repository. The git operations — pushing, pulling, committing — are plain English: ask the agent in plain language and it handles them for you.

**Build context into your repos.** Write a README for your project. Start a decision log. Add a CLAUDE.md with your preferences and conventions. This investment pays off twice — for your human teammates and for the agent. If you're not sure where to start, ask the agent to help you write them.

**Experiment safely.** Pick a low-stakes task — a weekly status update, a competitive analysis, an FAQ draft. Try it with an agent. See where it succeeds and where it fails. AI is unpredictably good and unpredictably bad — you can't guess where the edges are. You have to discover them first-hand. The agent can help you identify which of your recurring tasks are good candidates.{>>GAP-06 (agent-can-help is vague here): Good that the note is here, but "can help you identify" is underspecified. How? Suggest a concrete framing: "Try asking the agent to review your last month's calendar or task list with you — it will surface the patterns you're too close to see." A specific prompt example would close the loop and model the behavior for the reader.<<}

**Audit your drudgery.** Which recurring tasks drain you? The ones that are structured, repetitive, and information-heavy are your first candidates. Not the creative strategy work — the synthesis, formatting, and cross-referencing that consumes your Tuesday afternoons.

"Does it really get better over time?"

Maven: "Every correction, every skill, every piece of context compounds. In a month the agent is better — not because the model changed, but because you gave it more context, helped it learn your processes, and codified them in rules and skills. That's the real unlock."{>>GAP-07 (model improvement undersold): The "not because the model changed" clause is technically accurate for the short term, but models DO keep improving (new Claude releases, GPT updates) and those improvements also flow through the same harness — compounding on top of the context you've built. A reader who knows Anthropic ships quarterly updates might push back. Consider acknowledging both: "The context compounds. And when the model improves — which it will — all of that context comes with it."<<}

### Sources

1. **James Pember built "self-driving documentation" — an agent with browser access that explores software independently, identifies knowledge gaps, and creates documentation.** Autonomous, end-to-end, zero manual effort. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

2. **Gang Rui's slash command analyzes journal entries and git commits for the past 7 days, spots gaps between intentions and actions, and suggests system improvements — "like having a COO that learns from my patterns."** ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

3. **Claude Cowork, launched January 2026, brought Claude Code's agentic capabilities to non-developers via a desktop app — "Claude Code for the rest of your work."** Built in ~10 days using Claude Code itself. ([TechCrunch](https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/))

4. **Boris Cherny, Claude Code's creator: "An AI model like Claude is the horse, and a coding assistant like Claude Code is the harness."** Two critical factors: sufficient model capability AND adequate scaffolding. Both must be excellent simultaneously. ([OfficeChai](https://officechai.com/ai/claude-is-like-the-horse-and-claude-code-is-the-harness-anthropics-boris-cherny/))

---

## Epilogue

I wrote this story, with plenty of help from Claude, to get people thinking about the agentic moment that has rocked software development over the past year, and is now beginning to sweep through other knowledge work like product management.

In some ways it is similar to the ChatGPT moment — in other ways it is much, much bigger. This story is a conversation starter and probably opens more questions and avenues to explore than it does answers.

But the goal is to make agents feel different, tangible, and like something you can understand and excel at — because I know you will.

_— [Geoff Dudgeon](https://x.com/geoffdudgeon) ([GitHub](https://github.com/dudgeon/agents-for-everyone)) + Claude_
