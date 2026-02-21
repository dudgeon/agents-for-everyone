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
}

export interface ChapterData {
  id: string;
  number: number;
  title: string;
  navLabel: string;
  panels: Panel[];
  body: string[];
  sources: Source[];
}

export const chapters: ChapterData[] = [
  {
    id: "ch-1",
    number: 1,
    title: "The best tool you've never used is already on your computer — and it gets better every time you open it.",
    navLabel: "The Bold Claim",
    panels: [
      {
        label: "Let me show you something",
        description: "Maven opens a laptop toward the Skeptic, pointing at something on screen. She's leaning forward, eager to show rather than tell.",
        image: "/images/ch01-bold-claim-frame-a-20260221-144505.png",
        gradient: "warm",
      },
      {
        label: "That's just a text file?",
        description: "Skeptic leans slightly forward — still guarded, but pulled in by what he just saw. One hand shifts to his chin.",
        image: "/images/ch01-bold-claim-frame-b-20260221-144505.png",
        gradient: "warm",
      },
    ],
    body: [
      "In January 2026, Mark Pike — a product lawyer at Anthropic with no engineering background — built a legal review system using plain English. It screens NDAs against thirteen criteria, classifies them as green, yellow, or red, and generates routing recommendations. The whole thing: about 200 lines of structured text. No code. No infrastructure. He described the process: \"I just typed a normal sentence, describing what I wanted. And it worked.\"",
      "When Anthropic open-sourced it, the legal tech industry had what one Goldman Sachs trader called a \"SaaSpocalypse.\" Thomson Reuters dropped 18%. LegalZoom fell 20%. Total market impact: roughly $285 billion in a week.",
      "This is not a story about a lawyer who learned to code. It's a story about what's possible now that you don't have to.",
      "This book is short, evidence-based, and specific. It will not ask you to suspend your skepticism. It will ask you to update it.",
    ],
    sources: [
      {
        idea: "Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps.",
        name: "Anthropic knowledge-work-plugins repository",
        url: "https://github.com/anthropics/knowledge-work-plugins",
      },
      {
        idea: "I just typed a normal sentence, describing what I wanted. And it worked.",
        name: "How Anthropic Uses Claude in Legal",
        url: "https://claude.com/blog/how-anthropic-uses-claude-legal",
      },
      {
        idea: "Thomson Reuters -18%, RELX -14%, LegalZoom -20%. Goldman Sachs basket of U.S. software stocks: -6% in a single session.",
        name: "CNBC",
        url: "https://www.cnbc.com/2026/02/06/ai-anthropic-tools-saas-software-stocks-selloff.html",
      },
    ],
  },
  {
    id: "ch-2",
    number: 2,
    title: "In 2023, AI was confidently wrong about everything — and the people selling it didn't seem to notice.",
    navLabel: "Earned Skepticism",
    panels: [
      {
        label: "A lawyer submitted fake cases to a federal judge",
        description: "Skeptic leans forward, hands open, recounting something that happened. Not angry — making a point he's made before, to someone who usually argues back.",
        image: "/images/ch02-earned-skepticism-frame-a-20260221-144607.png",
        gradient: "cool",
      },
      {
        label: "You're right. That was bad.",
        description: "Maven nods, not defending, not qualifying. Just agreeing. This is the moment Skeptic hasn't seen before — someone on the AI side who doesn't argue.",
        image: "/images/ch02-earned-skepticism-frame-b-20260221-144607.png",
        gradient: "cool",
      },
    ],
    body: [
      "If you tried AI in 2023 and walked away unimpressed — or worse, burned — you were paying attention.",
      "ChatGPT launched in November 2022 as a \"research preview.\" It could write a decent email, explain a concept, help brainstorm. It could also confidently invent facts, fabricate sources, and present complete fiction as authoritative truth. It had no way to look anything up. No access to your files. No memory between conversations. Every chat started from scratch.",
      "The consequences were real. In May 2023, lawyer Steven Schwartz used ChatGPT to research case law and submitted a brief to federal court containing six fabricated cases — \"Martinez v. Delta Air Lines,\" \"Varghese v. China Southern Airlines\" — complete with invented citations and legal reasoning. Schwartz testified he was \"operating under the false perception that it could not possibly be fabricating cases on its own.\" He and his colleague were fined $5,000.",
      "Your skepticism from that era isn't wrong. It's just aimed at a target that has moved.",
    ],
    sources: [
      {
        idea: "Schwartz testified he was \"operating under the false perception that ChatGPT could not possibly be fabricating cases on its own.\"",
        name: "CNN / Mata v. Avianca",
        url: "https://www.cnn.com/2023/05/27/business/chat-gpt-avianca-mata-lawyers",
      },
      {
        idea: "GPT-4 Turbo was immediately reported as 'lazier' — shorter responses, truncated code blocks.",
        name: "OpenAI Community Forum",
        url: "https://community.openai.com/t/chatgpt-4-defaults-to-lazy/560886",
      },
      {
        idea: "ChatGPT reached 1 million users in 5 days and 100 million in two months — the fastest consumer app adoption in history at the time.",
        name: "History.com",
        url: "https://www.history.com/this-day-in-history/november-30/chatgpt-released-openai",
      },
    ],
  },
  {
    id: "ch-3",
    number: 3,
    title: "We've heard \"this time it's different\" before — remember when AI agents were going to change everything?",
    navLabel: "Hype Graveyard",
    panels: [
      {
        label: "AutoGPT. 174,000 stars. Infinite loops all night.",
        description: "Skeptic gestures toward a whiteboard listing AutoGPT, BabyAGI, Devin, ChatGPT Plugins — each with a large X. Not triumphant, making a fair point.",
        image: "/images/ch03-hype-graveyard-frame-a-20260221-144655.png",
        gradient: "cool",
      },
      {
        label: "I'm not going to defend any of that.",
        description: "Maven spreads her hands, making no attempt to defend any of it. Honest concession. She's looking at the Skeptic, not the whiteboard.",
        image: "/images/ch03-hype-graveyard-frame-b-20260221-144655.png",
        gradient: "cool",
      },
    ],
    body: [
      "In March 2023, AutoGPT and BabyAGI promised autonomous AI agents that could set goals, break them into tasks, execute them, and iterate without human intervention. AutoGPT became the number one GitHub repository of 2023 with 174,000 stars. Andrej Karpathy called it \"the next frontier of prompt engineering.\"",
      "The reality: agents got stuck in infinite loops all night, burned through API credits without producing anything, and forgot what they'd already done. Tom's Hardware's review headline was not subtle: \"Auto-GPT and BabyAGI Are AI's New Hotness, But They Suck Right Now.\" By late 2023, the AutoGPT team removed their external database support — agents didn't generate enough useful information to need one.",
      "The pattern repeated. ChatGPT Plugins launched as an \"App Store moment for AI\" in March 2023 and were quietly killed by April 2024. The GPT Store opened with 3 million custom GPTs; researchers found a 97% success rate extracting their supposedly secret system prompts. Devin, launched in March 2024 as the \"first fully autonomous AI software engineer,\" achieved a 15% success rate in independent testing.",
      "So when someone says \"AI agents are different now,\" your skepticism isn't cynicism. It's pattern recognition. The next two chapters explain exactly what changed — mechanically, not rhetorically.",
    ],
    sources: [
      {
        idea: "Auto-GPT and BabyAGI Are AI's New Hotness, But They Suck Right Now.",
        name: "Tom's Hardware",
        url: "https://www.tomshardware.com/news/autonomous-agents-new-big-thing",
      },
      {
        idea: "Researchers tested 200+ custom GPTs and found a 97.2% success rate at extracting system prompts.",
        name: "ArXiv: Assessing Prompt Injection Risks",
        url: "https://arxiv.org/html/2311.11538v2",
      },
      {
        idea: "Answer.AI tested Devin on 20 real-world tasks: 14 failures, 3 successes, 3 inconclusive — 15% success rate.",
        name: "Answer.AI",
        url: "https://www.answer.ai/posts/2025-01-08-devin.html",
      },
      {
        idea: "AutoGPT reached 174,000+ GitHub stars — the #1 GitHub repository of 2023.",
        name: "AutoGPT Wikipedia",
        url: "https://en.wikipedia.org/wiki/AutoGPT",
      },
    ],
  },
  {
    id: "ch-4",
    number: 4,
    title: "AI doesn't just answer anymore — it plans, tries, checks, and adjusts.",
    navLabel: "The Loop",
    panels: [
      {
        label: "What happens when it gets the first step wrong?",
        description: "Skeptic points at Maven's loop diagram on the whiteboard — PLAN, ACT, OBSERVE, ADJUST. Maven holds the marker, turns to face him.",
        image: "/images/ch04-the-loop-frame-a-20260221-144840.png",
        gradient: "warm-accent",
      },
      {
        label: "It reads the error. Then tries a different approach.",
        description: "Maven taps the OBSERVE box on the whiteboard. She's not explaining so much as demonstrating — this is the key point.",
        image: "/images/ch04-the-loop-frame-b-20260221-144840.png",
        gradient: "warm-accent",
      },
    ],
    body: [
      "The AI you tried in 2023 worked like this: you typed something in, it generated something back, and that was the transaction. One shot. If it got it wrong, you'd rephrase and try again. The AI never tried again on its own. It never checked its work.",
      "That is not how it works anymore.",
      "Simon Willison, one of the most rigorous voices writing about AI tooling, defines an agent as \"an LLM that runs tools in a loop to achieve a goal.\" That loop — plan, act, observe, adjust — is the mechanical difference between a chatbot and a coworker. The chatbot gives you an answer. The agent tries something, sees what happens, and course-corrects.",
      "Here's what this looks like outside software. Willison tested Anthropic's Cowork on a folder of 46 blog draft files. The agent needed to identify which ones were ready to publish. It executed 44 separate web searches to verify the publication status of each piece, cross-referenced what it found, and returned three publish-ready candidates with reasoning. No human intervention between the first step and the final answer.",
    ],
    sources: [
      {
        idea: "An LLM agent runs tools in a loop to achieve a goal.",
        name: "Simon Willison",
        url: "https://simonw.substack.com/p/i-think-agent-may-finally-have-a",
      },
      {
        idea: "Agent found 46 files, executed 44 website searches to verify publication status, identified 3 publish-ready candidates.",
        name: "Simon Willison: Claude Cowork",
        url: "https://simonwillison.net/2026/Jan/12/claude-cowork/",
      },
      {
        idea: "Claude Code outperforms Cursor using the same model due to superior prompting and scaffolding.",
        name: "Every.to Vibe Check",
        url: "https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code",
      },
    ],
  },
  {
    id: "ch-5",
    number: 5,
    title: "It remembers who you are and how you work.",
    navLabel: "Memory",
    panels: [
      {
        label: "Wait — I'd have to explain my whole job to it?",
        description: "Skeptic squints at a laptop screen showing a plain-English list of rules and preferences. His posture has opened up slightly — one hand on his knee.",
        image: "/images/ch05-memory-frame-a-20260221-145013.png",
        gradient: "cool-accent",
      },
      {
        label: "Once. Then it remembers.",
        description: "Maven closes the laptop gently, making eye contact. Session ten is different from session one.",
        image: "/images/ch05-memory-frame-b-20260221-145013.png",
        gradient: "cool-accent",
      },
    ],
    body: [
      "In 2023, every AI conversation started from scratch. You'd explain your role, your context, your preferences — and do it again tomorrow. It was like hiring a contractor who arrived every morning with no memory of the job.",
      "That problem is solved. Tools like Claude Code read a project instruction file — called CLAUDE.md — at the start of every session. This file tells the AI who you are, how you work, and what your standards are. Written in plain English: \"When I say 'format this,' use AP style.\" \"Always flag indemnification clauses in contracts before anything else.\" \"Never send anything externally without checking with me first.\"",
      "Teresa Torres, a product management consultant, built her system over months. She broke her context into dozens of small files — her business profile, her writing style, her research interests — stored in a vault the agent reads at session start. At the end of each session, she asks: \"What did you learn today that we should document?\" She calls it \"lazy prompting\" — the system already knows her, so she just describes what she needs.",
    ],
    sources: [
      {
        idea: "Torres breaks her context into dozens of focused markdown files. She calls it 'lazy prompting.'",
        name: "ChatPRD: Teresa Torres's Claude Code System",
        url: "https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management",
      },
      {
        idea: "Chat vs. Claude Code memory — 'search past chats' vs. 'all files act as memory.' Reusability — 'start fresh each chat' vs. 'systems that compound over time.'",
        name: "Product Talk: Claude Code",
        url: "https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/",
      },
      {
        idea: "After solving a problem, ask the AI how to prompt it better next time, then add that guidance to your rules file.",
        name: "Lenny's Newsletter",
        url: "https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code",
      },
    ],
  },
  {
    id: "ch-6",
    number: 6,
    title: "It can look things up and work with your actual files.",
    navLabel: "Grounding",
    panels: [
      {
        label: "How do I know it's not just making things up again?",
        description: "Skeptic looks at an open laptop on the coffee table showing a file folder, then back at Maven skeptically. One eyebrow raised.",
        image: "/images/ch06-grounding-frame-a-20260221-151017.png",
        gradient: "warm-accent",
      },
      {
        label: "Because it's reading your actual documents.",
        description: "Maven leans forward and points precisely at the file listing on the laptop screen. Her gesture is deliberate, not theatrical.",
        image: "/images/ch06-grounding-frame-b-20260221-151017.png",
        gradient: "warm-accent",
      },
    ],
    body: [
      "The hallucination problem from Chapter 2 had a structural cause: the AI only knew what was in its training data. When you asked about your contracts, your metrics, or last week's meeting notes, it had two choices — admit it didn't know, or fill in the gap. It usually chose the second option.",
      "Today's agents can read your files, search the web, and connect directly to the tools you already use. This isn't a small upgrade. It's the difference between describing your kitchen to a chef over the phone and letting the chef walk in and look around.",
      "Model Context Protocol — MCP — is the open standard that makes tool connections possible. Think of it as app integrations for your AI: connect it to Slack and it can read your messages; connect it to Google Drive and it can find and read your documents; connect it to your CRM and it can look up customer history before your next call. Reid Robinson at Zapier built a system where, after every meeting, the agent reads the transcript, finds the contact in his CRM, enriches the record, and updates it automatically.",
    ],
    sources: [
      {
        idea: "MCPs are 'app integrations for your AI tools.'",
        name: "ChatPRD: Zapier Workflows for CRM Automation",
        url: "https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep",
      },
      {
        idea: "Given MCPs to interact with other tools in our productivity stack — Fireflies, Linear, Notion — it's become my hub for ongoing product research.",
        name: "Lenny's Newsletter, Derek DeHart",
        url: "https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code",
      },
      {
        idea: "The architecture of an AI agent can be reduced to two components: the filesystem as state, and Claude as the orchestrator.",
        name: "@mernit on X",
        url: "https://x.com/mernit/status/2021324284875153544",
      },
    ],
  },
  {
    id: "ch-7",
    number: 7,
    title: "You have real controls — not code, but rules and skills that shape how it works.",
    navLabel: "Controls",
    panels: [
      {
        label: "That's just... English?",
        description: "Skeptic leans in to read a rules document Maven is holding — a printed list visible in large text. He's tilting his head, genuinely puzzled by what he's seeing.",
        image: "/images/ch07-controls-frame-a-20260221-145231.png",
        gradient: "cool-accent",
      },
      {
        label: "You're not programming — you're setting expectations.",
        description: "Maven sets the document down on the table between them, tapping it once. Like you would with a smart new hire.",
        image: "/images/ch07-controls-frame-b-20260221-145231.png",
        gradient: "cool-accent",
      },
    ],
    body: [
      "One of the most common objections to AI at work is: \"I can't control what it does.\" In 2023, that was largely true. You could write a prompt and hope for the best. If the AI didn't follow your instructions, your options were limited to rephrasing.",
      "Now there are rules, skills, and hooks — structured English that shapes how the AI behaves. A rule says: \"Always check with me before sending anything externally.\" A skill encodes your firm's contract review playbook — the specific criteria for NDA triage, the redline language for indemnification clauses, the green/yellow/red routing logic. A hook runs a spell-checker on everything the AI produces before you see it.",
      "These controls aren't deterministic the way code would be. They operate more like instructions to a smart employee — the AI interprets them with judgment. A rule says \"flag any contract over $50K.\" When the AI encounters a $48K contract with an automatic annual renewal clause, it flags it — because the spirit of the rule is about total commitment, not the dollar amount on page one. Hilary Gridley, VP at WHOOP, built a \"Deck Doctor\" by teaching the AI her implicit quality standards. The result: a system that evaluates her team's decks using her actual judgment, encoded and reused.",
    ],
    sources: [
      {
        idea: "Mark Pike (Anthropic legal team, no coding background) built contract redlining systems, marketing review tools, and COI workflows.",
        name: "How Anthropic Uses Claude in Legal",
        url: "https://claude.com/blog/how-anthropic-uses-claude-legal",
      },
      {
        idea: "Hilary Gridley built a 'Deck Doctor' by reverse-engineering her implicit quality standards. Key prompt: 'Be 100 times more specific.'",
        name: "ChatPRD: Scaling Yourself as a Manager",
        url: "https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts",
      },
      {
        idea: "Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps.",
        name: "GitHub: knowledge-work-plugins",
        url: "https://github.com/anthropics/knowledge-work-plugins",
      },
    ],
  },
  {
    id: "ch-8",
    number: 8,
    title: "You're not typing prompts — you're directing work.",
    navLabel: "The Architect",
    panels: [
      {
        label: "So I'd define the criteria upfront — then review what it produces.",
        description: "Skeptic stands at the whiteboard drawing a rough workflow diagram. He's thinking out loud, not asking for permission. The roles have reversed.",
        image: "/images/ch08-architect-frame-a-20260221-145343.png",
        gradient: "warm-accent",
      },
      {
        label: "Your job becomes designing the system and reviewing the work.",
        description: "Maven leans back in the chair, hands clasped, watching him work it out. She's not explaining anymore, just confirming.",
        image: "/images/ch08-architect-frame-b-20260221-145343.png",
        gradient: "warm-accent",
      },
    ],
    body: [
      "\"Prompt engineering\" was a 2023 skill — the art of crafting exactly the right sentence to extract useful output from a one-shot system. It mattered because you had one attempt. The quality of your output depended entirely on the quality of your input.",
      "That model is outdated. Working with an AI agent means setting up a system: defining rules, encoding preferences, connecting tools, and then reviewing what the agent produces. The skill isn't \"write a good sentence.\" It's \"delegate effectively.\"",
      "Teresa Torres built her morning routine as a system, not a prompt. A custom /today command triggers a Python script that scans her task files, assembles a prioritized to-do list with overdue items and in-progress research, and delivers a daily digest. Two automated jobs run in the background: one scanning academic sources in the morning, one summarizing what was found at night. She built this once. Every morning she reviews the output. She's not a developer. She's an architect.",
    ],
    sources: [
      {
        idea: "Torres's custom /today command: Python script scans task files, assembles daily digest. Two cron jobs. Built once, reviewed daily.",
        name: "ChatPRD: Teresa Torres's Claude Code System",
        url: "https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management",
      },
      {
        idea: "Management as AI Superpower — delegation skills become the differentiator as AI agents take on hours-long autonomous work.",
        name: "Referenced via Owen Gregorian",
        url: "https://x.com/OwenGregorian/status/2016841301673820250",
      },
      {
        idea: "Karpathy coined 'vibe coding' (Feb 2025). By late 2025, updated to 'agentic engineering.'",
        name: "Vibe Coding Wikipedia",
        url: "https://en.wikipedia.org/wiki/Vibe_coding",
      },
    ],
  },
  {
    id: "ch-9",
    number: 9,
    title: "The real unlock isn't a smarter brain — it's everything around it.",
    navLabel: "The Harness",
    panels: [
      {
        label: "The model is like the engine. But what makes it useful is all the other stuff.",
        description: "Skeptic taps the MODEL circle on the whiteboard, then sweeps his hand outward to gesture at all the surrounding components: MEMORY, TOOLS, RULES, LOOP, FILES.",
        image: "/images/ch09-harness-frame-a-20260221-145446.png",
        gradient: "cool-accent",
      },
      {
        label: "Now you're getting it.",
        description: "Maven smiles — the first full smile of the book. She's not explaining anymore. Just confirming what he figured out himself.",
        image: "/images/ch09-harness-frame-b-20260221-145446.png",
        gradient: "cool-accent",
      },
    ],
    body: [
      "The models are getting better. GPT-5 hallucinates six times less than its predecessor. Claude Opus 4.6 sustains coherent work across a million tokens. These are real, meaningful improvements, and they matter.",
      "But the step-function change — the thing that turned AI from a novelty into a coworker — isn't the model. It's the harness.",
      "Every chapter in Section 3 has been about something that wraps around the model, not the model itself. The loop (Chapter 4) is harness. Persistent memory (Chapter 5) is harness. Tool connections (Chapter 6) are harness. Rules and skills (Chapter 7) are harness. The role shift (Chapter 8) is the human side of the harness. The model is the engine. The harness is the steering wheel, the GPS, the mirrors, and the road.",
      "The proof of this thesis comes from outside software. The legal plugin that triggered the $285 billion selloff wasn't triggered by a new model. It was triggered by 200 lines of structured text that told an existing model how to do legal review. A product lawyer with no engineering background wrote the harness. A week later, $285 billion in legal software market cap had evaporated. A 2023 model in a 2025 harness is a coworker.",
    ],
    sources: [
      {
        idea: "Claude Code outperforms Cursor using the same model due to superior prompting and scaffolding. The harness matters more than the model.",
        name: "Every.to Vibe Check",
        url: "https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code",
      },
      {
        idea: "The legal plugin: ~200 lines of structured markdown. NDA triage against 13 criteria. Built by Mark Pike, product lawyer, no engineering background.",
        name: "GitHub: knowledge-work-plugins/legal",
        url: "https://github.com/anthropics/knowledge-work-plugins/tree/main/legal",
      },
      {
        idea: "An AI model like Claude is the horse, and a coding assistant like Claude Code is the harness.",
        name: "OfficeChai",
        url: "https://officechai.com/ai/claude-is-like-the-horse-and-claude-code-is-the-harness-anthropics-boris-cherny/",
      },
      {
        idea: "Cursor: $29.3B valuation. $1B ARR in 17 months. Uses other companies' models. The entire value proposition is the harness.",
        name: "CNBC",
        url: "https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html",
      },
    ],
  },
];
