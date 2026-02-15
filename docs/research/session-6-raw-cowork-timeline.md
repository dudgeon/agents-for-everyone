# Session 6 — Claude Code & Cowork for Non-SWE Tasks

Research session focused on proven use cases, proof points, techniques, and articles related to Claude Code and Cowork for NON-software-engineering tasks.

---

## PRIMARY SOURCES FETCHED

### 1. Anthropic: "How Anthropic Teams Use Claude Code" (Jul 24, 2025)

**URL**: https://claude.com/blog/how-anthropic-teams-use-claude-code (redirected from anthropic.com/news)

**Non-engineering teams highlighted:**

**Growth Marketing Team:**
- Processing CSV files with hundreds of ads to identify underperformers
- Generating new ad variations within strict character limits
- Built Figma plugin that generates up to 100 ad variations by swapping headlines/descriptions
- Reduced copy-pasting hours to "half a second per batch"

**Legal Team:**
- Created prototype "phone tree" systems to help team members connect with appropriate lawyers
- Non-technical lawyers building internal tools without engineering support

**Product Design Team:**
- Mapping error states and logic flows to identify edge cases during design
- Creating React applications for visualizing RL model performance without TypeScript fluency

**Data Scientists:**
- Building entire React visualizations from scratch without code fluency
- Creating complex visualizations without JavaScript knowledge
- Getting productive quickly on unfamiliar codebases

**Key quotes:**
- Claude Code "dissolves the boundary between technical and non-technical work, turning anyone who can describe a problem into someone who can build a solution."
- Most successful approach: treating Claude Code as "a thought partner rather than a code generator."

---

### 2. Anthropic: "How Anthropic Uses Claude in Legal" (date unknown, likely late 2025/early 2026)

**URL**: https://claude.com/blog/how-anthropic-uses-claude-legal

**Specific Legal Workflows Built:**

**Marketing Review Tool:**
- Self-service Slack tool where marketers paste content
- Claude analyzes using a "skill" file containing historical guidance and review frameworks
- Flags publicity rights concerns, overstated claims, statistical accuracy problems with risk levels
- Turnaround dropped from 2-3 days to 24 hours

**Contract Redlining:**
- Compares document versions in Google Docs and Office 365
- Highlights changes, recommends fallback language from commercial playbook
- Integrates directly into Google Docs comments for real-time feedback

**Conflict-of-Interest Reviews:**
- Employees submit outside business activity forms
- Claude analyzes against COI policy frameworks
- Sends recommendations via Slack to lawyers for approval
- Eliminates back-and-forth interviews for routine cases

**Privacy Impact Assessments:**
- MCP servers connect to folders of previous PIAs
- Applies formatting skills to generate new templates based on past documents

**Key quotes:**
- Mark Pike (Associate General Counsel): "I partner with Claude to tackle certain projects involving coding, but I am not the one coding. I'm just very good at troubleshooting."
- "We're not replacing lawyers. We're pushing out the frontier of what's possible."
- "The goal was to turn the legal team from 'the department of no' into cross-functional thought partners."
- Mark on Claude Code: "I just typed a normal sentence, describing what I wanted. And it worked."
- On hallucination: "AI systems can still hallucinate, and we want to make sure we're verifying citations."

**Critical detail:** Mark Pike, a product lawyer with NO coding background, built all these systems.

**Techniques used:**
- Skills (specialized instruction files for employment, commercial, privacy, corporate law)
- MCP integration (Google Drive, JIRA, Slack, Google Calendar)
- Human-in-the-loop workflows (all outputs route to lawyers for final approval)

---

### 3. Anthropic: "How AI Is Transforming Work at Anthropic" (research paper, late 2025)

**URL**: https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic

**Methodology:** Survey of 132 engineers/researchers (31% response rate), 53 in-depth interviews, 200,000 Claude Code transcripts (Feb-Aug 2025)

