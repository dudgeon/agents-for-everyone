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
    title: "A lawyer with no coding background just built something that helped crash $285 billion in stock value — using a text file.",
    navLabel: "The Bold Claim",
    panels: [
      {
        label: "Maven at the Whiteboard",
        description: "Maven stands at a whiteboard sketching a simple diagram — a document icon with an arrow pointing to a dollar sign with a downward trend line — explaining how a text file disrupted an entire industry.",
        gradient: "warm",
      },
      {
        label: "Skeptic's First Question",
        description: "The Skeptic sits nearby, arms crossed but leaning forward, intrigued despite themselves. A text file did that?",
        gradient: "warm",
      },
    ],
    body: [
      `In January 2026, Anthropic released eleven open-source "plugins" — bundles of instructions, workflows, and tool connections for different job functions. Legal, sales, marketing, finance, customer support. Each plugin was built the same way: structured text files describing how to do the work, connected to the tools people already use.`,
      `The legal plugin was about 200 lines of markdown — a structured text format, not code. It screened NDAs against thirteen criteria, classified them as green, yellow, or red, and generated routing recommendations. A newsletter described it as "first-year law school content dressed up with some clever workflow logic." It was built by Mark Pike, a product lawyer with no engineering background, using plain English descriptions of how legal review should work.`,
      `Thomson Reuters dropped 18%. LegalZoom fell 20%. A Goldman Sachs trader coined a word for it: "SaaSpocalypse." Total damage across the software sector: roughly $285 billion in market capitalization.`,
      `This book is about why that happened — and what it means for your work.`,
    ],
    sources: [
      {
        idea: "Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps.",
        name: "Anthropic knowledge-work-plugins",
        url: "https://github.com/anthropics/knowledge-work-plugins",
      },
      {
        idea: "A text file doing work that billion-dollar companies charge per-seat fees to access.",
        name: "Nate's Newsletter, 200 Lines of Markdown",
        url: "https://natesnewsletter.substack.com/p/200-lines-of-markdown-just-triggered",
      },
      {
        idea: "Thomson Reuters -18%, LegalZoom -20%. Goldman Sachs basket of U.S. software stocks: -6% in a single session.",
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
        label: "The Skeptic's Case",
        description: "The Skeptic counts off on their fingers, animated. A tablet between them shows a headline about AI hallucinations. The Maven sits across from them, not defending — just nodding.",
        gradient: "cool",
      },
      {
        label: "Maven Concedes",
        description: "The Maven meets the Skeptic's eyes. You're right. That was bad. And it wasn't a fluke.",
        gradient: "cool",
      },
    ],
    body: [
      `If you tried AI in 2023 and walked away unimpressed — or worse, burned — you were paying attention.`,
      `ChatGPT launched in November 2022 and reached 100 million users in two months. It could write a decent email, explain a concept, help brainstorm. It could also confidently invent facts, fabricate sources, and present complete fiction as authoritative truth. It had no way to look anything up. No access to your files. No memory between conversations. Every chat started from zero.`,
      `The consequences were real. In May 2023, lawyer Steven Schwartz used ChatGPT to research case law and submitted a brief to federal court containing six fabricated cases — "Martinez v. Delta Air Lines," "Varghese v. China Southern Airlines" — complete with invented citations and legal reasoning. When the judge asked him to explain, Schwartz testified he was "operating under the false perception that it could not possibly be fabricating cases on its own." He and his colleague were sanctioned with $5,000 fines.`,
      `By December, OpenAI's most advanced model had a different problem: it got lazier. GPT-4 Turbo was smarter, cheaper, and had a bigger memory — but users reported it cutting corners, truncating code, responding with "the rest is similar." Intelligence and reliability turned out to be different things. The model got an upgrade. Users got less work done.`,
    ],
    sources: [
      {
        idea: `Schwartz testified he was "operating under the false perception that ChatGPT could not possibly be fabricating cases on its own."`,
        name: "CNN",
        url: "https://www.cnn.com/2023/05/27/business/chat-gpt-avianca-mata-lawyers",
      },
      {
        idea: `GPT-4 Turbo was immediately reported as "lazier" — shorter responses, truncated code blocks, "...rest of the code is similar..."`,
        name: "The Decoder",
        url: "https://the-decoder.com/openai-looks-into-complaints-about-lazy-chatgpt-with-gpt-4/",
      },
      {
        idea: "ChatGPT reached 1 million users in 5 days and 100 million in two months — the fastest consumer app adoption in history.",
        name: "History.com",
        url: "https://www.history.com/this-day-in-history/november-30/chatgpt-released-openai",
      },
    ],
  },
  {
    id: "ch-3",
    number: 3,
    title: "We've heard \"this time it's different\" before — remember when AI agents were going to change everything?",
    navLabel: "The Hype Graveyard",
    panels: [
      {
        label: "The Graveyard of Promises",
        description: "The Skeptic sits back, arms behind head, grinning — they're enjoying this part. A board behind them lists failed promises: AutoGPT, BabyAGI, ChatGPT Plugins, GPT Store, Devin — each with a small X.",
        gradient: "warm",
      },
      {
        label: "Maven Admits It",
        description: "Maven leans forward, hands up in a fair-point gesture. I'm not going to defend any of that. The vision was right. The execution was a disaster.",
        gradient: "warm",
      },
    ],
    body: [
      `In March 2023, two open-source projects — AutoGPT and BabyAGI — promised autonomous AI agents that could set goals, break them into tasks, execute them, and iterate. AutoGPT became the number one GitHub repository of 2023 with 174,000 stars. Fortune called it "taking Silicon Valley by storm." Andrej Karpathy, co-founder of OpenAI, called it "the next frontier of prompt engineering."`,
      `The reality: agents got stuck in infinite loops for entire nights, forgot what they'd already done, never asked clarifying questions, and burned through API credits with nothing to show for it. Tom's Hardware's review headline: "Auto-GPT and BabyAGI Are AI's New Hotness, But They Suck Right Now." By late 2023, the AutoGPT team removed their external database support because agents didn't generate enough useful information to need one.`,
      `The pattern repeated. ChatGPT Plugins launched in March 2023 as an "App Store moment for AI" — and were quietly killed by April 2024 because the model couldn't reliably choose or use them. The GPT Store opened in January 2024 with 3 million custom GPTs; researchers found a 97% success rate extracting their supposedly secret instructions. Devin, announced in March 2024 as the "first fully autonomous AI software engineer," was independently tested in January 2025 and achieved a 15% success rate — with "no discernible pattern to predict which tasks would work."`,
      `So when someone says "AI agents are different now," your skepticism isn't cynicism. It's experience.`,
    ],
    sources: [
      {
        idea: `Tom's Hardware: "Auto-GPT and BabyAGI Are AI's New Hotness, But They Suck Right Now."`,
        name: "Tom's Hardware",
        url: "https://www.tomshardware.com/news/autonomous-agents-new-big-thing",
      },
      {
        idea: "Researchers tested 200+ custom GPTs and found a 97.2% success rate extracting system prompts and 100% success rate leaking uploaded knowledge files.",
        name: "ArXiv: Assessing Prompt Injection Risks",
        url: "https://arxiv.org/html/2311.11538v2",
      },
      {
        idea: `Answer.AI tested Devin on 20 real-world tasks: 14 failures, 3 successes, 3 inconclusive — a 15% success rate. They "couldn't discern any pattern to predict which tasks would work."`,
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
        label: "The Loop Explained",
        description: "Maven draws a loop diagram on the whiteboard: PLAN → ACT → OBSERVE → ADJUST → back to PLAN. The Skeptic leans forward, studying it. The dynamic has shifted — Skeptic is curious, not dismissive.",
        gradient: "warm-accent",
      },
      {
        label: "Error Recovery",
        description: "The Skeptic asks what happens when it gets the first step wrong. Maven answers: it reads the error message and tries a different approach. Like you would.",
        gradient: "warm-accent",
      },
    ],
    body: [
      `The AI you tried in 2023 worked like this: you typed something in, it generated something back, and you were done. One shot. If it got it wrong, you'd rephrase and try again. The AI never tried again on its own. It never checked its work. It never read an error message and adjusted.`,
      `That's not how it works anymore.`,
      `Simon Willison, one of the most respected voices in AI tooling, defines an AI agent as "an LLM that runs tools in a loop to achieve a goal." That loop — plan, act, observe, adjust — is the structural difference between a chatbot and a coworker. The chatbot gives you an answer. The agent tries something, sees what happens, and course-corrects.`,
      `This sounds abstract until you see it. When Claude Code encounters a failing test, it doesn't ask you what to do. It reads the error output, identifies the likely cause, edits the file, runs the test again, and repeats until it passes — or explains why it can't. When it searches for information and the first source is paywalled, it tries another source. When it misunderstands a file structure, it explores, reads, and adjusts its mental model.`,
      `The loop is also the answer to the AutoGPT failure from the last chapter. AutoGPT had the right idea — tools in a loop — but the models couldn't reliably observe their own errors, and the harnesses couldn't give them enough context to adjust. The concept wasn't wrong. The execution needed two more years of model and tooling improvements to actually work.`,
    ],
    sources: [
      {
        idea: `"An LLM agent runs tools in a loop to achieve a goal."`,
        name: "Simon Willison",
        url: "https://simonw.substack.com/p/i-think-agent-may-finally-have-a",
      },
      {
        idea: `Every.to on Claude Code: "better than anything I have used on the agent front" — and critically, "Claude Code outperforms Cursor using the same model due to superior prompting and scaffolding."`,
        name: "Every.to Vibe Check",
        url: "https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code",
      },
      {
        idea: `"An AI model like Claude is the horse, and a coding assistant like Claude Code is the harness."`,
        name: "Boris Cherny via OfficeChai",
        url: "https://officechai.com/ai/claude-is-like-the-horse-and-claude-code-is-the-harness-anthropics-boris-cherny/",
      },
    ],
  },
  {
    id: "ch-5",
    number: 5,
    title: "It remembers who you are and how you work.",
    navLabel: "The Memory",
    panels: [
      {
        label: "The Instruction File",
        description: "Maven shows the Skeptic a document on screen — a CLAUDE.md file with visible plain-English rules: 'When reviewing contracts, always flag indemnification clauses first.' The Skeptic peers at it with genuine surprise.",
        gradient: "cool-accent",
      },
      {
        label: "Once and Done",
        description: "The Skeptic asks: Wait — I'd have to explain my whole job to it? Maven answers: Once. And then it remembers. Every session after that starts where you left off.",
        gradient: "cool-accent",
      },
    ],
    body: [
      `In 2023, every AI conversation started from scratch. You'd explain your role, your preferences, your context — and then do it again tomorrow. It was like training a new intern every morning who had no memory of yesterday.`,
      `That problem is solved. Tools like Claude Code read a project instruction file — called CLAUDE.md — at the start of every session. This file tells the AI who you are, how you work, and what your conventions are. It's written in plain English. "When reviewing contracts, always flag indemnification clauses first." "My brand voice is conversational but not casual — think New York Times, not Twitter." "Never send anything externally without checking with me first."`,
      `Teresa Torres, a product management consultant, built her system iteratively. Instead of crafting elaborate prompts, she broke her context into dozens of small files — her business profile, her writing style, her research interests — and taught Claude where to find each one. At the end of each work session, she asks: "What did you learn today that we should document?" The instruction file grows as a side effect of working together. She calls it "lazy prompting" — the system already knows her context, so she just describes what she wants.`,
      `This is the compounding effect. Every correction you make, every preference you express, every convention you document — it persists. Session ten is better than session one, not because the AI got smarter, but because it knows more about your work.`,
    ],
    sources: [
      {
        idea: `Torres breaks her context into dozens of focused markdown files. Instead of crafting lengthy prompts, "she just works — the agent reads what it needs." She calls it "lazy prompting."`,
        name: "ChatPRD: Teresa Torres's Claude Code System",
        url: "https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management",
      },
      {
        idea: `Torres comparison table — Chat vs. Claude Code: Memory ("search past chats" vs. "all files act as memory"), Reusability ("start fresh each chat" vs. "systems that compound over time").`,
        name: "Product Talk: Claude Code — What It Is and How It's Different",
        url: "https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/",
      },
      {
        idea: `"After solving a problem, ask the AI how to prompt it better next time, then add that guidance to your rules file." Single file achieves compounding improvement across sessions.`,
        name: "Lenny's Newsletter",
        url: "https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code",
      },
    ],
  },
  {
    id: "ch-6",
    number: 6,
    title: "It can look things up and work with your actual files.",
    navLabel: "The Grounding",
    panels: [
      {
        label: "Old Way vs. New Way",
        description: "Split composition: left shows a person copy-pasting text from a document into a chat window — cramped and manual. Right shows the AI reading directly from a folder of files. Maven gestures toward the right side.",
        gradient: "warm-accent",
      },
      {
        label: "Real Documents",
        description: "The Skeptic asks how they know it's not just making things up again. Maven answers: because this time it's reading your actual documents — not guessing from memory.",
        gradient: "warm-accent",
      },
    ],
    body: [
      `The hallucination problem from Chapter 2 had a structural cause: the AI only knew what was in its training data. When you asked about your contracts, your team's metrics, or last week's meeting notes, it had two choices — admit it didn't know, or make something up. It usually chose the second one.`,
      `Today's AI agents can read your files, search the web, and connect to your existing tools. This isn't a small upgrade. It's the difference between describing your kitchen to a chef over the phone and letting the chef into your kitchen.`,
      `Model Context Protocol — MCP — is the open standard that makes this possible. Think of it as app integrations for your AI tools. Connect your AI to Slack, and it can read your messages. Connect it to Google Drive, and it can find and read your documents. Connect it to your CRM, and it can look up a customer's history before your next call. Each connection unlocks new workflows without requiring the user to learn anything new.`,
      `Derek DeHart, a product manager, connected Claude Code to Fireflies (call transcription), Linear (project management), and Notion (documentation). It became his "hub for ongoing product research and development" — synthesizing customer call transcripts, compiling evidence for product hypotheses, and creating project tickets, all from a single conversation. Reid Robinson at Zapier built a similar system: after every meeting, his AI reads the transcript, searches his CRM for the contact, enriches the record, and updates it. A fifteen-minute manual task became a copy-paste.`,
    ],
    sources: [
      {
        idea: `MCPs are "app integrations for your AI tools." That's the explanation for non-technical people.`,
        name: "ChatPRD: Zapier Workflows for CRM Automation",
        url: "https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep",
      },
      {
        idea: `"Given MCPs to interact with other tools in our productivity stack — Fireflies, Linear, Notion — it's become my hub for ongoing product research and development."`,
        name: "Lenny's Newsletter",
        url: "https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code",
      },
      {
        idea: `"The architecture of an AI agent can be reduced to two components: the filesystem as state, and Claude as the orchestrator."`,
        name: "@mernit on X",
        url: "https://x.com/mernit/status/2021324284875153544",
      },
    ],
  },
  {
    id: "ch-7",
    number: 7,
    title: "You have real controls — not code, but rules and skills that shape how it works.",
    navLabel: "The Controls",
    panels: [
      {
        label: "Plain English Rules",
        description: "Maven holds up a document showing rules written in plain English — visible enough to read: 'Never send without approval. Use AP style for all public content. Flag any contract over $50K.' The Skeptic's eyes widen.",
        gradient: "cool-accent",
      },
      {
        label: "Setting Expectations",
        description: "The Skeptic reads: 'That's just... English?' Maven nods: That's the point. You're not programming — you're setting expectations.",
        gradient: "cool-accent",
      },
    ],
    body: [
      `One of the most common objections to AI at work is: "I can't control what it does." In 2023, that was largely true. You could write a careful prompt and hope for the best. The AI might follow your instructions. It might not. There was no enforcement mechanism.`,
      `Now there are rules, skills, and hooks. They aren't code — they're structured English that shapes how the AI behaves. A rule might say: "Always check with me before sending anything externally." A skill might encode your firm's contract review playbook — the thirteen criteria for NDA triage, the specific redline language for indemnification clauses, the routing logic for green/yellow/red classification. A hook might automatically run a spell-checker on everything the AI writes before showing it to you.`,
      `These controls aren't deterministic the way an if/then statement in software would be. You can't guarantee the AI will follow every rule 100% of the time, any more than you can guarantee a new employee will. But they're real, they're powerful, and they compound. Hilary Gridley, VP at WHOOP, built a "Deck Doctor" by reverse-engineering her implicit quality standards. She had the AI analyze her before-and-after slide edits, told it to be "100 times more specific" about what made the difference, and turned those findings into a custom evaluator. Now her team gets consistent feedback matching her standards — without her reviewing every deck.`,
      `The key insight: you're not programming. You're setting expectations, the way you would with a smart new hire. And just like a new hire, the AI gets better at meeting those expectations over time as the instruction set grows.`,
    ],
    sources: [
      {
        idea: `Hilary Gridley built a "Deck Doctor" by reverse-engineering her implicit quality standards. Key prompt: "Be 100 times more specific."`,
        name: "ChatPRD: Scaling Yourself as a Manager with Custom GPTs",
        url: "https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts",
      },
      {
        idea: `Mark Pike (Anthropic legal team, no coding background) built marketing review tools, contract redlining systems, and COI workflows using skills and MCP. "I just typed a normal sentence, describing what I wanted. And it worked."`,
        name: "How Anthropic Uses Claude in Legal",
        url: "https://claude.com/blog/how-anthropic-uses-claude-legal",
      },
      {
        idea: `Cowork plugin architecture: "Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps."`,
        name: "GitHub: knowledge-work-plugins",
        url: "https://github.com/anthropics/knowledge-work-plugins",
      },
      {
        idea: "Meta-skill pattern — a skill that generates other skills. Build one factory skill, then produce domain-specific skills consistently.",
        name: "ChatPRD: Claude Skills Explained",
        url: "https://www.chatprd.ai/how-i-ai/claude-skills-explained",
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
        label: "The New Role",
        description: "The dynamic has shifted. The Skeptic leans forward now, engaged, sketching a workflow diagram — a proposal review checklist. Maven watches, contributing but not leading. The Skeptic is becoming the architect.",
        gradient: "warm-accent",
      },
      {
        label: "Managing, Not Doing",
        description: "The Skeptic thinks through the implications: So I'd set up the rules... and then just review what it produces? Like managing someone? Maven: Exactly like managing someone.",
        gradient: "warm-accent",
      },
    ],
    body: [
      `"Prompt engineering" was a 2023 skill — the art of phrasing your request just right to get a useful response from a chatbot. It mattered because you had one shot. The quality of the output depended on the quality of your input sentence.`,
      `That mental model is outdated. When you work with an AI agent, you're not crafting a single prompt. You're setting up a system: defining rules, connecting tools, encoding your preferences, and then reviewing what the agent produces. The skill isn't "write a good sentence." It's "delegate effectively."`,
      `Ethan Mollick, a Wharton professor who's studied human-AI collaboration more rigorously than almost anyone, calls this shift "management as AI superpower." As AI agents become capable of sustained autonomous work, the value of delegation skills — breaking tasks down, setting context, defining success criteria — increases dramatically. In one experiment, he had students create an entire startup from scratch in four days using AI agents. The students who succeeded weren't the best prompters. They were the best managers.`,
      `Andrej Karpathy, co-founder of OpenAI, captured the shift in terminology. In February 2025, he coined "vibe coding" — a playful term for letting AI write your code while you just describe what you want. By late 2025, he'd updated the term to "agentic engineering," acknowledging that what started as a novelty had become the professional default. The playful name couldn't contain what it had become.`,
    ],
    sources: [
      {
        idea: `Mollick: "Management as AI Superpower" — as AI agents become capable of hours-long autonomous work, delegation skills become the differentiator.`,
        name: "Referenced via Owen Gregorian",
        url: "https://x.com/OwenGregorian/status/2016841301673820250",
      },
      {
        idea: `Karpathy coined "vibe coding" (Feb 2025): "You fully give in to the vibes, embrace exponentials, and forget that the code even exists." By late 2025, updated to "agentic engineering."`,
        name: "Vibe Coding Wikipedia",
        url: "https://en.wikipedia.org/wiki/Vibe_coding",
      },
      {
        idea: "BCG study (758 consultants): AI users completed 12.2% more tasks, 25.1% faster, at 40% higher quality. But on tasks outside AI's capability frontier, users were 19 percentage points less accurate.",
        name: "Mollick: Centaurs and Cyborgs on the Jagged Frontier",
        url: "https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged",
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
        label: "Skeptic at the Whiteboard",
        description: "The Skeptic is at the whiteboard now, drawing a diagram: MODEL in the center, surrounded by MEMORY, TOOLS, RULES, LOOP, FILES. Maven stands behind them, hands in pockets, watching with satisfaction.",
        gradient: "cool-accent",
      },
      {
        label: "Now You're Getting It",
        description: "The Skeptic explains: A 2025 engine in a 2022 chassis is still a better car that can't go anywhere. Maven smiles: Now you're getting it. The student has become the teacher.",
        gradient: "cool-accent",
      },
    ],
    body: [
      `The models are getting better. They'll likely keep getting better for a while. GPT-5 hallucinates six times less than its predecessor. Claude Opus 4.6 can sustain coherent work across a million tokens of context. These are real, meaningful improvements, and they matter.`,
      `But the step-function change — the thing that turned AI from a novelty into a coworker — isn't the model. It's the harness.`,
      `Every chapter in this section has been about something that wraps around the model, not the model itself. The loop (Chapter 4) is harness. Persistent memory (Chapter 5) is harness. Tool connections (Chapter 6) are harness. Rules and skills (Chapter 7) are harness. The role shift to delegation (Chapter 8) is harness. The model is the engine. The harness is the steering wheel, the GPS, the mirrors, and the road.`,
      `The proof is in the data. Every.to found that Claude Code "outperforms Cursor using the same model due to superior prompting and scaffolding." Same brain, different harness, dramatically different results. Cursor — a company worth $29.3 billion — uses other companies' models. Its entire value is the harness. And the $285 billion selloff wasn't triggered by a new model. It was triggered by 200 lines of markdown — a harness — that told an existing model how to do legal review.`,
      `A 2025 model in a 2022 chat box is still just a better chat box. A 2023 model in a 2025 harness is a coworker.`,
    ],
    sources: [
      {
        idea: `"Claude Code outperforms Cursor using the same model due to superior prompting and scaffolding. The harness matters more than the model."`,
        name: "Every.to Vibe Check: Claude 3.7 Sonnet and Claude Code",
        url: "https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code",
      },
      {
        idea: "Cursor uses Claude, GPT-4, and other models interchangeably. $29.3B valuation. $1B ARR in 17 months with zero marketing spend. The value is entirely in the harness.",
        name: "CNBC",
        url: "https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html",
      },
      {
        idea: `Boris Cherny, creator of Claude Code: "An AI model like Claude is the horse, and a coding assistant like Claude Code is the harness."`,
        name: "OfficeChai",
        url: "https://officechai.com/ai/claude-is-like-the-horse-and-claude-code-is-the-harness-anthropics-boris-cherny/",
      },
      {
        idea: "The legal plugin that triggered the $285B selloff: ~200 lines of structured markdown. NDA triage against 13 criteria. No code. No infrastructure. Just the harness.",
        name: "GitHub: knowledge-work-plugins/legal",
        url: "https://github.com/anthropics/knowledge-work-plugins/tree/main/legal",
      },
    ],
  },
];
