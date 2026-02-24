export interface Source {
  idea: string;
  name: string;
  url: string;
}

export interface Panel {
  label: string;
  description: string;
  image?: string;
  gradient: "warm" | "cool" | "warm-accent" | "cool-accent";
  dialogue?: string;
}

export interface ChapterData {
  id: string;
  number: number;
  title: string;
  navLabel: string;
  panels: Panel[];
  body: string[];
  sources: Source[];
  variant?: "standard" | "epilogue";
  byline?: string;
}

export const chapters: ChapterData[] = [
  {
    id: "ch-1",
    number: 1,
    title: "\"Agents are here!\"",
    navLabel: "Agents Arrive",
    panels: [
      {
        label: "Maven presents the Agents box",
        description: "Maven holds up a sleek, minimalist white box labeled \"Agents\" — like a premium tech product with a small printed image of Claw'd on the front. Declan sits across, coffee in hand, leaning back and unimpressed.",
        image: "/images/ch01-the-box-frame-a-20260224-180641.png",
        gradient: "warm",
        dialogue: "The agents are here — and it's time to put them to work!",
      },
      {
        label: "Declan braces himself",
        description: "Maven has set the box on the table. Declan gestures dismissively with his coffee hand, not moving from his chair.",
        image: "/images/ch01-the-box-frame-b-20260224-180641.png",
        gradient: "warm",
        dialogue: "If this is another AI demo, I'm going back to my Jira board.",
      },
    ],
    body: [
      "The agents are here. That's how Maven puts it — not a prediction, not a hypothesis. A fact. She's been following what happened to software development over the past year: Claude Code, Windsurf, Cursor rewriting company codebases overnight. And now, she says, that same shift is starting to move through knowledge work. Including product management.",
      "Declan doesn't look up. He's a product manager, same as Maven, and he's sat through enough waves of \"this changes everything\" to have stopped counting. Early-2023 models that confidently hallucinated citations, statistics, and legal cases — one lawyer submitted six fabricated court cases to a federal judge because he trusted ChatGPT's research. AutoGPT, the autonomous agent that was going to run your errands forever, mostly burned through nights running in circles. Devin — launched with a demo showing it solving real engineering problems — quietly failed 85% of real-world tasks when researchers actually tested it.",
      "\"I don't code,\" he says. \"I write PRDs. I wrangle stakeholders. I sit in meetings about meetings. Last quarter my team spent a sprint building from an AI-generated spec that seemed plausible but was completely wrong. If your magic agent needs a terminal, I'm not interested.\"",
      "Maven doesn't argue. He's not uninformed — he needs to update his priors.",
      "\"Just — hold that thought for five minutes,\" she says. \"Someone else is coming.\"",
    ],
    sources: [
      {
        idea: "AutoGPT was the #1 GitHub repo of 2023 with 174,000+ stars — but users reported it getting stuck in infinite loops for entire nights.",
        name: "Tom's Hardware",
        url: "https://www.tomshardware.com/news/autonomous-agents-new-big-thing",
      },
      {
        idea: "Answer.AI tested Devin on 20 real-world tasks and found a 15% success rate — \"we couldn't discern any pattern to predict which tasks would work.\"",
        name: "Answer.AI",
        url: "https://www.answer.ai/posts/2025-01-08-devin.html",
      },
      {
        idea: "A lawyer who trusted ChatGPT's legal research submitted six entirely fabricated cases to federal court, resulting in sanctions.",
        name: "CNN",
        url: "https://www.cnn.com/2023/05/27/business/chat-gpt-avianca-mata-lawyers",
      },
      {
        idea: "\"If someone tells you coding with LLMs is easy they are probably misleading you.\"",
        name: "Simon Willison",
        url: "https://simonw.substack.com/p/i-think-agent-may-finally-have-a",
      },
    ],
  },
  {
    id: "ch-2",
    number: 2,
    title: "\"I tried AI; it was fine. But it didn't change my work.\"",
    navLabel: "Emery Enters",
    panels: [
      {
        label: "Emery joins the conversation",
        description: "Emery walks in with tablet tucked under arm, teal cardigan, sits down and glances at the box. Maven welcomes them warmly.",
        image: "/images/ch02-emery-enters-frame-a-20260224-180641.png",
        gradient: "cool",
        dialogue: "How are you using AI in your work today?",
      },
      {
        label: "Emery describes their setup",
        description: "Emery shrugs casually, one hand on their tablet, comfortable and self-aware.",
        image: "/images/ch02-emery-enters-frame-b-20260224-180641.png",
        gradient: "cool",
        dialogue: "I mean, I use Gemini? Like, every day. It's basically replaced Google for me.",
      },
    ],
    body: [
      "Emery is a PM on the platform team. They use AI. It's fine.",
      "Gemini, every day — as a search replacement, a writing helper, a brainstorming partner. A text file on their desktop, \"prompts.txt,\" with their twenty most-used prompts organized by task. They tried building Gems — Google's version of a saved assistant — but they're annoying to update and hard to share. Made one, got excited, then couldn't figure out how to tweak it without rebuilding the whole thing. On a recent weekend, they tried Lovable to prototype a feature tracker. It almost worked. That was for fun. It didn't feel related to actual work.",
      "\"The thing is,\" Emery says, \"it's all disconnected. I copy-paste context into a chat window every time. It doesn't know my project. It doesn't remember yesterday. Last week I pasted our PRD into Gemini for the third time and it still asked me what our target audience was. I'm sure I could be using it more — but honestly, it sometimes just feels like more work.\"",
      "Maven nods. \"That's exactly right — and you're not doing it wrong. What you've described is the ceiling of the chatbot paradigm.\"",
      "\"And I heard about coding agents — Claude Code, Windsurf, whatever. But I don't code. So I figured that was a developer thing.\"",
      "Maven smiles. \"That's exactly what we need to talk about.\"",
    ],
    sources: [
      {
        idea: "Google Gems let users save custom instructions for Gemini — personal productivity tools embedded in the Google ecosystem, but siloed with no file access or tool integrations.",
        name: "Google Blog",
        url: "https://blog.google/products-and-products/products/gemini/google-gemini-update-august-2024/",
      },
      {
        idea: "Teresa Torres broke her context into dozens of tiny focused markdown files so simple prompts produce rich output — she calls it \"lazy prompting.\"",
        name: "ChatPRD",
        url: "https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management",
      },
      {
        idea: "Helen Lee Kupp voice-records ideas on stroller walks, drops transcripts into a folder, and Claude Code organizes them into research themes, articles, and LinkedIn posts.",
        name: "Lenny's Newsletter",
        url: "https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code",
      },
      {
        idea: "ChatGPT Plugins, OpenAI's first attempt at giving AI access to external tools, never achieved product-market fit and were shut down in April 2024.",
        name: "OpenAI",
        url: "https://openai.com/index/chatgpt-plugins/",
      },
    ],
  },
  {
    id: "ch-3",
    number: 3,
    title: "\"So what's the difference between a chatbot and an agent?\"",
    navLabel: "The Unboxing",
    panels: [
      {
        label: "Maven opens the box",
        description: "Maven lifts the box lid. Warm light spills out. Claw'd is visible inside — a small boxy terracotta creature. Emery's eyes go wide. Declan freezes mid-sip.",
        image: "/images/ch03-the-unboxing-frame-a-20260224-180641.png",
        gradient: "warm",
        dialogue: "A chatbot answers questions in a window. An agent operates in your world.",
      },
      {
        label: "Claw'd emerges",
        description: "Claw'd has climbed out of the box and sits on the table, notebook open, looking up at the three humans. Emery reaches toward it.",
        image: "/images/ch03-the-unboxing-frame-b-20260224-180641.png",
        gradient: "warm",
        dialogue: "It has a notebook?",
      },
    ],
    body: [
      "\"That was a chatbot,\" Maven says, as Claw'd settles on the table and opens its notebook. \"This is an agent — and the difference matters.\"",
      "A chatbot is a text box. You type a question, it types an answer. It doesn't know your files. It can't connect to your tools. It forgets things unpredictably — some sessions remember more than others, but you can't know what, and you can't control it.",
      "An agent is different. It reads your project folder. It connects to your tools — Jira, Slack, Google Drive. It follows rules you write for it. And it doesn't just answer — it plans, tries something, checks if it worked, and adjusts. Like a junior teammate who actually listens.",
      "\"So there's the AI — the model itself,\" Declan says. \"And then there's all the stuff around it. The files it reads, the tools it connects to, the rules it follows.\"",
      "\"That's the harness,\" Maven says. \"The model is the engine. The harness is everything else — file access, instruction sets, tool connections. Claude Code and Windsurf are harnesses: they take a model and connect it to your codebase, your tools, your data. Without a harness, it's just a chat window.\"",
      "\"Like AutoGPT,\" Declan says. \"Plan, try, check, adjust — that was the pitch. And it spent the whole night in an infinite loop.\"",
      "\"AutoGPT was the right idea two years early. The models weren't capable enough and the harness wasn't smart enough. It got stuck because it couldn't recognize failure. Models now recognize when they're stuck. The harness learned to checkpoint progress, compact context, and ask for help instead of looping. What AutoGPT attempted, today's agents do reliably.\"",
      "Emery reaches out toward Claw'd. It tilts its head and opens to a fresh page.",
    ],
    sources: [
      {
        idea: "Simon Willison defined an agent as \"an LLM that runs tools in a loop to achieve a goal\" — widely quoted, but agency requires more: the ability to act on the world, read files, call APIs, take consequential steps. The loop is the mechanism; the actions are the substance.",
        name: "Simon Willison",
        url: "https://simonw.substack.com/p/i-think-agent-may-finally-have-a",
      },
      {
        idea: "Claude Code launched in February 2025 as a terminal-based agent that could search code, edit files, run tests, commit to GitHub, and execute CLI tools.",
        name: "Anthropic",
        url: "https://www.anthropic.com/news/claude-3-7-sonnet",
      },
      {
        idea: "\"The architecture of an AI agent can be reduced to two components: the filesystem as state, and Claude as the orchestrator.\"",
        name: "@mernit (Openclaw)",
        url: "https://x.com/mernit/status/2021324284875153544",
      },
      {
        idea: "By February 2026, Claude Code authored 4% of all public GitHub commits (~135,000/day), projected to reach 20%+ by year-end.",
        name: "Anthropic",
        url: "https://www.anthropic.com/news/claude-opus-4-6",
      },
    ],
  },
  {
    id: "ch-4",
    number: 4,
    title: "\"It works with your actual files — not a chat window.\"",
    navLabel: "Files & Context",
    panels: [
      {
        label: "Maven shows the project folder",
        description: "Maven points at a laptop showing a file explorer with project folders. Claw'd flips through its notebook. Emery leans in, aha moment dawning.",
        image: "/images/ch04-files-context-frame-a-20260224-180641.png",
        gradient: "warm-accent",
        dialogue: "See this file? CLAUDE.md. The agent reads it every time you start a session.",
      },
      {
        label: "Emery makes the connection",
        description: "Emery looks from their tablet to the screen, the lightbulb moment hitting — their prompts.txt could be the instruction file.",
        image: "/images/ch04-files-context-frame-b-20260224-180641.png",
        gradient: "warm-accent",
        dialogue: "Wait — so my prompts.txt on the desktop... that could just BE the instruction file? And it would read it automatically?",
      },
    ],
    body: [
      "Emery's prompts.txt file has twenty saved prompts. Every time they start a conversation with Gemini, they open the file, find the right prompt, copy it, paste it, then add whatever context is specific to today's task. It works. Barely.",
      "\"Here's what that looks like with an agent,\" Maven says. She opens a project folder on the laptop. Inside: docs/, specs/, research/, decisions/ — and at the root, a file called CLAUDE.md.",
      "\"This file is your prompts.txt — but permanent. The agent reads it automatically every time you start working. You put your project context here, your conventions, your preferences. 'When I ask for a PRD, use the template in the specs/ folder. Our users are developer teams at B2B software companies. Always check the research/ folder before answering questions about competitors.'\"",
      "Emery stares. \"And it just... reads my files?\"",
      "\"All of them — your specs, your meeting notes, your decision log. It searches the web and connects to other tools when you ask, but it starts with your project folder. It lives there. You don't paste anything.\"",
      "This is the first primitive: filesystem access. The agent isn't trapped in a chat window — it operates in your project folder. It reads what's there, creates new files, updates existing ones. The difference between describing your kitchen over the phone and letting the chef walk in.",
      "Declan, from behind them: \"So it reads everything. Including the stuff that's wrong?\"",
      "Maven: \"Yes. Which is why the files matter. Garbage context, garbage output. But here's the thing — investing in good project documentation now helps your human teammates AND the agent. It's the same investment paying off twice.\"",
    ],
    sources: [
      {
        idea: "Teresa Torres built her context into dozens of focused markdown files — at the end of each session she asks \"Claude, what did you learn today that we should document?\"",
        name: "ChatPRD",
        url: "https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management",
      },
      {
        idea: "CLAUDE.md files provide persistent project instructions loaded into every conversation — root, parent directories, home folder, child directories.",
        name: "Claude Code Docs",
        url: "https://code.claude.com/docs/en/overview",
      },
      {
        idea: "\"Chat is describing your kitchen to a chef over the phone. Filesystem access is letting the chef into your kitchen.\"",
        name: "Session 6 Research",
        url: "https://agents-for-everyone.ai-pm.cc",
      },
      {
        idea: "Abhi Chandwani maintains verbose git commits specifically to create context for future agent workflows — the commit history becomes the agent's memory.",
        name: "Lenny's Newsletter",
        url: "https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code",
      },
    ],
  },
  {
    id: "ch-5",
    number: 5,
    title: "\"You teach it how you work — and it remembers.\"",
    navLabel: "Rules & Skills",
    panels: [
      {
        label: "Maven explains skill files",
        description: "Closer view of the table. Maven points at a skill definition on the laptop. Claw'd looks up attentively. Emery sketches on their tablet with stylus.",
        image: "/images/ch05-rules-skills-frame-a-20260224-180641.png",
        gradient: "cool-accent",
        dialogue: "This is a skill file. It tells the agent exactly how to do a specific task — your format, your criteria, your workflow.",
      },
      {
        label: "Emery connects the dots",
        description: "Emery looks up from their tablet with an excited expression, something clicking into place.",
        image: "/images/ch05-rules-skills-frame-b-20260224-180641.png",
        gradient: "cool-accent",
        dialogue: "So it's like onboarding documentation... but the documentation actually gets read?",
      },
    ],
    body: [
      "Every PM has a way they do things. A format for PRDs. A checklist for launch readiness. A set of questions they always ask in customer interviews. Usually this lives in their head, in a Google Doc nobody reads, or in tribal knowledge that evaporates when someone changes teams.",
      "\"Skills,\" Maven says, opening a file on the laptop, \"are how you teach the agent your way of working.\"",
      "A skill file is structured text — markdown, not code — that describes a specific task: what inputs it needs, what steps to follow, what format to produce. They range from extremely specific to broad and conceptual. Specific end: \"If the user provides customer interview data, cite it inline. If the spec is missing acceptance criteria, flag it before proceeding.\" Conceptual end: \"When reviewing a technical spec, think like a skeptical engineer who has seen requirements change at the last minute.\" The same format handles both — precise checklists and general judgment.",
      "\"It's like onboarding a new hire,\" Emery says slowly, \"except they actually retain what you told them.\"",
      "\"And you don't have to write skill files from scratch. You can teach them in conversation — work a task with the agent, give feedback as you go, then ask: 'What did you learn today? Write it as a skill file.' The agent can author its own instructions from your corrections.\"",
      "\"Agents are also unusually good at introspection. After a working session, ask it to retro: what went well, what didn't, how should the skill file change? The output is specific — not 'improve communication' but 'always check the research/ folder before making claims about competitors.'\"",
      "\"Once you update the skill, it holds. Every time after that, the agent follows the new instructions reliably. The investment compounds. And when you nail a skill, you can share it — drop the file in a shared repo and your whole team has it. Someone else's expertise, running in your workflow.\"",
      "This is the second primitive: persistent instructions. CLAUDE.md gives the agent project context. Skills give it task-specific expertise. The model is the same for everyone — the instructions make it behave like YOUR expert.",
      "Declan, from the background: \"So you're encoding your preferences in text files and hoping the AI follows them?\"",
      "Maven: \"Not hoping. Testing. You run it, review the output, adjust the instructions. Same way you'd manage anyone.\"",
    ],
    sources: [
      {
        idea: "Hilary Gridley reverse-engineered her implicit quality standards from before/after slide examples into a \"Deck Doctor\" GPT — key prompt: \"Be 100 times more specific.\"",
        name: "ChatPRD",
        url: "https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts",
      },
      {
        idea: "\"After solving a problem, ask the AI how to prompt it better next time, then add that guidance to your rules file.\" A single rules file achieves compounding improvement across sessions.",
        name: "Lenny's Newsletter",
        url: "https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code",
      },
      {
        idea: "Claire Vo built a meta-skill — a \"skill that builds skills\" — demonstrating that agent capabilities are composable, not flat.",
        name: "ChatPRD",
        url: "https://www.chatprd.ai/how-i-ai/claude-skills-explained",
      },
      {
        idea: "The Cowork legal plugin is ~200 lines of structured markdown — NDA triage against 13 criteria, contract review with clause-by-clause analysis. It triggered a $285 billion stock selloff.",
        name: "Nate's Newsletter",
        url: "https://natesnewsletter.substack.com/p/200-lines-of-markdown-just-triggered",
      },
    ],
  },
  {
    id: "ch-6",
    number: 6,
    title: "\"It doesn't just answer — it does things.\"",
    navLabel: "Tools & Actions",
    panels: [
      {
        label: "The agent did the work",
        description: "The laptop shows terminal output with completed actions. Claw'd's notebook is full of checkmarks. Emery reads the output, impressed.",
        image: "/images/ch06-tools-actions-frame-a-20260224-180641.png",
        gradient: "warm-accent",
        dialogue: "It didn't just tell me what to do. It did it. Searched the web, pulled the data, updated the ticket, wrote the summary.",
      },
      {
        label: "Emery recalibrates",
        description: "Emery turns to look at Maven directly, something shifting in how they think about this.",
        image: "/images/ch06-tools-actions-frame-b-20260224-180641.png",
        gradient: "warm-accent",
        dialogue: "That's... not what I thought this was.",
      },
    ],
    body: [
      "Emery has used AI to draft emails, brainstorm feature names, and summarize meeting notes. In every case, the output was text. Suggestions. Ideas. Things they had to copy-paste into the actual tool and then do the work themselves.",
      "\"Watch this,\" Maven says. She types a single prompt: Analyze Q4 usage data, find the three features with the highest signup-to-week-2 drop-off, cross-reference our backlog, and draft priorities for planning.",
      "The agent reads the CSV files. It writes and runs an analysis script. It searches the backlog folder for related issues. It produces a markdown summary with three feature recommendations, each grounded in specific data points and linked to existing tickets.",
      "\"It didn't give me a suggestion,\" Maven says. \"It did the work.\"",
      "This is the third primitive: tool use and actions. Through MCP — think of it as USB ports for AI, letting you plug your existing tools in — agents can connect to Jira, Slack, Google Drive, databases, web search, APIs. The agent doesn't just generate text. It queries, updates, creates, and organizes. And for tools that don't yet have MCP servers, agents can use the CLI or operate a browser directly — navigating, clicking, extracting — without waiting for anyone to build an integration.",
      "Declan, now closer to the group than before: \"And when it does something wrong? When it updates the wrong ticket?\"",
      "Maven: \"You review before it acts. Most agents have approval gates — they show you what they're about to do and wait for a thumbs up. Same as reviewing a junior's PR.\"",
    ],
    sources: [
      {
        idea: "Reid Robinson (Zapier PM): Post-meeting transcript → agent searches CRM via MCP → enriches contact record → creates follow-up task. A 15-minute manual workflow became automated.",
        name: "ChatPRD",
        url: "https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep",
      },
      {
        idea: "Dennison Bertram built \"Claude CEO\" — connecting Gmail, Brex, Mercury, and Linear via MCP. A single morning prompt produces a cross-tool executive summary.",
        name: "Lenny's Newsletter",
        url: "https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code",
      },
      {
        idea: "MCP (Model Context Protocol), announced November 2024, is an open standard for connecting AI to external tools — replacing the fragmented, proprietary integrations that doomed ChatGPT Plugins.",
        name: "Anthropic",
        url: "https://www.anthropic.com/news/model-context-protocol",
      },
      {
        idea: "The Anthropic Growth Marketing team built an agent that processes a CSV of hundreds of ads, identifies underperformers, and generates new variations — reducing hours of copy-pasting to \"half a second per batch.\"",
        name: "Anthropic",
        url: "https://claude.com/blog/how-anthropic-teams-use-claude-code",
      },
    ],
  },
  {
    id: "ch-7",
    number: 7,
    title: "\"Show me what this looks like for a PM.\"",
    navLabel: "PM Lifecycle",
    panels: [
      {
        label: "Maven lists PM use cases",
        description: "Maven counts on her fingers listing use cases. Claw'd follows along flipping notebook pages. Emery sketches a workflow diagram on their tablet.",
        image: "/images/ch07-pm-lifecycle-frame-a-20260224-180641.png",
        gradient: "cool-accent",
        dialogue: "Discovery research synthesis. PRD drafting grounded in customer data. Spec review against acceptance criteria. Competitive analysis. Stakeholder updates.",
      },
      {
        label: "Emery recognizes their workflow",
        description: "Emery stops sketching and looks up, connecting the use cases to their own weekly routine.",
        image: "/images/ch07-pm-lifecycle-frame-b-20260224-180641.png",
        gradient: "cool-accent",
        dialogue: "Half my week is synthesizing information that already exists in four different places. That's what this does?",
      },
    ],
    body: [
      "Emery's calendar is mostly synthesis: customer notes into themes, specs against acceptance criteria, Jira and Slack into a stakeholder update. Structured information taken from here, filtered through judgment, produced over there. This is exactly what agents do.",
      "\"Discovery,\" Maven says. \"Your agent reads every call transcript in the calls/ folder, identifies recurring themes, and produces a summary with supporting quotes.\"",
      "\"PRD drafting. It pulls your product brief, your research, your existing PRD template from the skills/ folder, and produces a first draft that follows your format, grounded in your data.\"",
      "\"Spec review. The agent reads the engineering spec and your acceptance criteria, identifies gaps — missing edge cases, untested scenarios, ambiguous requirements — and flags them with specific questions.\"",
      "Emery has stopped sketching. They're doing math in their head.",
      "\"The cross-referencing alone,\" they say. \"That's half my time. Checking the spec against the PRD against the acceptance criteria against what customers actually said.\"",
      "\"And the agent does it in minutes because it can hold all those files in context simultaneously. You can't. No human can keep six documents in their head at once.\"",
      "Declan, from his chair: \"How good is it, actually? You're describing perfection.\"",
      "Maven: \"It's not perfect. It misses things. It gets confused by ambiguity. That's why you review the output. But it takes the job from 'synthesize six documents from scratch' to 'review and refine one summary.' That's a different job. A faster one.\"",
    ],
    sources: [
      {
        idea: "Derek DeHart: \"Given MCPs to interact with Fireflies, Linear, Notion — it's become my hub for ongoing product research and development.\"",
        name: "Lenny's Newsletter",
        url: "https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code",
      },
      {
        idea: "Trist Adlington: \"I talk to Claude more than anyone else\" — using it for continuous PRD iteration, competitive analysis, and roadmap planning.",
        name: "Lenny's Newsletter",
        url: "https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code",
      },
      {
        idea: "The Cowork product-management plugin connects to Figma, Amplitude, and Pendo — pre-wired for the tools PMs already use.",
        name: "GitHub",
        url: "https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management",
      },
      {
        idea: "Ethan Mollick's BCG study: Consultants with AI completed 12.2% more tasks, 25.1% faster, at 40% higher quality — but were 19 percentage points WORSE on tasks outside AI's capability frontier.",
        name: "One Useful Thing",
        url: "https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged",
      },
    ],
  },
  {
    id: "ch-8",
    number: 8,
    title: "\"Your dev team is about to move a lot faster.\"",
    navLabel: "Agentic Teams",
    panels: [
      {
        label: "Maven at the whiteboard",
        description: "Maven taps a flow chart on the whiteboard showing PM intent → Structured context → Agent → Code → Review. Declan has uncrossed his arms.",
        image: "/images/ch08-agentic-teams-frame-a-20260224-180641.png",
        gradient: "warm-accent",
        dialogue: "Your dev team is already using agents. The question is whether you're giving them what they need — or becoming the bottleneck.",
      },
      {
        label: "Declan engages",
        description: "Declan speaks up for the first time in chapters — not objecting, but thinking through a real problem.",
        image: "/images/ch08-agentic-teams-frame-b-20260224-180641.png",
        gradient: "warm-accent",
        dialogue: "So if engineering is using agents to turn specs into code faster... and the specs are unclear... the agent just builds the wrong thing faster.",
      },
    ],
    body: [
      "Andrej Karpathy coined \"vibe coding\" in February 2025 — developers describe intent and let AI write code. By late 2025, he updated it to \"agentic engineering.\" At Anthropic, Claude Code writes 70-90% of code with human review. Speed is the first effect.",
      "The second effect is less obvious. If agents can turn a clear spec into a working feature in hours instead of days, the quality of the spec becomes the rate-limiting factor. Agents follow specs literally. They don't push back the way an experienced developer would. They don't check their interpretation against your unstated intent.",
      "\"So if the agent builds from my spec,\" Declan says, \"and the spec is vague — it doesn't ask for clarification. It just goes.\"",
      "\"Yes. Your PRD, your acceptance criteria, your decision log — these are machine-readable inputs now. Clear specs aren't just good practice. They're an input to a system.\"",
      "But here's what most PMs haven't heard yet: the same agents that accelerate engineering can accelerate intent production. A PM who used to spend Tuesday synthesizing four documents before writing a first PRD draft can now do it in an hour. Some teams have already flipped the script — PMs have stopped waiting on engineering to finish one sprint before starting the next. Engineering is now waiting on the PM.",
      "\"The bottleneck moves upstream,\" Declan says. \"But you have tools to move faster at the new constraint.\"",
      "Maven: \"Exactly. The agents help both ends. Clear intent becomes a force multiplier. And now you can produce that intent faster than ever before.\"",
      "Teams that adopt agents don't just go faster — they become hungry for clarity. PMs who can express intent clearly in structured repos with good context become force multipliers. PMs who can't become the constraint in a system that just got three times faster. The skill isn't coding. It's clarity.",
    ],
    sources: [
      {
        idea: "Andrej Karpathy coined \"vibe coding\" in February 2025 and updated it to \"agentic engineering\" by late 2025 — from novelty to professional default in under a year.",
        name: "Wikipedia",
        url: "https://en.wikipedia.org/wiki/Vibe_coding",
      },
      {
        idea: "At Anthropic, Claude Code writes 70-90% of code, with CPO Mike Krieger stating \"for most products it's effectively 100 percent just Claude writing.\"",
        name: "Anthropic",
        url: "https://www.anthropic.com/news/claude-opus-4-6",
      },
      {
        idea: "\"Claude Code is the Inflection Point\" — documenting how agent-native development changes the role of everyone on the team.",
        name: "SemiAnalysis",
        url: "https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point",
      },
      {
        idea: "\"As AI agents become capable of hours-long autonomous work, delegation skills become the differentiator.\" Management — not prompting — is the AI superpower.",
        name: "Ethan Mollick",
        url: "https://x.com/OwenGregorian/status/2016841301673820250",
      },
    ],
  },
  {
    id: "ch-9",
    number: 9,
    title: "\"Okay — how do I actually start?\"",
    navLabel: "Getting Started",
    panels: [
      {
        label: "Emery makes a plan",
        description: "Emery has their tablet in hand, listing action items. Maven sits back, relaxed, letting Emery lead. Claw'd watches attentively. Declan's chair is empty.",
        image: "/images/ch09-getting-started-frame-a-20260224-180641.png",
        gradient: "cool",
        dialogue: "Okay. Markdown. GitHub. A project folder with a CLAUDE.md. Start with the drudgery.",
      },
      {
        label: "Claw'd shares its notes",
        description: "Claw'd hops closer to Emery and holds up its notebook with neat notes. Emery smiles warmly at it. Late afternoon light.",
        image: "/images/ch09-getting-started-frame-b-20260224-180641.png",
        gradient: "cool",
        dialogue: "It gets better the more you invest in it. The context, the skills, the corrections — they compound.",
      },
    ],
    body: [
      "Emery has their tablet out, ready to make a list.",
      "\"Here's what I'd actually tell you to do,\" Maven says.",
      "Learn markdown. Agents can't interpret visual formatting — bold in a Word doc, color-coding in a spreadsheet, indentation in a Google Doc. They read text. Markdown is how you add structure to text in a format agents actually understand: # headers, **bold**, bullet lists. It's not a programming language — it's closer to punctuation for meaning. The native format of skill files, CLAUDE.md, project docs, and decision logs. markdowntutorial.com takes twenty minutes.",
      "Get on GitHub. Not to code — to have a shared workspace that agents can also access. Think of it as Dropbox where every change is tracked and every collaborator (human or AI) can see the full history. Your decision logs, your specs, your research — put them in a repository. The git operations — pushing, pulling, committing — are plain English: ask the agent in plain language and it handles them for you.",
      "Build context into your repos. Write a README for your project. Start a decision log. Add a CLAUDE.md with your preferences and conventions. This investment pays off twice — for your human teammates and for the agent. If you're not sure where to start, ask the agent to help you write them.",
      "Experiment safely. Pick a low-stakes task — a weekly status update, a competitive analysis, an FAQ draft. Try it with an agent. See where it succeeds and where it fails. AI is unpredictably good and unpredictably bad — you can't guess where the edges are. You have to discover them first-hand. The agent can help you identify which of your recurring tasks are good candidates.",
      "Audit your drudgery. Which recurring tasks drain you? The ones that are structured, repetitive, and information-heavy are your first candidates. Not the creative strategy work — the synthesis, formatting, and cross-referencing that consumes your Tuesday afternoons.",
      "\"Does it really get better over time?\"",
      "Maven: \"Every correction, every skill, every piece of context compounds. In a month the agent is better — not because the model changed, but because you gave it more context, helped it learn your processes, and codified them in rules and skills. That's the real unlock.\"",
    ],
    sources: [
      {
        idea: "James Pember built \"self-driving documentation\" — an agent with browser access that explores software independently, identifies knowledge gaps, and creates documentation.",
        name: "Lenny's Newsletter",
        url: "https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code",
      },
      {
        idea: "Gang Rui's slash command analyzes journal entries and git commits for the past 7 days, spots gaps between intentions and actions — \"like having a COO that learns from my patterns.\"",
        name: "Lenny's Newsletter",
        url: "https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code",
      },
      {
        idea: "Claude Cowork, launched January 2026, brought Claude Code's agentic capabilities to non-developers — \"Claude Code for the rest of your work.\" Built in ~10 days using Claude Code itself.",
        name: "TechCrunch",
        url: "https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/",
      },
      {
        idea: "Boris Cherny, Claude Code's creator: \"An AI model like Claude is the horse, and a coding assistant like Claude Code is the harness.\" Both model capability and scaffolding must be excellent.",
        name: "OfficeChai",
        url: "https://officechai.com/ai/claude-is-like-the-horse-and-claude-code-is-the-harness-anthropics-boris-cherny/",
      },
    ],
  },
  {
    id: "epilogue",
    number: 10,
    title: "Epilogue",
    navLabel: "Epilogue",
    variant: "epilogue",
    byline: "Geoff Dudgeon (<a href=\"https://x.com/geoffdudgeon\" class=\"underline underline-offset-2 opacity-70 hover:opacity-100\">X</a>, <a href=\"https://github.com/dudgeon/agents-for-everyone\" class=\"underline underline-offset-2 opacity-70 hover:opacity-100\">GitHub</a>) + Claude",
    panels: [],
    body: [
      "I wrote this story, with plenty of help from Claude, to get people thinking about the agentic moment that has rocked software development over the past year, and is now beginning to sweep through other knowledge work like product management.",
      "In some ways it is similar to the ChatGPT moment — in other ways it is much, much bigger. This story is a conversation starter and probably opens more questions and avenues to explore than it does answers.",
      "But the goal is to make agents feel different, tangible, and like something you can understand and excel at — because I know you will.",
    ],
    sources: [],
  },
];
