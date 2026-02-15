# Agents for Everyone — Draft 001

_Trial run: 2026-02-15. Purpose: expose gaps in project structure. Not intended as final copy._

---

## Chapter 1: A lawyer with no coding background just built something that helped crash $285 billion in stock value — using a text file.

{>>GAP-01 (bold claim specificity): This headline is dramatic and specific, but may trigger the hype reflex the structure doc warns against. Is a $285B market event the right opening, or should the bold claim be more personally relatable — about YOUR work, not a financial headline? Needs user decision.<<}

<!-- IMG
id: ch01-bold-claim
characters: maven, skeptic
aspect: 16:9
mood: confident, intriguing
panel_direction: Maven is standing at a whiteboard, drawing a simple diagram. Skeptic sits nearby in an office chair, arms crossed but leaning forward slightly — intrigued despite themselves.
maven_says: "In January 2026, a lawyer at Anthropic — no coding background — built a legal review system using plain English instructions. When they open-sourced it, software stocks dropped $285 billion in a week."
skeptic_says: "A text file did that?"
background: A modern office. On the whiteboard behind the Maven, a simple sketch: a document icon with an arrow pointing to a dollar sign with a downward trend line.
-->

{>>GAP-04 (panel art direction): This panel_direction is prose, not a format our image pipeline can consume. Need: (a) a locked visual style guide, (b) a translation layer from narrative panel descriptions to generation prompts. Blocked on Phase 5 character/visual design.<<}

In January 2026, Anthropic released eleven open-source "plugins" — bundles of instructions, workflows, and tool connections for different job functions. Legal, sales, marketing, finance, customer support. Each plugin was built the same way: structured text files describing how to do the work, connected to the tools people already use.

The legal plugin was about 200 lines of markdown — a structured text format, not code. It screened NDAs against thirteen criteria, classified them as green, yellow, or red, and generated routing recommendations. A newsletter described it as "first-year law school content dressed up with some clever workflow logic." It was built by Mark Pike, a product lawyer with no engineering background, using plain English descriptions of how legal review should work.

Thomson Reuters dropped 18%. LegalZoom fell 20%. A Goldman Sachs trader coined a word for it: "SaaSpocalypse." Total damage across the software sector: roughly $285 billion in market capitalization.

This book is about why that happened — and what it means for your work.

### Sources

