import streamlit as st

st.title("Ultimate Tech & History Quiz")

score = 0

def ask_question(question, options, correct_answer):
    global score
    answer = st.radio(question, options, key=question)
    if st.button(f"Submit for: {question}", key=question + "_submit"):
        if answer.startswith(correct_answer):
            st.success("Correct")
            score += 1
        else:
            st.error("Wrong")
        st.write(f"Current Score: {score}")

questions = [
    ("Sr-71 highest speed record?", ["A) Mach 2.8", "B) Mach 3.3", "C) Mach 3.5", "D) Mach 4.0"], "B"),
    ("Isotope of a nuclear warhead?", ["A) titanium", "B) oxygen", "C) nitrogen", "D) uranium"], "D"),
    ("Cost of 1g antimatter?", ["A) $62.5 trillion", "B) $2 trillion", "C) $98 trillion", "D) $15 trillion"], "A"),
    ("Apollo11 launched in which year?", ["A) 2005", "B) 1964", "C) 1969", "D) 1961"], "C"),
    ("Soviet Union collapsed in which year?", ["A) 1991", "B) 1999", "C) 1995", "D) 1992"], "A"),
    ("Thrust of Plasma engine?", ["A) 2 newton", "B) 6 newton", "C) 7 newton", "D) 8 newton"], "B"),
    ("Largest black hole ever discovered is?", ["A) Ton-618", "B) keplep12", "C) neutron", "D) fx-91es"], "A"),
    ("1st nuclear warheads used by which country?", ["A) Germany", "B) Poland", "C) USA", "D) Soviet Union"], "C"),
    ("Operation Restore Hope launched by which country?", ["A) USA", "B) India", "C) Iran", "D) UK"], "A"),
    ("Energy source of Plasma engine?", ["A) nuclear reactor", "B) solar energy", "C) Wind energy", "D) Coal"], "A"),
    ("M82 .50 caliber sniper rifle made in which year?", ["A) 1982", "B) 1999", "C) 2006", "D) 2009"], "A"),
    ("King Baldwin-IV called as?", ["A) cobra", "B) Leper king", "C) KINGTH", "D) Warrior"], "B"),
    ("Delta force is a force belonging to which country?", ["A) Israel", "B) India", "C) Russia", "D) USA"], "D"),
    ("Country with largest number of warheads?", ["A) Russia", "B) Iran", "C) USA", "D) France"], "C"),
    ("Hindenberg incident occurred in which year?", ["A) 1945", "B) 1940", "C) 1937", "D) 1931"], "C"),
    ("3Hz frequency useful in?", ["A) produce sleep", "B) for energy", "C) for pain relief", "D) for alertness"], "A"),
    ("Stemcell treatment helps in treatment of?", ["A) backpain", "B) cancer", "C) HIV", "D) asthma"], "A"),
    ("Nuclear icebreaker was 1st invented by which country?", ["A) Russia", "B) Greenland", "C) Canada", "D) Germany"], "A"),
    ("F-22 Raptor operated by which country?", ["A) Ukraine", "B) UK", "C) USA", "D) Australia"], "C"),
    ("Roswell incident occurred in which country?", ["A) India", "B) Peru", "C) Vatican City", "D) Mexico"], "D"),
    ("Fastest hypersonic missile is?", ["A) BrahMos", "B) SCALP", "C) Satan-2", "D) Satan-1"], "C"),
    ("Operation Highjump launched by which country?", ["A) USA", "B) Germany", "C) Argentina", "D) Cuba"], "A"),
    ("Farthest man-made object is?", ["A) Voyager-1", "B) Voyager-2", "C) James Webb Telescope", "D) Hubble Telescope"], "A"),
    ("Newly found planet in habitable zone is?", ["A) Kepler-218", "B) Proxima Centauri", "C) Ton-618", "D) Kepler-21Ab"], "A"),
    ("Closest manmade object to sun is?", ["A) Parker", "B) Apollo 11", "C) Apollo 13", "D) Voyager-2"], "A"),
]

for q in questions:
    ask_question(*q)

st.write(f"Your final score is: **{score}/{len(questions)}**")

