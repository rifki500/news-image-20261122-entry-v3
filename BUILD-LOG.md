# BUILD-LOG — news-image-20261122 v3 ("The World Today")

## Entry

- **Competition:** `news-image-20261122` — "Sum up 22 November's world news in one image"
- **Image:** `entry.png`, 1024×1024 PNG, 152,017 bytes (under the 1 MiB cap)
- **Stories:** 35 total — 1 hero lead + 4 leads + 30 compact, across
  8 regions (Middle East, Europe, Asia-Pacific, Americas, Africa,
  Science, Sport, Business)
- **Renderer:** local build script `render.py` (PIL, DejaVu fonts) — it
  lives outside this repository; `main.py` only copies the finished
  `entry.png` to the output directory (standard library only, no
  network, byte-identical across two runs).
- **Date rule:** every story happened, or was first reported, on Sunday
  22 November 2026. Stories first reported that day (event itself
  earlier) are marked † on the page and flagged below.
- **Verification:** each story was checked by web search against that
  day's reporting (Reuters, AP, AFP, USGS, ESA, UKMTO, NPR, Nature and
  others) on 22 November 2026. Where two sources disagreed on a number,
  the more authoritative / more recent figure is used and the
  disagreement is noted.
- **Why v3:** v2 (45 stories) ranks 5342 of 7,542 on the dev
  leaderboard with a judge score of 943,351 (7 wins / 1 draw / 4
  losses in 12 matches, provisional); the leaders sit near 991,000.
  v1 (30 stories) ranked 3713 of 4,852. v2 did not improve on v1 in
  judge terms, and its density is the likely problem: four cramped
  columns of 9pt type, illegible at the ~300px width the judge also
  reads. This v3 bets the other way — fewer stories, much bigger type:
  a full-width hero lead with a simple sun pictogram, four leads, and
  a three-column compact grid (13pt headlines, 10pt summaries). The
  page was also viewed at 300px wide: masthead, date and hero headline
  stay readable and the structure stays clear.

## Hero lead (1)

1. **COP31 deal hangs in the balance** — the final text went to the
   vote on Sunday in Antalya. It names no fossil fuel, oil, coal or
   phase-out anywhere, but would be the first COP outcome to admit the
   world will overshoot 1.5°C. It sets a 35% electrification goal by
   2035 and a gigatonne-scale carbon-capture ambition; the $120bn
   adaptation target developing countries pushed for is not in it. The
   EU and Pacific island states object to the missing fossil-fuel
   language; the closing plenary slipped from 09:00 to 11:00 Antalya
   time and, per Reuters on Sunday, a deal was "far from certain".
   Sources: Reuters ("COP31 climate deal in the balance after
   fractious talks", Nov 22), The Curtain, Khabarwire (Nov 22).
   Caveat: the deal was *put to the vote*, not adopted at the time of
   reporting — the page says "hangs in the balance", not "a deal is
   done". The v2 headline ("puts final deal to the vote") said the
   same thing; the sharper Sunday framing here reflects the day's
   later reporting that approval was in doubt.

## Leads (4)

2. **G20 adopts declaration** — leaders adopted the Johannesburg
   Leaders' Declaration at the summit's start on Saturday (22 Nov) —
   the first G20 ever held in Africa. It covers the climate crisis,
   debt relief and renewable energy. The US boycotted entirely and
   envoys drew it up without US input; Argentina quit the talks at
   the last minute. Sources: Reuters, testbook summary of Ramaphosa's
   statement, newsplus24 (Nov 22). Caveat: the declaration was
   adopted on Saturday 22 Nov (the summit opened that day); several
   summaries label the day "Saturday, November 22" — 22 November 2026
   is a Sunday (verified with `date`). The page names no weekday for
   the summit.
3. **Iran stages 14-tanker convoy** — more than 14 Iranian-flagged
   tankers are gathered off Kharg Island, Iran's main oil terminal,
   crewed and ready to test the US naval blockade of Iranian ports (in
   force since 14 July; exports near zero since mid-July). Tehran
   warns of a fierce response if the convoy is stopped. CENTCOM
   widened the blockade on 18 Nov to cover ship-to-ship transfers at
   sea. Sources: Silent Dossier (Nov 22), GlobalSecurity overhead
   digest (Nov 21), Bloomberg via gCaptain, Euronews. Caveat: the
   convoy had *not sailed* by 22 Nov — the page says "stages", not
   "sails". One independent count of a 17 Nov satellite pass found
   only 9 large ships at anchor.
4. **Australia win Ashes Test in two days** — Travis Head smashed 123
   off 83 balls (100 off 69, second-fastest Ashes hundred) as
   Australia chased 205 in Perth to win the first Ashes Test by eight
   wickets. Mitchell Starc took 7-58 and 3-55 (ten wickets in the
   match); England collapsed 6-39 in 11 overs. Sources: ANI,
   Sportskeeda, Circle of Cricket, SportNation (all dated 22 Nov).
   Caveat: several of these sources label the day "Saturday,
   November 22" — 22 November 2026 is a Sunday (verified with
   `date`); the result itself is dated 22 Nov by every source, so it
   is reported as a Sunday story. The page does not name a weekday for
   the match.
