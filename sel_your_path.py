import streamlit as st

ds, aws, fs, sdet = [], [], [], []

coding_dict = {"I love too much": {"ds": 2, "aws": 1, "fs": 4, "sdet": 3},
               "I like": {"ds": 1, "aws": 2, "fs": 3, "sdet": 4},
               "So so": {"ds": 4, "aws": 3, "fs": 2, "sdet": 1},
               "I don't like": {"ds": 3, "aws": 4, "fs": 1, "sdet": 2}}

st.title('Your Path Advice')
st.write("""
### (Attention: This is only a recommendation)

""")

coding = st.selectbox("Select your coding level", list(coding_dict.keys()))

ds.append(coding_dict[coding]["ds"])
aws.append(coding_dict[coding]["aws"])
fs.append(coding_dict[coding]["fs"])
sdet.append(coding_dict[coding]["sdet"])

acad_back_dict = {"Math/Statistics": {"ds": 4, "aws": 1, "fs": 3, "sdet": 2},
                  "Engineer": {"ds": 3, "aws": 2, "fs": 4, "sdet": 1},
                  "Balanced": {"ds": 2, "aws": 3, "fs": 1, "sdet": 4},
                  "Social": {"ds": 1, "aws": 4, "fs": 2, "sdet": 3}}

acad = st.selectbox("Select your academical background", list(acad_back_dict.keys()))

ds.append(acad_back_dict[acad]["ds"])
aws.append(acad_back_dict[acad]["aws"])
fs.append(acad_back_dict[acad]["fs"])
sdet.append(acad_back_dict[acad]["sdet"])

com_skill_dict = {"Very good": {"ds": 3, "aws": 1, "fs": 2, "sdet": 4},
                  "Good": {"ds": 4, "aws": 2, "fs": 1, "sdet": 3},
                  "So so": {"ds": 1, "aws": 3, "fs": 4, "sdet": 2},
                  "Bad": {"ds": 2, "aws": 4, "fs": 3, "sdet": 1}}

com_skill = st.selectbox("Select your communication skill level", list(com_skill_dict.keys()))

ds.append(com_skill_dict[com_skill]["ds"])
aws.append(com_skill_dict[com_skill]["aws"])
fs.append(com_skill_dict[com_skill]["fs"])
sdet.append(com_skill_dict[com_skill]["sdet"])

eng_level_dict = {"Advanced": {"ds": 4, "aws": 2, "fs": 3, "sdet": 1},
                  "High Intermediate": {"ds": 3, "aws": 1, "fs": 4, "sdet": 2},
                  "Intermediate": {"ds": 2, "aws": 4, "fs": 1, "sdet": 3},
                  "Beginner": {"ds": 1, "aws": 3, "fs": 2, "sdet": 4}}

eng_level = st.selectbox("Select your English level", list(eng_level_dict.keys()))

ds.append(eng_level_dict[eng_level]["ds"])
aws.append(eng_level_dict[eng_level]["aws"])
fs.append(eng_level_dict[eng_level]["fs"])
sdet.append(eng_level_dict[eng_level]["sdet"])

job_urgency_dict = {"Very urgent": {"ds": 1, "aws": 3, "fs": 2, "sdet": 4},
                    "Urgent": {"ds": 2, "aws": 4, "fs": 1, "sdet": 3},
                    "So so": {"ds": 3, "aws": 1, "fs": 4, "sdet": 2},
                    "No Urgency": {"ds": 4, "aws": 2, "fs": 3, "sdet": 1}}

job_urgency = st.selectbox("Select your finding job urgency", list(job_urgency_dict.keys()))

ds.append(job_urgency_dict[job_urgency]["ds"])
aws.append(job_urgency_dict[job_urgency]["aws"])
fs.append(job_urgency_dict[job_urgency]["fs"])
sdet.append(job_urgency_dict[job_urgency]["sdet"])

it_back_dict = {"Advanced": {"ds": 3, "aws": 2, "fs": 4, "sdet": 1},
                "High Intermediate": {"ds": 4, "aws": 1, "fs": 3, "sdet": 2},
                "Intermediate": {"ds": 1, "aws": 4, "fs": 2, "sdet": 3},
                "Beginner": {"ds": 2, "aws": 3, "fs": 1, "sdet": 4}}

it_back = st.selectbox("Select your IT background level", list(it_back_dict.keys()))

ds.append(it_back_dict[it_back]["ds"])
aws.append(it_back_dict[it_back]["aws"])
fs.append(it_back_dict[it_back]["fs"])
sdet.append(it_back_dict[it_back]["sdet"])

path_dict = {"Data Science": sum(ds),
             "AWS-DevOps": sum(aws),
             "Full Stack": sum(fs),
             "SDET": sum(sdet)}

st.success(f"We recommend you '{sorted(path_dict.items(), key=lambda x: x[1])[3][0]}' path.")
