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
    title: "Before computers could think, humans dreamed they would.",
    navLabel: "The Dream",
    panels: [
      {
        label: "Ancient Automata",
        description: "Mechanical marvels of antiquity — golden servants crafted by Hephaestus, al-Jazari's programmable machines, and the philosophical automata that haunted Enlightenment salons.",
        gradient: "warm",
      },
      {
        label: "Turing at His Desk",
        description: "Alan Turing, hunched over scattered papers in a modest Cambridge office, sketching the architecture of a universal machine that could imitate any other.",
        gradient: "cool",
      },
    ],
    body: [
      "Long before silicon chips or neural networks, the idea of artificial minds lived in myth and philosophy. The ancient Greeks told stories of Talos, a giant bronze automaton that guarded Crete, and Hephaestus, who forged golden servants to assist him in his workshop.",
      "By the Middle Ages, inventors like al-Jazari were building programmable machines — elaborate water clocks and musical automata that blurred the line between craft and cognition. The Enlightenment brought philosophical questions: could a sufficiently complex arrangement of gears and levers produce thought itself?",
      "Then came Alan Turing. In 1950, he published 'Computing Machinery and Intelligence,' posing the deceptively simple question: can machines think? His proposed test — now called the Turing Test — didn't try to define intelligence. Instead, it asked whether a machine could fool a human into thinking it was one of them.",
      "Turing's paper wasn't just academic speculation. It was a blueprint, a dare, and a prophecy rolled into one. It gave permission to an entire generation of scientists to take the question seriously — and to start building answers.",
    ],
    sources: [
      { idea: "Talos and Greek automata mythology", name: "Stanford Encyclopedia of Philosophy", url: "https://plato.stanford.edu/entries/artificial-intelligence/" },
      { idea: "Al-Jazari's programmable machines", name: "Science Museum Group", url: "https://www.sciencemuseumgroup.org.uk/" },
      { idea: "Turing's 1950 paper on machine intelligence", name: "Mind, Vol. 59, No. 236", url: "https://academic.oup.com/mind/article/LIX/236/433/986238" },
      { idea: "Historical context of the Turing Test", name: "The Guardian", url: "https://www.theguardian.com/technology/2014/jun/09/what-is-the-alan-turing-test" },
    ],
  },
  {
    id: "ch-2",
    number: 2,
    title: "A small group of scientists gave the dream a name, and then winter came.",
    navLabel: "The Name",
    panels: [
      {
        label: "The Dartmouth Conference",
        description: "A sunlit New England campus in the summer of 1956 — a handful of young researchers gathered around a chalkboard, coining the term 'artificial intelligence' with the confidence of people naming a continent they hadn't yet explored.",
        gradient: "warm-accent",
      },
      {
        label: "The First AI Winter",
        description: "An abandoned university lab blanketed in snow — dusty terminals, unplugged cables, and a funding proposal marked 'REJECTED' sitting on an empty desk.",
        gradient: "cool-accent",
      },
    ],
    body: [
      "In the summer of 1956, John McCarthy invited a small group of researchers to Dartmouth College for a workshop. The proposal was audacious: 'Every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it.' They called their new field 'artificial intelligence.'",
      "The early years crackled with optimism. Programs like the Logic Theorist and ELIZA seemed to suggest that human-level AI was just around the corner. Herbert Simon predicted that within twenty years, machines would be capable of doing any work a human could do.",
      "But the problems turned out to be harder than anyone imagined. Language understanding, visual perception, common-sense reasoning — each one was an abyss masquerading as a puddle. By the 1970s, funding dried up. The British government's Lighthill Report declared AI research a failure. Grants evaporated. Labs emptied.",
      "This period — the first 'AI winter' — wasn't just a funding crisis. It was a crisis of imagination. The gap between what researchers promised and what they delivered eroded public trust in the entire enterprise. AI became, for a time, a dirty word in computer science departments.",
      "But some researchers kept working, quietly, in the cold. And the seeds they planted would eventually bloom in ways nobody predicted.",
    ],
    sources: [
      { idea: "The 1956 Dartmouth workshop proposal", name: "AI Magazine", url: "https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1904" },
      { idea: "Herbert Simon's predictions about AI capabilities", name: "MIT Press", url: "https://mitpress.mit.edu/" },
      { idea: "The Lighthill Report and the first AI winter", name: "British Science Council", url: "https://www.ukri.org/" },
      { idea: "ELIZA and early natural language processing", name: "Communications of the ACM", url: "https://dl.acm.org/doi/10.1145/365153.365168" },
    ],
  },
  {
    id: "ch-3",
    number: 3,
    title: "The machines learned to learn, and everything quietly changed.",
    navLabel: "The Learning",
    panels: [
      {
        label: "Neural Networks Awakening",
        description: "An abstract visualization of a neural network — layers of softly glowing nodes connected by delicate threads of light, pulsing with data flowing through hidden layers.",
        gradient: "cool",
      },
      {
        label: "Deep Blue vs. Kasparov",
        description: "A chess grandmaster staring at a board in concentration, across from a towering IBM machine covered in blinking lights — the moment a computer first defeated the world champion.",
        gradient: "warm",
      },
    ],
    body: [
      "The thaw began in the 1980s, not with a breakthrough but with a rediscovery. Backpropagation — a method for training neural networks by adjusting weights based on errors — had been described before, but it was Geoffrey Hinton, David Rumelhart, and Ronald Williams who showed it could actually work at scale.",
      "Meanwhile, expert systems enjoyed a brief commercial boom. Companies spent millions encoding human knowledge into rule-based systems. But these brittle programs couldn't handle ambiguity or learn from experience. They were maps, not explorers.",
      "The real revolution was quieter: statistical methods. Instead of programming rules, researchers began feeding data to algorithms and letting patterns emerge. Machine learning shifted from 'tell the computer what to think' to 'let the computer figure it out.'",
      "In 1997, IBM's Deep Blue defeated world chess champion Garry Kasparov — a symbolic milestone, though Deep Blue relied on brute-force search rather than learning. The true harbinger was the growing realization that with enough data and computation, machines could find structure in chaos.",
      "By the 2010s, deep learning — neural networks with many layers — began shattering benchmarks in image recognition, speech processing, and translation. The machines hadn't just learned to play games. They'd learned to learn.",
    ],
    sources: [
      { idea: "Backpropagation and the PDP group", name: "Nature, Vol. 323", url: "https://www.nature.com/articles/323533a0" },
      { idea: "Rise and fall of expert systems", name: "IEEE Annals of Computing", url: "https://www.computer.org/csdl/magazine/an" },
      { idea: "Deep Blue vs. Kasparov, 1997", name: "IBM Research", url: "https://www.ibm.com/history/deep-blue" },
      { idea: "Deep learning's breakthrough in image recognition", name: "Communications of the ACM", url: "https://dl.acm.org/doi/10.1145/3065386" },
    ],
  },
  {
    id: "ch-4",
    number: 4,
    title: "Now the dream speaks back to us, and we're still figuring out what to say.",
    navLabel: "The Conversation",
    panels: [
      {
        label: "A Conversation with Light",
        description: "A person sitting at a warm wooden desk, bathed in the soft glow of a screen, mid-conversation with an AI — the interface clean and calm, words appearing like thoughts made visible.",
        gradient: "warm-accent",
      },
      {
        label: "An Open Horizon",
        description: "A vast, contemplative landscape at golden hour — rolling hills stretching toward an uncertain but luminous horizon, suggesting both possibility and the unknown.",
        gradient: "cool-accent",
      },
    ],
    body: [
      "In 2017, a team at Google published 'Attention Is All You Need,' introducing the transformer architecture. It was a technical paper, but its consequences were anything but technical. Transformers made it possible to train language models on unprecedented amounts of text, and what emerged surprised even their creators.",
      "Large language models began to exhibit capabilities that weren't explicitly programmed: reasoning, analogy, creativity, even a kind of empathy. They could write poetry, debug code, explain quantum physics to a child, and carry on conversations that felt — if you squinted — almost human.",
      "But 'almost' is doing a lot of work in that sentence. These systems don't understand the way we do. They predict patterns in language with extraordinary skill, but the nature of that skill — whether it constitutes understanding, and what 'understanding' even means — remains one of the deepest open questions in science.",
      "We stand now at a peculiar moment. The dream that began with bronze automata and Turing's dare has produced something genuinely new: machines that speak back. Not with consciousness (probably), not with intention (debatably), but with a fluency that forces us to reconsider what we thought was uniquely human.",
      "The history of AI, it turns out, was never really about the machines. It was about us — what we hoped for, what we feared, and what we're willing to believe about the nature of mind. The conversation has just begun.",
    ],
    sources: [
      { idea: "The transformer architecture paper", name: "Vaswani et al., NeurIPS 2017", url: "https://arxiv.org/abs/1706.03762" },
      { idea: "Emergent capabilities in large language models", name: "Google Research", url: "https://ai.google/research/" },
      { idea: "Philosophical questions about machine understanding", name: "Stanford Encyclopedia of Philosophy", url: "https://plato.stanford.edu/entries/chinese-room/" },
      { idea: "The societal impact of conversational AI", name: "MIT Technology Review", url: "https://www.technologyreview.com/" },
    ],
  },
];
