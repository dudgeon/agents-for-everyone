# Agents for Everyone — Draft 002

_Trial run: 2026-02-21. Purpose: validate COMIC spec format with locked character bibles; improve non-SWE examples in Ch4, Ch8, Ch9; add spirit-of-a-rule example in Ch7. Not intended as final copy._

---

## Chapter 1: The best tool you've never used is already on your computer — and it gets better every time you open it.

{>>GAP-01 (bold claim): Structure doc flags the Ch1 headline as an open question — "specific, testable, non-hypey." The working headline leans toward the personal unlock (per the arc spec) but is still softer than ideal. Consider variants: "A lawyer with no coding experience just replaced a $200K/yr legal SaaS tool with 200 lines of plain text" (vivid, specific, concrete). User should decide before draft-003.<<}

<!-- COMIC
id: ch01-bold-claim
characters: maven, declan
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Modern open-plan office, arched windows letting in soft afternoon light. Near-monochromatic background — warm greys and muted beiges — with a wooden desk and low bookshelf behind the characters. One fiddle-leaf fig in the far corner. Maven stands near a laptop on the desk, mid-explanation. Declan sits in a fabric chair across from her, arms crossed. Studio Ghibli-inspired illustration, painterly, watercolor-wash background.

frame_a:
  action: Maven opens a laptop screen toward the Declan, pointing to something on it. She's leaning forward, eager to show rather than tell.
  expression_maven: animated, leaning-forward
  expression_declan: guarded, arms-crossed
  dialogue: ["Let me show you something a lawyer built in a weekend. No coding.", ""]

frame_b:
  action: Declan leans slightly forward — still guarded, but pulled in by what they just saw. His arms shift from fully crossed to one hand on his chin.
  expression_maven: attentive, watching
  expression_declan: pulled-in, reluctant-curiosity
  dialogue: ["", "That's... just a text file?"]
-->

In January 2026, Mark Pike — a product lawyer at Anthropic with no engineering background — built a legal review system using plain English. It screens NDAs against thirteen criteria, classifies them as green, yellow, or red, and generates routing recommendations. The whole thing: about 200 lines of structured text. No code. No infrastructure. He described the process: "I just typed a normal sentence, describing what I wanted. And it worked."

When Anthropic open-sourced it, the legal tech industry had what one Goldman Sachs trader called a "SaaSpocalypse." Thomson Reuters dropped 18%. LegalZoom fell 20%. Total market impact: roughly $285 billion in a week.

This is not a story about a lawyer who learned to code. It's a story about what's possible now that you don't have to.

This book is short, evidence-based, and specific. It will not ask you to suspend your skepticism. It will ask you to update it.

### Sources

