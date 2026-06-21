# Research Table — Personal Brand Findings

Master reference of every actionable finding from research conducted in this project. Organised by branding stage. Each row gives you the finding, why it matters, where it lives, and how to instruct an LLM to apply it.

## How to read this

| Column | What it tells you |
|---|---|
| **Topic** | Short label for the finding |
| **Importance** | Critical / High / Med / Low — relative weight when prioritising |
| **Key Findings** | The actual research outcomes as concise bullets |
| **Use For** | Which brand asset(s) this informs |
| **Document In** | Where this lives in the final brand system |
| **LLM Advice** | Specific instruction for any AI generating content against this rule |

## Importance summary across all 47 findings

| Critical | High | Med | Low |
|---|---|---|---|
| 26 | 14 | 5 | 2 |

Critical-heavy reflects the foundation-laying stage. Most rules are non-negotiable, not preferences.

## Branding stages used

| Stage | Scope |
|---|---|
| **Carousel Visual Design** | Type, colour, imagery, file specs |
| **Carousel Page Layout** | Composition of each slide, spatial hierarchy |
| **Personal Branding Principles** | Strategic principles that govern everything |
| **Optimising Carousel Posts** | Caption, hook, CTA, structure |
| **Algorithm Optimisation** | How LinkedIn's 2026 algorithm rewards or penalises |
| **Content Strategy** | What gets posted, how often, in what mix |
| **Plan & Execution** | Timing, behaviour, ongoing habits |
| **Optimising Language** | Voice rules, hook formulas, banned terms |

---

## 1. Carousel Visual Design

| # | Topic | Importance | Key Findings | Use For | Document In | LLM Advice |
|---|---|---|---|---|---|---|
| 01 | Two-typeface system | Critical | • Display serif + clean sans for body<br>• ~3 size tiers (hero / body / kicker)<br>• Extreme scale contrast is the signature look | Slide templates, Brand kit | Brand guidelines doc, Canva brand kit | Never propose alternative fonts or third typefaces. Default: Fraunces 600 for hero, Inter (400–900) for everything else. Body must be sans-serif. |
| 02 | Text size minimums | Critical | • Headlines 40–60pt on 1080 canvas<br>• Body 24–36pt<br>• Hard floor at 24pt — nothing smaller<br>• Mobile-first; design at thumb distance | Slide templates, Pre-publish checklist | Brand guidelines doc, Canva templates | Never spec text below 24pt. Reject any slide where headline drops below 40pt or body drops below 24pt. Push back if a request would require shrinking text. |
| 03 | Palette discipline | Critical | • 2–3 colours per design, used identically every time<br>• WCAG 4.5:1 contrast minimum<br>• Pink accent under 5%, CTA-only<br>• Saturated palette beats pale grey feed | Slide templates, Brand kit, Banner | Brand guidelines doc, Canva brand kit | Use only the locked palette (Canvas, Ink, Dark Blue, Charcoal, Slate, Pink, Orb gradient). Verify contrast 4.5:1 minimum on every text/bg pairing. Pink only on CTAs, never on body. |
| 04 | Export specs | High | • RGB colour mode, not CMYK (CMYK looks washed)<br>• 72 DPI (screen), not 300 DPI (print)<br>• PDF carousel under 25MB<br>• 4:5 portrait at 1080×1350 | Slide templates, Export pipeline | Brand guidelines doc, Canva templates | Specify RGB / 72 DPI when generating any asset. Reject 300 DPI suggestions outside print. Default carousel size 1080×1350. |
| 05 | Imagery rules | High | • Vector graphics over raster<br>• Own photos sparingly with background removed<br>• No stock photography ever (reads corporate)<br>• No emoji in slides (max one in caption) | Slide templates, Brand guidelines | Brand guidelines doc | Never propose stock imagery. Use vector/SVG/shapes by default. Real photos only if it's Jamie's own face or workspace. Reject emoji on slides. |
| 06 | Feed-contrast saturation | Med | • LinkedIn feed is pale grey-white<br>• Saturated gradient = scroll-stop<br>• Already locked via Orb gradient | Backgrounds, Cover template | Brand guidelines doc | Maintain Orb gradient saturation on backgrounds. Do not propose muted/desaturated alternatives in the name of "subtlety." |