> "Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps."
> — [Anthropic knowledge-work-plugins repository](https://github.com/anthropics/knowledge-work-plugins)

> "A text file doing work that billion-dollar companies charge per-seat fees to access."
> — [Nate's Newsletter, "200 Lines of Markdown"](https://natesnewsletter.substack.com/p/200-lines-of-markdown-just-triggered)

> Thomson Reuters -18%, RELX -14%, Wolters Kluwer -13%, LegalZoom -20%, FactSet -10%. Goldman Sachs basket of U.S. software stocks: -6% in a single session.
> — [CNBC](https://www.cnbc.com/2026/02/06/ai-anthropic-tools-saas-software-stocks-selloff.html), [Fortune](https://fortune.com/2026/02/06/anthropic-claude-opus-4-6-stock-selloff-new-upgrade/)

---

## Chapter 2: In 2023, AI was confidently wrong about everything — and the people selling it didn't seem to notice.

{>>GAP-05 (tone): This chapter's body text is conversational but the sources section is academic. Tone guide needed to lock whether sources should read like footnotes, pull-quotes, or something else. Applies to all chapters.<<}

<!-- IMG
id: ch02-skepticism-earned
characters: skeptic, maven
aspect: 16:9
mood: frustrated, validating
panel_direction: Skeptic is animated, counting off on their fingers. Maven sits across from them at a coffee shop table, nodding — not defending, not arguing. A newspaper or tablet between them shows a headline about AI.
skeptic_says: "A lawyer submitted fake cases to a federal judge because ChatGPT made them up. The AI didn't just get it wrong — it invented six court cases with full citations. And the lawyer said he didn't think it COULD fabricate things."
maven_says: "You're right. That was bad. And it wasn't a fluke."
background: Coffee shop. Warm lighting. The dynamic is two people having an honest conversation, not a debate.
-->

{>>GAP-03 (character voice): The Skeptic's dialog here is functional but generic. Without a character profile (age, profession, what specifically burned them on AI, speech patterns), this reads like "generic skeptical person." Need at least a basic voice profile for both characters.<<}

If you tried AI in 2023 and walked away unimpressed — or worse, burned — you were paying attention.

ChatGPT launched in November 2022 and reached 100 million users in two months. It could write a decent email, explain a concept, help brainstorm. It could also confidently invent facts, fabricate sources, and present complete fiction as authoritative truth. It had no way to look anything up. No access to your files. No memory between conversations. Every chat started from zero.

The consequences were real. In May 2023, lawyer Steven Schwartz used ChatGPT to research case law and submitted a brief to federal court containing six fabricated cases — "Martinez v. Delta Air Lines," "Varghese v. China Southern Airlines" — complete with invented citations and legal reasoning. When the judge asked him to explain, Schwartz testified he was "operating under the false perception that it could not possibly be fabricating cases on its own." He and his colleague were sanctioned with $5,000 fines.

By December, OpenAI's most advanced model had a different problem: it got lazier. GPT-4 Turbo was smarter, cheaper, and had a bigger memory — but users reported it cutting corners, truncating code, responding with "the rest is similar." Intelligence and reliability turned out to be different things. The model got an upgrade. Users got less work done.

### Sources

> Schwartz testified he was "operating under the false perception that [ChatGPT] could not possibly be fabricating cases on its own."
> — [CNN](https://www.cnn.com/2023/05/27/business/chat-gpt-avianca-mata-lawyers), [Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023)](https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.)

> GPT-4 Turbo was immediately reported as "lazier" — shorter responses, truncated code blocks, "...rest of the code is similar..."
> — [OpenAI Community Forum](https://community.openai.com/t/chatgpt-4-defaults-to-lazy/560886), [The Decoder](https://the-decoder.com/openai-looks-into-complaints-about-lazy-chatgpt-with-gpt-4/)

> ChatGPT launched as a six-sentence announcement. It reached 1 million users in 5 days and 100 million in two months — the fastest consumer app adoption in history.
> — [History.com](https://www.history.com/this-day-in-history/november-30/chatgpt-released-openai)

---

## Chapter 3: We've heard "this time it's different" before — remember when AI agents were going to change everything?

<!-- IMG
id: ch03-hype-graveyard
characters: skeptic, maven
aspect: 16:9
mood: wry, honest
panel_direction: Skeptic is sitting back, arms behind head, grinning — they're enjoying this part. Maven leans forward, hands up in a "fair point" gesture. Between them, perhaps on a screen or board, a list or graveyard of failed promises.
skeptic_says: "AutoGPT got 174,000 GitHub stars and was the number one repository of 2023. It also got stuck in infinite loops all night. Then there was Devin, the 'first AI software engineer' — 85% failure rate."
maven_says: "I'm not going to defend any of that. The vision was right. The execution was a disaster."
background: Same coffee shop. Maybe a whiteboard or screen behind them listing: AutoGPT, BabyAGI, ChatGPT Plugins, GPT Store, Devin — each with a small X or skull icon.
-->

In March 2023, two open-source projects — AutoGPT and BabyAGI — promised autonomous AI agents that could set goals, break them into tasks, execute them, and iterate. AutoGPT became the number one GitHub repository of 2023 with 174,000 stars. Fortune called it "taking Silicon Valley by storm." Andrej Karpathy, co-founder of OpenAI, called it "the next frontier of prompt engineering."

The reality: agents got stuck in infinite loops for entire nights, forgot what they'd already done, never asked clarifying questions, and burned through API credits with nothing to show for it. Tom's Hardware's review headline: "Auto-GPT and BabyAGI Are AI's New Hotness, But They Suck Right Now." By late 2023, the AutoGPT team removed their external database support because agents didn't generate enough useful information to need one.

The pattern repeated. ChatGPT Plugins launched in March 2023 as an "App Store moment for AI" — and were quietly killed by April 2024 because the model couldn't reliably choose or use them. The GPT Store opened in January 2024 with 3 million custom GPTs; researchers found a 97% success rate extracting their supposedly secret instructions. Devin, announced in March 2024 as the "first fully autonomous AI software engineer," was independently tested in January 2025 and achieved a 15% success rate — with "no discernible pattern to predict which tasks would work."

So when someone says "AI agents are different now," your skepticism isn't cynicism. It's experience.

### Sources

> Tom's Hardware: "Auto-GPT and BabyAGI Are AI's New Hotness, But They Suck Right Now."
> — [Tom's Hardware](https://www.tomshardware.com/news/autonomous-agents-new-big-thing)

> Researchers tested 200+ custom GPTs and found a 97.2% success rate extracting system prompts and 100% success rate leaking uploaded knowledge files.
> — [ArXiv: Assessing Prompt Injection Risks](https://arxiv.org/html/2311.11538v2)

> Answer.AI tested Devin on 20 real-world tasks: 14 failures, 3 successes, 3 inconclusive — a 15% success rate. They "couldn't discern any pattern to predict which tasks would work."
> — [Answer.AI](https://www.answer.ai/posts/2025-01-08-devin.html)

> AutoGPT reached 174,000+ GitHub stars — the #1 GitHub repository of 2023. Significant Gravitas raised $12M in October 2023.
> — [AutoGPT Wikipedia](https://en.wikipedia.org/wiki/AutoGPT)

---

## Chapter 4: AI doesn't just answer anymore — it plans, tries, checks, and adjusts.

{>>GAP-02 (non-SWE examples): This chapter's examples are entirely SWE-adjacent (Claude Code, failing tests, paywalled sources). Need a vivid non-SWE example of the agentic loop in action — e.g., Willison's Cowork blog-draft review (46 files, 44 web searches, 3 candidates identified) or the Anthropic marketing team's ad variation workflow. The loop concept is universal; the examples should prove it.<<}

{>>GAP-09 (jagged frontier): Mollick's jagged frontier concept — the idea that AI capabilities are unpredictably uneven — would be powerful here as a bridge from Section 2's skepticism. Something like: "The frontier is still jagged. But now the agent can check its own work against the edge." This would acknowledge real limitations while explaining what changed.<<}

<!-- IMG
id: ch04-the-loop
characters: skeptic, maven
aspect: 16:9
mood: curious, explanatory
panel_direction: Maven is at a whiteboard drawing a loop diagram: PLAN → ACT → OBSERVE → ADJUST → (back to PLAN). Skeptic leans forward in their chair, studying the diagram. The dynamic has shifted — Skeptic is curious, not dismissive.
skeptic_says: "Okay but what happens when it gets the first step wrong?"
maven_says: "It reads the error message and tries a different approach. Like you would."
background: Office or workshop. The loop diagram is central to the composition. Maybe show a small "before" sketch to one side: a simple arrow from INPUT → OUTPUT (the old model).
-->

The AI you tried in 2023 worked like this: you typed something in, it generated something back, and you were done. One shot. If it got it wrong, you'd rephrase and try again. The AI never tried again on its own. It never checked its work. It never read an error message and adjusted.

That's not how it works anymore.

Simon Willison, one of the most respected voices in AI tooling, defines an AI agent as "an LLM that runs tools in a loop to achieve a goal." That loop — plan, act, observe, adjust — is the structural difference between a chatbot and a coworker. The chatbot gives you an answer. The agent tries something, sees what happens, and course-corrects.

This sounds abstract until you see it. When Claude Code encounters a failing test, it doesn't ask you what to do. It reads the error output, identifies the likely cause, edits the file, runs the test again, and repeats until it passes — or explains why it can't. When it searches for information and the first source is paywalled, it tries another source. When it misunderstands a file structure, it explores, reads, and adjusts its mental model.

The loop is also the answer to the AutoGPT failure from the last chapter. AutoGPT had the right idea — tools in a loop — but the models couldn't reliably observe their own errors, and the harnesses couldn't give them enough context to adjust. The concept wasn't wrong. The execution needed two more years of model and tooling improvements to actually work.

### Sources

> "An LLM agent runs tools in a loop to achieve a goal."
> — [Simon Willison](https://simonw.substack.com/p/i-think-agent-may-finally-have-a)

> Every.to on Claude Code: "better than anything I have used on the agent front" — and critically, "Claude Code outperforms Cursor using the same model due to superior prompting and scaffolding."
> — [Every.to Vibe Check](https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code)

> "An AI model like Claude is the horse, and a coding assistant like Claude Code is the harness."
> — Boris Cherny, creator of Claude Code, [via OfficeChai](https://officechai.com/ai/claude-is-like-the-horse-and-claude-code-is-the-harness-anthropics-boris-cherny/)

---

## Chapter 5: It remembers who you are and how you work.

<!-- IMG
id: ch05-memory
characters: skeptic, maven
aspect: 16:9
mood: surprised, warm
panel_direction: Maven shows Skeptic a screen or document — a CLAUDE.md file or project instruction document. Skeptic peers at it with genuine surprise. The file should have visible text (even if not fully legible) showing things like "When I say 'format this,' use AP style" or "Always check with legal before publishing."
skeptic_says: "Wait — I'd have to explain my whole job to it?"
maven_says: "Once. And then it remembers. Every session after that starts where you left off."
background: Same setting. The screen/document is the focal point. Maybe show a stack of previous conversations fading behind the current one, to convey persistence.
-->

In 2023, every AI conversation started from scratch. You'd explain your role, your preferences, your context — and then do it again tomorrow. It was like training a new intern every morning who had no memory of yesterday.

That problem is solved. Tools like Claude Code read a project instruction file — called CLAUDE.md — at the start of every session. This file tells the AI who you are, how you work, and what your conventions are. It's written in plain English. "When reviewing contracts, always flag indemnification clauses first." "My brand voice is conversational but not casual — think New York Times, not Twitter." "Never send anything externally without checking with me first."

Teresa Torres, a product management consultant, built her system iteratively. Instead of crafting elaborate prompts, she broke her context into dozens of small files — her business profile, her writing style, her research interests — and taught Claude where to find each one. At the end of each work session, she asks: "What did you learn today that we should document?" The instruction file grows as a side effect of working together. She calls it "lazy prompting" — the system already knows her context, so she just describes what she wants.

This is the compounding effect. Every correction you make, every preference you express, every convention you document — it persists. Session ten is better than session one, not because the AI got smarter, but because it knows more about your work.

### Sources

> Torres breaks her context into dozens of focused markdown files. Instead of crafting lengthy prompts, "she just works — the agent reads what it needs." She calls it "lazy prompting."
> — [ChatPRD: Teresa Torres's Claude Code System](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management)

> Torres comparison table — Chat vs. Claude Code: Memory ("search past chats" vs. "all files act as memory"), Reusability ("start fresh each chat" vs. "systems that compound over time").
> — [Product Talk: Claude Code — What It Is and How It's Different](https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/)

> Lazar Jovanovic, professional "vibe coder": "After solving a problem, ask the AI how to prompt it better next time, then add that guidance to your rules file." Single file achieves compounding improvement across sessions.
> — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code)

---

## Chapter 6: It can look things up and work with your actual files.

<!-- IMG
id: ch06-grounding
characters: skeptic, maven
aspect: 16:9
mood: revelatory, practical
panel_direction: Split composition. Left side shows the "old way": a person copy-pasting text from a document into a chat window. Right side shows the "new way": the AI reading directly from a folder of files on a desk/computer. Maven gestures toward the right side. Skeptic looks at the contrast.
skeptic_says: "How do I know it's not just making things up again?"
maven_says: "Because this time it's reading your actual documents — not guessing from memory."
background: The split composition should make the before/after visceral. Left side is cramped, manual, tedious. Right side is clean and direct.
-->

The hallucination problem from Chapter 2 had a structural cause: the AI only knew what was in its training data. When you asked about your contracts, your team's metrics, or last week's meeting notes, it had two choices — admit it didn't know, or make something up. It usually chose the second one.

Today's AI agents can read your files, search the web, and connect to your existing tools. This isn't a small upgrade. It's the difference between describing your kitchen to a chef over the phone and letting the chef into your kitchen.

Model Context Protocol — MCP — is the open standard that makes this possible. Think of it as app integrations for your AI tools. Connect your AI to Slack, and it can read your messages. Connect it to Google Drive, and it can find and read your documents. Connect it to your CRM, and it can look up a customer's history before your next call. Each connection unlocks new workflows without requiring the user to learn anything new.

Derek DeHart, a product manager, connected Claude Code to Fireflies (call transcription), Linear (project management), and Notion (documentation). It became his "hub for ongoing product research and development" — synthesizing customer call transcripts, compiling evidence for product hypotheses, and creating project tickets, all from a single conversation. Reid Robinson at Zapier built a similar system: after every meeting, his AI reads the transcript, searches his CRM for the contact, enriches the record, and updates it. A fifteen-minute manual task became a copy-paste.

### Sources

> Reid Robinson's frame: MCPs are "app integrations for your AI tools." That's it. That's the explanation for non-technical people.
> — [ChatPRD: Zapier Workflows for CRM Automation](https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep)

> Derek DeHart: "Given MCPs to interact with other tools in our productivity stack — Fireflies, Linear, Notion — it's become my hub for ongoing product research and development."
> — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code)

> Openclaw (@mernit): "The architecture of an AI agent can be reduced to two components: the filesystem as state, and Claude as the orchestrator."
> — [@mernit on X](https://x.com/mernit/status/2021324284875153544)

---

## Chapter 7: You have real controls — not code, but rules and skills that shape how it works.

{>>GAP-10 (not deterministic): This chapter says rules "aren't deterministic the way an if/then statement in software would be" but doesn't give a vivid example of the AI interpreting a rule with JUDGMENT. Need a concrete case: e.g., a rule says "flag anything over $50K" and the agent flags a $48K contract because it noticed an automatic renewal clause that would push total value over the threshold. The AI understood the SPIRIT of the rule, not just the letter. That's the "not code, but not nothing either" nuance.<<}

<!-- IMG
id: ch07-controls
characters: skeptic, maven
aspect: 16:9
mood: surprised, empowered
panel_direction: Maven holds up or displays a document/screen showing a skill or rule — written in plain English. Skeptic reads it, eyes widening. The rule should be legible enough to see it's natural language, not code.
skeptic_says: "That's just... English?"
maven_says: "That's the point. 'Always check with me before sending externally.' 'When I say format this, use our house style.' You're not programming — you're setting expectations."
background: The document/screen should be prominent. Perhaps show a small snippet: "## Rules\n- Never send without approval\n- Use AP style for all public content\n- Flag any contract over $50K"
-->

One of the most common objections to AI at work is: "I can't control what it does." In 2023, that was largely true. You could write a careful prompt and hope for the best. The AI might follow your instructions. It might not. There was no enforcement mechanism.

Now there are rules, skills, and hooks. They aren't code — they're structured English that shapes how the AI behaves. A rule might say: "Always check with me before sending anything externally." A skill might encode your firm's contract review playbook — the thirteen criteria for NDA triage, the specific redline language for indemnification clauses, the routing logic for green/yellow/red classification. A hook might automatically run a spell-checker on everything the AI writes before showing it to you.

These controls aren't deterministic the way an if/then statement in software would be. You can't guarantee the AI will follow every rule 100% of the time, any more than you can guarantee a new employee will. But they're real, they're powerful, and they compound. Hilary Gridley, VP at WHOOP, built a "Deck Doctor" by reverse-engineering her implicit quality standards. She had the AI analyze her before-and-after slide edits, told it to be "100 times more specific" about what made the difference, and turned those findings into a custom evaluator. Now her team gets consistent feedback matching her standards — without her reviewing every deck.

The key insight: you're not programming. You're setting expectations, the way you would with a smart new hire. And just like a new hire, the AI gets better at meeting those expectations over time as the instruction set grows.

### Sources

> Hilary Gridley built a "Deck Doctor" by reverse-engineering her implicit quality standards. Key prompt: "Be 100 times more specific."
> — [ChatPRD: Scaling Yourself as a Manager with Custom GPTs](https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts)

> Mark Pike (Anthropic legal team, no coding background) built marketing review tools, contract redlining systems, and COI workflows — all in Claude Code using skills and MCP. "I just typed a normal sentence, describing what I wanted. And it worked."
> — [How Anthropic Uses Claude in Legal](https://claude.com/blog/how-anthropic-uses-claude-legal)

> Cowork plugin architecture: "Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps."
> — [GitHub: knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

> Claire Vo: Meta-skill pattern — a skill that generates other skills. Build one factory skill, then produce domain-specific skills consistently.
> — [ChatPRD: Claude Skills Explained](https://www.chatprd.ai/how-i-ai/claude-skills-explained)

---

## Chapter 8: You're not typing prompts — you're directing work.

{>>GAP-02 (non-SWE examples): Mollick's "management as AI superpower" and Karpathy's "vibe coding" are both SWE-adjacent framings. Need a non-SWE example of the delegation/architect role shift — e.g., Torres's /today command that assembles her daily agenda autonomously, or Gridley scaling her feedback through the Deck Doctor. Show a knowledge worker who moved from "doing the work" to "reviewing the work."<<}

<!-- IMG
id: ch08-architect
characters: skeptic, maven
aspect: 16:9
mood: engaged, collaborative
panel_direction: The dynamic has shifted. Skeptic is leaning forward now, engaged, thinking through implications. They're sketching something — a workflow diagram, an idea, a plan. Maven watches, contributing but not leading. The Skeptic is becoming the architect.
skeptic_says: "So I'd set up the rules for how my team reviews proposals, define the checklist... and then I'd just review what it produces? Like managing someone?"
maven_says: "Exactly like managing someone. Your job becomes reviewing plans and catching edge cases — not doing the mechanical work."
background: The Skeptic's engagement is the story. They should look like someone who's starting to see how this fits their own work.
-->

"Prompt engineering" was a 2023 skill — the art of phrasing your request just right to get a useful response from a chatbot. It mattered because you had one shot. The quality of the output depended on the quality of your input sentence.

That mental model is outdated. When you work with an AI agent, you're not crafting a single prompt. You're setting up a system: defining rules, connecting tools, encoding your preferences, and then reviewing what the agent produces. The skill isn't "write a good sentence." It's "delegate effectively."

Ethan Mollick, a Wharton professor who's studied human-AI collaboration more rigorously than almost anyone, calls this shift "management as AI superpower." As AI agents become capable of sustained autonomous work, the value of delegation skills — breaking tasks down, setting context, defining success criteria — increases dramatically. In one experiment, he had students create an entire startup from scratch in four days using AI agents. The students who succeeded weren't the best prompters. They were the best managers.

Andrej Karpathy, co-founder of OpenAI, captured the shift in terminology. In February 2025, he coined "vibe coding" — a playful term for letting AI write your code while you just describe what you want. By late 2025, he'd updated the term to "agentic engineering," acknowledging that what started as a novelty had become the professional default. The playful name couldn't contain what it had become.

### Sources

> Mollick: "Management as AI Superpower" — as AI agents become capable of hours-long autonomous work, delegation skills become the differentiator.
> — [Referenced via Owen Gregorian](https://x.com/OwenGregorian/status/2016841301673820250)

> Karpathy coined "vibe coding" (Feb 2025): "You fully give in to the vibes, embrace exponentials, and forget that the code even exists." By late 2025, updated to "agentic engineering."
> — [Vibe Coding Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding)

> BCG study (758 consultants): AI users completed 12.2% more tasks, 25.1% faster, at 40% higher quality. But on tasks outside AI's capability frontier, users were 19 percentage points LESS accurate — "falling asleep at the wheel."
> — [Mollick: Centaurs and Cyborgs on the Jagged Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)

---

## Chapter 9: The real unlock isn't a smarter brain — it's everything around it.

{>>GAP-02 (non-SWE examples): The Cursor/$29.3B example is compelling but SWE-specific. Need a harness-vs-model proof point from outside coding — e.g., the Cowork legal plugin (same model, 200 lines of markdown harness = $285B impact) or Torres's system (same Claude model in chat vs. in Claude Code = dramatically different productivity). The thesis chapter must prove the thesis is universal, not just a coding insight.<<}

{>>GAP-08 (before/after motif): The structure doc calls for "a concrete demo, example, or before/after." Each chapter has isolated examples but there's no single recurring task shown across chapters — e.g., "reviewing a contract" attempted in 2023 chat, then with the loop, then with memory, then with tools, then with rules. A motif like that would tie Section 3 together and make the progression visceral.<<}

<!-- IMG
id: ch09-thesis
characters: skeptic, maven
aspect: 16:9
mood: click-moment, collaborative
panel_direction: The Skeptic has fully turned. They're at the whiteboard now, drawing or extending a diagram. Maven is behind them, hands in pockets, watching with satisfaction. The Skeptic is the one explaining now — the student has become the teacher. The diagram shows: MODEL (circle) in the center, surrounded by: MEMORY, TOOLS, RULES, LOOP, FILES — the harness components.
skeptic_says: "So the model is like the engine, but what makes it useful is the steering wheel, the GPS, the mirrors, the road... A 2025 engine in a 2022 chassis is still just a better car that can't go anywhere."
maven_says: "Now you're getting it."
background: Bright. Energized. The whiteboard diagram is the hero of the shot. The relationship between the characters has fundamentally shifted — they're peers now.
-->

The models are getting better. They'll likely keep getting better for a while. GPT-5 hallucinates six times less than its predecessor. Claude Opus 4.6 can sustain coherent work across a million tokens of context. These are real, meaningful improvements, and they matter.

But the step-function change — the thing that turned AI from a novelty into a coworker — isn't the model. It's the harness.

Every chapter in this section has been about something that wraps around the model, not the model itself. The loop (Chapter 4) is harness. Persistent memory (Chapter 5) is harness. Tool connections (Chapter 6) are harness. Rules and skills (Chapter 7) are harness. The role shift to delegation (Chapter 8) is harness. The model is the engine. The harness is the steering wheel, the GPS, the mirrors, and the road.

The proof is in the data. Every.to found that Claude Code "outperforms Cursor using the same model due to superior prompting and scaffolding." Same brain, different harness, dramatically different results. Cursor — a company worth $29.3 billion — uses other companies' models. Its entire value is the harness. And the $285 billion selloff wasn't triggered by a new model. It was triggered by 200 lines of markdown — a harness — that told an existing model how to do legal review.

A 2025 model in a 2022 chat box is still just a better chat box. A 2023 model in a 2025 harness is a coworker.

### Sources

> "Claude Code outperforms Cursor using the same model due to superior prompting and scaffolding. The harness matters more than the model."
> — [Every.to Vibe Check: Claude 3.7 Sonnet and Claude Code](https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code)

> Cursor uses Claude, GPT-4, and other models interchangeably. $29.3B valuation. $1B ARR in 17 months with zero marketing spend. The value is entirely in the harness.
> — [CNBC](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html), [SaaStr](https://www.saastr.com/cursor-hit-1b-arr-in-17-months-the-fastest-b2b-to-scale-ever-and-its-not-even-close/)

> Boris Cherny, creator of Claude Code: "An AI model like Claude is the horse, and a coding assistant like Claude Code is the harness." Two critical factors — sufficient model capability AND adequate scaffolding — must both be excellent simultaneously.
> — [OfficeChai](https://officechai.com/ai/claude-is-like-the-horse-and-claude-code-is-the-harness-anthropics-boris-cherny/)

> The legal plugin that triggered the $285B selloff: ~200 lines of structured markdown. NDA triage against 13 criteria. Contract review with clause-by-clause analysis. No code. No infrastructure. Just the harness.
> — [GitHub: knowledge-work-plugins/legal](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal)

---

## Section 4: What We're Asking — And What We're Offering

<!-- This section breaks from the standard chapter format. No panel. Direct address. -->

If we've done our job in the chapters above, you're past the question of whether AI agents work. The question now is what you're going to do about it.

We have two offers and three asks.

---

### What we're offering

**Right now**: A curated set of videos showing real people — not engineers — using these tools for work you'd recognize. Product managers, lawyers, marketers, consultants, writers. Not demos of what's theoretically possible, but recordings of what people are actually doing today. {>>GAP-06 (video curation): Specific videos not yet selected. User will curate from ai-pm.cc sources list. This is a blocking dependency for Section 4.<<}

**Coming soon**: Starter packs — pre-built collections of rules, skills, and workflows for common knowledge work domains. Legal review. Sales research. Content creation. Project management. Designed so you can install them and start working, then customize as you learn.

---

### What we're asking

**1. Get comfortable with tools you thought were just for software engineers.**

Spreadsheets were purpose-built for financial analysts. Nobody thinks of Excel as "accounting software" anymore — it's just how everyone works with numbers. The same transition is happening with AI development tools.

Tools like Claude Cowork already exist for simpler use cases — a friendly interface that gives AI access to your files without a terminal. But for now, you'll be more capable in tools like Codex, VS Code with Claude Code, or similar environments. These tools aren't "for programmers." They're for anyone who works with information — which is all of us.

Helen Lee Kupp said it well: "I'm a mom who voice-records ideas during morning stroller walks, not a developer. The word 'Code' was intimidating. But what if I don't have a 'coding project'?" She now uses Claude Code to turn voice recordings into organized research, then articles, then LinkedIn posts. The tool was never about code. The name was just in the way.

**2. Learn markdown.**

Markdown is not a programming language. It's an intuitive, structured way of formatting your writing — bold text, headers, bullet lists, numbered lists. You probably already use most of it without knowing the name. When you type **bold** or create a bulleted list, that's markdown.

Why it matters: AI agents read and write in markdown. Your instruction files, your rules, your skills — they're all markdown. Learning it takes an afternoon and makes every interaction with an agent more effective. It's the difference between giving directions verbally and drawing a map.

**3. Learn Git and GitHub.**

Think of GitHub as Dropbox that gives your agent access to your files — with version history, so nothing is ever lost and every change can be undone. Software engineers have used it for decades, but its time for the rest of us.

Git tracks every change to every file. If the AI edits something you don't like, you roll it back. If you want to try two different approaches, you branch. If you want to share your skills and rules with a colleague, you share the repository. It's the infrastructure that makes AI collaboration safe, reversible, and shareable.

---

### Sources

> Helen Lee Kupp: "I'm a mom who voice-records ideas during morning stroller walks, not a developer. The terminal interface? Overwhelming at first. The word 'Code'... but what if I don't have a 'coding project'?"
> — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code)

> Lenny Rachitsky's reframe: "forget that it's called Claude Code and instead think of it as Claude Local or Claude Agent."
> — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code)

> Anthropic built Cowork in ~10 days using Claude Code. "Claude Code for the rest of your work" — same underlying technology, GUI for non-developers.
> — [TechCrunch](https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/)

---

## Appendix: Getting Started

{>>GAP-07 (appendix missing): This is entirely a placeholder. Needs its own structure decision: how prescriptive (step-by-step vs. pointers)? Which tools? Include tutorials or link externally? Template CLAUDE.md files? Sample skills?<<}

[TODO: This section is not yet designed. Open questions:
- How prescriptive? Step-by-step install guide vs. "here are the resources" pointers?
- Which tools to recommend? Claude Code / Cowork / Codex / multiple?
- Should we include markdown and Git tutorials, or link to existing ones?
- Template CLAUDE.md files for different domains?
- Sample skills and rules for non-SWE work?]