> "Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps."
> — [Anthropic knowledge-work-plugins repository](https://github.com/anthropics/knowledge-work-plugins)

> "I just typed a normal sentence, describing what I wanted. And it worked."
> — [How Anthropic Uses Claude in Legal](https://claude.com/blog/how-anthropic-uses-claude-legal)

> Thomson Reuters -18%, RELX -14%, LegalZoom -20%. Goldman Sachs basket of U.S. software stocks: -6% in a single session.
> — [CNBC](https://www.cnbc.com/2026/02/06/ai-anthropic-tools-saas-software-stocks-selloff.html)

---

## Chapter 2: In 2023, AI was confidently wrong about everything — and the people selling it didn't seem to notice.

<!-- COMIC
id: ch02-earned-skepticism
characters: maven, declan
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office, same arched windows. Both characters are seated across from each other at a low coffee table. A tablet between them, face down — as if it's been set aside after a bad experience. The Declan leans forward this time, hands gesturing. Maven sits back, listening. Studio Ghibli-inspired, muted warm background.

frame_a:
  action: Declan leans forward, hands open, recounting something that happened to him. He's not angry — he's making a point he's made before, to someone who usually argues back.
  expression_maven: attentive, open
  expression_declan: emphatic, pointing
  dialogue: ["", "A lawyer submitted AI-generated fake cases to a federal judge. ChatGPT invented them. With full citations."]

frame_b:
  action: Maven nods, not defending, not qualifying. Just agreeing. This is the moment Declan hasn't seen before — someone on the AI side who doesn't argue.
  expression_maven: acknowledging, direct
  expression_declan: caught-off-guard, waiting
  dialogue: ["You're right. That was bad. And it wasn't a fluke.", ""]
-->

If you tried AI in 2023 and walked away unimpressed — or worse, burned — you were paying attention.

ChatGPT launched in November 2022 as a "research preview." It could write a decent email, explain a concept, help brainstorm. It could also confidently invent facts, fabricate sources, and present complete fiction as authoritative truth. It had no way to look anything up. No access to your files. No memory between conversations. Every chat started from scratch.

The consequences were real. In May 2023, lawyer Steven Schwartz used ChatGPT to research case law and submitted a brief to federal court containing six fabricated cases — "Martinez v. Delta Air Lines," "Varghese v. China Southern Airlines" — complete with invented citations and legal reasoning. Schwartz testified he was "operating under the false perception that it could not possibly be fabricating cases on its own." He and his colleague were fined $5,000.

By December, OpenAI's most advanced model developed a different problem: laziness. GPT-4 Turbo was smarter, cheaper, and had a larger memory — but users reported it cutting corners, truncating code, responding with "the rest is similar." Intelligence and reliability turned out to be different things. The model improved. User output didn't.

Your skepticism from that era isn't wrong. It's just aimed at a target that has moved.

### Sources

> Schwartz testified he was "operating under the false perception that [ChatGPT] could not possibly be fabricating cases on its own."
> — [CNN](https://www.cnn.com/2023/05/27/business/chat-gpt-avianca-mata-lawyers), [Mata v. Avianca, Inc., 678 F. Supp. 3d 443 (S.D.N.Y. 2023)](https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc.)

> GPT-4 Turbo was immediately reported as "lazier" — shorter responses, truncated code blocks, "...rest of the code is similar..."
> — [OpenAI Community Forum](https://community.openai.com/t/chatgpt-4-defaults-to-lazy/560886)

> ChatGPT reached 1 million users in 5 days and 100 million in two months — the fastest consumer app adoption in history at the time.
> — [History.com](https://www.history.com/this-day-in-history/november-30/chatgpt-released-openai)

---

## Chapter 3: We've heard "this time it's different" before — remember when AI agents were going to change everything?

<!-- COMIC
id: ch03-hype-graveyard
characters: maven, declan
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office. The Declan is now standing beside a whiteboard they've clearly been using — a list visible in marker: AutoGPT, BabyAGI, Devin, ChatGPT Plugins. Each with a large X beside it. Maven sits in a chair across from the board, elbows on knees. Studio Ghibli-inspired, slightly wider shot to show the full whiteboard.

frame_a:
  action: Declan gestures toward the whiteboard list, looking at Maven with an expression that says "you know I'm right." Not triumphant — making a fair point.
  expression_maven: attentive, nodding-slowly
  expression_declan: matter-of-fact, making-a-point
  dialogue: ["", "AutoGPT. 174,000 GitHub stars. Infinite loops all night. Then Devin — the 'first AI software engineer' — 85% failure rate."]

frame_b:
  action: Maven spreads her hands, making no attempt to defend any of it. Honest concession. She's not looking at the whiteboard — she's looking at the Declan.
  expression_maven: candid, direct
  expression_declan: surprised-by-concession, still-guarded
  dialogue: ["I'm not going to defend any of that. The vision was right. The execution was a disaster. Here's what changed.", ""]
-->

In March 2023, AutoGPT and BabyAGI promised autonomous AI agents that could set goals, break them into tasks, execute them, and iterate without human intervention. AutoGPT became the number one GitHub repository of 2023 with 174,000 stars. Andrej Karpathy called it "the next frontier of prompt engineering."

The reality: agents got stuck in infinite loops all night, burned through API credits without producing anything, and forgot what they'd already done. Tom's Hardware's review headline was not subtle: "Auto-GPT and BabyAGI Are AI's New Hotness, But They Suck Right Now." By late 2023, the AutoGPT team removed their external database support — agents didn't generate enough useful information to need one.

The pattern repeated. ChatGPT Plugins launched as an "App Store moment for AI" in March 2023 and were quietly killed by April 2024. The GPT Store opened with 3 million custom GPTs; researchers found a 97% success rate extracting their supposedly secret system prompts. Devin, launched in March 2024 as the "first fully autonomous AI software engineer," achieved a 15% success rate in independent testing — with "no discernible pattern to predict which tasks would work."

So when someone says "AI agents are different now," your skepticism isn't cynicism. It's pattern recognition. The next two chapters explain exactly what changed — mechanically, not rhetorically.

### Sources

> Tom's Hardware: "Auto-GPT and BabyAGI Are AI's New Hotness, But They Suck Right Now."
> — [Tom's Hardware](https://www.tomshardware.com/news/autonomous-agents-new-big-thing)

> Researchers tested 200+ custom GPTs and found a 97.2% success rate at extracting system prompts.
> — [ArXiv: Assessing Prompt Injection Risks](https://arxiv.org/html/2311.11538v2)

> Answer.AI tested Devin on 20 real-world tasks: 14 failures, 3 successes, 3 inconclusive — 15% success rate. "Couldn't discern any pattern to predict which tasks would work."
> — [Answer.AI](https://www.answer.ai/posts/2025-01-08-devin.html)

> AutoGPT reached 174,000+ GitHub stars — the #1 GitHub repository of 2023.
> — [AutoGPT Wikipedia](https://en.wikipedia.org/wiki/AutoGPT)

---

## Chapter 4: AI doesn't just answer anymore — it plans, tries, checks, and adjusts.

<!-- COMIC
id: ch04-the-loop
characters: maven, declan
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office. Maven has moved to the whiteboard and drawn a simple loop diagram: PLAN → ACT → OBSERVE → ADJUST → back to PLAN. Declan sits in the chair, leaning forward now — genuinely curious rather than defensive. The whiteboard diagram is visible between them. Studio Ghibli-inspired, warm afternoon light.

frame_a:
  action: Declan points at the loop diagram on the whiteboard with a skeptical finger. Maven holds the marker, having just drawn it, and turns to face him.
  expression_maven: attentive, ready
  expression_declan: skeptical, leaning-forward
  dialogue: ["", "Okay. But what happens when it gets the first step wrong?"]

frame_b:
  action: Maven taps the OBSERVE box on the whiteboard. She's not explaining so much as demonstrating — this is the key point, and she knows it.
  expression_maven: confident, direct
  expression_declan: processing, arms-uncrossing
  dialogue: ["It reads the error. Then tries a different approach. Like you would.", ""]
-->

The AI you tried in 2023 worked like this: you typed something in, it generated something back, and that was the transaction. One shot. If it got it wrong, you'd rephrase and try again. The AI never tried again on its own. It never checked its work.

That is not how it works anymore.

Simon Willison, one of the most rigorous voices writing about AI tooling, defines an agent as "an LLM that runs tools in a loop to achieve a goal." That loop — plan, act, observe, adjust — is the mechanical difference between a chatbot and a coworker. The chatbot gives you an answer. The agent tries something, sees what happens, and course-corrects.

Here's what this looks like outside software. Willison tested Anthropic's Cowork — a GUI agent tool built for non-developers — on a folder of 46 blog draft files. The agent needed to identify which ones were ready to publish. It didn't just read the files and guess. It executed 44 separate web searches to verify the publication status of each piece, cross-referenced what it found, and returned three publish-ready candidates with reasoning. No human intervention between the first step and the final answer. That's the loop in practice: plan (find the candidates), act (search for each one), observe (what did the search return?), adjust (update the candidate list), repeat.

The loop also explains the AutoGPT failure. AutoGPT had the right idea. The problem was that the models in 2023 couldn't reliably observe their own errors — and the harnesses couldn't give them enough context to adjust. The concept wasn't wrong. The execution needed two more years.

### Sources

> "An LLM agent runs tools in a loop to achieve a goal."
> — [Simon Willison](https://simonw.substack.com/p/i-think-agent-may-finally-have-a)

> Willison on Cowork: agent found 46 files, executed 44 website searches to verify publication status, identified 3 publish-ready candidates. "Autonomous, multi-step, judgment-intensive."
> — [Simon Willison: Claude Cowork](https://simonwillison.net/2026/Jan/12/claude-cowork/)

> "Claude Code outperforms Cursor using the same model due to superior prompting and scaffolding."
> — [Every.to Vibe Check: Claude 3.7 Sonnet and Claude Code](https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code)

---

## Chapter 5: It remembers who you are and how you work.

<!-- COMIC
id: ch05-memory
characters: maven, declan
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office. Maven has rotated a laptop screen toward the Declan, showing a text document — visible enough to read as a plain-English list of rules and preferences. The Declan leans in to read it, brow slightly furrowed. The laptop is the focal point of the frame. Studio Ghibli-inspired, intimate mid-shot.

frame_a:
  action: Declan squints at the laptop screen, reading. His posture has opened up slightly — arms no longer fully crossed, one hand on his knee.
  expression_maven: calm, attentive
  expression_declan: reading, slightly-surprised
  dialogue: ["", "Wait — I'd have to explain my whole job to it?"]

frame_b:
  action: Maven closes the laptop gently, making eye contact. This is the key point and she's delivering it simply.
  expression_maven: direct, warm
  expression_declan: considering, hands-on-knees
  dialogue: ["Once. Then it remembers. Session ten is different from session one.", ""]
-->

In 2023, every AI conversation started from scratch. You'd explain your role, your context, your preferences — and do it again tomorrow. It was like hiring a contractor who arrived every morning with no memory of the job.

{>>GAP-05 (compounding example): The Torres example is good but the before/after isn't vivid enough. What would the contrast be for a skeptic? What did session one look like vs. session thirty? Need a concrete before/after of what "lazy prompting" actually feels like — what does she have to type now vs. what she had to type before? This would make the compounding argument visceral.<<}

That problem is solved. Tools like Claude Code read a project instruction file — called CLAUDE.md — at the start of every session. This file tells the AI who you are, how you work, and what your standards are. Written in plain English: "When I say 'format this,' use AP style." "Always flag indemnification clauses in contracts before anything else." "Never send anything externally without checking with me first."

Teresa Torres, a product management consultant, built her system over months. Instead of elaborate prompts, she broke her context into dozens of small files — her business profile, her writing style, her research interests — stored in an Obsidian vault the agent reads at session start. At the end of each session, she asks: "What did you learn today that we should document?" The instruction set grows as a side effect of working together. She calls it "lazy prompting" — the system already knows her, so she just describes what she needs.

This is the compounding effect: every correction, every preference, every convention you document persists. Session ten is better than session one not because the AI got smarter, but because it knows more about how you work.

### Sources

> Torres breaks her context into dozens of focused markdown files. "She just works — the agent reads what it needs." She calls it "lazy prompting."
> — [ChatPRD: Teresa Torres's Claude Code System](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management)

> Torres's comparison: Chat vs. Claude Code memory — "search past chats" vs. "all files act as memory." Reusability — "start fresh each chat" vs. "systems that compound over time."
> — [Product Talk: Claude Code — What It Is and How It's Different](https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/)

> "After solving a problem, ask the AI how to prompt it better next time, then add that guidance to your rules file." Single file achieves compounding improvement across sessions.
> — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code)

---

## Chapter 6: It can look things up and work with your actual files.

<!-- COMIC
id: ch06-grounding
characters: maven, declan
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office. Maven has set two printed pages on the coffee table between them — one labeled "2023" showing a person laboriously copy-pasting text between windows; one labeled "Now" showing the agent directly reading from a folder of documents. She points to the contrast. Studio Ghibli-inspired, warm afternoon light.

frame_a:
  action: Declan glances at the two-page comparison on the table, then back at Maven. One eyebrow raised — the question forming.
  expression_maven: steady, waiting-for-the-question
  expression_declan: skeptical, arms-recrossing
  dialogue: ["", "How do I know it's not just making things up again?"]

frame_b:
  action: Maven points to the "Now" page — specifically to the arrow showing the agent reading directly from files. Her gesture is precise, not theatrical.
  expression_maven: direct, measured
  expression_declan: processing, leaning-in
  dialogue: ["Because this time it's reading your actual documents. Not guessing from memory.", ""]
-->

The hallucination problem from Chapter 2 had a structural cause: the AI only knew what was in its training data. When you asked about your contracts, your metrics, or last week's meeting notes, it had two choices — admit it didn't know, or fill in the gap. It usually chose the second option.

Today's agents can read your files, search the web, and connect directly to the tools you already use. This isn't a small upgrade. It's the difference between describing your kitchen to a chef over the phone and letting the chef walk in and look around.

Model Context Protocol — MCP — is the open standard that makes tool connections possible. Think of it as app integrations for your AI: connect it to Slack and it can read your messages; connect it to Google Drive and it can find and read your documents; connect it to your CRM and it can look up customer history before your next call. Reid Robinson at Zapier built a system where, after every meeting, the agent reads the transcript, finds the contact in his CRM, enriches the record, and updates it automatically. A fifteen-minute manual task became a copy-paste.

The hallucination problem isn't fixed because the model got smarter at guessing. It's fixed because the model no longer has to guess.

### Sources

> Reid Robinson's frame: MCPs are "app integrations for your AI tools." That's it — the explanation for non-technical people.
> — [ChatPRD: Zapier Workflows for CRM Automation](https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep)

> "Given MCPs to interact with other tools in our productivity stack — Fireflies, Linear, Notion — it's become my hub for ongoing product research and development."
> — [Lenny's Newsletter, Derek DeHart](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code)

> "The architecture of an AI agent can be reduced to two components: the filesystem as state, and Claude as the orchestrator."
> — [@mernit on X](https://x.com/mernit/status/2021324284875153544)

---

## Chapter 7: You have real controls — not code, but rules and skills that shape how it works.

<!-- COMIC
id: ch07-controls
characters: maven, declan
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office. Maven holds up a printed document — a rules list visible in large text: "Always check with me before sending externally." "Flag any contract over $50K." "Use AP style for all public content." The Declan squints at it from across the coffee table, genuinely puzzled. Studio Ghibli-inspired, warm light.

frame_a:
  action: Declan leans in to read the document Maven is holding, glasses-check instinct without glasses — tilting his head slightly. The rules are readable but he's still processing what he's looking at.
  expression_maven: presenting, attentive
  expression_declan: reading, puzzled
  dialogue: ["", "That's just... English?"]

frame_b:
  action: Maven sets the document down on the table between them, tapping it once. The gesture conveys: yes, that's the point, and that's why it works.
  expression_maven: direct, satisfied
  expression_declan: processing, arms-slowly-uncrossing
  dialogue: ["That's the point. You're not programming — you're setting expectations. Like you would with a smart new hire.", ""]
-->

One of the most common objections to AI at work is: "I can't control what it does." In 2023, that was largely true. You could write a prompt and hope for the best. If the AI didn't follow your instructions, your options were limited to rephrasing.

Now there are rules, skills, and hooks — structured English that shapes how the AI behaves. A rule says: "Always check with me before sending anything externally." A skill encodes your firm's contract review playbook — the specific criteria for NDA triage, the redline language for indemnification clauses, the green/yellow/red routing logic. A hook runs a spell-checker on everything the AI produces before you see it.

These controls aren't deterministic the way code would be. They operate more like instructions to a smart employee — the AI interprets them with judgment. A rule says "flag any contract over $50K." When the AI encounters a $48K contract with an automatic annual renewal clause, it flags it — because the spirit of the rule is about total commitment, not the dollar amount on page one. That's not a bug in the control system. That's the control system working.

Hilary Gridley, VP at WHOOP, built a "Deck Doctor" by teaching the AI her implicit quality standards. She had it analyze her before-and-after slide edits, then pushed it to be "100 times more specific" about what made the difference. The result: a system that evaluates her team's decks using her actual standards — not generic advice, her judgment, encoded and reused.

{>>GAP-10 (rule interpretation): The $48K auto-renewal contract example is new and strong — but it needs a source or a more concrete scenario to be credible. Is there a real documented case of an AI agent interpreting a rule's spirit rather than its letter? Or should this be framed explicitly as a designed behavior? User should decide: real example or design principle.<<}

### Sources

> Mark Pike (Anthropic legal team, no coding background) built contract redlining systems, marketing review tools, and COI workflows. "I just typed a normal sentence, describing what I wanted. And it worked."
> — [How Anthropic Uses Claude in Legal](https://claude.com/blog/how-anthropic-uses-claude-legal)

> Hilary Gridley built a "Deck Doctor" by reverse-engineering her implicit quality standards. Key prompt: "Be 100 times more specific."
> — [ChatPRD: Scaling Yourself as a Manager with Custom GPTs](https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts)

> Cowork plugin architecture: "Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps."
> — [GitHub: knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

---

## Chapter 8: You're not typing prompts — you're directing work.

{>>GAP-02 (non-SWE architect example): The Torres /today command is a strong non-SWE example of the architect role — she set up the system once (Python script, cron jobs, research digest pipeline) and now reviews what it produces each morning. This is the role shift made concrete for a non-developer. Needs to be the lead example, not relegated to supporting position.<<}

<!-- COMIC
id: ch08-architect
characters: maven, declan
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office. Now the Declan is standing beside the whiteboard — Maven is in the chair watching. The Declan is sketching something himself: a simple workflow diagram. The role has reversed. Studio Ghibli-inspired, late afternoon light, slightly warmer than earlier chapters.

frame_a:
  action: Declan is at the whiteboard, drawing boxes and arrows — a rough workflow diagram of what his own system might look like. He's thinking out loud, not asking for permission.
  expression_maven: watching, quietly-pleased
  expression_declan: engaged, problem-solving
  dialogue: ["", "So I'd define the criteria upfront — the rules. Then review what it produces. Like managing a team."]

frame_b:
  action: Maven leans back in the chair, hands clasped. She's watching him work it out — not explaining anymore, just confirming.
  expression_maven: satisfied, leaning-back
  expression_declan: nodding-to-himself, connecting-dots
  dialogue: ["Exactly. Your job becomes designing the system and reviewing the work. Not doing it.", ""]
-->

"Prompt engineering" was a 2023 skill — the art of crafting exactly the right sentence to extract useful output from a one-shot system. It mattered because you had one attempt. The quality of your output depended entirely on the quality of your input.

That model is outdated. Working with an AI agent means setting up a system: defining rules, encoding preferences, connecting tools, and then reviewing what the agent produces. The skill isn't "write a good sentence." It's "delegate effectively."

Teresa Torres built her morning routine as a system, not a prompt. A custom `/today` command triggers a Python script that scans her task files, assembles a prioritized to-do list with overdue items and in-progress research, and delivers a daily digest. Two automated cron jobs run in the background: one in the morning scanning academic sources (arXiv, Google Scholar), one at night summarizing what was found. She built this once. Every morning she reviews the output. She's not a developer. She's an architect — someone who designed a system and now evaluates what it produces.

Ethan Mollick, a Wharton professor studying human-AI collaboration, calls this shift "management as AI superpower." In one experiment, students created entire startups from scratch in four days using AI agents. The students who succeeded weren't the best prompters. They were the best at breaking work into clear subtasks, setting constraints, and evaluating output. The underlying skill — effective delegation — is one that knowledge workers have been developing for their entire careers.

### Sources

> Torres's custom `/today` command: Python script scans task files, assembles daily digest with overdue items and in-progress research. Two cron jobs (morning search + nightly summarization). Built once, reviewed daily.
> — [ChatPRD: Teresa Torres's Claude Code System](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management)

> Mollick: "Management as AI Superpower" — delegation skills become the differentiator as AI agents take on hours-long autonomous work.
> — [Referenced via Owen Gregorian](https://x.com/OwenGregorian/status/2016841301673820250)

> Karpathy coined "vibe coding" (Feb 2025). By late 2025, updated to "agentic engineering" — the playful name couldn't contain what it had become.
> — [Vibe Coding Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding)

---

## Chapter 9: The real unlock isn't a smarter brain — it's everything around it.

<!-- COMIC
id: ch09-harness
characters: maven, declan
aspect: 16:9
render: carousel-mobile, side-by-side-desktop

setting: Same office, same whiteboard. The Declan has drawn a diagram of their own: a circle labeled MODEL in the center, with surrounding labels: MEMORY, TOOLS, RULES, LOOP, FILES. Maven stands slightly to one side, watching. The Declan is teaching now. Studio Ghibli-inspired, warm late-afternoon light — the room has softened.

frame_a:
  action: Declan taps the MODEL circle on the whiteboard, then sweeps his hand outward to gesture at all the surrounding components. He's arrived somewhere — working it out as he speaks.
  expression_maven: watching, quietly-proud
  expression_declan: engaged, realizing
  dialogue: ["", "So the model is like the engine. But what makes it actually useful is... all the other stuff. The steering wheel, the GPS, the road."]

frame_b:
  action: Maven smiles — the first full smile of the book. She's not explaining anymore. She's just confirming what he figured out himself.
  expression_maven: warm, genuinely-pleased
  expression_declan: nodding, settled
  dialogue: ["Now you're getting it.", ""]
-->

The models are getting better. GPT-5 hallucinates six times less than its predecessor. Claude Opus 4.6 sustains coherent work across a million tokens. These are real, meaningful improvements, and they matter.

But the step-function change — the thing that turned AI from a novelty into a coworker — isn't the model. It's the harness.

Every chapter in Section 3 has been about something that wraps around the model, not the model itself. The loop (Chapter 4) is harness. Persistent memory (Chapter 5) is harness. Tool connections (Chapter 6) are harness. Rules and skills (Chapter 7) are harness. The role shift (Chapter 8) is the human side of the harness. The model is the engine. The harness is the steering wheel, the GPS, the mirrors, and the road.

The proof of this thesis comes from outside software. The legal plugin that triggered the $285 billion selloff wasn't triggered by a new model — GPT-4, Claude 3, and others had existed for years before it. It was triggered by 200 lines of structured text that told an existing model how to do legal review. The harness made the model useful for a job it couldn't do from a chat window. A product lawyer with no engineering background wrote the harness. A week later, $285 billion in legal software market cap had evaporated.

A 2025 model in a 2022 chat box is still just a better chat box. A 2023 model in a 2025 harness is a coworker.

### Sources

> "Claude Code outperforms Cursor using the same model due to superior prompting and scaffolding. The harness matters more than the model."
> — [Every.to Vibe Check: Claude 3.7 Sonnet and Claude Code](https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code)

> The legal plugin: ~200 lines of structured markdown. NDA triage against 13 criteria. Contract review with clause-by-clause analysis. No code, no infrastructure. Built by Mark Pike, product lawyer, no engineering background.
> — [GitHub: knowledge-work-plugins/legal](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal)

> Boris Cherny, creator of Claude Code: "An AI model like Claude is the horse, and a coding assistant like Claude Code is the harness."
> — [OfficeChai](https://officechai.com/ai/claude-is-like-the-horse-and-claude-code-is-the-harness-anthropics-boris-cherny/)

> Cursor: $29.3B valuation. $1B ARR in 17 months. Uses other companies' models. The entire value proposition is the harness.
> — [CNBC](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html)

---

## Section 4: What We're Asking — And What We're Offering

_This section breaks from the standard chapter format. No panel. Direct address to the reader._

If we've done our job in the chapters above, you're past the question of whether AI agents work. The question is what you're going to do about it.

Two offers, three asks.

---

### What we're offering

{>>GAP-06 (video curation): Specific videos still not selected. This is a blocking dependency — Section 4 can't be completed until the user curates from ai-pm.cc sources list. Defer to user.<<}

**Right now**: A curated set of short videos showing real people — not engineers — using these tools for work you'd recognize. Product managers, lawyers, marketers, consultants. Not demos of what's theoretically possible, but recordings of what people are doing today.

**Coming soon**: Starter packs — pre-built collections of rules, skills, and workflows for common knowledge work domains. Install and use, then customize as you learn.

---

### What we're asking

**1. Get comfortable with tools you thought were just for software engineers.**

Spreadsheets were built for financial analysts. Nobody thinks of Excel as "accounting software" anymore. The same transition is happening with AI development tools.

Claude Cowork exists for simpler use cases — a friendly GUI that gives AI access to your files without a terminal. But the power tools (Claude Code, Codex, VS Code with AI extensions) are where serious capability lives today. They're not for programmers. They're for anyone who works with information.

Helen Lee Kupp described it: "I'm a mom who voice-records ideas during morning stroller walks, not a developer. The word 'Code' was intimidating. But what if I don't have a 'coding project'?" She uses Claude Code to turn voice recordings into research, then articles, then LinkedIn posts. The tool was never about code. The name was just in the way.

**2. Learn markdown.**

Markdown is not a programming language. It's an intuitive way of formatting text — bold, headers, lists — that you probably already use without knowing the name. When you type `**bold**` or make a bulleted list, that's markdown.

It matters because AI agents read and write in markdown. Your instruction files, rules, and skills are all markdown. Learning it takes an afternoon and makes every interaction more effective.

**3. Learn Git and GitHub.**

Think of GitHub as Dropbox that gives your agent access to your files — with version history, so nothing is ever permanently lost. Software engineers have used it for decades. It's time for the rest of us.

Git tracks every change to every file. If the AI edits something you don't like, you roll it back. If you want to try two approaches, you branch. If you want to share your system with a colleague, you share the repository.

---

### Sources

> Helen Lee Kupp: "I'm a mom who voice-records ideas during morning stroller walks, not a developer. The terminal interface? Overwhelming at first."
> — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code)

> Lenny Rachitsky's reframe: "forget that it's called Claude Code and instead think of it as Claude Local or Claude Agent."
> — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code)

> Anthropic built Cowork in ~10 days using Claude Code itself. "Claude Code for the rest of your work."
> — [TechCrunch](https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/)

---

## Appendix: Getting Started

{>>GAP-07 (appendix): Still a placeholder. Design questions unresolved: prescriptive vs. pointer-based, which tool to recommend first, whether to include sample CLAUDE.md files, whether to include a markdown tutorial inline. This needs a dedicated planning conversation before drafting.<<}

_[Content not drafted. Open questions require user decisions before this section can be written.]_

_Unresolved: How prescriptive? Which tools? Tutorial content inline or linked? Template CLAUDE.md files for different domains? Sample skills and rules?_