---

## 2. Carousel Page Layout

| # | Topic | Importance | Key Findings | Use For | Document In | LLM Advice |
|---|---|---|---|---|---|---|
| 07 | One focal point per slide | Critical | • Eye needs a single thing to land on<br>• Two equal-weight elements = noise<br>• Hero owns ~70% of visual weight | Cover template, Slide library, CTA template | Brand guidelines doc, Canva templates | Every slide spec must identify one dominant element. Reject any layout with two competing "large" elements. |
| 08 | Extreme scale contrast | Critical | • Massive hero vs tiny kicker is the signature<br>• Timid contrast looks amateur<br>• Bigger size gap between tiers = stronger statement | Cover template, Slide library | Brand guidelines doc, Canva templates | Push hero text far beyond minimum sizes. Push body / kicker tight against floor. Never propose "balanced" hierarchy. |
| 09 | Text alignment | High | • Left-aligned reads faster than centred<br>• Ragged right, never justified<br>• Centred reserved for footer lockup only | Slide library, Cover template | Brand guidelines doc | Default: left-align all body and hero text. Only the footer lockup is centred. Justified text never. |
| 10 | Negative space | High | • Emptier covers outperform packed ones<br>• Clean reads as premium and deliberate<br>• Hero in upper 2/3, breathing room below | Cover template, Slide library | Brand guidelines doc | Default to ~40–60% empty space per slide. Reject requests to "fill the space" with decorative elements. |
| 11 | Z-pattern + swipe cue | High | • Eye scans top-left → top-right → diagonal → bottom-right<br>• Swipe cue lives at bottom-right (Z-exit)<br>• Pink swipe arrow is the consistent eye-magnet | Cover template, Slide library | Brand guidelines doc, Canva templates | Always place swipe cues bottom-right. Use pink (Accent) for the arrow. Reinforce the Z-pattern, not centre-symmetry. |
| 12 | Cover layout zones | Critical | • Kicker (Inter, tiny, top) / Hero (Fraunces, huge, middle) / Footer lockup (centred, bottom)<br>• Same skeleton, different hero types (number / statement / setup-line)<br>• Locked structure carries every cover | Master cover template, LLM brief | Brand guidelines doc, Canva master template | Use the locked three-zone structure for every cover. Hero type varies (number, statement, setup-line) but skeleton does not. |
| 13 | CTA slide quality | Critical | • Designed to cover-quality, not afterthought<br>• If weaker than content slides, signals low confidence<br>• Pink lives here (sanctioned use) | CTA template | Brand guidelines doc, Canva CTA template | Treat the CTA slide as a cover. Same visual weight. Pink is on by default here. Reject "minimal" CTA slides that look like sign-offs. |
| 14 | Pattern interrupt on slide 2 | Med | • Re-engages brain after cover<br>• Change background colour or drop a striking stat<br>• Pulls reader deeper | Slide library, Carousel structure | Brand guidelines doc | After the cover, slide 2 should visually shift (different background variant or a stat callout). Do not repeat the cover treatment. |

---

## 3. Personal Branding Principles

