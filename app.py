
# ==========================================================
# STORYLOOP AI v0.8 - CINEMATIC EDITION
# Tagalog Original + Automatic Subtitles + Original BGM
# ==========================================================

import html
import base64

import streamlit as st

st.set_page_config(
    page_title="YOUR MOVE | What Would You Do?",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------
# 1. LANGUAGES
# ----------------------------------------------------------

LANGUAGES = {
    "fil": "Filipino",
    "en": "English",
    "zh": "简体中文",
}

UI = {
    "fil": {
        "welcome": "Maligayang pagdating, Manlalakbay!",
        "tagline": "Bawat desisyon ay simula ng bagong kuwento.",
        "start": "Simulan ang Pakikipagsapalaran",
        "question": "Ano ang susunod mong gagawin?",
        "replay": "Subukan ang Ibang Landas",
        "ending": "Ang Iyong Natatanging Katapusan",
        "chapter": "Kabanata",
        "music": "Musika",
    },
    "en": {
        "welcome": "Welcome, Adventurer!",
        "tagline": "Every choice begins a new story.",
        "start": "Begin Your Adventure",
        "question": "What will you do next?",
        "replay": "Explore Another Path",
        "ending": "Your Unique Ending",
        "chapter": "Chapter",
        "music": "Music",
    },
    "zh": {
        "welcome": "欢迎你，冒险者！",
        "tagline": "每一个选择都是新故事的开始。",
        "start": "开始冒险",
        "question": "接下来你会怎么做？",
        "replay": "探索另一条道路",
        "ending": "你的独特结局",
        "chapter": "章节",
        "music": "音乐",
    },
}

# ----------------------------------------------------------
# 2. ORIGINAL STORY AND TRANSLATIONS
# Every language uses identical node IDs and destinations.
# ----------------------------------------------------------

STORIES = {
    "fil": {
        "title": "Ang Misteryo ng Mahiwagang Maleta",
        "intro": (
            "Isang tahimik na gabi. Isang mahiwagang maleta. "
            "Isang tawag na maaaring magbago ng lahat."
        ),
        "nodes": {
            "start": (
                "Habang naghihintay ka ng bus, may nakita kang "
                "maletang puno ng pera. Biglang tumunog ang "
                "telepono sa loob nito.",
                [
                    ("Tumawag ng pulis", "police"),
                    ("Sagutin ang telepono", "phone"),
                    ("Hanapin ang may-ari", "owner"),
                ],
            ),
            "police": (
                "Dumating ang pulis. Ngunit may isang estrangherong "
                "biglang tumakbo palayo!",
                [
                    ("Sabihin ang iyong nakita", "witness"),
                    ("Humingi ng opisyal na rekord", "record"),
                    ("Sundan ang estranghero", "stranger"),
                ],
            ),
            "phone": (
                "May bumulong sa telepono: "
                "'Hindi iyan ang inaakala mong maleta.'",
                [
                    ("Alamin kung sino ang tumatawag", "clue"),
                    ("Humingi ng tulong", "witness"),
                    ("Sundin ang misteryosong boses", "stranger"),
                ],
            ),
            "owner": (
                "May nakita kang lumang litrato at isang "
                "lihim na mensahe sa loob ng maleta.",
                [
                    ("Suriin ang litrato", "clue"),
                    ("Iulat ang iyong natuklasan", "record"),
                    ("Maghanap sa paligid", "stranger"),
                ],
            ),
            "witness": (
                "Dahil sa iyong salaysay, may mahalagang "
                "palatandaang nabunyag. Malapit na ang katotohanan!",
                [
                    ("Ibahagi ang nalalaman", "hero"),
                    ("Suriin ang ebidensya", "detective"),
                    ("Pangalagaan ang ebidensya", "guardian"),
                ],
            ),
            "record": (
                "Nalaman mong nawawala ang maleta mula pa kahapon. "
                "May pagkakataon kang makatulong.",
                [
                    ("Tulungan ang may-ari", "hero"),
                    ("Suriin ang rekord", "detective"),
                    ("Siguraduhing ligtas ang maleta", "guardian"),
                ],
            ),
            "stranger": (
                "Huminto ang estranghero. "
                "'May sinusubukan akong protektahan,' sabi niya.",
                [
                    ("Pakinggan ang paliwanag", "detective"),
                    ("Humingi ng tulong sa awtoridad", "guardian"),
                    ("Tulungan siyang malaman ang totoo", "hero"),
                ],
            ),
            "clue": (
                "Natuklasan mo ang isang lihim na mensaheng "
                "maaaring makalutas sa buong misteryo!",
                [
                    ("Sundan ang mga palatandaan", "detective"),
                    ("Tulungan ang may-ari", "hero"),
                    ("Protektahan ang ebidensya", "guardian"),
                ],
            ),
        },
        "endings": {
            "hero": (
                "Ang Bayaning May Malasakit",
                "Ang iyong kabutihan ay nagbigay ng pag-asa. "
                "Sa mundong puno ng pagsubok, "
                "ang malasakit ay isang tunay na lakas.",
            ),
            "detective": (
                "Ang Matalinong Imbestigador",
                "Ang iyong pagiging mapanuri ang nagbukas "
                "ng daan sa katotohanan. "
                "Huwag matakot magtanong at tumuklas!",
            ),
            "guardian": (
                "Ang Maingat na Tagapangalaga",
                "Pinatunayan mong may lakas sa pagiging maingat. "
                "Ang maliliit na mabubuting desisyon "
                "ay maaaring magkaroon ng malaking epekto.",
            ),
        },
    },
    "en": {
        "title": "The Mystery of the Enchanted Suitcase",
        "intro": (
            "A quiet night. A mysterious suitcase. "
            "A call that could change everything."
        ),
        "nodes": {
            "start": (
                "While waiting for a bus, you discover a suitcase "
                "full of money. Suddenly, a phone inside rings.",
                [
                    ("Call the police", "police"),
                    ("Answer the phone", "phone"),
                    ("Find the owner", "owner"),
                ],
            ),
            "police": (
                "The police arrive, but a stranger suddenly runs away!",
                [
                    ("Explain what you saw", "witness"),
                    ("Request an official record", "record"),
                    ("Follow the stranger", "stranger"),
                ],
            ),
            "phone": (
                "A voice whispers: "
                "'The suitcase is not what you think.'",
                [
                    ("Ask who is calling", "clue"),
                    ("Seek help", "witness"),
                    ("Follow the mysterious voice", "stranger"),
                ],
            ),
            "owner": (
                "You find an old photograph and a secret message "
                "inside the suitcase.",
                [
                    ("Examine the photograph", "clue"),
                    ("Report your discovery", "record"),
                    ("Search the area", "stranger"),
                ],
            ),
            "witness": (
                "Your account reveals an important clue. "
                "The truth is getting closer!",
                [
                    ("Share what you know", "hero"),
                    ("Examine the evidence", "detective"),
                    ("Protect the evidence", "guardian"),
                ],
            ),
            "record": (
                "You discover that the suitcase has been missing "
                "since yesterday. You have a chance to help.",
                [
                    ("Help the owner", "hero"),
                    ("Examine the record", "detective"),
                    ("Keep the suitcase safe", "guardian"),
                ],
            ),
            "stranger": (
                "The stranger stops. "
                "'I'm trying to protect someone,' he says.",
                [
                    ("Listen to the explanation", "detective"),
                    ("Ask the authorities for help", "guardian"),
                    ("Help uncover the truth", "hero"),
                ],
            ),
            "clue": (
                "You discover a secret message that might "
                "solve the entire mystery!",
                [
                    ("Follow the clues", "detective"),
                    ("Help the owner", "hero"),
                    ("Protect the evidence", "guardian"),
                ],
            ),
        },
        "endings": {
            "hero": (
                "The Compassionate Hero",
                "Your kindness brought hope. "
                "In a world full of challenges, "
                "compassion is a true strength.",
            ),
            "detective": (
                "The Brilliant Investigator",
                "Your curiosity opened the path to truth. "
                "Never be afraid to ask questions and explore!",
            ),
            "guardian": (
                "The Thoughtful Guardian",
                "You proved that careful choices carry strength. "
                "Small acts of wisdom can make a big difference.",
            ),
        },
    },
    "zh": {
        "title": "神秘手提箱之谜",
        "intro": "一个安静的夜晚，一个神秘的手提箱，一通可能改变一切的电话。",
        "nodes": {
            "start": (
                "等公交车时，你发现一个装满现金的手提箱。"
                "突然，里面的电话响了。",
                [
                    ("报警", "police"),
                    ("接听电话", "phone"),
                    ("寻找失主", "owner"),
                ],
            ),
            "police": (
                "警察赶到了，但一名陌生人突然跑开了！",
                [
                    ("说明你看到的情况", "witness"),
                    ("索取正式记录", "record"),
                    ("跟随陌生人", "stranger"),
                ],
            ),
            "phone": (
                "电话里有人低声说：'这个箱子并不像你想的那样。'",
                [
                    ("询问来电者身份", "clue"),
                    ("寻求帮助", "witness"),
                    ("按照神秘声音的指示行动", "stranger"),
                ],
            ),
            "owner": (
                "你在箱子里发现一张旧照片和一条秘密信息。",
                [
                    ("查看照片", "clue"),
                    ("报告你的发现", "record"),
                    ("搜索附近区域", "stranger"),
                ],
            ),
            "witness": (
                "你的描述揭示了重要线索。真相越来越近了！",
                [
                    ("分享你知道的情况", "hero"),
                    ("检查证据", "detective"),
                    ("保护证据", "guardian"),
                ],
            ),
            "record": (
                "你发现这个箱子从昨天起就已失踪。"
                "现在你有机会提供帮助。",
                [
                    ("帮助失主", "hero"),
                    ("查看记录", "detective"),
                    ("妥善保管箱子", "guardian"),
                ],
            ),
            "stranger": (
                "陌生人停下来说：'我正在努力保护一个人。'",
                [
                    ("听取解释", "detective"),
                    ("向有关部门求助", "guardian"),
                    ("帮助查明真相", "hero"),
                ],
            ),
            "clue": (
                "你发现一条可能解开整个谜团的秘密信息！",
                [
                    ("追查线索", "detective"),
                    ("帮助失主", "hero"),
                    ("保护证据", "guardian"),
                ],
            ),
        },
        "endings": {
            "hero": (
                "富有同情心的英雄",
                "你的善良带来了希望。"
                "在充满挑战的世界里，同情心是真正的力量。",
            ),
            "detective": (
                "聪明的调查员",
                "你的好奇心打开了通往真相的道路。"
                "永远不要害怕提问和探索！",
            ),
            "guardian": (
                "细心的守护者",
                "你证明了谨慎选择的力量。"
                "小小的明智决定也能带来巨大的改变。",
            ),
        },
    },
}

# ----------------------------------------------------------
# 3. CINEMATIC DESIGN
# ----------------------------------------------------------

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 80% 0%, #35205c, transparent 48%),
        linear-gradient(155deg, #0b1120, #1d1535);
    color: #f9f7ff;
}

.block-container {
    max-width: 740px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}

h1, h2, h3, p {
    color: #f9f7ff !important;
}

.stCaption, [data-testid="stCaptionContainer"] {
    color: #c7bce5 !important;
}

.hero-panel {
    padding: 30px 22px;
    border-radius: 24px;
    background:
        radial-gradient(circle at 75% 20%, #7651ad55, transparent 45%),
        linear-gradient(135deg, #31264e, #17182e);
    border: 1px solid #7359a4;
    text-align: center;
    margin: 20px 0;
}

.hero-icon {
    font-size: 72px;
    margin-bottom: 12px;
}

.hero-title {
    font-size: 1.6rem;
    font-weight: 800;
    color: #f4c76d;
}

.story-card {
    background: linear-gradient(140deg, #292141, #181a31);
    border: 1px solid #67538e;
    border-radius: 20px;
    padding: 24px;
    margin: 16px 0;
    color: #ffffff;
    line-height: 1.8;
    font-size: 1.13rem;
}

.subtitle-text {
    color: #d6c7ff;
    font-size: 0.96rem;
    line-height: 1.7;
    border-top: 1px solid #58466e;
    margin-top: 14px;
    padding-top: 12px;
}

.gold-text {
    color: #f4c76d;
    font-weight: 700;
    letter-spacing: 0.04em;
}

div.stButton > button {
    width: 100%;
    min-height: 66px;
    background: linear-gradient(110deg, #39265e, #51338b);
    border: 1px solid #9471e8;
    border-radius: 16px;
    color: #ffffff;
    font-weight: 650;
    text-align: left;
    white-space: pre-wrap;
    padding: 12px 18px;
}

div.stButton > button:hover {
    background: #7452bc;
    color: #ffffff;
    border-color: #f4c76d;
}

div[data-testid="stExpander"] {
    background: #241d3b;
    border: 1px solid #65538b;
    border-radius: 12px;
}

div[data-testid="stExpander"] summary,
div[data-testid="stExpander"] summary * {
    color: #ffffff !important;
}

div[data-testid="stWidgetLabel"] *,
div[data-testid="stWidgetLabel"] {
    color: #f9f7ff !important;
}

.ending-card {
    background: linear-gradient(135deg, #50367a, #231c3c);
    border: 2px solid #e7bb65;
    border-radius: 24px;
    padding: 30px 20px;
    text-align: center;
    margin: 22px 0;
    box-shadow: 0 0 32px #e7bb6520;
}

.ending-title {
    color: #f4c76d;
    font-size: 1.55rem;
    font-weight: 800;
}

@media (max-width: 600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .hero-title {
        font-size: 1.35rem;
    }
}




/* STORYLOOP AI - COMPACT RESPONSIVE LAYOUT */

.block-container {
    max-width: 1250px !important;
    padding-top: 3.5rem !important;
    padding-bottom: 1rem !important;
}

h1 {
    font-size: clamp(1.6rem, 3vw, 2rem) !important;
    line-height: 1.3 !important;
    margin-top: 0 !important;
    margin-bottom: 0.25rem !important;
}


h2 {
    font-size: clamp(1.3rem, 2.5vw, 1.7rem) !important;
    line-height: 1.25 !important;
}

.stApp {
    font-size: 16px;
}

.story-card {
    padding: 14px 18px !important;
    margin: 6px 0 !important;
    font-size: 1.05rem !important;
    line-height: 1.5 !important;
    border-radius: 14px !important;
}

.subtitle-text {
    font-size: 0.95rem !important;
    line-height: 1.4 !important;
    margin-top: 8px !important;
    padding-top: 8px !important;
}

div.stButton > button {
    width: 100% !important;
    min-height: 52px !important;
    padding: 9px 16px !important;
    font-size: 1rem !important;
    line-height: 1.35 !important;
    border-radius: 12px !important;
}

div.stButton > button[kind="primary"] {
    background: linear-gradient(
        100deg, #7456e8, #a05de8
    ) !important;
    color: white !important;
    font-weight: 700 !important;
    text-align: center !important;
    border: 1px solid #b99aff !important;
}

div[data-testid="stExpander"] {
    margin-bottom: 0 !important;
}

div[data-testid="stCaptionContainer"] {
    font-size: 0.9rem !important;
    line-height: 1.35 !important;
}

@media (max-width: 600px) {
    .block-container {
        max-width: 860px !important;
        padding-top: 1.5rem !important;
        padding-bottom: 1rem !important;
    }

    .story-card {
        padding: 12px !important;
    }
}




/* STORYLOOP GAMEPLAY DESIGN */

div[data-testid="stImage"] img {
    width: 100%;
    max-height: 18vh;
    object-fit: cover;
    object-position: center;
    border-radius: 16px;
}

div.stButton > button {
    width: 100% !important;
    min-height: 60px !important;
    text-align: left !important;
    padding: 12px 18px !important;
    font-size: 1rem !important;
    border-radius: 14px !important;
}

div.stButton > button:hover {
    border-color: #f4c76d !important;
    background: #6445a3 !important;
}


/* COMPACT GAMEPLAY SPACING */

div[data-testid="stProgress"] {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

div[data-testid="stImage"] {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

.story-card {
    padding: 12px 16px !important;
    margin: 4px 0 !important;
    line-height: 1.4 !important;
}

div.stButton > button {
    min-height: 48px !important;
    padding: 8px 14px !important;
    line-height: 1.25 !important;
}

h3 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}






/* STORYLOOP AI - RESPONSIVE CINEMATIC VIDEO */

div[data-testid="stVideo"] video {
    width: 100% !important;
    max-height: clamp(140px, 25vh, 260px) !important;
    object-fit: cover !important;
    object-position: center !important;
    border-radius: 14px !important;
}

/* Compact spacing around videos */
div[data-testid="stVideo"] {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

/* Laptop screens */
@media (max-height: 800px) {
    div[data-testid="stVideo"] video {
        max-height: 22vh !important;
    }
}

/* Mobile phones */
@media (max-width: 600px) {
    div[data-testid="stVideo"] video {
        max-height: 20vh !important;
        border-radius: 10px !important;
    }

    .block-container {
        padding-top: 1rem !important;
    }
    
}



/* StoryLoop AI - Subtitle settings header */

div[data-testid="stExpander"] summary {
    background: #241d3b !important;
    border-radius: 12px !important;
}

div[data-testid="stExpander"] summary,
div[data-testid="stExpander"] summary * {
    color: #ffffff !important;
}



/* YOUR MOVE — bilingual button formatting */

div.stButton > button {
    white-space: pre-line !important;
    line-height: 1.55 !important;
    text-align: center !important;
    padding: 10px 16px !important;
}


/* YOUR MOVE - Bilingual buttons */

div.stButton > button {
    white-space: pre-wrap !important;
    text-align: center !important;
}

div.stButton > button p {
    white-space: pre-wrap !important;
}

/* YOUR MOVE - English button subtitle */

div.stButton > button p {
    white-space: pre-wrap !important;
    line-height: 1.6 !important;
}

div.stButton > button p::first-line {
    color: #FFFFFF;
}

/* Gold color for italic English button subtitles */
div.stButton > button em {
    color: #FFD978 !important;
    font-style: italic !important;
}


/* YOUR MOVE - Story subtitles */

.story-card .subtitle-text {
    color: #FFD978 !important;
    font-size: 20px !important;
    font-style: italic !important;
    line-height: 1.4 !important;
    margin-top: 8px !important;
    padding-top: 8px !important;
    
}



/* YOUR MOVE - MOBILE OPTIMIZATION */
@media (max-width: 600px) {

    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 1rem !important;
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
    }

    h1 {
        font-size: 1.5rem !important;
        margin-bottom: 0 !important;
    }

    h2, h3 {
        font-size: 1.2rem !important;
        line-height: 1.25 !important;
    }

    div[data-testid="stVideo"] video {
        max-height: 190px !important;
        object-fit: cover !important;
        border-radius: 10px !important;
    }

    .story-card {
        padding: 10px 12px !important;
        margin: 2px 0 !important;
        font-size: 0.95rem !important;
        line-height: 1.35 !important;
    }

    .story-card .subtitle-text {
        font-size: 0.95rem !important;
        line-height: 1.35 !important;
        margin-top: 5px !important;
        padding-top: 5px !important;
    }

    div.stButton > button {
        min-height: 44px !important;
        padding: 7px 10px !important;
        font-size: 0.9rem !important;
        line-height: 1.25 !important;
    }

    div[data-testid="stProgress"] {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }
    
}
    
/* YOUR MOVE - EXTRA COMPACT MOBILE */
@media (max-width: 600px) {

    .block-container {
        padding-top: 0.25rem !important;
        padding-bottom: 0.5rem !important;
    }

    h1 {
        font-size: 1.3rem !important;
    }

    h2, h3 {
        font-size: 1.05rem !important;
        margin: 0 !important;
    }

    /* Reduce spacing between Streamlit elements */
    div[data-testid="stVerticalBlock"] {
        gap: 0.35rem !important;
    }

    div[data-testid="stHorizontalBlock"] {
        gap: 0.35rem !important;
    }

    /* Compact cinematic video */
    div[data-testid="stVideo"] video {
        max-height: 135px !important;
        object-fit: cover !important;
    }

    /* Compact story text */
    .story-card {
        padding: 8px 10px !important;
        margin: 0 !important;
        font-size: 0.85rem !important;
        line-height: 1.25 !important;
    }

    .story-card .subtitle-text {
        font-size: 0.85rem !important;
        line-height: 1.25 !important;
        margin-top: 4px !important;
        padding-top: 4px !important;
    }

    /* Smaller choice buttons */
    div.stButton > button {
        min-height: 38px !important;
        padding: 5px 8px !important;
        font-size: 0.8rem !important;
        line-height: 1.15 !important;
    }

    /* Compact progress bar */
    div[data-testid="stProgress"] {
        margin: 0 !important;
    }
}

    
/* YOUR MOVE - MOBILE OVERLAP FIX */
@media (max-width: 600px) {

    /* Restore safe spacing between elements */
    div[data-testid="stVerticalBlock"] {
        gap: 0.65rem !important;
    }

    /* Allow story cards to grow with their text */
    .story-card {
        height: auto !important;
        min-height: 0 !important;
        overflow: visible !important;
        margin-bottom: 10px !important;
    }

    /* Keep English subtitles inside the card */
    .story-card .subtitle-text {
        height: auto !important;
        overflow: visible !important;
        margin-bottom: 5px !important;
    }

    /* Avoid buttons overlapping preceding content */
    div[data-testid="stButton"] {
        margin-top: 8px !important;
    }

    /* Prevent negative spacing on translated titles */
    h2 + div {
        margin-top: 0 !important;
    }
}

    /* YOUR MOVE - Opening label spacing */
@media (max-width: 600px) {
    .opening-label {
        position: relative;
        top: -8px;
        margin-bottom: 4px;
    }
}

    /* YOUR MOVE - Chapter header spacing */
@media (max-width: 600px) {
    .chapter-label {
        position: relative;
        top: -8px;
        margin-bottom: 6px;
    }
}







</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------------
# 5. SESSION STATE AND LANGUAGE
# ----------------------------------------------------------

def detect_language():
    locale = (st.context.locale or "").lower()

    if locale.startswith(("fil", "tl")):
        return "fil"

    if locale.startswith("zh"):
        return "zh"

    return "en"


if "language" not in st.session_state:
    st.session_state.language = detect_language()

if "started" not in st.session_state:
    st.session_state.started = False

if "node" not in st.session_state:
    st.session_state.node = "start"

if "step" not in st.session_state:
    st.session_state.step = 0

if "music_enabled" not in st.session_state:
    st.session_state.music_enabled = True


def restart():
    st.session_state.started = False
    st.session_state.node = "start"
    st.session_state.step = 0


def make_choice(destination):
    st.session_state.node = destination
    st.session_state.step += 1


def story_card(original, translated=None):
    content = html.escape(original)

    if translated:
        content += (
            '<div class="subtitle-text">'
            + html.escape(translated)
            + "</div>"
        )

    st.markdown(
        '<div class="story-card">' + content + "</div>",
        unsafe_allow_html=True,
    )



def bilingual_label(tagalog, translated, language):
    if language == "fil":
        return tagalog
    return tagalog + "\n*" + translated + "*"






# ----------------------------------------------------------
# 6. MAIN APPLICATION
# ----------------------------------------------------------

st.title("🎬 YOUR MOVE")
st.caption("WHAT WOULD YOU DO? | Every choice changes the story.")

with st.expander("🌐 Subtitle settings / Mga Wika"):
    selected_language = st.selectbox(
        "Subtitle language",
        list(LANGUAGES.keys()),
        index=list(LANGUAGES.keys()).index(
            st.session_state.language
        ),
        format_func=lambda code: LANGUAGES[code],
    )

    if selected_language != st.session_state.language:
        st.session_state.language = selected_language
        st.rerun()

    
   

# ----------------------------------------------------------
# CINEMATIC BACKGROUND MUSIC
# ----------------------------------------------------------



from pathlib import Path


from pathlib import Path
import base64
import streamlit.components.v1 as components




def render_background_music():
    music_file = (
        Path(__file__).resolve().parent
        / "assets"
        / "audio"
        / "storyloop_main_theme.mp3"
    )

    if not music_file.exists():
        st.error("Suno music file not found.")
        return

    audio_base64 = base64.b64encode(
        music_file.read_bytes()
    ).decode("ascii")

    components.html(
        f"""
        <audio id="bgm" loop preload="auto">
            <source
                src="data:audio/mpeg;base64,{audio_base64}"
                type="audio/mpeg">
        </audio>

        <script>
        const audio = document.getElementById("bgm");
        audio.volume = 0.18;

        function startMusic() {{
            audio.play().catch(() => {{}});
        }}

        window.parent.document.addEventListener(
            "pointerdown", startMusic, {{ once: true }}
        );

        window.parent.document.addEventListener(
            "keydown", startMusic, {{ once: true }}
        );
        </script>
        """,
        height=0,
    )


render_background_music()


lang = st.session_state.language
original = STORIES["fil"]
translated = STORIES[lang]


if not st.session_state.started:


    # Responsive cinematic opening layout
    st.markdown(
        '<div class="gold-text opening-label">'
        '🎬 YOUR STORY · YOUR CHOICES · YOUR ENDING'
        '</div>',
        unsafe_allow_html=True,
    )


    left_col, right_col = st.columns(
        [1.15, 1],
        gap="medium",
        vertical_alignment="center",
    )

    with left_col:
        
        st.video(
            "assets/videos/opening.mp4",
            autoplay=True,
            muted=True,
            loop=True,
            width="stretch",
        )


    with right_col:
       

        st.markdown("## " + original["title"])

        if lang != "fil":
            st.markdown(
                f'<div style="color:#FFD978; font-size:20px; '
                f'font-style:italic; margin-top:-10px; '
                f'margin-bottom:8px;">'
                f'{html.escape(translated["title"])}</div>',
                unsafe_allow_html=True,
            )





        story_card(
            original["intro"],
            translated["intro"] if lang != "fil" else None,
        )

        start_text = bilingual_label(
            "IKAW, ANO ANG GAGAWIN MO?",
            UI[lang]["start"],
            lang,
        )

        if st.button(
            "🚀 " + start_text,
            type="primary",
            width="stretch",
        ):
            st.session_state.started = True
            st.rerun()


else:
    # ======================================================
    # STORYLOOP AI - CINEMATIC GAMEPLAY AND ENDINGS
    # ======================================================

    node_id = st.session_state.node

    # Map story nodes to cinematic videos
    scene_videos = {
        "start": "opening.mp4",
        "police": "police.mp4",
        "phone": "phone.mp4",
        "owner": "mystery.mp4",
        "witness": "police.mp4",
        "record": "mystery.mp4",
        "stranger": "mystery.mp4",
        "clue": "mystery.mp4",
    }

    # Map achievements to cinematic ending videos
    ending_videos = {
        "hero": "ending_hero.mp4",
        "detective": "ending_detective.mp4",
        "guardian": "ending_guardian.mp4",
    }

    # ======================================================
    # CINEMATIC ENDING
    # ======================================================

    
    if node_id in original["endings"]:

        title, description = original["endings"][node_id]
        translated_title, translated_description = (
            translated["endings"][node_id]
        )

        st.progress(1.0)

        left_col, right_col = st.columns(
            [1.15, 1],
            gap="medium",
            vertical_alignment="center",
        )

        with left_col:
            ending_file = ending_videos.get(node_id)

            if ending_file:
                st.video(
                    f"assets/videos/{ending_file}",
                    autoplay=True,
                    muted=False,
                    loop=False,
                    width="stretch",
                )

        with right_col:
            st.markdown(
                '<div class="gold-text">'
                '✨ ACHIEVEMENT UNLOCKED ✨'
                '</div>',
                unsafe_allow_html=True,
            )

            st.markdown("## " + title)

          

            if lang != "fil":
                st.markdown(
                    f'<div style="color:#FFD978; font-size:17px; '
                    f'font-style:italic; margin-top:0px; '
                    f'margin-bottom:10px; line-height:1.4;">'
                    f'{html.escape(translated_title)}</div>',
                    unsafe_allow_html=True,
                )
            story_card(
                description,
                translated_description if lang != "fil" else None,
            )

            st.markdown(
                "### 🌟 Bawat desisyon ay may kahulugan!"
            )

            replay_text = bilingual_label(
                UI["fil"]["replay"],
                UI[lang]["replay"],
                lang,
            )

            if st.button(
                "🔄 " + replay_text,
                width="stretch",
            ):
                restart()
                st.rerun()

    # ======================================================
    # CINEMATIC GAMEPLAY
    # ======================================================

    else:

        original_node = original["nodes"][node_id]
        translated_node = translated["nodes"][node_id]

        chapter = st.session_state.step + 1

        st.progress(st.session_state.step / 3)

        st.markdown(
            f'<div class="gold-text chapter-label">'
            f'✨ KABANATA {chapter} / 3'
            f'</div>',
            unsafe_allow_html=True,
        )

        
        # Responsive cinematic split-screen gameplay
        left_col, right_col = st.columns(
            [1.15, 1],
            gap="medium",
            vertical_alignment="top",
        )

        with left_col:
            video_file = scene_videos.get(
                node_id,
                "opening.mp4",
            )

            st.video(
                f"assets/videos/{video_file}",
                autoplay=True,
                muted=False,
                loop=True,
                width="stretch",
            )

        with right_col:
            # Story text and automatic subtitles
            story_card(
                original_node[0],
                translated_node[0] if lang != "fil" else None,
            )

            st.markdown(
                "### ✨ " + UI["fil"]["question"]
            )


            if lang != "fil":
                st.markdown(
                    f'<div style="color:#FFD978; font-size:20px; '
                    f'font-style:italic; margin-top:-10px; '
                    f'margin-bottom:8px;">'
                    f'{html.escape(UI[lang]["question"])}</div>',
                    unsafe_allow_html=True,
                )



            # Three interactive choices
            for index, (label, destination) in enumerate(
                original_node[1]
            ):
                translated_label = translated_node[1][index][0]

                button_text = bilingual_label(
                    label,
                    translated_label,
                    lang,
                )

                if st.button(
                    f"{index + 1}. {button_text}",
                    key=f"{node_id}_{index}",
                    width="stretch",
                ):
                    make_choice(destination)
                    st.rerun()