**Key statistics:**
- Claude used in 59% of daily work (up from 28% one year prior)
- 50% average productivity boost (up from 20%)
- 27% of Claude-assisted work = tasks that wouldn't have been done otherwise
- Claude Code autonomy increased from ~10 to ~20 consecutive tool calls
- Average task complexity rose from 3.2 to 3.8 (1-5 scale)
- Human turns decreased 33% (from 6.2 to 4.1 per transcript)
- Feature implementation jumped from 14% to 37% of Claude Code usage

**Non-engineering highlights:**
- Non-technical employees use Claude Code for debugging (51.5%) and data science (12.7%)
- Front-end development = 7.5% of Claude Code usage for alignment/safety teams (creating data visualizations)
- Engineers increasingly describe role as "managers of AI agents"
- 8.6% of Claude Code tasks = "papercut fixes" (minor QoL improvements previously deprioritized)

**Quotes on skill expansion:**
- "I can very capably work on front-end, or transactional databases... where previously I would've been scared to touch stuff I'm less of an expert on."
- "When producing output is so easy and fast, it gets harder and harder to actually take the time to learn something."
- "I ask way more questions [now] in general, but like 80-90% of them go to Claude."
- "It's been sad that more junior people don't come to me with questions as often."
- "I feel optimistic in the short term but in the long term I think AI will end up doing everything and make me irrelevant."

---

### 4. Claude Cowork Launch (Jan 12, 2026)

**Primary URLs:**
- TechCrunch: https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/
- Fortune: https://fortune.com/2026/01/13/anthropic-claude-cowork-ai-agent-file-managing-threaten-startups/
- VentureBeat: https://venturebeat.com/technology/anthropic-launches-cowork-a-claude-desktop-agent-that-works-in-your-files-no
- Simon Willison: https://simonwillison.net/2026/Jan/12/claude-cowork/
- Anthropic blog: https://claude.com/blog/cowork-research-preview
- Help Center: https://support.claude.com/en/articles/13345190-getting-started-with-cowork

**What Cowork is:**
- Desktop application (initially macOS, Windows added Feb 10, 2026) built into Claude Desktop
- "Claude Code for the rest of your work" — same underlying technology, but for non-developers
- Users grant Claude access to specific folders; Claude reads, edits, creates, and organizes files
- Operates autonomously — "less like a back-and-forth and more like leaving messages for a coworker"
- Runs through Apple's VZVirtualMachine framework (custom Linux filesystem in a VM)

**Timeline:**
- Jan 12, 2026: Research preview for Claude Max subscribers (macOS)
- Jan 16, 2026: Expanded to Pro subscribers
- Jan 23, 2026: Team and Enterprise plans
- Jan 30, 2026: Plugins launched (11 open-source)
- Feb 10, 2026: Windows version

**Demo use cases:**
- Reorganizing downloaded files
- Converting receipt screenshots into expense spreadsheets
- Generating initial drafts from scattered desktop notes

**Critical detail:** Anthropic built Cowork in approximately 10 days, primarily using Claude Code itself (per Boris Cherny, head of Claude Code).

**Simon Willison's review:**
- Tested on his "blog-drafts" folder — asked Cowork to find draft articles, check which hadn't been published, recommend closest-to-ready
- Cowork found 46 draft files, executed 44 individual website searches to verify publication status
- Identified three strong candidates for publishing including a 22,602-byte article "very close to ready"
- Verdict: "a really smart product" that "unlocks significant existing Claude Code value for broader audiences"
- Characterizes it as "Claude Code wrapped in a less intimidating default interface"
- Concern: guidance telling non-programmers to "watch out for suspicious actions that may indicate prompt injection" is unrealistic

---

### 5. Cowork Plugins & The $285B Selloff (Jan 30 – Feb 6, 2026)