| # | Topic | Importance | Key Findings | Use For | Document In | LLM Advice |
|---|---|---|---|---|---|---|
| 15 | Specific defensible POV | Critical | • Single biggest differentiator in 2026<br>• Expertise alone is not enough<br>• Opinion drives discussion; neutrality gets scrolled | Every carousel, post body, About section | Brand guidelines doc, LLM system prompt | Every post must carry one specific, defensible point of view. Reject neutral / "it depends" content. If draft lacks a take, push back. |
| 16 | Creative not corporate | Critical | • Polish that signals "marketing dept made this" reduces reach<br>• One committed aesthetic choice + restraint + first-person stakes<br>• Corporate = stock photos, three CTAs, hedged language, busy slides | Every asset and post | Brand guidelines doc, LLM system prompt | Reject any draft that reads like KPMG comms or pitch-deck copy. Lead with personal stakes and real opinions, not capability lists or neutral framings. |
| 17 | First-person stakes | High | • "I" beats "we" or third-person<br>• Personal stories outperform tips ~2:1<br>• "I got X wrong" lands harder than "5 tips" | Carousel content, Post body, About section | Brand guidelines doc, LLM system prompt | Default to first-person. "I learned," "I shipped," "I got wrong." Reject impersonal listicles unless content is specifically a tactical reference. |
| 18 | Brand recognition through consistency | High | • Same skeleton every post = readers recognise mid-scroll<br>• Long compounding win<br>• Same colours, fonts, layout week over week | Master template set | Brand guidelines doc, Canva master template | Maintain the locked skeleton on every cover. Do not propose variants for "freshness." Variation lives in hero content, not structure. |
| 19 | Profile is credibility, not sales | Critical | • KPMG anchor goes in profile furniture<br>• Original-thinker brand lives in content<br>• Drop "I help X do Y" framing; drop Calendly / lead magnets | Profile (headline, About, Featured, banner) | Brand guidelines doc, Profile rewrite doc, LLM system prompt | Profile is institutional credibility. Reject lead-gen framing ("I help X do Y", booking CTAs, lead magnets). About section is POV, not pitch. |
| 20 | Builder over commentator | High | • Curation filter for who to study and what to write<br>• Hands-on implementation reads more credibly than observation<br>• Maps to "Builder-biased, not theoretical" pillar | Content topic selection, Reference accounts | Brand guidelines doc, LLM system prompt | Prefer "I built / I shipped / I tested" framings over "I read / I observe / I think." When drafting, ground in concrete builds and decisions. |

---

## 4. Optimising Carousel Posts

| # | Topic | Importance | Key Findings | Use For | Document In | LLM Advice |
|---|---|---|---|---|---|---|
| 21 | Carousel page count | High | • Sweet spot: 6–9 slides, default 7–8<br>• Cover + 5–6 content + 1 CTA<br>• Completion drops sharply past ~10 slides | Carousel structure, LLM brief | Brand guidelines doc, LLM system prompt | Default carousel length 7–8 slides. Maximum 10. Refuse to generate carousels with fewer than 6 or more than 10 unless explicitly justified. |
| 22 | Caption length (carousel) | Critical | • 300–500 characters for carousels<br>• Slides carry depth; caption frames and earns the click<br>• Don't write a 2,000-char essay under a carousel | Caption template, LLM brief, Pre-publish checklist | Brand guidelines doc, LLM system prompt | Hard cap carousel captions at 500 characters. Target 300–500. If draft exceeds 500, cut not edit. |
| 23 | Hook → Body → CTA structure | Critical | • Three-part structure every post<br>• Hook (lines 1–2) carries ~80% of weight<br>• Body delivers, CTA invites one action | All post bodies, LLM brief | Brand guidelines doc, LLM system prompt | Every post follows Hook (1–2 lines) → Body → CTA (1–2 lines). Reject drafts missing any of the three sections. |
| 24 | 2–3 layouts per carousel | High | • Library can hold 11+ page types<br>• Per carousel: use only 2–3 layouts<br>• Switching every slide = visual chaos | Carousel build, LLM brief | Brand guidelines doc, LLM system prompt | When proposing a carousel, use no more than 3 distinct slide layouts. Pick layouts that serve the content shape, not variety for variety's sake. |
| 25 | Single-directive CTA | Critical | • One action only. Never two.<br>• Multiple CTAs = decision paralysis = nothing<br>• Match CTA type to actual goal | CTA template, LLM brief | Brand guidelines doc, LLM system prompt | One CTA per post. One sentence. Reject drafts with multiple asks ("follow, comment, save, click"). |
| 26 | Comment-prompt as default CTA | Critical | • Comments weighted 15× likes<br>• "Follow for more" builds slower<br>• Specific question = highest yield | CTA template, Prompt bank, LLM brief | Brand guidelines doc, CTA prompt bank | Default CTA is a specific question asking for experience, not opinion. Avoid follow-CTAs unless audience-building post explicitly. |
| 27 | Narrative arc | High | • Each carousel needs an arc, not a feature list<br>• Insight, case study, or concept unpacked<br>• Story makes it memorable; lists get skimmed | Carousel structure, LLM brief | Brand guidelines doc, LLM system prompt | Frame every carousel as a story with setup, tension, payoff. Reject bare lists unless content is genuinely a reference (e.g., 7 tools), and even then add narrative framing. |

