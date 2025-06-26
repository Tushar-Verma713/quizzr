import streamlit as st

st.title("Ultimate Tech & History Quiz")

score = 0

# Replace input() with st.text_input (each needs a unique key)
aircraft = st.text_input("Sr-71 highest speed record?\nA) Mach 2.8\nB) Mach 3.3\nC) Mach 3.5\nD) Mach 4.0", key="q1")
isotope = st.text_input("Isotope of a nuclear warhead?\nA) titanium\nB) oxygen\nC) nitrogen\nD) uranium", key="q2")
antimatter = st.text_input("Cost of 1g antimatter?\nA) $62.5 trillion\nB) $2 trillion\nC) $98 trillion\nD) $15 trillion", key="q3")
apollo = st.text_input("Apollo11 launched in which year?\nA) 2005\nB) 1964\nC) 1969\nD) 1961", key="q4")
sovietunion = st.text_input("Soviet Union collapsed in which year?\nA) 1991\nB) 1999\nC) 1995\nD) 1992", key="q5")
thrust = st.text_input("Thrust of Plasma engine?\nA) 2 newton\nB) 6 newton\nC) 7 newton\nD) 8 newton", key="q6")
blackhole = st.text_input("Largest black hole ever discovered is?\nA) Ton-618\nB) keplep12\nC) neutron\nD) fx-91es", key="q7")
nukes = st.text_input("1st nuclear warheads used by which country?\nA) Germany\nB) Poland\nC) USA\nD) Soviet Union", key="q8")
restorehope = st.text_input("Operation Restorehope launched by which country?\nA) USA\nB) India\nC) Iran\nD) UK", key="q9")
energysource = st.text_input("Energy source of Plasma engine?\nA) nuclear reactor\nB) solar energy\nC) Wind energy\nD) Coal", key="q10")
m82 = st.text_input("M82 .50 caliber sniper rifle made in which year?\nA) 1982\nB) 1999\nC) 2006\nD) 2009", key="q11")
baldwin = st.text_input("King Baldwin-IV called as?\nA) cobra\nB) Leper king\nC) KINGTH\nD) Warrior", key="q12")
delta = st.text_input("Delta force is a force belong to which country?\nA) Israel\nB) India\nC) Russia\nD) USA", key="q13")
nuc = st.text_input("Country with large no. of warheads?\nA) Russia\nB) Iran\nC) USA\nD) France", key="q14")
hinden = st.text_input("Hindenberg incident occurred in which year?\nA) 1945\nB) 1940\nC) 1937\nD) 1931", key="q15")
threehz = st.text_input("3Hz frequency useful in?\nA) produce sleep\nB) for energy\nC) for pain relief\nD) for alertness", key="q16")
cure = st.text_input("Stemcell treatment helps in treatment of?\nA) backpain\nB) cancer\nC) hiv\nD) asthma", key="q17")
ice = st.text_input("Nuclear icebreaker was 1st invented by which country?\nA) russia\nB) greenland\nC) canada\nD) germany", key="q18")
raptor = st.text_input("F-22 raptor operated by which country?\nA) ukraine\nB) uk\nC) usa\nD) australia", key="q19")
roswell = st.text_input("Roswell incident occur in which country?\nA) india\nB) peru\nC) vatican city\nD) mexico", key="q20")
hypersonic = st.text_input("Fastest hypersonic missile is?\nA) brahmos\nB) scalp\nC) satan-2\nD) satan-1", key="q21")
bywhichc = st.text_input("Operation Highjump launched by which country?\nA) usa\nB) germany\nC) argentina\nD) cuba", key="q22")
farest = st.text_input("Farthest man made object is?\nA) voyger-1\nB) voyger-2\nC) james web telescope\nD) hubble telescope", key="q23")
kep218 = st.text_input("Newly found planet in habitable zone is?\nA) kepler-218\nB) proxima century\nC) ton-618\nD) kepler-21Ab", key="q24")
closetosun = st.text_input("Closest manmade object to sun is?\nA) parker\nB) apollo11\nC) apollo13\nD) voyger-2", key="q25")

if st.button("Submit Quiz"):
    score = 0
    def check(ans, correct):
        global score
        if ans.strip().lower() == correct.lower():
            st.success("Correct")
            score += 1
        else:
            st.error("Wrong")

    check(aircraft, "b")
    check(isotope, "d")
    check(antimatter, "a")
    check(apollo, "c")
    check(sovietunion, "a")
    check(thrust, "b")
    check(blackhole, "a")
    check(nukes, "c")
    check(restorehope, "a")
    check(energysource, "a")
    check(m82, "a")
    check(baldwin, "b")
    check(delta, "d")
    check(nuc, "c")
    check(hinden, "c")
    check(threehz, "a")
    check(cure, "a")
    check(ice, "a")
    check(raptor, "c")
    check(roswell, "d")
    check(hypersonic, "c")
    check(bywhichc, "a")
    check(farest, "a")
    check(kep218, "a")
    check(closetosun, "a")
    
    st.info(f"Your Final Score is: **{score}/25**")
