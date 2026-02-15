# Session 5: Claude Code for Non-Software-Engineering Use Cases

Research date: 2026-02-15

## Summary

Comprehensive research sweep on proven, documented use cases of Claude Code (the CLI agentic tool) for tasks outside traditional software development. This covers writing, research, data analysis, legal/financial/academic work, project management, knowledge management, creative applications, accessibility, journalism, education, and the emerging "CLAUDE.md as alignment" pattern applied to non-code domains.

---

## 1. LANDMARK ARTICLES & ESSAYS

### Ethan Mollick — "Claude Code and What Comes Next"
- **Source**: [https://www.oneusefulthing.org/p/claude-code-and-what-comes-next](https://www.oneusefulthing.org/p/claude-code-and-what-comes-next)
- **Who**: Ethan Mollick, Wharton professor, author of "Co-Intelligence"
- **What was done**:
  - Had Claude Code autonomously create a complete web-based business selling prompt sets for $39. Claude asked 3 multiple-choice questions, then worked independently for 1 hour 14 minutes generating hundreds of code files and a deployed website with payments.
  - Had Claude Code conduct user testing on a live website from different personas — it browsed the site "like a human would" and produced both optimistic and critical reports.
  - Built a civilization simulation game with evolving languages, cultures, economies, plate tectonics, and weather systems.
  - Claude Code analyzed credit card records for anomalies.
  - Marketing managers scraped competitor ads.
- **Why better than chat**: The system worked "independently" without user intervention — autonomous multi-step execution, not back-and-forth conversation. Claude would playtest results and iterate without prompting.
- **Key quote**: Mollick says the biggest secret is that "Claude Code isn't just for developers — it's the transition from 'Chat AI' (where you talk to a bot) to 'Action AI' (where the bot actually does the work on your computer)."
- **Tweet**: [https://x.com/emollick/status/2009043516643832029](https://x.com/emollick/status/2009043516643832029) — "I wrote about Claude Code and why non-coders should be paying attention"

### Lenny Rachitsky — "Everyone should be using Claude Code more"
- **Source**: [https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code](https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code)
- **Who**: Lenny Rachitsky, Lenny's Newsletter (largest PM newsletter)
- **What was done**: Compiled 50+ non-coding use cases from 500+ people on X and LinkedIn. Specific named examples:
  - **Justin Dielmann** — "personal organization assistant" organizing downloads, finding duplicates, suggesting directory improvements
  - **Martin Merschroth** — automatically renaming and sorting scattered invoice files into tax-ready folders
  - **Anthony Roux** — analyzing Mac performance issues by checking memory, processes, and disk usage
  - **Jeff Lindquist** — analyzing app source code to identify target companies, then messaging them on LinkedIn
  - **Sergei Zotov** — mining GitHub repos for sensitive data patterns to find companies using coding agents
  - **Ben Aiad** — brainstorming domain names across multiple extensions, checking availability
  - **Justin Bleuel** — generating complete hiring materials including job descriptions, interview plans, evaluation rubrics
  - **Teresa Torres** — iterating on article outlines, improving hooks, conducting research with citations, section feedback
  - **Helen Lee Kupp** — transcribing morning stroller voice recordings, organizing thematically, generating article + LinkedIn versions
  - **Dan Shipper** — reviewing all meeting recordings to identify moments where he subtly avoided conflict
  - **Derek DeHart** — compiling call transcripts to validate/invalidate product assumptions
  - **Dan Heller** — manipulating audio files, converting sample rates, renaming, translating Portuguese to English
  - **James Pember** — "self-driving documentation" having Claude independently explore software and identify knowledge gaps
  - **Gang Rui** — analyzing journal entries + Git commits weekly to spot gaps between stated goals and actual behavior
  - **John Conneely** — built DIY instructions for a children's slide tower with design specifications
- **Why better than chat**: "Think of it as Claude Local or Claude Agent — an AI running locally able to do things directly on your computer"
- **Tweet**: [https://x.com/lennysan/status/1978130461596745856](https://x.com/lennysan/status/1978130461596745856)

### Dan Shipper / Every.to — "How to Use Claude Code for Everyday Tasks — No Programming Required"
- **Source**: [https://every.to/source-code/how-to-use-claude-code-for-everyday-tasks-no-programming-required](https://every.to/source-code/how-to-use-claude-code-for-everyday-tasks-no-programming-required)
- **Who**: Dan Shipper, CEO of Every
- **What was done**:
  - **Expense tracking**: Downloads credit card transactions, places in folder, opens terminal, types "claude," requests expense report — functional tracker in 10-20 minutes. "Because everything lives on his computer, the system gets smarter with each trip."
  - **Content analytics**: Analyzing massive content datasets to identify high-engagement patterns. "File size restrictions, context window caps, and chat length constraints disappear when AI runs on your computer instead of the cloud."
  - **Customer support research**: Non-developers investigating technical codebases to answer customer questions without engineering involvement.
  - **Marketing content**: Reviewing recent code changes and drafting feature release newsletter copy.
- **Named commenter**: David Sadofsky: "Hooking Claude Code up to Playwright MCP is a game changer... I no-code automated my whole online grocery shopping experience, had it walk me through a complex CRM software."
- **Why better than chat**: File size restrictions, context window caps, and chat length constraints disappear with local execution.

### Teresa Torres — Product Talk / ChatPRD Interview
- **Sources**:
  - [https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/](https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/)
  - [https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management)
  - [https://creatoreconomy.so/p/automate-your-life-with-claude-code-teresa-torres](https://creatoreconomy.so/p/automate-your-life-with-claude-code-teresa-torres)
- **Who**: Teresa Torres, Product Talk founder, product discovery expert
- **What was done**:
  - Uses Claude Code for "pair programming for everything" — task management, writing, research automation, content review
  - Custom `/update-competitors` slash command triggers multi-step competitive analysis workflow
  - `/today` command generates daily to-do list by scanning all task files, assembling overdue items, in-progress projects, research digests
  - Tasks stored as individual markdown files in Obsidian with YAML front matter (type, due_date, tags)
  - Natural language input creates files: "new task, send thank you to Claire. do today"
  - Modular CLAUDE.md architecture: moved from single massive file to dozens of focused markdown files. Global CLAUDE.md contains conditional logic: "If business question, load business profile"
  - After each session: "Claude, what'd you learn today that we should document?" — conversations automatically update context files
- **Techniques**: Slash commands, agents (parallel processing), markdown files as persistent memory, modular CLAUDE.md
- **Why better than chat**: "Your files are your context" — no copy-paste, builds compounding systems, enables parallel work, data stored locally as plain text

---

## 2. WRITING, EDITING & CONTENT CREATION

### Aaron Held — Blog Writing Workflow
- **Source**: [https://www.aaronheld.com/post/streamlining-blog-writing-with-claude-code/](https://www.aaronheld.com/post/streamlining-blog-writing-with-claude-code/)
- **What was done**: Five-step systematic process — content planning (TodoWrite for decomposition), research & context (grep searches of existing content + web research), collaborative writing (targeted edits, not full rewrites), image selection (Unsplash integration), publishing (git commits with GitHub Actions)
- **Technique**: Four-window setup (Hugo server, Claude Code workspace, VSCode editor, mobile-preview browser). Documented workflow files in `.claude/workflows/create-blog-post-with-image.md` ensure consistency across sessions.
- **Key quote**: "This isn't Claude writing *for* me — it's Claude writing *with* me."

### Wyndo / The AI Maker — "Claude Code as Personal AI Agent OS for Writing and Research"
- **Source**: [https://aimaker.substack.com/p/how-i-turned-claude-code-into-personal-ai-agent-operating-system-for-writing-research-complete-guide](https://aimaker.substack.com/p/how-i-turned-claude-code-into-personal-ai-agent-operating-system-for-writing-research-complete-guide)
- **What was done**: Built a complete AI writing/research operating system
- **Techniques**:
  - `/quick-edit` — strengthens openings, clarifies frameworks, improves transitions, enhances conclusions while maintaining brand voice
  - `/generate-ideas` — analyzes audience engagement and suggests newsletter ideas aligned with expertise
  - `/seo-optimize` — reviews past posts and suggests search optimization improvements
  - `/perspective-analysis` — examines content through 5 different lenses to uncover blind spots
  - Sub-agents for daily AI news summaries, Substack notes generation, tool analysis
  - Pre-configured output styles: Growth Strategist, Funnel Conversion, Social Media Strategist
  - MCP connections: Perplexity for real-time research, Firecrawl for website content extraction
  - Mobile integration via GitHub issues + Obsidian syncing for 24/7 project access

### Nicolas Cole — Fiction Writing Voice Skill
- **Source**: [https://nicolascolefiction.substack.com/p/how-to-build-a-claude-cowork-skill](https://nicolascolefiction.substack.com/p/how-to-build-a-claude-cowork-skill)
- **Who**: Nicolas Cole, founder of Commercial Fiction Club, co-founder of Ship 30 for 30
- **What was done**: Built Claude .Skill files that crystallize writing voice patterns. Multiple skills for different genres (Sci-Fi/Fantasy, Mystery/Thriller, Romance) and contexts (fiction vs. non-fiction).
- **Key quote**: "Your bottleneck to using AI to its maximum capacity as a writer is to be able to articulate how you do what you do."
- **Technique**: Detailed voice guidelines documenting specific syntax preferences, structural decisions, stylistic rules — intentional documentation, not AI inference.

### Creative Writing Skills (GitHub)
- **Source**: [https://github.com/haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills)
- **Skills included**: cw-prose-writing (generates scenes/chapters matching writer's style), cw-brainstorming (plot options, character arcs, story structure), cw-story-critique (pacing, character consistency, dialogue quality), cw-style-skill-creator (extracts voice patterns from existing work), cw-official-docs (character profiles, location wikis, lore documentation)
- **Workflow**: Project directory with style guides, character profiles in dedicated folders, world-building documentation. Iterative cycle of brainstorming → documenting → analyzing patterns → drafting → feedback.

### Content Research Writer Skill
- **Source**: [https://github.com/ComposioHQ/awesome-claude-skills/blob/master/content-research-writer/SKILL.md](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/content-research-writer/SKILL.md)
- **Capabilities**: Research with citations, collaborative outlining, hook enhancement (data-driven, question-based, story-driven alternatives), section-by-section feedback, voice preservation
- **Four phases**: Understanding the project → Research → Drafting → Polish

### WomenDefiningAI/claudecode-writer
- **Source**: [https://github.com/WomenDefiningAI/claudecode-writer](https://github.com/WomenDefiningAI/claudecode-writer)
- **What it does**: Transforms ideas into multi-format content: research → long-form articles → platform-specific versions (LinkedIn, newsletter, social media, podcast Q&A)

---

## 3. DATA ANALYSIS & FINANCIAL APPLICATIONS

### Vladimir Klimontovich — Claude Code Did My Taxes
- **Source**: [https://klmn.sh/essays/claude-code-for-taxes](https://klmn.sh/essays/claude-code-for-taxes)
- **Who**: Vladimir Klimontovich, tech entrepreneur
- **What was done**: Prepared complex multi-state tax return (Federal, NYS, NYC) — joint filing, W-2 and consulting income, dual Schedule C, SEP IRA optimization, HSA contributions, child care credits, foreign accounts. ~2 hours across 5 sessions.
- **Techniques**:
  - Sub-agent architecture: spawned separate agents for parsing large PDFs, converting W-2s into concise markdown summaries
  - Persistent state: `answers.md` and `COMMONSENSE_CLASSIFICATION_RULES.md` files prevented re-asking questions across sessions
  - Two-step processing: generate `results.json` first, then map to PDF tax forms
  - Explicit constraints: "If it's large, don't read it directly — launch a Python script to extract the data"
- **Cost**: "A few dozen dollars" in tokens vs. $1,300-$2,000+ CPA fees
- **Limitation**: Final-step PDF form filling remained problematic. E-filing still requires CPA/TurboTax.

### Matt Stockton — Portfolio Optimization with Claude Code
- **Source**: [https://mattstockton.com/2026/02/10/building-a-portfolio-optimization-plan-with-claude-code.html](https://mattstockton.com/2026/02/10/building-a-portfolio-optimization-plan-with-claude-code.html)
- **What was done**: Fed brokerage CSV exports, account details, and detailed goals/constraints to Claude Code across multiple sessions. Output: allocation tables, style-box grids, phased action sequence, tax impact analysis with payback periods, fund swaps with expense ratio comparisons and Morningstar ratings.
- **CLAUDE.md technique**: Created persistent instructions file carrying "data quirks, strategy decisions, target allocations" across sessions. "Claude picked up right where we left off" after several days.
- **Goal prompt technique**: Wrote extensively about desired outputs, constraints, preferences, asked Claude to "ask me questions exhaustively" before jumping to conclusions.
- **Key quote**: "The kind of plan you'd pay a financial advisor to produce" accomplished in "a few evenings."
- **Why better than chat**: Portfolio analysis involves parsing multiple CSV formats simultaneously. Chat requires copy-paste piecemeal; Code handles entire directories.

### The Prompt Warrior — Data Analysis Use Cases
- **Source**: [https://www.thepromptwarrior.com/p/5-powerful-claude-code-use-cases-you-probably-didn-t-know-about-5826bfb7f5b8fdd8](https://www.thepromptwarrior.com/p/5-powerful-claude-code-use-cases-you-probably-didn-t-know-about-5826bfb7f5b8fdd8)
- **Competitor analysis**: "Do a deep competitor analysis" for an industry — Claude searches, processes, generates comprehensive reports
- **Content scraping**: Built YouTube scraper using Google API, retrieves video lists with view counts for strategy analysis
- **Business data**: Uploaded CSV files (SaaS churn data), prompted "Pretend you're a consultant. Analyze this data and provide actionable insights."
- **Why better than chat**: "Unlike ChatGPT, Claude Code can actually write and execute code on your machine"

---

## 4. JOURNALISM & DATA REPORTING

### Kevin Schaul / Washington Post — Data Journalism
- **Source**: [https://kschaul.com/post/2026/02/09/2026-02-09-ai-data-journalism/](https://kschaul.com/post/2026/02/09/2026-02-09-ai-data-journalism/)
- **Who**: Kevin Schaul, visual journalist at The Washington Post
- **What was done**: Used Claude Code (Opus 4.5) for a story examining federal government AI usage. Consolidated government AI use case inventories across multiple agencies — different formats, locations, inconsistent columns.
- **Technique**: Discrete steps rather than one-shot. Claude searched for agency inventory pages, downloaded files, wrote and refined consolidation scripts.
- **Key quote**: "I have been told 'You're absolutely right!' far too many times by these tools to trust them" — but AI-generated scripts are suitable for code review. "Don't try to one-shot a complicated process. Go one step at a time."

### Florent Daudens — AI as Reporting Assistant
- **Source**: [https://fdaudens.substack.com/p/how-to-use-ai-as-a-reporting-assistant](https://fdaudens.substack.com/p/how-to-use-ai-as-a-reporting-assistant)
- **Who**: Florent Daudens, 15+ years journalism/newsroom leadership
- **What was done**: Three practical workflows for journalists:
  1. **Daily news monitoring**: `/daily-digest` slash command generates 8-10 summarized items in markdown (20-min setup, saves 25+ min daily)
  2. **Interview preparation**: Claude fetches YouTube transcripts automatically, reviews background materials, generates questions, identifies coverage gaps
  3. **Publication packages**: After article drafts, Claude generates push notifications, Twitter threads, LinkedIn posts, Facebook versions, style guide checks
- **Techniques**: Persistent source folders (`/sources/municipal-budget/`), `context.md` tracking findings, reusable skills (`foia-request.md`, `interview-prep.md`), MCP integrations for newsroom CMS archives and public records databases
- **Why better than chat**: "Every single time, starting from zero. Re-uploading files." Persistent folders solve this.
- **Cost**: $20/month, 2-4 hours initial setup, 1-2 weeks to proficiency

---

## 5. SCIENTIFIC & ACADEMIC RESEARCH

### Patrick Mineault — "Claude Code for Scientists"
- **Source**: [https://www.neuroai.science/p/claude-code-for-scientists](https://www.neuroai.science/p/claude-code-for-scientists)
- **Who**: Patrick Mineault, NeuroAI lead at Amaranth; previously Google, Meta, Mila
- **What was done**:
  - Data processing pipelines (raw data → processed outputs)
  - Diagnostic visualization (exploratory plots to validate data correctness)
  - Repository improvement (READMEs, dead code removal, dependency clarification)
  - Interactive analysis (plotly, streamlit, leaflet visualizations)
  - Code refactoring while maintaining test coverage
- **CLAUDE.md strategy**: Specifying project structure, dependency management (mamba/uv), framework-specific guidance. For marimo notebooks: "add this text to CLAUDE.md for best results."
- **Folder structure rails**: data/raw → data/processed → src → notebooks + data/generated/
- **Key insight**: Agentic tools enable senior researchers to "remain productive and somewhat in the weeds" while making solo research feasible. "It lowers the cost of both exploration and exploitation."
- **Warning**: "You can produce wrong results faster than ever before" — validation and metacognition essential.

### Claude Scientific Writer (GitHub)
- **Source**: [https://github.com/K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer)
- **Capabilities**: Publication-ready papers (Nature, Science, NeurIPS formats with IMRaD structure), clinical reports, research posters (LaTeX-based), grant proposals (NSF, NIH, DOE, DARPA formatting), literature reviews
- **Features**: Real-time research via Perplexity Sonar Pro Search, AI diagram generation, peer review feedback with ScholarEval framework, bibliography management, figure integration

### Simon Willison — Async Code Research Pattern
- **Source**: [https://simonwillison.net/2025/Nov/6/async-code-research/](https://simonwillison.net/2025/Nov/6/async-code-research/)
- **Who**: Simon Willison, Django co-creator, datasette author
- **Pattern**: Pick a research question, spin up an async coding agent, let it run experiments and report back. "Coding agents like Claude Code and Codex are a fantastic fit for research work — the code itself doesn't lie."
- **Repository**: [https://github.com/simonw/research](https://github.com/simonw/research) — each directory is a separate research project, every line written by LLM

---

## 6. LEGAL & COMPLIANCE

### Mastering AI — Legal Use Cases
- **Source**: [https://www.masteringai.io/guides/50-non-coding-uses-claude-code](https://www.masteringai.io/guides/50-non-coding-uses-claude-code)
- **50,000 contracts analyzed**: International law firm analyzed contracts for $2.3B acquisition in 72 hours vs. 3 weeks traditionally
- **Contract redlining**: Automatic comparison, change tracking, risk assessment, response language drafting
- **Due diligence automation**: Systematically reviews documents for risks, obligations, red flags across categories
- **Legal document extraction**: Pulls relevant provisions into searchable, filterable databases

### Anthropic — Claude Legal Plugin
- **Source**: [https://legaltechnology.com/2026/02/03/anthropic-unveils-claude-legal-plugin-and-causes-market-meltdown/](https://legaltechnology.com/2026/02/03/anthropic-unveils-claude-legal-plugin-and-causes-market-meltdown/)
- **Capabilities**: Document review, risk flagging, NDA triage, compliance tracking

### Anthropic — How Anthropic Uses Claude in Legal
- **Source**: [https://claude.com/blog/how-anthropic-uses-claude-legal](https://claude.com/blog/how-anthropic-uses-claude-legal)
- Employment lawyers using Claude-powered workflow for conflict-of-interest form reviews — can now focus on edge cases rather than routine approvals

---

## 7. PROJECT MANAGEMENT & KNOWLEDGE MANAGEMENT

### Claude Code Course for PMs
- **Source**: [https://ccforpms.com/](https://ccforpms.com/)
- **Who**: Carl Vellotti
- **Covers**: PRD writing via Socratic questioning + sub-agent reviews, data analysis (product funnels, A/B tests), research synthesis from meeting transcripts, competitive strategy with parallel agents, meeting management
- **Technique**: Custom AI reviewers representing engineering, executive, and UX perspectives before sharing work

### Second Brain Systems
- **Remember Plugin**: [https://github.com/remember-md/remember](https://github.com/remember-md/remember) — Free, local-first plugin using PARA + Zettelkasten methodology. Say "remember this" and knowledge auto-organizes.
- **COG Second Brain**: [https://github.com/huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain) — Self-evolving intelligence using Claude Code + Obsidian + GitHub
- **Second Brain Skills**: [https://github.com/coleam00/second-brain-skills](https://github.com/coleam00/second-brain-skills) — Brand & voice generator, PPTX generator, SOP creator, MCP client, Remotion video creator

### Animalz — Content Marketing Knowledge Base
- **Source**: [https://www.animalz.co/blog/claude-code](https://www.animalz.co/blog/claude-code)
- **Five core use cases for content marketers**: Queryable database from multiple sources, interview transcript analysis, content library audits (publishing cadence, topic percentages, internal linking gaps), interactive HTML presentations, style guide extraction from published articles

---

## 8. PRODUCT MANAGEMENT SPECIFIC

### Builder.io — Claude Code for Product Managers
- **Source**: [https://www.builder.io/blog/claude-code-for-product-managers](https://www.builder.io/blog/claude-code-for-product-managers)
- **Capabilities**: Plain English → working prototypes, CSV data analysis, documentation generation, MCP integrations with Linear/Jira/Slack

### prodmgmt.world
- **Source**: [https://www.prodmgmt.world/claude-code](https://www.prodmgmt.world/claude-code)
- **Source**: [https://www.prodmgmt.world/blog/how-to-use-claude-code](https://www.prodmgmt.world/blog/how-to-use-claude-code)
- Plugins, guides, and workflows specifically for PMs

---

## 9. CREATIVE & UNCONVENTIONAL USES

### Generative Art with Claude Skills
- **Source**: [https://blog.lmorchard.com/2025/11/05/hunting-horizon/](https://blog.lmorchard.com/2025/11/05/hunting-horizon/)
- **Who**: Les Orchard (blog.lmorchard.com)
- **What was done**: Created "Hunting Horizon" — animated web component depicting birds hunting fish at air-water interface, with particle systems, swooping birds, scattering fish, environmental elements. Used Anthropic's "algorithmic-art" skill.
- **Workflow**: Conceptual prompt → iterative refinement → feature additions (flight behavior, twinkling stars, water ripples, fish schooling, predator-death mechanics, animated moon)
- **Key quote**: "While Claude generated the bulk of the code, I didn't just sit back: I gave it ideas, did some debugging and coding, and steered things to make it my own."

### Accessibility Applications
- **Source**: [https://www.masteringai.io/guides/50-non-coding-uses-claude-code](https://www.masteringai.io/guides/50-non-coding-uses-claude-code)
- **Communication app for ALS/stroke patients**: Predictive text tool with voice output built in one hour
- **Speech therapy practice app**: Targeting specific sounds and therapy goals
- **Visual schedules for autism**, memory aids for dementia, medication reminders with alerts
- **Simplified interfaces for cognitive disabilities**: Customized UIs tailored to individual abilities

### Video Creation & Editing
- **Source**: [https://www.thepromptwarrior.com/p/5-powerful-claude-code-use-cases-you-probably-didn-t-know-about-5826bfb7f5b8fdd8](https://www.thepromptwarrior.com/p/5-powerful-claude-code-use-cases-you-probably-didn-t-know-about-5826bfb7f5b8fdd8)
- Marketing videos via Remotion (React-based video components)
- Audio extraction, auto-transcription via Whisper API, clip editing via FFmpeg
- Presentation slides using Reveal.js from screenshots

### Danielle Morrill — Cooking with Claude
- **Source**: [https://ellemorrill.substack.com/p/cooking-with-claude](https://ellemorrill.substack.com/p/cooking-with-claude)
- Using Claude as a cooking companion, multi-day meal prep scheduler

### Recipe Development Lab
- **Source**: [https://www.claudecodehq.com/playbooks/recipe-development-lab](https://www.claudecodehq.com/playbooks/recipe-development-lab)
- Version and perfect recipes, track modifications, plan menus from tested recipe library

---

## 10. EDUCATION

### Anthropic — Claude for Education
- **Source**: [https://www.anthropic.com/news/introducing-claude-for-education](https://www.anthropic.com/news/introducing-claude-for-education)
- **Source**: [https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude](https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude)
- Learning mode guides students' reasoning rather than providing answers
- Teachers building lessons as interactive HTML files instead of PowerPoints

### Codecademy — Lesson Plan Generator Tutorial
- **Source**: [https://www.codecademy.com/article/how-to-build-claude-skills](https://www.codecademy.com/article/how-to-build-claude-skills)
- Tutorial on building a lesson plan generator skill

### Johns Hopkins / LinkedIn Learning
- **Source**: [https://imagine.jhu.edu/classes/claude-code-for-non-programmers-automating-daily-tasks/](https://imagine.jhu.edu/classes/claude-code-for-non-programmers-automating-daily-tasks/)
- **Source**: [https://www.linkedin.com/learning/claude-code-for-non-programmers-automating-daily-tasks](https://www.linkedin.com/learning/claude-code-for-non-programmers-automating-daily-tasks)
- Course: "Claude Code for Non-Programmers: Automating Daily Tasks"

---

## 11. CLAUDE COWORK — The "Claude Code for Normies" Product

### Anthropic Product Launch (January 2026)
- **Source**: [https://claude.com/product/cowork](https://claude.com/product/cowork)
- **Source**: [https://www.theneuron.ai/explainer-articles/claude-cowork-explained-everything-to-know-about-anthropics-answer-to-claude-code-for-normies](https://www.theneuron.ai/explainer-articles/claude-cowork-explained-everything-to-know-about-anthropics-answer-to-claude-code-for-normies)
- **Source**: [https://www.theneurondaily.com/p/breaking-claude-cowork-claude-code-for-normies](https://www.theneurondaily.com/p/breaking-claude-cowork-claude-code-for-normies)
- **What it is**: Same agentic architecture as Claude Code, accessible within Claude Desktop without terminal. Research preview for Claude Max subscribers on macOS.
- **Capabilities**: Sub-agent coordination, Excel spreadsheets with working formulas, PowerPoint presentations, long-running tasks without context limits
- **Use cases**: Expense reports, file organization, research synthesis, presentations
- **Knowledge Work Plugins**: [https://github.com/anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) — Open source plugins for knowledge workers

---

## 12. CLAUDE.md AS ALIGNMENT — NON-CODE PATTERNS

### The Core Insight
CLAUDE.md is not just for code projects. It's a persistent alignment document that tells Claude who you are, what you care about, how you work, and what standards to apply. Applied to non-code domains, it becomes:

- **A style guide** for writing projects (voice, tone, structure preferences)
- **A research methodology** for academic/journalism projects (source standards, citation format, verification requirements)
- **A business context** for knowledge work (org structure, goals, customer profiles, competitive landscape)
- **A personal operating manual** for daily life automation (preferences, routines, priorities)

### Documented Patterns

**Teresa Torres** — Modular CLAUDE.md: Dozens of focused markdown files with conditional logic. Global CLAUDE.md loads context-specific files based on task type.
- Source: [https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management](https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management)

**Matt Stockton** — Financial CLAUDE.md: "data quirks, strategy decisions, target allocations" persisted across sessions for portfolio optimization.
- Source: [https://mattstockton.com/2026/02/10/building-a-portfolio-optimization-plan-with-claude-code.html](https://mattstockton.com/2026/02/10/building-a-portfolio-optimization-plan-with-claude-code.html)

**Vladimir Klimontovich** — Tax CLAUDE.md: `COMMONSENSE_CLASSIFICATION_RULES.md` for transaction categorization, `answers.md` for persistent Q&A state.
- Source: [https://klmn.sh/essays/claude-code-for-taxes](https://klmn.sh/essays/claude-code-for-taxes)

**Florent Daudens** — Journalism CLAUDE.md: `context.md` tracking investigation findings, `/.claude/skills/` with `foia-request.md` and `interview-prep.md`.
- Source: [https://fdaudens.substack.com/p/how-to-use-ai-as-a-reporting-assistant](https://fdaudens.substack.com/p/how-to-use-ai-as-a-reporting-assistant)

**Patrick Mineault** — Scientific CLAUDE.md: Project structure, dependency management, framework-specific guidance, folder structure rails.
- Source: [https://www.neuroai.science/p/claude-code-for-scientists](https://www.neuroai.science/p/claude-code-for-scientists)

**Shrivu Shankar** — Constitutional CLAUDE.md pattern: "Start with Guardrails, Not a Manual." Don't embed full reference docs; instead specify *when* and *why* to consult them. Replace negative constraints with positive alternatives.
- Source: [https://blog.sshh.io/p/how-i-use-every-claude-code-feature](https://blog.sshh.io/p/how-i-use-every-claude-code-feature)

**Rhonda Britten** — Voice-segmented skills: Separate CLAUDE.md-style files for overall voice, public audience, and coaches audience to prevent "mixing up audiences."
- Source: [https://aiblewmymind.substack.com/p/claude-skills-36-examples](https://aiblewmymind.substack.com/p/claude-skills-36-examples)

### The HumanLayer Guide
- **Source**: [https://www.humanlayer.dev/blog/writing-a-good-claude-md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- Defines CLAUDE.md as onboarding Claude into your project's WHY, WHAT, and HOW
- Keep contents concise and universally applicable
- Iterative refinement from failed attempts into modules of task context, rules, numbered steps and examples

---

## 13. COMPREHENSIVE GUIDES FOR NON-TECHNICAL USERS

### Eleanor Berger — "Claude Code for Non-Coders"
- **Source**: [https://everything.intellectronica.net/p/claude-code-for-non-coders](https://everything.intellectronica.net/p/claude-code-for-non-coders)
- Core argument: local agents transform AI from conversational tool to autonomous worker. "You won't be writing any code yourself."
- Desktop alternatives to terminal: Claude Desktop App (Code tab), VS Code extension, Goose (open-source)

### Jonas Braadbaart — "Claude Code for Non-Coders"
- **Source**: [https://metacircuits.substack.com/p/claude-code-for-non-coders](https://metacircuits.substack.com/p/claude-code-for-non-coders)
- Use cases: voice memos → polished articles, competitor ad scraping, client research, meeting notes → action items, wedding/holiday planning, PowerPoint from notes, PDF data extraction, file organization by date/type
- **Key quote on persistent context**: "Unlike standard chat, Claude Code maintains a 'persistent library of context that Claude draws from automatically.'"

### Nate's Newsletter — "Claude Code Without the Code"
- **Source**: [https://natesnewsletter.substack.com/p/claude-code-without-the-code-the](https://natesnewsletter.substack.com/p/claude-code-without-the-code-the)
- 64-page guide covering legal workflows, research systems, document automation
- Claims: recruitment workflow automation (paste interview transcripts, get structured analysis + automatic Notion cards), marketing system at $0.15/week operational cost, Obvi automated 10,000+ support tickets monthly with 65% faster response

### JP Caparas — "Claude Code is turning non-programmers into builders"
- **Source**: [https://blog.devgenius.io/claude-code-is-turning-non-programmers-into-builders-heres-how-to-start-6a70d06cdcfd](https://blog.devgenius.io/claude-code-is-turning-non-programmers-into-builders-heres-how-to-start-6a70d06cdcfd)

### Vinay Bhaskarla — "Beyond the Chatbox: A Non-Technical Guide to Mastering Claude Code in 2026"
- **Source**: [https://medium.com/@vinayanand2/beyond-the-chatbox-a-non-technical-guide-to-mastering-claude-code-in-2026-8f7acd3a6e7d](https://medium.com/@vinayanand2/beyond-the-chatbox-a-non-technical-guide-to-mastering-claude-code-in-2026-8f7acd3a6e7d)

### The Blueprint Newsletter — Non-Technical Getting Started Guide
- **Source**: [https://theblueprintnewsletter.com/p/a-non-technical-guide-to-getting-started-with-claude-code](https://theblueprintnewsletter.com/p/a-non-technical-guide-to-getting-started-with-claude-code)

---

## 14. SKILLS & TOOLS ECOSYSTEM

### 36 Claude Skills Examples (from 23 creators)
- **Source**: [https://aiblewmymind.substack.com/p/claude-skills-36-examples](https://aiblewmymind.substack.com/p/claude-skills-36-examples)
- **Non-coding skills documented**:
  - Content Extraction (Alex McFarland) — long-form → platform-specific content tables
  - Newsletter Ideation (Raghav Mehra) — 5-7 unique angles using SCAMPER, Jobs-to-be-Done
  - Creative QA Check (Mariam Vossough) — voice authenticity, structure, scanability, SEO, accessibility
  - Publication Proofreader (Mariam Vossough) — curly quotes, bullet styles, broken links, missing alt text
  - Voice Skills (Rhonda Britten) — separate skills for different audiences
  - Hero Image Prompt Generator (Dheeraj Sharma) — brand-consistent image prompts
  - The Self-Interview (Nick Quick) — "the skill asks you progressively deeper questions"
  - YouTube Toolkit (Jean-Paul Paoli) — downloads videos, audio, transcripts
  - Pre-Sale Article/Lead Magnet (Rhonda Britten)
  - Email Conversion Tester (Rhonda Britten)
  - Business Case Builder (Zain Haseeb) — executive-ready templates: quick, standard, comprehensive
  - Presentation Builder (Raghav Mehra)
  - Inventory Analyst (Alex Willen) — sales projections, stock-out dates, order timing
  - Word Document Styling (Ed Rodgers) — .docx output following custom templates
  - Meeting Analyzer (Daria Cupareanu) — action items, decisions, missed opportunities
  - Job Description Analyzer (Jose Antonio Morales) — compatibility score and recommendation
  - Micro-Experiments (Dee McCrorey) — low-stakes career explorations
  - Blue Fish (mark) — extracts learning moments from conversations into Notion database
  - The Skill Builder (Karo) — generates properly formatted SKILL.md files

### Awesome Agent Skills (300+)
- **Source**: [https://github.com/VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
- Skills from Anthropic, Google Labs, Vercel, Stripe, Cloudflare, Trail of Bits, Sentry, Expo, Hugging Face, and community

### Anthropic Official Skills
- **Source**: [https://github.com/anthropics/skills](https://github.com/anthropics/skills)
- **Source**: [https://claude.com/skills](https://claude.com/skills)

---

## 15. WHY CLAUDE CODE BEATS CHAT (RECURRING THEMES)

Every source converges on the same structural advantages:

1. **Direct file system access**: Read/write files on your machine without upload limits or context window compression. "File size restrictions, context window caps, and chat length constraints disappear." (Dan Shipper)

2. **Persistent context via CLAUDE.md and local files**: "Your files are your context" — no re-explaining, no re-uploading. Sessions build on each other. (Teresa Torres)

3. **Autonomous multi-step execution**: Agent completes complex workflows without back-and-forth. "Action AI" vs. "Chat AI." (Ethan Mollick)

4. **Compounding systems**: One setup yields reusable commands that work indefinitely. Slash commands, skills, and CLAUDE.md create institutional knowledge that compounds. (Teresa Torres, Wyndo)

5. **Sub-agents for parallel processing**: Multiple research threads or analysis tasks run simultaneously. (Mollick, Torres, Mineault)

6. **No vendor lock-in**: Data stored locally as plain text. Switch AI platforms without losing context. (Torres)

7. **MCP integrations**: Connect to external services (Playwright for browser automation, Perplexity for research, CMS, databases, CRMs) without leaving the workflow. (Daudens, Wyndo)

---

## 16. ALL SOURCE URLs (MASTER LIST)

### Landmark Articles
- https://www.oneusefulthing.org/p/claude-code-and-what-comes-next
- https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code
- https://every.to/source-code/how-to-use-claude-code-for-everyday-tasks-no-programming-required
- https://www.producttalk.org/claude-code-what-it-is-and-how-its-different/
- https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management
- https://creatoreconomy.so/p/automate-your-life-with-claude-code-teresa-torres

### Writing & Content
- https://www.aaronheld.com/post/streamlining-blog-writing-with-claude-code/
- https://aimaker.substack.com/p/how-i-turned-claude-code-into-personal-ai-agent-operating-system-for-writing-research-complete-guide
- https://nicolascolefiction.substack.com/p/how-to-build-a-claude-cowork-skill
- https://github.com/haowjy/creative-writing-skills
- https://github.com/ComposioHQ/awesome-claude-skills/blob/master/content-research-writer/SKILL.md
- https://github.com/WomenDefiningAI/claudecode-writer
- https://medium.com/@pa_sherman/how-i-built-my-personal-ai-writing-agent-with-claude-code-and-you-can-too-4f3ae29019d2
- https://kenny-kane.com/blog/claude-ai-for-writing
- https://www.animalz.co/blog/claude-code

### Data Analysis & Finance
- https://klmn.sh/essays/claude-code-for-taxes
- https://mattstockton.com/2026/02/10/building-a-portfolio-optimization-plan-with-claude-code.html
- https://medium.com/@briandonelan/how-claude-code-built-my-tax-refund-calculator-and-saved-me-300-9f786f3baa8d
- https://cloudnativeengineer.substack.com/p/pay-your-taxes-with-claude-code
- https://www.bogleheads.org/forum/viewtopic.php?t=443339
- https://sidsaladi.substack.com/p/the-claude-financial-modeling-workshop
- https://www.thepromptwarrior.com/p/5-powerful-claude-code-use-cases-you-probably-didn-t-know-about-5826bfb7f5b8fdd8

### Journalism
- https://kschaul.com/post/2026/02/09/2026-02-09-ai-data-journalism/
- https://fdaudens.substack.com/p/how-to-use-ai-as-a-reporting-assistant
- https://www.platformer.news/journalism-job-automation-claude/

### Scientific & Academic
- https://www.neuroai.science/p/claude-code-for-scientists
- https://github.com/K-Dense-AI/claude-scientific-writer
- https://simonwillison.net/2025/Nov/6/async-code-research/
- https://github.com/simonw/research
- https://www.chatprd.ai/how-i-ai/workflows/how-to-automate-academic-research-with-claude-code-and-python-scripts

### Legal
- https://legaltechnology.com/2026/02/03/anthropic-unveils-claude-legal-plugin-and-causes-market-meltdown/
- https://claude.com/blog/how-anthropic-uses-claude-legal
- https://claude.com/resources/use-cases-category/legal
- https://www.masteringai.io/guides/50-non-coding-uses-claude-code

### Product Management
- https://ccforpms.com/
- https://www.builder.io/blog/claude-code-for-product-managers
- https://www.prodmgmt.world/claude-code
- https://www.prodmgmt.world/blog/how-to-use-claude-code
- https://medium.com/product-powerhouse/claude-code-for-product-managers-complete-setup-guide-real-pm-workflows-2026-c94ec7087b6f
- https://maven.com/p/a422db/from-zero-to-claude-code-pro-in-90-minutes-for-p-ms
- https://medium.com/@rakesh.malloju/context-engineering-for-product-managers-the-next-big-10x-skill-38de541e8b9b

### Knowledge Management / Second Brain
- https://github.com/remember-md/remember
- https://github.com/huytieu/COG-second-brain
- https://github.com/coleam00/second-brain-skills
- https://medium.com/vibe-coding/building-your-ai-powered-second-brain-how-claude-code-obsidian-changed-everything-about-my-37dc3bdd199e
- https://trailway.medium.com/using-claude-code-for-organizing-your-second-brain-39137af6f596

### Non-Technical Guides
- https://everything.intellectronica.net/p/claude-code-for-non-coders
- https://metacircuits.substack.com/p/claude-code-for-non-coders
- https://natesnewsletter.substack.com/p/claude-code-without-the-code-the
- https://blog.devgenius.io/claude-code-is-turning-non-programmers-into-builders-heres-how-to-start-6a70d06cdcfd
- https://medium.com/@vinayanand2/beyond-the-chatbox-a-non-technical-guide-to-mastering-claude-code-in-2026-8f7acd3a6e7d
- https://theblueprintnewsletter.com/p/a-non-technical-guide-to-getting-started-with-claude-code
- https://departmentofproduct.substack.com/p/how-to-use-claude-code-for-non-engineering
- https://medium.com/@joe.njenga/claude-code-is-not-for-coding-only-i-tested-and-discovered-these-20-non-code-use-cases-6b7d9dc010c0

### Skills & Ecosystem
- https://aiblewmymind.substack.com/p/claude-skills-36-examples
- https://github.com/VoltAgent/awesome-agent-skills
- https://github.com/anthropics/skills
- https://claude.com/skills
- https://github.com/ComposioHQ/awesome-claude-skills
- https://github.com/travisvn/awesome-claude-skills
- https://awesomeclaude.ai/awesome-claude-skills
- https://www.lennysnewsletter.com/p/claude-skills-explained
- https://simonw.substack.com/p/claude-skills-are-awesome-maybe-a
- https://code.claude.com/docs/en/skills
- https://medium.com/data-science-collective/i-created-a-claude-skill-that-turns-piles-of-messy-documents-media-into-a-structured-report-19e9950f93b2

### Creative & Unconventional
- https://blog.lmorchard.com/2025/11/05/hunting-horizon/
- https://interconnected.org/home/2025/09/18/muzak
- https://ellemorrill.substack.com/p/cooking-with-claude
- https://www.claudecodehq.com/playbooks/recipe-development-lab

### Claude Cowork
- https://claude.com/product/cowork
- https://www.theneuron.ai/explainer-articles/claude-cowork-explained-everything-to-know-about-anthropics-answer-to-claude-code-for-normies
- https://www.theneurondaily.com/p/breaking-claude-cowork-claude-code-for-normies
- https://github.com/anthropics/knowledge-work-plugins
- https://medium.com/@cdcore/claude-cowork-feels-like-agi-until-you-try-to-use-it-041e94ffcd7c
- https://thezvi.substack.com/p/claude-coworks
- https://support.claude.com/en/articles/13345190-getting-started-with-cowork
- https://cowork.fast/

### Education
- https://www.anthropic.com/news/introducing-claude-for-education
- https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude
- https://www.codecademy.com/article/how-to-build-claude-skills
- https://imagine.jhu.edu/classes/claude-code-for-non-programmers-automating-daily-tasks/
- https://www.linkedin.com/learning/claude-code-for-non-programmers-automating-daily-tasks
- https://medium.com/@ajtracysk/using-claude-for-teaching-english-is-like-finding-cheat-codes-heres-my-workflow-c35df642b6a2

### Accessibility
- https://www.masteringai.io/guides/50-non-coding-uses-claude-code (accessibility section)
- https://github.com/anthropics/claude-code/issues/11002 (screen reader accessibility request)

### CLAUDE.md Patterns
- https://www.humanlayer.dev/blog/writing-a-good-claude-md
- https://blog.sshh.io/p/how-i-use-every-claude-code-feature
- https://www.builder.io/blog/claude-md-guide
- https://www.maxitect.blog/posts/maximising-claude-code-building-an-effective-claudemd
- https://medium.com/@patraqushe/knowledge-management-for-efficient-development-with-claude-code-bdd88b22bd68

### Hacker News Discussions
- https://news.ycombinator.com/item?id=44864185 (Claude Code is all you need)
- https://news.ycombinator.com/item?id=46470017 (Creator of Claude Code's setup)
- https://news.ycombinator.com/item?id=46098838 (Writing a good CLAUDE.md)
- https://news.ycombinator.com/item?id=45416228 (Claude Code 2.0)

### Tweets
- https://x.com/emollick/status/2009043516643832029 (Mollick on non-coders)
- https://x.com/lennysan/status/1978130461596745856 (Rachitsky on everyone using Claude Code)

### Anthropic Research
- https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- https://www.anthropic.com/news/advancing-claude-for-financial-services

### Other
- https://www.theneuron.ai/explainer-articles/how-to-turn-claude-code-into-your-personal-ai-assistant/
- https://cc.deeptoai.com/docs/en/community-tips/claude-code-life-os
- https://www.aitooldiscovery.com/guides/claude-code-reddit
- https://medium.com/@ondrej.machart/from-vibe-coding-to-tinystakeholders-an-effective-guide-for-the-non-technical-solo-builder-8125c0fac25b
- https://rogerwong.me/2025/10/everyone-should-be-using-claude-code-more
- https://aimultiple.com/agentic-coding
- https://www.datacamp.com/tutorial/claude-code-2-1-guide
- https://claudelog.com/