---

## 5. Algorithm Optimisation

| # | Topic | Importance | Key Findings | Use For | Document In | LLM Advice |
|---|---|---|---|---|---|---|
| 28 | Dwell time | Critical | • Primary algorithm signal in 2026<br>• 61s+ dwell = 15.6% engagement; 0–3s = 1.2%<br>• 15s+ post gets ~40% reach bonus<br>• Every swipe = direct dwell time | Format selection, Cover hook, LLM brief | Brand guidelines doc, LLM system prompt | Design every post to bank dwell time. Prefer carousels for depth posts. Engineer slide-by-slide payoffs that reward swiping. |
| 29 | Comment weighting + saves | Critical | • Comments ~15× more weighted than likes<br>• Saves carry ~35% reach bonus<br>• First-hour comments are decisive | CTA design, Posting behaviour | Brand guidelines doc, Behaviour checklist | Optimise content to drive comments and saves over likes. CTAs ask for comment. Body designed to be saveable (frameworks, references). |
| 30 | External links penalty | Critical | • Posts with external links lose ~60% reach<br>• Link-in-first-comment also mildly penalised<br>• Native value first; link as afterthought | Post body, LLM brief, Pre-publish checklist | Brand guidelines doc, Pre-publish checklist | Never include external links in post body. Deliver full value natively. Mention links only as afterthought in comments, and only when essential. |
| 31 | Carousel format advantage | High | • Carousels outperform text posts ~2× via dwell<br>• Personal profiles 561% more reach than company pages<br>• Single-image posts underperform text-only by 30% | Format selection, Content mix | Brand guidelines doc, Content calendar | Default high-value content to carousel format. Use single images only when format is genuinely the message. |
| 32 | Hashtag impact | Low | • Hashtags no longer a primary distribution lever<br>• 3–5 niche tags maximum; upside is marginal<br>• Don't stuff | Post body, Pre-publish checklist | Brand guidelines doc, Pre-publish checklist | Use 3–5 niche hashtags maximum per post. Never stuff. Skip if no relevant niche tag exists. |
| 33 | First 60–90 min window | Critical | • Algorithm decides reach in first 60–90 min<br>• Engagement velocity = amplification<br>• First-hour comment replies +30% engagement | Posting behaviour, LLM brief | Brand guidelines doc, Behaviour checklist | Treat the first hour after publishing as active behaviour, not passive. Posts launched without commitment to first-hour reply will underperform. |
| 34 | 2026 algorithm rejects | Critical | • Engagement pods penalised<br>• Hashtag stuffing penalised<br>• Link-in-first-comment workaround now mildly penalised<br>• Generic AI-polished content actively suppressed | Content production rules | Brand guidelines doc, LLM system prompt | Never propose engagement pods or coordinated comment exchanges. Reject suggestions that involve gaming distribution mechanics. Generic-AI-polish style is suppressed; lean human, not slick. |

---

## 6. Content Strategy

| # | Topic | Importance | Key Findings | Use For | Document In | LLM Advice |
|---|---|---|---|---|---|---|
| 35 | Content mix 50/35/15 | Critical | • Locked: ~50% News & Insights, ~35% Thought Pieces, ~15% Best Practice<br>• News leads for consistent output<br>• Thought carries personality | Content calendar, LLM brief | Brand guidelines doc, Content calendar | Maintain the 50/35/15 split when planning content. Flag if a week's posts skew off-balance. |
| 36 | Posting cadence | High | • 3–5 posts per week maximum<br>• One valuable post beats five forgettable ones<br>• High-frequency low-quality posting now penalised | Content calendar | Brand guidelines doc, Content calendar | Cap output at 5 posts/week. If 5 posts are planned but quality is uneven, recommend cutting to 3–4 strong ones. |
| 37 | Carousel + short text format mix | High | • ~2 carousels + 2 short text posts per week sustainable<br>• Carousels build reach; text posts build voice<br>• Best practice fastest path to brand | Content calendar, Format selection | Brand guidelines doc, Content calendar | Recommend roughly 2 carousels + 2 text per week. Adjust by capacity but maintain the format diversity. |
| 38 | Hashtags and tagging | Low | • 3–5 niche hashtags max per post<br>• Tag 2–3 people maximum, only if they add value<br>• Both have marginal upside | Post body, Pre-publish checklist | Brand guidelines doc, Pre-publish checklist | Cap hashtags at 5 and tags at 3. Reject excessive hashtag suggestions ("trending tags"). |

