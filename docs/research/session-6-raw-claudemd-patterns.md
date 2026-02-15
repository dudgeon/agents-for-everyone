# Session 6 Research: CLAUDE.md and Claude Code for Non-Coding Projects

**Date**: 2026-02-15
**Research focus**: Evidence that CLAUDE.md / persistent instruction patterns and Claude Code's agentic architecture work beyond software engineering
**Thesis relevance**: CLAUDE.md is the perfect illustration of "the harness matters more than the model" -- a persistent instruction mechanism that creates domain-specific alignment for ANY domain

---

## 1. THE CORE RECOGNITION: Claude Code Is Misnamed

### Simon Willison (October 2025)
> "Claude Code is, with hindsight, poorly named. It's not purely a coding tool: it's a tool for general computer automation. Anything you can achieve by typing commands into a computer is something that can now be automated by Claude Code."
- Source: [Claude Code as general purpose agent - Chase McCoy](https://chsmc.org/2025/10/claude-code/) (quoting Willison)
- Source: [Simon Willison on Claude Skills](https://simonwillison.net/2025/Oct/16/claude-skills/)
- Source: [First impressions of Claude Cowork](https://simonw.substack.com/p/first-impressions-of-claude-cowork) -- Willison calls Claude Code "a general agent disguised as a developer tool"

### Chase McCoy (October 2025)
- Argues the CLI-based distribution model is actually the key advantage -- CLIs provide programmatic access to machines, easy distribution
- Web apps *lack* the ability to interact with systems outside the browser (intentional for security, but constraining for general agents)
- Source: [Claude Code as general purpose agent](https://chsmc.org/2025/10/claude-code/)

### TransformerNews Article
- Author has "absolutely zero coding experience" and uses Claude Code for:
  - Processing bank statements and invoices for tax filing
  - Booking theater tickets after reviewing calendar + website
  - Creating automation tools (saving teams ~half a day weekly)
  - Planning vacation itineraries with restaurant extraction from social media
  - Writing articles
  - Syncing Letterboxd data to personal notes
- Core insight: "Code is just a language by which we instruct computers to do things" -- so an AI that writes+executes code can do virtually any digital task
- Source: [Claude Code is about so much more than coding](https://www.transformernews.ai/p/claude-code-is-about-so-much-more)

### Boris Cherny / Fortune (January 2026)
- Head of Claude Code at Anthropic: **"We just want to make it much easier for non-programmers."**
- Describes users deploying Claude Code to search museum archives for basketry collections
- Users handling spreadsheet data shuffling, Slack-Salesforce integration, email organization
- **Strategy**: Anthropic tested with technical users first via Claude Code, then extended to broader audiences -- "a tested foundation rather than starting from scratch with consumer tools"
- Source: [Fortune - Claude Code gives Anthropic its viral moment](https://fortune.com/2026/01/24/anthropic-boris-cherny-claude-code-non-coders-software-engineers/)

### Anthropic's Agent SDK Blog Post
- Anthropic themselves state: **"Claude Code has become far more than a coding tool"** at Anthropic, being used "for deep research, video creation, and note-taking, among countless other non-coding applications."
- Core design principle: "The key design principle behind the Claude Agent SDK is to give your agents a computer, allowing them to work like humans do."
- Non-coding SDK use cases mentioned: finance agents evaluating investments, personal assistant agents booking travel/managing calendars, research agents processing files and generating insights, customer support agents
- Source: [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

### Cobus Greyling / Medium (January 2026)
- Title: "Anthropic Says Coding Agents Are Becoming the Universal Everything Agent"
- Enterprise customers using Skills in production for legal, finance, accounting, and data science
- Source: [Medium - Anthropic Says Coding Agents...](https://cobusgreyling.medium.com/anthropic-says-coding-agents-are-becoming-the-universal-everything-agent-039f9bb709fc)
- Note: Article returned 403 on WebFetch; search snippet only

---

## 2. CLAUDE COWORK: The Non-Technical Rebrand (January 2026)

### Launch
- January 12, 2026: Anthropic launched Cowork as a research preview
- Built on the same Claude Agent SDK that powers Claude Code
- **Built in approximately 10 days** using Claude Code itself
- Available to Pro subscribers ($100+/month)

### What it does
- User points Claude at a folder on their computer
- Claude can read, edit, or create files in that folder
- Chat-based interface instead of terminal
- No terminal expertise required

### Key quote from Willison
> "Claude Code has an enormous amount of value that hasn't yet been unlocked for a general audience." Cowork is "a really smart product" that pragmatically democratizes these capabilities.
- Source: [Simon Willison - First impressions of Claude Cowork](https://simonw.substack.com/p/first-impressions-of-claude-cowork)

### Sources
- [TechCrunch - Anthropic's new Cowork tool offers Claude Code without the code](https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/)
- [Fortune - Anthropic launches Cowork](https://fortune.com/2026/01/13/anthropic-claude-cowork-ai-agent-file-managing-threaten-startups/)
- [Byteiota - Anthropic Cowork Brings Claude Code to Non-Technical Users](https://byteiota.com/anthropic-cowork-brings-claude-code-to-non-technical-users/)
- [Claude Blog - Introducing Cowork](https://claude.com/blog/cowork-research-preview)
- [Axios - Anthropic's Claude Cowork wrote itself](https://www.axios.com/2026/01/13/anthropic-claude-code-cowork-vibe-coding)

---

## 3. VIRAL NON-CODING USE CASES (The "Misuse" That Became the Product)

Anthropic observed users "misusing" Claude Code for non-coding tasks, which directly inspired Cowork:

- **Vacation planning** -- using a developer tool to research destinations and plan trips
- **Tomato plant monitoring** -- tracking plant growth
- **Museum archive research** -- combing through basketry collections
- **Recovering wedding photos** from corrupted drives
- **Controlling ovens**
- **Building presentation slide decks**
- **Cleaning up email inboxes and cancelling subscriptions**
- **Doing taxes**
- **Designing knitting patterns**
- **Booking theater tickets** after checking calendar availability

> "The fact that they watched users repurpose a terminal coding tool for vacation planning and kitchen appliances, then built a new interface specifically for that emergent behavior, felt like the opposite of most product development."
- Source: [Roger Wong - Claude Is Taking the AI World by Storm](https://rogerwong.me/2026/01/claude-is-taking-the-ai-world-by-storm)
- Source: [Fortune - Claude Code gives Anthropic its viral moment](https://fortune.com/2026/01/24/anthropic-boris-cherny-claude-code-non-coders-software-engineers/)

---

## 4. CLAUDE.md AS A GENERAL-PURPOSE ALIGNMENT MECHANISM

### How it works
- CLAUDE.md is a markdown file that Claude reads automatically at the start of every session
- Creates persistent, domain-specific context that survives session resets
- Operates as a hierarchical control system: CLAUDE.md instructions override user prompts
- Memory hierarchy: directory-level (most specific) > project-level > global > user prompts
- Source: [Claude Code Docs - Manage Claude's memory](https://code.claude.com/docs/en/memory)
- Source: [Using CLAUDE.MD files](https://claude.com/blog/using-claude-md-files)

### CLAUDE.md as "law"
> "Your CLAUDE.md file is treated as law -- instructions there override user prompts and persist across entire sessions."
- Source: [CLAUDE.md Supremacy - ClaudeLog](https://claudelog.com/mechanics/claude-md-supremacy/)

### Instruction budget
- Claude reliably follows about 100-150 custom instructions
- System prompt already uses ~50, leaving ~100-150 for the user's project
- CLAUDE.md and always-on rules share this budget
- LLMs bias toward instructions at the peripheries of the prompt (beginning and end)
- Source: [ClaudeLog](https://claudelog.com/mechanics/claude-md-supremacy/)

### Key insight for our thesis
A concise, structured CLAUDE.md guide *completely outperformed* more sophisticated skill-based retrieval systems in evaluations. The static markdown file -- the simplest possible harness -- was the most effective alignment mechanism.

---

## 5. NON-CODING DOMAIN EXAMPLES (DETAILED)

### A. Writing Projects

#### Casey Newton / Platformer -- "Claude Code for Writers"
- Built a searchable database of 818 newsletter editions using Claude Code
- Runs semantic queries like "When was the last time I wrote about Grok?" with quick links
- Something he'd wanted "for nearly half a decade" -- Claude built it in less than half an hour
- Philosophy: tools that **enhance thinking rather than replace writing**
- Source: [Platformer - Claude Code for writers](https://www.platformer.news/claude-code-for-writers-tips-ideas/)

#### Claude Book -- Multi-Agent Novel Writing Framework
- Orchestrator-worker pattern with 4 specialized agents: Planner (Opus), Writer (Opus), Perplexity Gate (Ministral 8B), Reviewers (Sonnet)
- "Bible" folder (immutable style reference), "state" (current situation), "story" (content), "timeline" (updates)
- Perplexity gate measures sentence-level predictability to fight "AI slope" (text sliding toward statistical averages)
- 9 rewriting techniques when flagged: Verbalized Sampling, Fragmentation, Character Voice, Rare Vocabulary, etc.
- Author proved concept with 18-chapter French novel mimicking Enid Blyton's style
- Source: [HackerNoon - Claude Book Framework](https://hackernoon.com/claude-book-a-multi-agent-framework-for-writing-novels-with-claude-code)
- Source: [GitHub - Claude-Code-Novel-Writer](https://github.com/forsonny/Claude-Code-Novel-Writer)

#### Creative Writing Skills (Open Source)
- 6 specialized skills: cw-router, cw-prose-writing, cw-brainstorming, cw-story-critique, cw-style-skill-creator, cw-official-docs
- Supports: ideation, style analysis from sample chapters, production aligned with established voice, story bibles, targeted critique
- Source: [GitHub - haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills)

#### Aaron Held -- Blog Writing Workflow
- 4-window system: Hugo server, Claude Code terminal, VSCode editor, browser with mobile emulation
- CLAUDE.md contains workflow document for consistency across sessions
- Workflow file stored at `.claude/workflows/create-blog-post-with-image.md`
- Phases: Planning (TodoWrite), Research (grep + web), Writing (iterative editing), Images (Unsplash), Deployment (GitHub Actions)
- Source: [Aaron Held - Streamlining Blog Writing with Claude Code](https://www.aaronheld.com/post/streamlining-blog-writing-with-claude-code/)

#### AI Maker Substack -- Personal AI Agent OS for Writing & Research
- Uses /init to auto-generate CLAUDE.md from entire project folder
- Custom slash commands: /quick-edit, /generate-ideas, /seo-optimize
- Sub-agents for daily news monitoring, Substack note generation, tool analysis
- MCP integrations: Perplexity for research, Firecrawl for web content extraction
- 3 output modes: Growth Strategist, Funnel Conversion, Social Media Strategist
- Source: [AI Maker Substack](https://aimaker.substack.com/p/how-i-turned-claude-code-into-personal-ai-agent-operating-system-for-writing-research-complete-guide)

### B. Knowledge Management

#### Matt Stockton -- Claude Code as Knowledge Management System
- Uses Claude Code for consulting work: client documentation, meeting notes, email drafts, project organization
- Creates CLAUDE.md instruction files in EACH client folder with: client background, communication preferences, document templates, writing style guidelines
- Workflow: records audio after client meetings -> Claude turns rambling audio into structured meeting summaries -> stores in right place -> updates work log
- Cross-project intelligence via Git version tracking
- **Compounding effect**: system value increases over time as captured instructions/documents/processes build on each other
- Source: [Matt Stockton - How Claude Code Became My Knowledge Management System](https://mattstockton.com/2025/09/19/how-claude-code-became-my-knowledge-management-system.html)

#### Noah Brier / Every.to -- Claude Code as Second Brain / Thinking Partner
- Cofounder of Alephic (AI strategy consultancy)
- Runs Claude Code within Obsidian (~1,500 notes)
- Key quote: **"There's entirely too much focus on [AI's] ability to write and not enough focus on its ability to read... arguably [that's] much more useful on a day-to-day basis."**
- Uses AI to search existing vault, not generate new content
- Subfolders: Chats, Daily Progress, Research
- Agents that ask clarifying questions, track inquiries, maintain research logs
- Mobile access via Termius + Tailscale
- Source: [Every.to - How to Use Claude Code as a Second Brain](https://every.to/podcast/how-to-use-claude-code-as-a-thinking-partner)

#### Claude Code + Obsidian "Second Brain" Ecosystem
- Multiple open-source starter kits:
  - COG-second-brain: daily intelligence briefings, weekly pattern analysis, monthly knowledge consolidation
  - obsidian-claude-pkm: complete PKM system in 15 minutes
  - Knowledge Vault: replaces Evernote, Notion, Asana, Otter.ai with local markdown + Claude Code
- Source: [GitHub - COG-second-brain](https://github.com/huytieu/COG-second-brain)
- Source: [GitHub - obsidian-claude-pkm](https://github.com/ballred/obsidian-claude-pkm)
- Source: [Knowledge Vault Gist](https://gist.github.com/naushadzaman/164e85ec3557dc70392249e548b423e9)
- Source: [Medium - Obsidian + Claude Code = Second Brain](https://medium.com/aimonks/obsidian-claude-code-second-brain-521e87adbe91)
- Source: [Building Your AI-Powered Second Brain](https://medium.com/vibe-coding/building-your-ai-powered-second-brain-how-claude-code-obsidian-changed-everything-about-my-37dc3bdd199e)

### C. Product Management

#### Claude Code for PMs (ccforpms.com)
- Free interactive course teaching PMs to use Claude Code
- CLAUDE.md as "project constitution" -- permanent context about the product
- PM-specific CLAUDE.md entries: product context, user personas, writing style standards, product terminology, immutable rules
- Example: "ALWAYS include acceptance criteria in user stories"
- Example: Terminology enforcement -- "Task not Todo or Issue"
- No coding or terminal experience required
- Covers: PRD authoring, roadmap planning, customer feedback analysis, competitive intelligence, ticket generation, stakeholder updates
- Source: [ccforpms.com](https://ccforpms.com/)
- Source: [ccforpms.com/fundamentals/project-memory](https://ccforpms.com/fundamentals/project-memory)

#### Teresa Torres / ProductTalk
- Central argument: "using Claude Code isn't about being technical. It's about being willing to try three to four simple terminal commands."
- Detailed competitive research workflow example showing Claude Code vs browser Claude
- File-based persistence vs vendor-locked chat sessions
- Parallel agents analyzing multiple competitors simultaneously
- Source: [ProductTalk - Claude Code: What It Is, How It's Different](https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/)
- Source: [ProductTalk - How to Use Claude Code Features](https://www.producttalk.org/how-to-use-claude-code-features/)

#### Real PM Outcomes
- PMs built three working prototypes, automated competitive analysis, generated comprehensive PRDs from scattered meeting notes -- all without writing a single line of code
- Synthesis that used to take a full day now takes a few minutes
- Source: [Builder.io - Claude Code for Product Managers](https://www.builder.io/blog/claude-code-for-product-managers)
- Source: [Lenny's Newsletter - Claude Code for PMs](https://www.lennysnewsletter.com/p/this-week-on-how-i-ai-claude-code)

### D. Data Science & Data Journalism

#### Kevin Schaul / Washington Post -- Data Journalism
- Consolidated AI use case inventories from multiple federal agencies
- Each agency published data in different formats, locations, inconsistent column names
- Key lesson: "Don't try to one-shot a complicated process. Go one step at a time."
- Emphasis on code review: **"When you're doing data journalism, vibes are not enough."**
- Completed in days what would have taken weeks of manual work
- Source: [Kevin Schaul - How I used Claude Code in a real data journalism project](https://kschaul.com/post/2026/02/09/2026-02-09-ai-data-journalism/)

#### Claude Code for Data Scientists
- Workflows: load/clean data, exploratory analysis, statistical summaries, visualizations
- Non-developers can drop CSV into interface without coding
- "Claude Code for Non-Coders" series covers managers and professionals
- Source: [Dataquest - Getting Started with Claude Code for Data Scientists](https://www.dataquest.io/blog/getting-started-with-claude-code-for-data-scientists/)
- Source: [Claude Code for Non-Coders - Week 3](https://claudecodefornoncoders.substack.com/p/week-3-make-claude-code-your-secret)

#### Health Data Analysis
- One researcher gave Claude Code 9.5 years of Apple Watch health data to find patterns for thyroid disease management
- Source: [Medium - I Gave Claude Code 9.5 Years of Health Data](https://medium.com/data-science-collective/i-gave-claude-code-9-5-years-of-health-data-to-help-manage-my-thyroid-disease-85fcd8c0449f)

### E. Legal & Professional Services

#### Claude Legal Skill (Open Source)
- Contract review, NDA triage, compliance workflows
- RED/YELLOW/GREEN flags with specific redline suggestions
- 200K context window enables analyzing entire contracts including exhibits/schedules/amendments in a single pass
- Source: [GitHub - claude-legal-skill](https://github.com/evolsb/claude-legal-skill)
- Source: [Spellbook - How to Use Claude AI for Legal Document Analysis](https://www.spellbook.legal/learn/claude-ai-legal-document-analysis)

#### Anthropic Legal Plugin (February 2026)
- Official Anthropic plugin for contract review
- Caused "market meltdown" in legal tech sector
- Source: [Legal IT Insider](https://legaltechnology.com/2026/02/03/anthropic-unveils-claude-legal-plugin-and-causes-market-meltdown/)
- Source: [Claude Plugins - Legal](https://claude.com/plugins/legal)

### F. Tax Preparation & Finance

#### Martin Alderson -- Tax Agent with Claude Code
- Used Claude Code to scrape ~10,000 UK tax documents from government websites
- Created CLAUDE.md configuration: "You are an expert UK tax professional capable of handling complex tax situations"
- Parallel subagents researching different tax domains (corporate, personal, rates, anti-avoidance, legislation)
- Tested against Association of Taxation Technicians exam papers -- scored 2.5/3
- Author notes approach applies to: contract management, content libraries, any professional service requiring document analysis
- Source: [Martin Alderson - Building a Tax Agent with Claude Code](https://martinalderson.com/posts/building-a-tax-agent-with-claude-code/)

#### Multiple "Claude Code Did My Taxes" Stories
- Source: [klmn.sh - Claude Code Did My Taxes](https://klmn.sh/essays/claude-code-for-taxes)
- Source: [Substack - Pay your taxes with Claude Code](https://cloudnativeengineer.substack.com/p/pay-your-taxes-with-claude-code)
- Source: [Medium - How Claude Code Built My Tax Refund Calculator](https://medium.com/@briandonelan/how-claude-code-built-my-tax-refund-calculator-and-saved-me-300-9f786f3baa8d)

#### Invoice Organization Skill
- Auto-organizes invoices/receipts: reads messy files, extracts key info, renames consistently, sorts into logical folders
- Source: [awesome-claude-skills/invoice-organizer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/invoice-organizer/SKILL.md)

### G. Education

#### Anthropic Education Report
- 57% of educator conversations with Claude related to curriculum development (lesson plans, assignments)
- Professors using Claude to develop interactive simulations for students
- Educators building functional resources deployable immediately in classrooms
- Example: "A vocabulary matching game with drag-and-drop, then a reading passage with comprehension questions that give instant feedback, then three discussion prompts" -- working lesson file in 15 minutes with no coding
- Source: [Anthropic - How educators use Claude](https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude)
- Source: [NPR - How professors are using AI](https://www.npr.org/2025/10/02/nx-s1-5550365/college-professors-ai-classroom)

### H. Scientific Research

#### Patrick Mineault -- Claude Code for Scientists
- Classic scientific loop: data acquisition -> processing -> analysis -> visualization
- Scientists should maintain CLAUDE.md documenting: project dependencies, framework requirements, difficult bug solutions, system constraints
- Key caution: "vibecoding without that metacognition is, IMO, quite dangerous"
- Source: [NeuroAI Science - Claude Code for Scientists](https://www.neuroai.science/p/claude-code-for-scientists)

#### Claude Scientific Skills (Open Source)
- Ready-to-use scientific skills for Claude
- Source: [GitHub - K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)

#### Biomni (Stanford)
- Agentic AI platform collecting hundreds of biological tools
- Claude-powered agent navigates them with plain English requests
- Can form hypotheses, design experimental protocols, perform analyses across 25+ biological subfields
- Source: [Anthropic - How scientists are using Claude](https://www.anthropic.com/news/accelerating-scientific-research)

#### Healthcare Applications
- Claude for Healthcare: HIPAA-ready products for providers, payers, health tech
- Source: [Anthropic - Advancing Claude in healthcare](https://www.anthropic.com/news/healthcare-life-sciences)
- Source: [IntuitionLabs - Claude Code in Life Sciences](https://intuitionlabs.ai/articles/claude-code-life-science-applications)

### I. Business / Marketing / Sales

#### Nate's Newsletter -- "Claude Code Without the Code" (64-page guide)
- Legal, marketing, research, document automation, sales, HR, finance, product management
- Marketing automation example: "analyzes writing style, generates personalized content, optimizes keywords, schedules through Buffer -- total operational cost of fifteen cents weekly"
- Healthcare platform "recovered $1.2M in pipeline within six weeks"
- Recruitment automation: "paste an interview transcript, get structured analysis, automatic Notion card creation"
- Obvi: "automated 10,000+ support tickets monthly with 65% faster response times"
- Source: [Nate's Newsletter - Claude Code Without the Code](https://natesnewsletter.substack.com/p/claude-code-without-the-code-the)

---

## 6. SKILLS & SLASH COMMANDS FOR NON-SWE WORKFLOWS

### Skills System Overview
- Skills = SKILL.md files with YAML frontmatter + markdown instructions
- Can be invoked manually (slash commands) or automatically by Claude when task matches
- Token-efficient: each skill takes only a few dozen extra tokens until activated
- Willison predicts "a Cambrian explosion in Skills which will make this year's MCP rush look pedestrian"
- Source: [Claude Code Docs - Extend Claude with skills](https://code.claude.com/docs/en/skills)
- Source: [Simon Willison - Claude Skills are awesome](https://simonwillison.net/2025/Oct/16/claude-skills/)

### Non-Coding Skill Examples
- **Content Research Writer**: conducts research, adds citations, improves hooks, provides section-by-section feedback
  - Source: [awesome-claude-skills/content-research-writer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/content-research-writer/SKILL.md)
- **Invoice Organizer**: reads messy files, extracts info, renames, sorts
  - Source: [awesome-claude-skills/invoice-organizer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/invoice-organizer/SKILL.md)
- **Legal Contract Review**: clause-by-clause analysis with risk flags
  - Source: [GitHub - claude-legal-skill](https://github.com/evolsb/claude-legal-skill)
- **Creative Writing Suite**: 6 skills for prose, brainstorming, critique, style analysis, documentation
  - Source: [GitHub - creative-writing-skills](https://github.com/haowjy/creative-writing-skills)
- **Scientific Research Skills**: ready-to-use scientific workflows
  - Source: [GitHub - claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)

### Skills as Open Standard (December 2025)
- Anthropic made Skills an open standard
- Enterprise customers using skills in production for legal, finance, accounting, data science
- Source: [SiliconAngle - Anthropic makes agent Skills an open standard](https://siliconangle.com/2025/12/18/anthropic-makes-agent-skills-open-standard/)
- Source: [VentureBeat - Anthropic launches enterprise Agent Skills](https://venturebeat.com/technology/anthropic-launches-enterprise-agent-skills-and-opens-the-standard)

### Slash Commands for Non-Code Tasks
> "The usefulness of slash commands isn't just limited to writing and testing code. You can use them to automate almost any repetitive, text-based task in your project."
- Example: /newpost "My Awesome Blog Title" -- generates markdown file with date, filename format, front matter
- Source: [eesel.ai - Practical guide to Claude Code slash commands](https://www.eesel.ai/blog/claude-code-slash-commands)
- Source: [OneAway - Claude Code Skills and Slash Commands](https://oneaway.io/blog/claude-code-skills-slash-commands)

### Gend.co Guide (2026)
- CLAUDE.md skeleton for non-dev work: "stabilize outputs for non-dev work like policy drafts and briefs"
- Sections: purpose, triggers, inputs, steps, outputs, refusal/escalation guidelines
- Creating Projects for marketing, support, or client work
- Source: [Gend.co - Claude Skills and CLAUDE.md guide](https://www.gend.co/blog/claude-skills-claude-md-guide)

---

## 7. HOOKS FOR NON-CODING AUTOMATION

### How Hooks Work
- User-defined shell commands at specific lifecycle points
- Types: "command" (runs shell command), "prompt" (single-turn evaluation), "agent" (multi-turn verification)
- Communicate via stdin/stdout/stderr/exit codes
- Source: [Claude Code Docs - Automate workflows with hooks](https://code.claude.com/docs/en/hooks-guide)

### Non-Coding Hook Applications
- Auto-updating work logs after meetings or substantial work
- Structured meeting note summaries from voice recordings
- Client-specific to-do list maintenance based on project progress
- Memory persistence hooks
- Source: [Matt Stockton](https://mattstockton.com/2025/09/19/how-claude-code-became-my-knowledge-management-system.html)
- Source: [GitHub - everything-claude-code/hooks/memory-persistence](https://github.com/affaan-m/everything-claude-code/tree/main/hooks/memory-persistence)

---

## 8. AGENT SDK FOR NON-SWE APPLICATIONS

### Anthropic's Own Statement
> "Claude Code has become far more than a coding tool" at Anthropic, being used "for deep research, video creation, and note-taking, among countless other non-coding applications."
- Design principle: "give your agents a computer, allowing them to work like humans do"
- Source: [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

### Specific Non-Coding Agent Types
- **Finance agents**: evaluate investments via API + calculations
- **Personal assistant agents**: book travel, manage calendars, schedule appointments, compile briefs
- **Research agents**: process files, generate insights across document collections
- **Customer support agents**: handle ambiguous requests, collect/review data, escalate to humans

---

## 9. THE ECOSYSTEM: Curated Resources

### Awesome Lists
- **awesome-claude-code**: 75+ repositories covering CMS, system design, deep research, IoT, agentic workflows
  - Source: [GitHub - hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)
- **awesome-claude-skills** (Composio): content research writer, invoice organizer, and more
  - Source: [GitHub - ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- **awesome-agent-skills** (VoltAgent): 300+ agent skills from official dev teams and community
  - Source: [GitHub - VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
- **awesome-claude-skills visual directory**
  - Source: [awesomeclaude.ai/awesome-claude-skills](https://awesomeclaude.ai/awesome-claude-skills)

### Courses & Guides
- **Claude Code for PMs**: [ccforpms.com](https://ccforpms.com/)
- **From Zero to Claude Code Pro in 90 Minutes (For PMs)**: [Maven course](https://maven.com/p/a422db/from-zero-to-claude-code-pro-in-90-minutes-for-p-ms)
- **Beyond the Chatbox: A Non-Technical Guide** (2026): [Medium](https://medium.com/@vinayanand2/beyond-the-chatbox-a-non-technical-guide-to-mastering-claude-code-in-2026-8f7acd3a6e7d)
- **Claude Code for Non-Coders** (Substack series): [claudecodefornoncoders.substack.com](https://claudecodefornoncoders.substack.com/p/week-3-make-claude-code-your-secret)
- **InterWorks - Get Work Done with Claude Code**: [interworks.com](https://interworks.com/blog/2026/02/11/get-work-done-with-claude-code-an-intro-to-using-agents)

### CLAUDE.md Guides
- [HumanLayer - Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [Builder.io - How to Write a Good CLAUDE.md File](https://www.builder.io/blog/claude-md-guide)
- [Dometrain - Creating the Perfect CLAUDE.md](https://dometrain.com/blog/creating-the-perfect-claudemd-for-claude-code/)
- [Arun Iyer - Instruction Files for AI Coding Assistants (AGENTS.md overview)](https://aruniyer.github.io/blog/agents-md-instruction-files.html)

---

## 10. INDUSTRY CONTEXT: Agentic AI Beyond Coding

### Enterprise Adoption Stats
- **Deloitte**: 2026 agentic AI strategy report
  - Source: [Deloitte - Agentic AI Strategy](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html)
- **IDC**: By 2026, AI copilots embedded in nearly 80% of enterprise workplace applications
- **Gartner**: By 2026, 40% of enterprise applications will include task-specific AI agents
- **UiPath** (mid-2025): ~65% of organizations piloting or deploying agentic systems; ~90% of executives planning increased investment
- Source: [Machine Learning Mastery - 7 Agentic AI Trends](https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/)

### No-Code Agent Platforms
- n8n, OpenAI Agent Builder, Gemini Opal
- Integration with email, calendars, documents, CRMs, ticketing systems
- Building an agent takes 15-60 minutes on most platforms
- Early adopters report 20-30% faster workflow cycles
- Source: [Gumloop - How to build agentic AI workflows in 2026 without coding](https://www.gumloop.com/blog/how-to-build-agentic-ai-workflows)
- Source: [Stack AI - 2026 Guide to Agentic Workflow Architectures](https://www.stack-ai.com/blog/the-2026-guide-to-agentic-workflow-architectures)

---

## 11. KEY QUOTES FOR THE BOOK

### On Claude Code being misnamed
> "Claude Code is, with hindsight, poorly named. It's not purely a coding tool: it's a tool for general computer automation." -- Simon Willison

### On the harness mattering more than the model
> "A concise, structured guide in the form of Claude.md always outperformed simply wiring in documentation tools." (evaluation finding)

### On reading vs. writing
> "There's entirely too much focus on [AI's] ability to write and not enough focus on its ability to read... arguably [that's] much more useful on a day-to-day basis." -- Noah Brier

### On non-technical accessibility
> "Using Claude Code isn't about being technical. It's about being willing to try three to four simple terminal commands." -- Teresa Torres

### On the compounding effect
Matt Stockton's knowledge management system has a "compounding effect" -- the value increases over time as instructions, documents, and processes build on each other. This is the opposite of stateless chat sessions.

### On the observation-to-product cycle
> Anthropic watched users repurpose a terminal coding tool for vacation planning and kitchen appliances, then built a new interface specifically for that emergent behavior.

### On domain-specific alignment
The CLAUDE.md file for a UK tax agent: "You are an expert UK tax professional capable of handling complex tax situations with comprehensive research" -- and it scored 2.5/3 on professional exams.

---

## 12. SYNTHESIS: Why This Matters for Our Book

### CLAUDE.md is the perfect "harness > model" example
1. **Same model, different alignment**: The exact same Claude model becomes a tax professional, a novelist, a PM co-pilot, a knowledge management system, or a data journalism tool -- purely through the harness (CLAUDE.md + skills + hooks + file system access)
2. **Persistent instruction beats ephemeral prompting**: The static markdown file outperformed more sophisticated approaches
3. **The compounding effect**: Unlike chat sessions, file-based context accumulates domain knowledge over time
4. **Non-technical users succeed**: PMs, writers, teachers, consultants -- none of them need to understand the model's architecture
5. **Anthropic's own trajectory proves it**: They built a "coding" tool, watched non-coders adopt it, then built Cowork -- the users showed them the harness mattered more than the original framing

### The progression for the story
- 2022-2023: Stateless chat (copy-paste, re-explain everything each session)
- 2024: Projects/system prompts (persistent context, but locked in vendor UI)
- 2025: CLAUDE.md + file system access (persistent, portable, hierarchical, domain-agnostic alignment)
- 2026: Skills as open standard + Cowork (the harness pattern becomes universal, non-technical)

### What the Skeptic would say
"So you're telling me I need to write a config file for my AI? That sounds like programming with extra steps."

### What the Maven would say
"That config file IS the magic. The same model that writes code for Google engineers just helped a teacher build an interactive vocabulary game in 15 minutes. The difference isn't the model -- it's the instructions you give it about YOUR domain, YOUR standards, YOUR workflow. And those instructions persist. Every session, it already knows what you told it last time."
