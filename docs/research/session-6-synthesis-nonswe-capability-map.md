# Session 6 — Current State: Non-SWE Capabilities, Applications, Tools & Methods

Research focused on the **destination** — what Claude Code, Cowork, and agentic AI tools can do TODAY for non-software-engineers. Not a timeline; a capability map.

Cross-referenced with `home-brain/domains/professional-development/ai-pm/sources/` (31 sources, 11 processed, 29 knowledge entries).

---

## THE CAPABILITY STACK

The non-SWE capability of Claude Code/Cowork rests on five architectural layers. Each layer builds on the one below it. Understanding this stack is essential for the book because it explains WHY these tools work for non-technical people — and what makes them different from chat interfaces.

### Layer 1: Filesystem Access
**What it is**: The agent can read, write, create, delete, and organize files on the user's computer.

**Why it matters for non-SWE**: Chat interfaces require the user to copy-paste context into every conversation. Filesystem access means the agent can read your documents, spreadsheets, meeting notes, and project files directly. It's the difference between describing your work and the agent SEEING your work.

**Proof points**:
- Teresa Torres broke her context into dozens of tiny focused markdown files in an "LLM Context" Obsidian vault. Instead of crafting lengthy prompts each time, she just works — the agent reads what it needs from the filesystem. She calls it "lazy prompting." ([source](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management))
- Helen Lee Kupp: voice-records ideas on stroller walks, drops transcripts into a folder, Claude Code organizes them into research themes → articles → LinkedIn posts → ready to publish ([source](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))
- Openclaw (@mernit): "The architecture of an AI agent can be reduced to two components: the filesystem as state, and Claude as the orchestrator." When you connect Gmail, the emails become files. When you connect Eight Sleep, your sleep data becomes a file. The filesystem IS the state. ([source](https://x.com/mernit/status/2021324284875153544))

**Conceptual frame for the book**: "Chat is describing your kitchen to a chef over the phone. Filesystem access is letting the chef into your kitchen."

---

### Layer 2: Tool Connections (MCP)
**What it is**: Model Context Protocol lets the agent connect to external tools — Slack, Notion, Jira, Google Calendar, CRM systems, databases, etc. The agent can read FROM and write TO these systems.

**Why it matters for non-SWE**: Knowledge workers live across 5-15 SaaS tools. The agent becomes the hub that orchestrates across all of them, replacing the manual cross-tool workflow that consumes PM/manager/analyst time.

**Proof points**:
- Derek DeHart: "Given MCPs to interact with other tools in our productivity stack—Fireflies, Linear, Notion—it's become my hub for ongoing product research and development." Synthesizes customer call transcripts → compiles evidence for/against hypotheses → creates Linear tickets. ([source](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))
- Dennison Bertram: "Claude CEO" — Gmail + Brex + Mercury + Linear → daily briefing on what to focus on. Single morning prompt produces a cross-tool executive summary. ([source](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))
- Reid Robinson (Zapier PM): MCP-powered CRM automation. Post-meeting transcript → Claude reads Zapier MCP bundle → searches Coda for existing contact → enriches with internal lookup → creates/updates CRM entry. 15-minute manual task → copy-paste. ([source](https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep))
- Anthropic Legal team: MCP servers connect Claude to Google Drive, Jira, Slack, Google Calendar. Privacy impact assessments use MCP to access previous PIAs and apply formatting skills. ([source](https://claude.com/blog/how-anthropic-uses-claude-legal))
- Cowork plugins use `.mcp.json` to connect: Slack, Notion, HubSpot, Figma, Snowflake, PubMed, Benchling, etc. Each plugin comes pre-wired to the tools that role uses. ([source](https://github.com/anthropics/knowledge-work-plugins))

**Key insight from home-brain**: "The highest-leverage investment for agent products may be MCP breadth (more tool connections) rather than model depth (smarter reasoning). Each integration unlocks new workflow patterns without requiring the user to learn new prompts." (from [Agent as Cross-Tool Workflow Hub](home-brain knowledge entry))

**Reid Robinson's frame**: MCPs are "app integrations for your AI tools." That's it. That's the explanation for non-technical people.

---

### Layer 3: Persistent Instructions (CLAUDE.md / Skills / Plugins)
**What it is**: Files that the agent reads at the start of every session, providing persistent context about who you are, how you work, and what your conventions are. Progresses from:
- **CLAUDE.md**: A single project instruction file
- **Skills**: Reusable domain expertise bundles (SKILL.md + templates + scripts)
- **Plugins**: Role-specific packages of skills + commands + MCP connectors

**Why it matters for non-SWE**: This is the "alignment without fine-tuning" layer. A lawyer can encode their firm's playbook. A PM can encode their PRD format. A marketer can encode their brand voice. The model is the same for everyone — the persistent instructions make it behave like YOUR expert.

**Proof points**:
- Anthropic Legal team: Skills files encode domain expertise for employment law, commercial contracts, privacy, and corporate work. Each skill teaches Claude the team's preferences, formatting styles, and substantive frameworks. Mark Pike (no coding background) built all of this. ([source](https://claude.com/blog/how-anthropic-uses-claude-legal))
- Teresa Torres: Global claude.md routes queries — business question → business profile context files, personal → personal profile context files. Built iteratively: at end of each session, asks "Claude, what'd you learn today that we should document?" The context library grows as a side effect of working. ([source](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management))
- Hilary Gridley (WHOOP): Built a "Deck Doctor" custom GPT by reverse-engineering her implicit quality standards from before/after slide examples. Key prompt: "Be 100 times more specific." Forces AI past vague principles into concrete, actionable criteria. The GPT then evaluates decks for her team using HER standards consistently. ([source](https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts))
- Cowork plugins: 200 lines of structured markdown in the legal plugin triggered a $285B selloff. The NDA triage command screens against 13 criteria, classifies GREEN/YELLOW/RED, generates routing recommendations. **"Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps."** ([source](https://github.com/anthropics/knowledge-work-plugins))
- Claire Vo: Meta-skill pattern — a skill that generates other skills. Build one factory skill, then use it to produce domain-specific skills consistently. Demonstrates composability: agent capabilities are NOT flat — they can invoke and build on each other. ([source](https://www.chatprd.ai/how-i-ai/claude-skills-explained))
- Lazar Jovanovic (professional "vibe coder"): "After solving a problem, ask the AI how to prompt it better next time, then add that guidance to your rules.md file." Single rules file achieves compounding improvement across sessions. ([source](https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code))

**Conceptual frame for the book**: CLAUDE.md is the most important file in the project. Not because of what it contains — but because it's the mechanism for teaching the model YOUR judgment. It's alignment without machine learning.

---

### Layer 4: Autonomous Execution (Agents / Subagents / Teams)
**What it is**: The agent can execute multi-step tasks autonomously — breaking complex work into subtasks, running them in parallel, and coordinating results. Subagents can be specialized for different domains.

**Why it matters for non-SWE**: This is what separates "answering questions" from "doing work." The agent doesn't just tell you what to do — it does it. Organizes 200 files, processes 46 blog drafts, generates 100 ad variations, triages an inbox of NDAs.

**Proof points**:
- Cowork: Willison tested on blog-drafts folder. Agent found 46 files, executed 44 website searches to verify publication status, identified 3 publish-ready candidates. Autonomous, multi-step, judgment-intensive. ([source](https://simonwillison.net/2026/Jan/12/claude-cowork/))
- Anthropic Growth Marketing: Agent processes CSV with hundreds of ads → identifies underperformers → generates new variations within character limits. Also built a Figma plugin generating up to 100 ad variations by swapping headlines/descriptions. ([source](https://claude.com/blog/how-anthropic-teams-use-claude-code))
- Danny Shmueli: 4 custom subagents in `.claude/agents/`: Reddit replier, Reddit promoter, X specialist. One command → finds relevant threads → drafts replies. Each subagent has its own specialized context. ([source](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))
- Teresa Torres: Custom `/today` slash command triggers Python script that scans task files, assembles daily to-do list with overdue items, in-progress ideas, and research digest. Two cron jobs: morning search (arXiv, Google Scholar) + nightly summarization. All automated, all non-SWE. ([source](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management))
- James Pember: "Self-driving documentation" — agent with Playwright access explores software independently, identifies knowledge gaps in docs, creates changes itself. Autonomous end-to-end. ([source](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

**Conceptual frame for the book**: "It's less like a back-and-forth and more like leaving messages for a coworker." (Anthropic's description of Cowork)

---

### Layer 5: Knowledge Capture (Side-Effect Learning)
**What it is**: As the agent works, it captures knowledge as a byproduct — corrections become documented conventions, tribal knowledge gets codified, the system improves without anyone explicitly "doing documentation."

**Why it matters for non-SWE**: The #1 failure mode of organizational knowledge management is that nobody maintains the wiki. This layer makes documentation a side effect of correcting the agent, not a separate task.

**Proof points**:
- Devin (Cognition): "You don't have to think about documentation while you're working, you just correct the agent the way you'd correct a teammate, and the system prompts you to persist what's worth keeping." Multi-source: chat corrections + repo scanning + suggested updates. ([source](https://x.com/dabit3/status/2022459842342916559))
- Teresa Torres: End-of-session ritual — "Claude, what'd you learn today that we should document?" Builds the context library incrementally. ([source](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management))
- Gang Rui: Slash command analyzes journal entries + git commits for past 7 days, spots gaps between stated intentions and actions, suggests system improvements. "Like having a COO that learns from my patterns." ([source](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))
- Reid Robinson: Self-improving customer feedback loop — closed tickets → AI extracts FAQ → human reviews → approved entries enrich chatbot knowledge base. "The chatbot gets smarter and more helpful every single day, automatically." ([source](https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep))
- Abhi Chandwani: Maintains verbose git commits specifically to create context for future agent workflows. The commit history becomes the agent's memory. ([source](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

**Conceptual frame for the book**: "The best documentation system is one nobody has to maintain. The agent writes it as a side effect of doing other work."

---

## PROVEN NON-SWE APPLICATION DOMAINS

### 1. Legal
**Current capabilities**: NDA triage, contract review/redlining, compliance assessment, marketing content legal review, COI processing, privacy impact assessments
**Key proof points**: Mark Pike (Anthropic, no coding background), Cowork legal plugin ($285B selloff), Openclaw (filesystem-as-state for law firms), Pulkit Agrawal (querying contract clauses across stored contracts)
**Tools/methods**: Skills with domain expertise, MCP to document management (Box, Egnyte), playbook files, GREEN/YELLOW/RED classification frameworks
**Sources**: [Anthropic legal blog](https://claude.com/blog/how-anthropic-uses-claude-legal), [knowledge-work-plugins/legal](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal)

### 2. Product Management
**Current capabilities**: PRD generation, competitive analysis, roadmapping with effort/impact estimates, user research synthesis, backlog management, release notes, customer call analysis
**Key proof points**: Teresa Torres (writing workflow, task management, research automation), Derek DeHart (hypothesis tracking across calls), Abhi Chandwani (repo-based roadmapping), Trist Adlington ("I talk to Claude more than anyone else"), Claire Vo (idea → product in 30 min with Devin delegation)
**Tools/methods**: CLAUDE.md with paths to engineering repos, MCP to Linear/Jira/Notion/Fireflies, `/today` command for daily assembly, competitive analysis subagents running in parallel
**Sources**: [Torres task management](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management), [Torres Claude Code guide](https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/), [Lenny's 50 use cases](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code)

### 3. Sales & Lead Generation
**Current capabilities**: CRM automation, prospect research, meeting prep briefings, lead scoring, competitive battlecards, outreach drafting
**Key proof points**: Jeff Lindquist (find top 5 pilot companies), Sergei Zotov (GitHub repo scraping for leads with priority scores + LinkedIn URLs), Reid Robinson (MCP-powered CRM updates, always-on meeting prep), Cowork sales plugin
**Tools/methods**: MCP to CRM (HubSpot, Close, Coda), Zapier MCP bundles, Claude Projects with tool-usage instructions, automated pre-meeting briefs via Zap triggers
**Sources**: [Zapier workflows](https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep), [knowledge-work-plugins/sales](https://github.com/anthropics/knowledge-work-plugins/tree/main/sales)

### 4. Marketing & Content
**Current capabilities**: Ad variation generation, brand voice enforcement, campaign planning, content drafting, competitor ad research, social media management, SEO audits
**Key proof points**: Anthropic Growth Marketing (100 ad variations via Figma plugin), Sumant Subrahmanya (competitor ad library extraction), Chad Boyda (Slack → organic social posts), Danny Shmueli (4 social media subagents)
**Tools/methods**: CSV processing for ad performance, Figma integration, subagents with platform-specific personas, MCP to Canva/Ahrefs/SimilarWeb/Klaviyo
**Sources**: [Anthropic teams blog](https://claude.com/blog/how-anthropic-teams-use-claude-code), [knowledge-work-plugins/marketing](https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing)

### 5. Writing & Research
**Current capabilities**: Outline iteration, hook improvement, citation research, section-by-section feedback, voice-note-to-article pipelines, academic paper digests, competitor analysis reports
**Key proof points**: Teresa Torres (full writing workflow in VS Code), Helen Lee Kupp (stroller-walk voice notes → published content), Lenny Rachitsky (image enhancement, YouTube downloads, raffle picking), Hilary Gridley (writing coach workflow: brain dump → thesis validation → blind spots → restructure)
**Tools/methods**: MCP to Notion for synced notes, writing assistant subagents, arXiv/Scholar cron jobs, "lazy prompting" via pre-loaded context libraries
**Sources**: [Torres writing workflow](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code), [Gridley writing coach](https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts)

### 6. Finance & Operations
**Current capabilities**: Expense analysis, journal entries, account reconciliation, financial statements, variance analysis, invoice management, audit support
**Key proof points**: Cowork demo (receipt screenshots → expense spreadsheets), Martin Merschroth (invoice file renaming + sorting), Dennison Bertram ("Claude CEO" pulling from Brex + Mercury), Cowork finance plugin
**Tools/methods**: MCP to Snowflake/Databricks/BigQuery, CSV processing, receipt OCR
**Sources**: [knowledge-work-plugins/finance](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance), [Fortune Cowork article](https://fortune.com/2026/01/13/anthropic-claude-cowork-ai-agent-file-managing-threaten-startups/)

### 7. Management & Self-Improvement
**Current capabilities**: Conflict avoidance detection in meetings, intention-action gap analysis, unregistered learning capture, team feedback scaling, interview prep, job description generation
**Key proof points**: Dan Shipper (meeting recordings → conflict avoidance patterns), Gang Rui (weekly journal + commit analysis → system improvements, "like having a COO"), Hilary Gridley ("Deck Doctor" GPT that scales her feedback), Justin Bleuel (generated JD + hiring plan + interview rubric)
**Tools/methods**: Slash commands on periodic cadence, behavioral pattern analysis, reverse-engineering judgment into reusable agents
**Sources**: [Lenny's 50 use cases](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code), [Gridley scaling yourself](https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts)

### 8. Customer Support
**Current capabilities**: Ticket triage, response drafting, escalation packaging, knowledge base article generation, self-improving FAQ systems
**Key proof points**: Reid Robinson (self-improving feedback loop: closed tickets → AI extract → human review → chatbot enrichment), Cowork customer-support plugin, Eren Gündüz (Intercom tickets → Asana bug reports)
**Tools/methods**: MCP to Intercom/HubSpot/Guru, Zapier-based analysis triggers, human-in-the-loop review gates
**Sources**: [Zapier workflows](https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep), [knowledge-work-plugins/customer-support](https://github.com/anthropics/knowledge-work-plugins/tree/main/customer-support)

### 9. Personal Life & Family
**Current capabilities**: File cleanup/organization, photo management, calendar coordination, interview prep, music creation with kids, system diagnostics, storage management
**Key proof points**: Reid Robinson (family calendar from photo of physical calendar → Google Calendar sync with drive-time blocking; custom interview prep podcast for wife's job search; songwriting with 4-year-old using Suno), John Conneely (DIY slide tower planning), Lenny (storage cleanup, image enhancement, YouTube downloads, raffle picking)
**Tools/methods**: Claude Projects for family context, Zapier MCP for Google Calendar actions, Notebook AI for podcast generation
**Sources**: [Zapier workflows](https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep), [Lenny's use cases](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code)

### 10. Life Sciences / Biology
**Current capabilities**: Literature search, genomics analysis, target prioritization, preclinical research, clinical trial data
**Key proof points**: Cowork bio-research plugin (PubMed, BioRender, bioRxiv, ClinicalTrials.gov, ChEMBL, Benchling), Claude for Life Sciences (Oct 2025), Claude for Healthcare (Jan 2026, HIPAA-ready)
**Tools/methods**: MCP to scientific databases, domain-specific skills
**Sources**: [knowledge-work-plugins/bio-research](https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research), [IntuitionLabs](https://intuitionlabs.ai/articles/claude-code-life-science-applications)

---

## KEY TECHNIQUES (domain-agnostic methods)

### 1. "Lazy Prompting" via Context Libraries
**What**: Pre-load context into well-organized files so simple prompts produce rich output.
**How**: Break context into small focused files. Use index files as maps. Global CLAUDE.md routes to appropriate context. Built iteratively — capture learnings at end of each session.
**Who uses it**: Teresa Torres
**Why it works**: Eliminates the "prompt engineering" burden. The system knows your context; you just describe what you want.

### 2. Reverse-Engineering Judgment
**What**: Have AI analyze before/after examples to discover your implicit quality criteria, then encode into reusable agent/GPT.
**How**: Collect examples → open-ended AI analysis → "be 100x more specific" → build custom evaluator.
**Who uses it**: Hilary Gridley (slide evaluation), applicable to any domain with quality standards.
**Why it works**: Turns tacit expertise into explicit, consistent, scalable feedback.

### 3. MY Job / YOUR Job Role Delineation
**What**: Explicitly partition human/AI responsibility in the prompt: "MY job is X, YOUR job is Y."
**How**: Scopes AI authority, sets output format, preserves human agency. Prevents the AI from overstepping.
**Who uses it**: Hilary Gridley, broadly applicable.
**Why it works**: Sets clear expectations and prevents AI from "helping" in ways you don't want.

### 4. Meta-Skill Factory
**What**: Build a "skill that builds skills" — a reusable factory for creating new agent capabilities.
**How**: Create a `create_skill` skill with structure conventions, validation script. Invoke it to generate domain-specific skills.
**Who uses it**: Claire Vo
**Why it works**: Scales agent capability creation across a team. Encodes quality standards into the generation process.

### 5. Self-Improving Feedback Loops
**What**: Agent corrections → persisted as knowledge → future sessions retrieve that knowledge → compounding improvement.
**How**: At correction moment, agent suggests persisting. Human reviews/approves. Knowledge scoped appropriately (project vs org-wide).
**Who uses it**: Teresa Torres (end-of-session "what did we learn"), Devin (team memory), Lazar Jovanovic (rules.md after each solved problem)
**Why it works**: Documentation as side effect of natural work, not separate task.

### 6. Cross-Tool Hub via MCP
**What**: Connect 3+ tools to a single agent that orchestrates across them with judgment.
**How**: MCP connections, natural language workflow definition, progressive capability as new tools are added.
**Who uses it**: Derek DeHart, Dennison Bertram, Reid Robinson, Terry Lin
**Why it works**: Agent applies judgment at each step (summarize, prioritize, decide) — different from Zapier-style rigid rules.

### 7. Behavioral Pattern Analysis
**What**: Agent ingests digital exhaust (recordings, journals, commits, chats) and identifies behavioral patterns you can't see yourself.
**How**: Specify behavioral dimension to analyze. Run on periodic cadence (weekly). Feed findings into system improvements.
**Who uses it**: Dan Shipper (conflict avoidance), Gang Rui (intention-action gaps), Chad Boyda (unregistered learning)
**Why it works**: Humans are poor observers of own behavioral tendencies. Agent + raw data = honest mirror.

### 8. Parallel Execution for Competitive Analysis
**What**: Run multiple analyses simultaneously (one per competitor, customer, document) with consistent framework.
**How**: Each gets own context window (no degradation), same framework (no drift), simultaneous processing. Build reusable `/update-competitors` command.
**Who uses it**: Teresa Torres (competitive analysis use case)
**Why it works**: First setup takes 15 minutes. Every future run takes 1 minute. Systems that compound.

---

## THE ADOPTION BARRIER: "CODE" AS IDENTITY GATE

The biggest barrier to non-SWE adoption is the word "Code" in "Claude Code."

- Lenny's reframe: "forget that it's called Claude Code and instead think of it as Claude Local or Claude Agent"
- Helen Lee Kupp: "I'm a mom who voice-records ideas during morning stroller walks, not a developer. The terminal interface? Overwhelming at first. The word 'Code'... but what if I don't have a 'coding project'?"
- Anthropic's response: Cowork (Jan 2026) — literally "Claude Code without the code" for non-developers
- The diagnostic: Who COULD this tool serve (capability audit) vs who DOES this tool serve (adoption reality)?

([source: Tool Identity as Adoption Gate](home-brain knowledge entry), from [Lenny's article](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code))

---

## ARCHITECTURAL INSIGHT: WHY THIS WORKS FOR NON-TECHNICAL PEOPLE

Teresa Torres's comparison table is the clearest articulation:

| Feature | Claude Chat | Claude Code / Cowork |
|---------|------------|---------------------|
| Memory | Search past chats | All files act as memory/context |
| Access files | Upload manually | Automatic filesystem access |
| Shortcuts | None / Agent Skills | /commands, agents, hooks, skills, plugins |
| Portability | None | Complete — all stored locally as markdown |
| Reusability | Start fresh each chat | Systems that compound over time |

The shift from chat to agent is: **from describing your work to the agent SEEING your work. From one-shot answers to compounding systems. From vendor lock-in to portable markdown.**

([source](https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/))

---

## SOURCE INDEX (all URLs referenced in this document)

### Anthropic Primary Sources
- How Anthropic Teams Use Claude Code: https://claude.com/blog/how-anthropic-teams-use-claude-code
- How Anthropic Uses Claude in Legal: https://claude.com/blog/how-anthropic-uses-claude-legal
- How AI Is Transforming Work at Anthropic: https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- Cowork Help Center: https://support.claude.com/en/articles/13345190-getting-started-with-cowork
- Knowledge Work Plugins (GitHub): https://github.com/anthropics/knowledge-work-plugins

### Key Articles
- Lenny Rachitsky, "Everyone Should Be Using Claude Code More" (Oct 14, 2025): https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code
- Lenny Rachitsky, "Getting Paid to Vibe Code" (2025): https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code
- Teresa Torres, "Claude Code: What It Is..." (Oct 29, 2025): https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/
- Claire Vo / Torres, "Teresa Torres's Claude Code System" (Jan 19, 2026): https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management
- Claire Vo, "Claude Skills Explained" (Feb 14, 2026): https://www.chatprd.ai/how-i-ai/claude-skills-explained
- Claire Vo / Gridley, "Scaling Yourself with Custom GPTs" (May 19, 2025): https://www.chatprd.ai/how-i-ai/scaling-yourself-as-a-manager-with-custom-gpts
- Claire Vo / Robinson, "Zapier Workflows for CRM" (Feb 4, 2026): https://www.chatprd.ai/how-i-ai/zapier-workflows-for-crm-automation-meeting-prep
- Claire Vo / Peter Yang, "Idea to Product in 30 Min" (May 18, 2025): https://creatoreconomy.so/p/from-idea-to-product-in-30min-using-ai-agents-claire-vo
- Simon Willison, "First Impressions of Claude Cowork" (Jan 12, 2026): https://simonwillison.net/2026/Jan/12/claude-cowork/
- @mernit, "Openclaw: Filesystem as State" (Feb 12, 2026): https://x.com/mernit/status/2021324284875153544
- Nate's Newsletter, "200 Lines of Markdown" (Feb 2026): https://natesnewsletter.substack.com/p/200-lines-of-markdown-just-triggered
- Rich Holmes, "Claude Code for Non-Engineering" (Dec 5, 2025): https://departmentofproduct.substack.com/p/how-to-use-claude-code-for-non-engineering
- Prompt Warrior, "5 Powerful Claude Code Use Cases": https://www.thepromptwarrior.com/p/5-powerful-claude-code-use-cases-you-probably-didn-t-know-about-5826bfb7f5b8fdd8

### Market Impact
- Fortune (selloff): https://fortune.com/2026/02/06/anthropic-claude-opus-4-6-stock-selloff-new-upgrade/
- CNBC (SaaS selloff): https://www.cnbc.com/2026/02/06/ai-anthropic-tools-saas-software-stocks-selloff.html
- TechCrunch (Cowork launch): https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/
- TechCrunch (Cowork plugins): https://techcrunch.com/2026/01/30/anthropic-brings-agentic-plugins-to-cowork/
- Fortune (startup threat): https://fortune.com/2026/01/13/anthropic-claude-cowork-ai-agent-file-managing-threaten-startups/

### Home-Brain Cross-References (not public URLs)
- home-brain/domains/professional-development/ai-pm/knowledge-base/horizontal/agents/ — 9 entries on agent patterns
- home-brain/domains/professional-development/ai-pm/knowledge-base/ai-adoption/ — 6 entries on adoption barriers
- home-brain/domains/professional-development/ai-pm/knowledge-base/horizontal/context/ — 5 entries on context management
- home-brain/domains/professional-development/ai-pm/knowledge-base/horizontal/prompting/ — 4 entries on prompting techniques
- home-brain/domains/professional-development/ai-pm/sources/ — 31 total sources, 19 unread (additional material available)