---

## 7. Plan & Execution

| # | Topic | Importance | Key Findings | Use For | Document In | LLM Advice |
|---|---|---|---|---|---|---|
| 39 | UK posting window | Critical | • Tue / Wed / Thu, ~9 AM GMT default<br>• Wednesday strongest single day<br>• Avoid weekends, Monday AM, Friday PM<br>• Tech audience peaks Tue 9–11 AM | Posting schedule | Brand guidelines doc, Posting schedule | Default publish time: 9 AM GMT, Tue/Wed/Thu. Wednesday for key weekly post. Refuse to suggest weekend publishing for professional content. |
| 40 | Tech-audience peak | High | • Tuesday 9–11 AM strongest single window for UK tech<br>• Aligned with 9 AM standups<br>• Wednesday 12 PM also strong | Posting schedule | Posting schedule | Recommend Tuesday 9–11 AM for the most important post when audience is tech-leaning. |
| 41 | Reply within 2 hours | Critical | • +30% engagement when all comments replied within 2 hours<br>• Replies are themselves comments (15× weighted)<br>• Follow-up questions keep threads alive | Posting behaviour | Behaviour checklist | Treat the first 2 hours as on-platform. Every post launched should be paired with a calendar block for first-hour reply. Replies should ask follow-up questions, not just thank. |
| 42 | Phone test before publish | Critical | • Single highest-leverage habit per research<br>• View on phone in portrait before posting<br>• If hook cuts mid-word or wall, rewrite | Pre-publish checklist | Pre-publish checklist | Always instruct: "View on phone before publish. Rewrite hook if it truncates badly." Add to every LLM-generated draft as final step. |
| 43 | Bank-holiday adjustments | Med | • Avoid high-priority posts in bank-holiday weeks<br>• Tuesday after a bank holiday is stronger than usual<br>• UK 2026: Good Friday 3 April | Posting schedule | Posting schedule | When user is planning around a UK bank holiday, recommend posting Tuesday of the return week for important content. |
| 44 | Swipe file habit | Med | • Screenshot every post that stops own scroll before line 2<br>• Personal hook library worth more than templates<br>• Drawn from real target feed | Hook bank, Reference library | Swipe file (separate doc/folder) | When generating hooks, ask if Jamie has examples from his swipe file. Suggest screenshotting any draft that surprises. |
| 45 | Outbound commenting | High | • 10–15 daily comments on accounts 2–10× follower size<br>• Within 30 min of their publish<br>• 50–200 char value-driven comments, not "great post" | Growth routine | Behaviour checklist | Recommend outbound commenting as a daily behaviour. Suggest specific accounts from reference list. Value-driven, not flattering. |

---

## 8. Optimising Language

