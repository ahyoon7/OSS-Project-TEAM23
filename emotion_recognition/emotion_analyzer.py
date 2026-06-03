emotion_keywords = {
    "우울": [
        "우울", "슬퍼", "슬프", "눈물", "외로", "허무", "공허",
        "무기력", "아무것도 하기 싫", "힘이 안 나", "기운이 없"
    ],
    "불안": [
        "불안", "걱정", "초조", "긴장", "무섭", "두렵",
        "떨려", "심장이", "불안정", "겁나"
    ],
    "분노": [
        "화나", "짜증", "분노", "열받", "억울", "빡쳐",
        "미치겠", "답답", "화가 나"
    ],
    "무기력": [
        "귀찮", "무기력", "하기 싫", "움직이기 싫", "침대",
        "의욕", "포기", "지쳤", "피곤"
    ],
    "긍정": [
        "좋아", "행복", "기뻐", "괜찮", "고마워", "감사",
        "편안", "재밌", "즐거"
    ]
}

risk_words = [
    "자살",
    "자해",
    "극단적 선택",

    "죽고 싶",
    "죽고싶",
    "죽고 싶다",
    "죽고싶다",
    "죽어버리고 싶",
    "죽어 버리고 싶",

    "살기 싫",
    "살기싫",
    "살기 싫다",
    "살기싫다",

    "사라지고 싶",
    "사라지고싶",
    "없어지고 싶",
    "없어지고싶",
    "내가 없어졌으면",
    "나 없어졌으면",

    "끝내고 싶",
    "끝내고싶",
    "그만 살고 싶",
    "그만살고 싶",

    "버티기 힘들",
    "버틸 수 없",
    "못 버티겠",
    "더는 못 버티",
    "한계야",

    "해치고 싶",
    "해치고싶",
    "나를 해치",
    "내 몸을 해치"
]

def analyze_emotion(text):
    scores = {}

    for emotion, keywords in emotion_keywords.items():
        count = 0

        for keyword in keywords:
            if keyword in text:
                count += 1

        scores[emotion] = count

    total = sum(scores.values())

    if total == 0:
        return [
            {"label": "중립", "score": 1.0}
        ]

    result = []

    for emotion, count in scores.items():
        if count > 0:
            result.append({
                "label": emotion,
                "score": round(count / total, 3)
            })

    result.sort(key=lambda x: x["score"], reverse=True)

    return result

def detect_risk_words(text):
    for word in risk_words:
        if word in text:
            return True
    return False