**Primary URLs:**
- GitHub repo: https://github.com/anthropics/knowledge-work-plugins
- TechCrunch: https://techcrunch.com/2026/01/30/anthropic-brings-agentic-plugins-to-cowork/
- Nate's Newsletter: https://natesnewsletter.substack.com/p/200-lines-of-markdown-just-triggered
- Fortune: https://fortune.com/2026/02/06/anthropic-claude-opus-4-6-stock-selloff-new-upgrade/
- Tech Startups: https://techstartups.com/2026/02/05/anthropics-claude-plugins-spark-285-billion-software-stock-selloff-as-ai-targets-entire-saas-workflows/
- CNBC: https://www.cnbc.com/2026/02/06/ai-anthropic-tools-saas-software-stocks-selloff.html
- InfoQ: https://www.infoq.com/news/2026/01/claude-cowork/
- Aragon Research: https://aragonresearch.com/anthropic-claude-cowork/
- AI Business: https://aibusiness.com/agentic-ai/anthropic-introduces-claude-cowork
- Axios: https://www.axios.com/2026/01/30/ai-anthropic-enterprise-claude
- PYMNTS: https://www.pymnts.com/news/artificial-intelligence/2026/anthropic-says-new-cowork-plugins-tailor-claude-specific-job-functions/

**The 11 open-source plugins (from GitHub repo README):**

| Plugin | Function | Connectors |
|--------|----------|------------|
| **productivity** | Tasks, calendars, daily workflows, personal context | Slack, Notion, Asana, Linear, Jira, Monday, ClickUp, Microsoft 365 |
| **sales** | Research prospects, prep calls, review pipeline, draft outreach, build battlecards | Slack, HubSpot, Close, Clay, ZoomInfo, Notion, Jira, Fireflies, Microsoft 365 |
| **customer-support** | Triage tickets, draft responses, package escalations, build knowledge base | Slack, Intercom, HubSpot, Guru, Jira, Notion, Microsoft 365 |
| **product-management** | Write specs, plan roadmaps, synthesize research, track competitors | Slack, Linear, Asana, Monday, ClickUp, Jira, Notion, Figma, Amplitude, Pendo, Intercom, Fireflies |
| **marketing** | Draft content, plan campaigns, enforce brand voice, report on performance | Slack, Canva, Figma, HubSpot, Amplitude, Notion, Ahrefs, SimilarWeb, Klaviyo |
| **legal** | Review contracts, triage NDAs, navigate compliance, assess risk | Slack, Box, Egnyte, Jira, Microsoft 365 |
| **finance** | Journal entries, reconcile accounts, financial statements, variance analysis, audit support | Snowflake, Databricks, BigQuery, Slack, Microsoft 365 |
| **data** | Query/visualize/interpret datasets, write SQL, run statistical analysis, build dashboards | Snowflake, Databricks, BigQuery, Hex, Amplitude, Jira |
| **enterprise-search** | Find anything across email, chat, docs, wikis — one query across all tools | Slack, Notion, Guru, Jira, Asana, Microsoft 365 |
| **bio-research** | Literature search, genomics analysis, target prioritization for preclinical R&D | PubMed, BioRender, bioRxiv, ClinicalTrials.gov, ChEMBL, Synapse, Wiley, Owkin, Open Targets, Benchling |
| **cowork-plugin-management** | Create new plugins or customize existing ones | — |

**Plugin architecture (from README):**
```
plugin-name/
├── .claude-plugin/plugin.json   # Manifest
├── .mcp.json                    # Tool connections
├── commands/                    # Slash commands you invoke explicitly
└── skills/                      # Domain knowledge Claude draws on automatically
```

**Critical quote from README:** "Every component is file-based — markdown and JSON, no code, no infrastructure, no build steps."

**The $285B selloff:**
- Triggered primarily by the legal plugin (specifically the NDA triage and contract review commands)
- The legal plugin was described as "roughly 200 lines of structured markdown prompts" with "first-year law school content dressed up with some clever workflow logic"
- A Goldman Sachs trader termed it the "SaaSpocalypse"
- Goldman Sachs basket of U.S. software stocks sank 6% in a single session
- Financial services names followed, dragging sector down almost 7%
- Thomson Reuters: -18% (biggest single-day decline on record)
- RELX/LexisNexis: -14%
- Wolters Kluwer: -13%
- LegalZoom: -20%
- FactSet: -10%
- Total market cap destroyed: ~$285B