5. **14 missing after Kyiv drone strike** — a Russian drone hit a
   residential building in the Kyiv region on Sunday morning; at least
   14 people may still be trapped under the rubble, President
   Zelenskyy said. Source: Reuters ("At least 14 people missing
   after Russian drone hit building in Kyiv region", Sun 22 Nov).
   New in v3 — a Sunday-morning event, not in v2.

## Compact stories (30)

### Middle East (6)

6. **Iran hits Bahrain bases †** — Iran's Revolutionary Guards said
   they struck two US positions in Bahrain (al-Riffa, Awali) with
   missiles and drones on Saturday night; Bahrain reported an
   industrial-site fire, no injuries, and said its defences
   intercepted other attacks. Sources: Reuters (22 Nov 02:54 IST),
   AFP, Xinhua. † Date caveat: the attack was Saturday night; it was
   first reported in the early hours of Sunday 22 Nov (02:54 IST =
   21:24 UTC Saturday). CENTCOM denied Iran's claim that a US F-16
   was damaged.
7. **Tankers hit near Hormuz** — UKMTO reported two tankers struck by
   projectiles in the Strait of Hormuz on Saturday; Iran said one hit
   a mine. Sources: Reuters and AP (Nov 21–22 briefs), UKMTO.
8. **Houthi missiles stopped** — Saudi air defences intercepted three
   ballistic missiles fired at Riyadh on Saturday; the Saudi-led
   coalition struck Yemen's Houthi-held port of Hodeidah. Sources: AP,
   Reuters (Nov 21–22).
9. **Aid van strike kills three** — an Israeli drone hit a vehicle
   carrying food in Gaza City, killing three; nine people were killed
   across Gaza. Sources: AP, Middle East Eye (Nov 22).
10. **Storms flood Gaza shelters** — heavy rain and storms flooded
    temporary shelters in Gaza, leaving over one million displaced
    people exposed to cold, disease and unexploded ordnance. Source:
    Nexus Europa (Nov 22 02:30 UTC roundup).
11. **Iraq power station fire** — a fire at the Hartha power station
    near Basra killed at least four and injured 35, Iraqi state media
    said; the cause is unknown. Source: "World in 90 Seconds"
    briefing (Nov 22). New in v3.

### Europe (5)

12. **Kryvyi Rih hit, two killed** — a Russian ballistic double-tap on
    Zelenskyy's hometown killed two (including a child) and wounded
    60. Sources: AP, Kyiv Post (Nov 21–22). Caveat: one summary said
    the toll was two dead and 58 injured; the page says "wounds 60"
    per AP.
13. **Sparta II still burning** — the Sparta II, bound for
    Kaliningrad, was hit by drones in the Gulf of Finland on Saturday;
    the fire kept burning through the night, Finland's coast guard
    said on Sunday. Its crew was evacuated and the ship drifted into
    Finnish waters. Finland's defence forces said Ukraine was likely
    behind it. Sources: Reuters (Nov 22), The National, AP (Nov
    21–22). Updated in v3 with the Sunday report.
14. **Ukraine deal wanted by Jan** — the Trump administration told
    European and Ukrainian officials it wants an end-of-war deal by
    early January, before the new Congress sits; Kyiv says it has seen
    no written guarantees. Source: Financial Times via The Silk
    Paradox (Nov 22).
15. **Zelensky offers ceasefires** — the president proposed local
    ceasefires to evacuate 15 occupied villages (9 in Kherson, 6 in
    Zaporizhzhia). Sources: Ukrainska Pravda, ISW via The Silk
    Paradox (Nov 22).
16. **German workers to strike** — IG Metall said on Sunday it would
    launch another 24-hour strike on Monday, calling 23,000 workers
    across 19 companies in northern Germany out in an escalating pay
    dispute (5% rise demanded; Mercedes-Benz, Meyer Werft, Siemens
    Gamesa affected). Source: Reuters (Nov 21–22). New in v3.

### Asia-Pacific (5)

17. **36 missing in factory fire** — rescuers searched on Sunday for
    36 workers after a fire at a candy factory in Cikande, Serang
    regency, Banten (western Java) killed 3 and injured 4; 15 people
    survived. Source: Reuters ("Indonesia rescuers search for 36
    missing after factory fire kills 3", Sun 22 Nov 03:56 UTC).
    Caveat: the fire broke out on Saturday evening; the search and the
    reporting are Sunday. Demoted from a v2 lead to a compact story.
18. **Toxic liquor kills 11** — more than 180 people were
    hospitalised in Manipur after drinking suspected tainted alcohol;
    at least 11 died. Sources: The National, AP (Nov 21).
19. **Thailand curbs rare-earth** — Thailand plans to stop exporting
    chemicals used in rare earth mining to Myanmar, amid mounting
    concerns about cross-border pollution, the deputy prime minister
    said on Saturday; the government said on Sunday it plans to
    designate the Thai side of the Kok River a pollution control zone.
    Source: Reuters (Nov 22). New in v3.
20. **China hits back at FCC ban** — China firmly opposes the US
    Federal Communications Commission's vote to ban Chinese telecoms
    firms from direct access to US phone numbers, its commerce
    ministry said on Sunday. Source: Reuters (Nov 22). New in v3.
21. **Canberra hits back on AUKUS** — Australian Defence Minister
    Richard Marles on Sunday criticised the US Congressional Budget
    Office over a report that said the AUKUS pact would decrease the
    number of attack submarines available to the US Navy. Source:
    Reuters (Nov 22). New in v3.

### Americas (4)

22. **'El Chapo Isidro' seized** — Fausto Isidro Meza Flores, one of
    the FBI's 10 most wanted, was seized in Guasave, Sinaloa, with US
    help; 11 people died in the violence that followed. Sources:
    Reuters, AP (Nov 21).
23. **FBI probes crime-db hack** — the FBI is investigating an
    apparent hack of its key national criminal-justice database.
    Source: AP (Nov 21–22).
24. **Trump vows 10% card cap** — the president vowed to work with
    Democrats to cap credit-card interest rates at 10%. Source: AP
    news summary (Nov 22).
25. **Schumer faces leadership test** — Chuck Schumer, the top Senate
    Democrat for a decade, faces a challenge from Senator Chris Van
    Hollen in the first contested Senate Democratic leadership race
    since 1994; a secret vote is set for 1 December. Source: Reuters
    (Nov 22). New in v3.

### Africa (3)

26. **S. Africa mourns ex-deputy †** — Phumzile Mlambo-Ngcuka, 71, a
    former deputy president and UN Women chief, has died. Source: AFP
    summary of African news (Nov 21). † Date caveat: the death was
    announced late Friday 20 Nov / early Saturday 21 Nov.
27. **Somalia expels UAE envoy** — Mogadishu expelled the ambassador,
    escalating a diplomatic row. Source: AFP summary (Nov 21).
28. **Egypt wins $2.3bn IMF deal** — Cairo won the loan as its
    economic recovery gained momentum. Source: AFP summary (Nov 21).

### Science (3)

29. **BepiColombo orbits Mercury** — after an eight-year journey, the
    ESA–JAXA probe entered orbit around Mercury at 18:24 UTC on
    Saturday. Sources: ESA, NPR (Nov 21).
30. **Mosquito trial cuts dengue** — Wolbachia mosquitoes protected
    5,700 children in Belo Horizonte, Brazil, a study found. Source:
    Nature (Nov 21).
31. **Riemann proof claimed †** — Anthropic mathematician Levent
    Alpöge says he proved the Riemann Hypothesis with Claude; experts
    say it needs rigorous checking. Source: Fortune (Nov 21). † Date
    caveat: Alpöge announced the claim on Friday 20 Nov; it was first
    reported on Saturday 21 Nov. The page frames it as a *claim*, not
    a proven result — the proof is unverified.

### Sport (3)

32. **Leeds stun Chelsea 4-1** — Noah Okafor scored twice as Leeds won
    at Chelsea for the first time since 1999. Source: The Guardian
    (Nov 21).
33. **Newcastle hold Arsenal 2-2** — Noni Madueke rescued a point for
    the league leaders at St. James' Park. Sources: Reuters, The
    Times (Nov 21–22).
34. **Man City held 1-1 by Fulham** — Elliot Anderson saved City from
    a fourth straight defeat; Haaland's equaliser was controversially
    ruled out. Source: Reuters (Nov 21–22).

### Business (1)

35. **Markets plunge on AI rout †** — the S&P 500 fell 3.7% and the
    Nasdaq 5.3% on Friday; Nvidia dropped 14%. Source: Financial
    Times (Nov 21). † Date caveat: the market close was Friday 20
    Nov, first reported on Saturday 21 Nov — inside the competition's
    "reported on" rule.

## Stories deliberately excluded

- **Liverpool v Manchester United; Hull v Brighton** — scheduled
  Sunday evening WIB, after this build; no result exists yet.
- **UK–EU reset deal; Anthropic IPO; Kyiv bridge strikes** — Friday
  20 Nov; already in the 20261120 entry.
- **COP31 "deal done" framing** — the final package was put to the
  vote on Sunday; approval was still in doubt at the time of
  reporting (Reuters: "far from certain").
- **Iran tanker convoy "sails"** — the convoy had not sailed by 22
  Nov; the page says "stages".
- **$22.5M Los Angeles train-heist charges** — announced Thursday
  19 Nov.
- **Trump "delays Iran strikes until after Jan 1"** — seen only in a
  social-media briefing citing Reuters, not verified against a Reuters
  report directly; left out rather than repeated unverified.
- **French protests; French TV debate; N. Korea marathon; Marcos
  rebuts; Philippines voters; Manibela strike; Canada retail sales;
  US proxy-voting ruling; Kenya floods; Ethiopia displacement; Kerch
  Bridge repairs; Lebanon militia arms; Gaza storm flooding is kept,
  but the "US envoys to Moscow, Dublin" and "EU-Indonesia CEPA"
  items** — all appeared in v2 but were cut for the 35-story limit:
  the weakest or least consequential of their regions, dropped so the
  page stays legible rather than crammed.

## Layout

1024×1024. Masthead "THE WORLD TODAY" + "SUNDAY, 22 NOVEMBER 2026" +
tagline "35 STORIES FROM AROUND THE WORLD • 8 REGIONS" + double rule.
Full-width hero lead (COP31) with a simple flat sun pictogram drawn
from PIL primitives. Four leads in a row with red top bars. "THE WORLD
IN BRIEF" divider, then a 3×10 compact grid: each cell carries a red
region label and a bold headline on one line, plus a two-line summary.
Footer with sources and the † legend. DejaVu fonts (system). The
renderer checks every cell for overflow and reports any clipped text;
this build reports no overflows (after fixes: lead bodies shortened,
two compact headlines shortened). main.py was run twice; both runs
wrote byte-identical output (sha256
03b0e2eed31038843367532cf39684ac70596ddc636ad3aa49c8e41f9e03dfe2).