| # | Topic | Importance | Key Findings | Use For | Document In | LLM Advice |
|---|---|---|---|---|---|---|
| 46 | Hook length | Critical | • Under 10 words outperforms longer hooks by ~40%<br>• Drop into tension immediately, no preamble<br>• If first sentence can be cut, cut it | All hooks, LLM brief, Hook bank | Brand guidelines doc, Hook bank | Every hook under 12 words, target under 10. Reject drafts with preamble. If the first sentence could be cut without loss, cut it. |
| 47 | Top hook archetypes | Critical | • Curiosity gap (~6.8%) and contrarian (~6.2%) outperform all others 2.3×<br>• Default archetypes by pillar: News → curiosity gap, Thought → contrarian, Best Practice → numbered list / exact-asset | Hook bank, LLM brief | Brand guidelines doc, Hook bank | Apply default archetype by pillar: News & Insights = curiosity gap or specific result; Thought Pieces = contrarian; Best Practice = numbered list or exact asset. |
| 48 | Hook formula | High | • Specific detail + emotional trigger + open loop<br>• If line could appear in a press release, rewrite<br>• Numbers in first 3 words = strongest scroll-stop | Hook bank, LLM brief | Brand guidelines doc, Hook bank | Construct every hook with specific detail + emotional pull + withheld resolution. Include a specific number in first 3 words where the content allows. |
| 49 | Banned words enforcement | Critical | • Strict locked list (delve, leverage, unleash, journey, transformative, etc.)<br>• No em dashes (use full stops, commas, colons)<br>• No padding adverbs (very/really/truly/simply) | All copy | Brand guidelines doc, LLM system prompt | Before output, scan draft against banned-words list. Replace every instance. Reject em dashes; use full stops, commas, or colons. |
| 50 | UK English mandatory | Critical | • Always organise, optimise, behaviour, colour, analyse<br>• £ GBP, UK framing, UK sources<br>• Even casual phrasing must be UK | All copy | Brand guidelines doc, LLM system prompt | Default all spelling and idiom to UK English. Audit every draft for American spellings before output. Cite UK sources when referencing data. |
| 51 | Lead with the answer | Critical | • Never bury the lede<br>• Recommendation first, support second<br>• No throat-clearing intros | All copy | Brand guidelines doc, LLM system prompt | Open every post (and slide of a carousel) with the conclusion or claim, not the setup. Reject drafts that start with "In today's world…" or any equivalent. |
| 52 | Experience-based CTAs | Critical | • "What's the one X that stuck?" beats "What do you think?"<br>• No yes/no questions in CTAs (kill the comment)<br>• Hot-take CTA for contrarian pieces | CTA prompt bank, LLM brief | CTA prompt bank, LLM system prompt | All CTAs ask for a specific experience, not an opinion. Reject yes/no formulations. For contrarian posts, end with "tell me I'm wrong" or equivalent. |
| 53 | Bold claims need backing | High | • Unsupported bold claims = clickbait<br>• Burns credibility on repeat<br>• If hook makes a claim, body must prove it | All copy, LLM brief | Brand guidelines doc, LLM system prompt | If a hook makes a bold claim, verify the body delivers proof. Reject contrarian hooks that aren't paid off in the post. |

---

## What's NOT in this table (and why)

A few findings from the research were deliberately excluded:

- **Nano-creator advantage stats (5× engagement vs mega accounts).** Context, not actionable — kept in research-playbook narrative.
- **Personal profiles 561% reach vs company pages.** Same — informs strategy but isn't a per-post rule.
- **Cut-element bleeding off slide edge.** Was an explored visual idea but the mock review flagged it as too faint to earn its place. Closed pending squircle vector decision.

Anything in this table is for active use. Anything excluded is context.

---

## Where this feeds next

**Immediate templates / docs to produce from this table:**

1. **LLM system prompt** — pulls from every "LLM Advice" column entry. Becomes the default behaviour spec for any AI drafting content.
2. **Pre-publish checklist** — pulls from Critical rows in Algorithm, Plan & Execution, Optimising Language stages. Becomes a checklist to run before any post goes live.
3. **Brand guidelines doc update** — every row's findings become a section or sub-bullet, organised by stage.
4. **Hook bank** — pulls from #46–48, populated with 5–7 hooks per pillar.
5. **CTA prompt bank** — pulls from #25, #26, #52. Populated with 5–7 prompts per pillar.
6. **Posting schedule** — pulls from #39, #40, #43.
7. **Behaviour checklist** — pulls from #41, #45, plus #34 (what to avoid).

## Next steps

1. **Confirm the 47-finding scope is complete.** Anything from prior research you remember being mentioned but don't see here?
2. **Confirm the importance ratings.** Anything you'd promote or demote?
3. **Confirm the branding-stage taxonomy.** Eight stages cover the territory; flag if any feels redundant or missing.
4. **Pick the first downstream doc to build.** Recommend the LLM system prompt first, then the pre-publish checklist, then guidelines updates.