**Why it mattered (from Nate's Newsletter):**
- "if AI compresses the cost of legal and financial analysis, then every firm charging premium fees for that analysis has a margin problem. Not next year. **Now.**"
- The markdown file didn't cause the crash — "it revealed an existing structural vulnerability"
- The per-seat SaaS licensing model was already cracking
- Market confronted "a text file doing work that billion-dollar companies charge per-seat fees to access"

**NDA Triage Command** (actual content from repo — `/triage-nda`):
- Accepts NDA in any format (PDF, DOCX, URL, pasted text)
- Loads org-specific NDA playbook from local settings (or uses market-standard defaults)
- Screens against 13 criteria: mutual obligations, definition scope, term, standard carveouts, permitted disclosures, return/destruction, residuals, non-solicitation, non-compete, injunctive relief, governing law, assignment, unusual provisions
- Classifies as GREEN (standard approval), YELLOW (counsel review), or RED (full legal review)
- Generates structured triage report with routing suggestions

**Contract Review Command** (`/review-contract`):
- Accepts contract in any format
- Gathers context (which side you're on, deadline, focus areas, deal context)
- Loads organization's negotiation playbook
- Clause-by-clause analysis against 12+ categories
- Three-tier deviation flagging (GREEN/YELLOW/RED)
- Generates redline suggestions with specific alternative language
- Business impact summary with negotiation strategy

---

### 6. Department of Product: "How to Use Claude Code for Non-Engineering Use Cases" (Dec 5, 2025)

**URL**: https://departmentofproduct.substack.com/p/how-to-use-claude-code-for-non-engineering
**Author**: Rich Holmes (Knowledge Series #84, 52,000+ subscribers)

**Use cases described:**
1. PRD and Jira ticket generation
2. File organization and spreadsheet editing
3. SEO audits
4. Task management
5. Personal knowledge systems ("second brain")
6. Product OS development

**Key quote:** Anthropic's philosophy emphasizes treating "Claude Code as a thought partner rather than a code generator. They explore possibilities, prototype rapidly, and share discoveries across technical and non-technical users."

**Note:** Article is paywalled beyond preview. Setup instructions aimed at zero terminal experience.

---

### 7. The Prompt Warrior: "5 Powerful Claude Code Use Cases You Probably Didn't Know About"

**URL**: https://www.thepromptwarrior.com/p/5-powerful-claude-code-use-cases-you-probably-didn-t-know-about-5826bfb7f5b8fdd8

**The 5 use cases:**

**1. Writing & Note-Taking:**
- Notion MCP integration synced locally with markdown files
- Claude Code writes new files and reorganizes in batch
- Custom "writing assistant" subagents with custom prompts for blog posts and tweets
- Described as "the best system I've found for using AI in my writing process"

**2. Research & Data Analysis:**
- Competitor analysis: "Do a deep competitor analysis for [your industry]" → comprehensive reports
- Content scraping: Built YouTube scrapers using Google API to analyze video metrics
- Business data analysis: Upload CSV → "Pretend you're a consultant. Analyze this data and provide actionable insights"
- Key differentiator from ChatGPT: "can actually write and execute code on your machine, making it possible to integrate easily with other workflows"

**3. Video Creation & Editing:**
- Remotion (React-based video components) for programmatic marketing videos
- FFmpeg integration for extracting audio, transcribing via Whisper API, editing clips
- "Claude Code handled the entire FFmpeg workflow and OpenAI API integration automatically"

**4. UI Design (Screenshot to Code):**
- Find designs on Dribbble → screenshot → "Create 3 variations of this design in HTML"
- Working prototypes in minutes
- Creating presentation slides with Reveal.js, interactive landing pages
- Caveat: "This doesn't replace Figma level designs yet"

**5. Automations:**
- AI News Bot: auto-scrapes and summarizes industry news
- Content Scheduler: processes and schedules social media posts
- Data Pipeline: processes customer feedback and generates reports
- "Unlike no-code tools, you're not limited by pre-built integrations"
- Real example: morning email automation via GitHub Actions + Firecrawl API

---

### 8. Anthropic Legal Tech Expansion & Cowork Plugins (Jan 30 – Feb 2, 2026)

**URLs:**
- Artificial Lawyer: https://www.artificiallawyer.com/2026/02/02/anthropic-moves-into-legal-tech/
- Legal IT Insider: https://legaltechnology.com/2026/02/03/anthropic-unveils-claude-legal-plugin-and-causes-market-meltdown/
- Law.com: https://www.law.com/legaltechnews/2026/02/02/anthropic-releases-legal-plugin-in-cowork-among-other-extensions-for-enterprise-work/
- Clio: https://www.clio.com/blog/anthropic-legal/
- Tavant: https://tavant.com/blog/anthropics-enterprise-revolution/

**Key detail:** For the first time, a foundation-model company packaged a legal workflow product directly into its platform, rather than merely supplying an API to legal-tech vendors. This is what spooked the market.

---

### 9. Additional Sources Found

**Anthropic blog — Introducing Anthropic Labs:**
- URL: https://www.anthropic.com/news/introducing-anthropic-labs
- Context for Cowork's position in Anthropic's product strategy

**Anthropic interactive Claude apps (Jan 26, 2026):**
- URL: https://techcrunch.com/2026/01/26/anthropic-launches-interactive-claude-apps-including-slack-and-other-workplace-tools/
- Slack and workplace integrations for non-SWE teams

**Claude Life Sciences:**
- URL: https://intuitionlabs.ai/articles/claude-code-life-science-applications
- Claude Code in life sciences research, biomedical discovery

**Claude Healthcare (Jan 2026):**
- HIPAA-ready enterprise tools and EHR connectors
- Expansion beyond SWE into regulated industries

**VentureBeat — Cowork on Windows (Feb 10, 2026):**
- URL: https://venturebeat.com/technology/anthropics-claude-cowork-finally-lands-on-windows-and-it-wants-to-automate
- Windows expansion, workday automation focus

---

## KEY THEMES FOR THE BOOK

### Theme 1: "Claude Code for the Rest of Your Work"
The arc from Claude Code (Feb 2025, SWE-only) → Cowork (Jan 2026, everyone) is the harness thesis in action. The SAME underlying technology — tools in a loop, file system access, skills, MCP — simply got a friendlier interface for non-technical users.

### Theme 2: "200 Lines of Markdown"
The legal plugin that triggered a $285B selloff was literally markdown files — skills and slash commands, no code. This is the most vivid proof point in the entire timeline that **the harness matters more than the model.** The model (Claude Opus 4.6) was available to everyone. The plugin was 200 lines of structured prompts. The WORKFLOW DESIGN was the value.

### Theme 3: Non-Technical People Building Tools
Mark Pike (lawyer, no coding background) built legal workflows. Growth marketing built ad pipelines. Product designers built visualizations. The pattern: Claude Code dissolves the technical/non-technical boundary.

### Theme 4: The Plugin Architecture Is CLAUDE.md at Scale
The knowledge-work-plugins repo is the logical evolution of CLAUDE.md:
- CLAUDE.md = persistent instructions for one project
- Skills = reusable domain expertise
- Plugins = bundled skills + commands + connectors for an entire role
- All of it is markdown and JSON. No code. No infrastructure.

### Theme 5: The SaaS Existential Crisis
When a text file can do the work of per-seat SaaS, the business model cracks. This isn't about AI replacing humans — it's about AI replacing middleware.
