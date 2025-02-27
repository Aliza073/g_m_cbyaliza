import streamlit as st

st.set_page_config(page_title="Growth Mindset Project")
st.title("Growth Mindset Project AI Project Challenge By Aliza")

st.header("Wellcome to your growth journey! with Aliza")
st.write("In a growth mindset, challenges are exciting rather than threatening. So rather than thinking, oh, I'm going to reveal my weaknesses, you say, wow, here's a chance to grow. The idea that excellence is something you can build, that you can grow!")

st.header("Today's Growth Mindset Quotes")
st.write("'Success is not the end, failure is not destiny. Remember.. -Aliza Aleem'")

#quote section
st.header("What is the challenge in your life for 2025?")
user_input = st.text_input("Describe your challenge?")
if user_input:
    st.success(f" you'r facing {user_input} keep pushing forward for your goals!")
else:
    st.warning("Set your goal right now!")

#reflexing section
st.header("Reflect on your learning")
Reflection = st.text_area("write your reflection here..")
if Reflection:
    st.success(f"Great Insight! your reflection: {Reflection}")
else:
    st.info("Reflecting on past experience grow! Share your difficulties")

#time period
st.header("Time period..!")
timeperiod = st.number_input("How many days did you take to complete your goals?", min_value=1, max_value=100, value=20)
if 10 < timeperiod < 30:
    st.success("WaOo! Great job u must achieved your goals")
elif 30 < timeperiod < 50:
    st.success("good job! but do it faster.")
elif 50 < timeperiod < 100:
    st.success("too late! if u go with this speed u r achieved your goals.")
else:
    st.error("Invalid! please enter a number between 1 and 100 days.")

#progress
st.header("progress")
progress_value = st.slider("How about your progress (0-100)?", 0, 100, 50)
st.progress(progress_value)
if progress_value == 100:
    st.success("Welldone champ")
elif progress_value >= 50:
    st.success("keep it up")
else:
    st.write("work hard")

#achievements
st.header("Celebrate your wins..!")
achievements = st.text_input("Share something u have recently accomplished")
if achievements:
    st.success(f"Amazing! you achieved: {achievements}")
else:
    st.info("Big or small achievements make u big")

#footer
st.write("_ _ _")
st.write("Keep beliving in youself")
st.write("Created By Aliza Aleem..1")

