import streamlit as st
import whisper

st.title("Emotion Recognition 테스트")
st.write("마이크로 말하면 Whisper STT를 통해 텍스트로 변환합니다.")

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")

audio_file = st.audio_input("마이크로 말하기")

if audio_file is not None:

    with open("recorded_audio.wav", "wb") as f:
        f.write(audio_file.getbuffer())

    st.audio(audio_file)
    st.success("음성 입력이 완료되었습니다.")
    st.write("recorded_audio.wav 파일로 저장되었습니다.")

    if st.button("텍스트로 변환하기"):
        with st.spinner("Whisper가 음성을 텍스트로 변환하는 중입니다..."):
            model = load_whisper_model()
            result = model.transcribe("recorded_audio.wav", language="ko", fp16=False)
            text = result["text"]

        st.subheader("STT 변환 결과")
        st.write(text)
