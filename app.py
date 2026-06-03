import streamlit as st
import pandas as pd
from datetime import datetime
from routine_db import create_table, add_record, get_all_records

create_table()

st.set_page_config(
    page_title="Emotion Mate 루틴 대시보드",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 Emotion Mate 마이크로 루틴 & 대시보드")

st.write("""
AI가 추천한 작은 미션을 사용자가 완료하면 기록을 저장하고,
주간 달성률을 그래프로 확인할 수 있는 화면입니다.
""")

st.divider()

st.subheader("오늘의 마이크로 루틴")

default_missions = [
    "창문 열고 1분 동안 바깥 공기 마시기",
    "물 한 컵 마시기",
    "침대 정리하기",
    "가벼운 스트레칭 3분 하기",
    "오늘 기분 한 문장으로 적기",
    "집 앞이나 복도까지 잠깐 나가보기"
]

selected_mission = st.selectbox(
    "AI가 제안한 미션을 선택하세요.",
    default_missions
)

custom_mission = st.text_input(
    "직접 미션을 입력할 수도 있어요.",
    placeholder="예: 세수하기, 밥 챙겨 먹기, 햇빛 보기"
)

mission = custom_mission if custom_mission.strip() else selected_mission

st.info(f"오늘의 미션: {mission}")

if st.button("완료"):
    add_record(mission, completed=1)
    st.success("미션 완료 기록이 저장되었습니다!")

st.divider()

st.subheader("미션 수행 기록")

records = get_all_records()

if len(records) == 0:
    st.warning("아직 저장된 미션 기록이 없습니다.")
else:
    df = pd.DataFrame(
        records,
        columns=["ID", "미션", "완료여부", "기록시간"]
    )

    df["기록시간"] = pd.to_datetime(df["기록시간"])
    df["날짜"] = df["기록시간"].dt.date
    df["요일"] = df["기록시간"].dt.day_name()

    st.dataframe(df, use_container_width=True)

    st.divider()

    st.subheader("주간 미션 달성률")

    today = datetime.now().date()
    df["날짜"] = pd.to_datetime(df["날짜"])

    recent_df = df[df["기록시간"].dt.date >= pd.to_datetime(today).date() - pd.Timedelta(days=6)]

    daily_count = recent_df.groupby(recent_df["기록시간"].dt.date)["완료여부"].sum()

    chart_df = pd.DataFrame({
        "날짜": daily_count.index,
        "완료한 미션 수": daily_count.values
    })

    st.bar_chart(chart_df.set_index("날짜"))

    total_completed = df["완료여부"].sum()
    st.metric("전체 완료 미션 수", int(total_completed))
