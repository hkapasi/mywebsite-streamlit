import streamlit as st
#import pandas as pd

# Set page config
st.set_page_config(layout="wide", page_title="About Me", page_icon="ℹ️")

# Inject custom CSS
st.markdown(
    """
    <style>
    /* Hide the entire top-right toolbar (Deploy + Menu) */
    [data-testid="stToolbar"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


########################## Start of Introduction ######################################################



st.title("Hozefa Kapasi 🧑‍💻")


row1_col1, row1_col2 = st.columns([1,2])

with row1_col1:
    st.image("personal_pic.png", use_container_width=True)

with row1_col2:
    content = """
Hi there! 👋

I’m a Senior Infrastructure engineer at General Mills India, in the Web Hosting - DevOps Platform team which is in charge to build and support scalable, reliable platforms for GM applications.

With 11+ years of experience across Telecommunications, Network Security, and IT, I bring a strong foundation in building and efficiently operating platforms, DevOps practices, customer success, technical support and team management.

🎓 I hold a degree in Electronics and Telecommunications Engineering, I also have a Post Graduate Certificate from IIIT Bengaluru in DevOps specialization, which landed me my first official role in field of DevOps and Cloud.

Certified Google Cloud Professional Architect ☁️   &   Certified Kubernetes Administrator ⚓️

When not buried in my laptop either working or learning, you’ll usually find me enjoying quality time with family and friends, watching football or unwinding with music or video games.  
"""

    st.info(content)

########################## End of Introduction ######################################################


########################## Family & Personal Details ######################################################

# Add a horizontal separator (optional); This is outside the with columns above, so it will add a new row below.
st.markdown("---")

fam1row1, fam2row2 = st.columns(2)
with fam1row1:
    family_info = """
Born in city of Rajkot in Gujarat, I’ve spent the majority of my life growing up and working in the vibrant city of Mumbai.\n
I earned my Bachelor’s degree in Electronics and Telecommunications from Mumbai University in 2013, which led to my first Job at Reliance Jio where I was part of team experiencing 4G connectivity in India first hand.\n
I’ve been happily married for six wonderful years, and together we’re raising our delightfully spirited 3-year-old son, who keeps life interesting with his sweet nature and ever-changing moods.\n
"""
    st.warning(family_info)

    # st.markdown(
    #     """
    #     <div style="background-color:#f9f9a9;padding:10px;border-radius:5px">
    #         <b>Born in small town of Rajkot in Gujarat, I have spent most of my life in Mumbai.</br>
    #         <b>Born in small town of Rajkot in Gujarat, I have spent most of my life in Mumbai.</b>
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )



with fam2row2:
    st.image("familyart.jpg", caption = "Here is a Ghibli glimpse of us on one of our Weekend Drives", width=400)

teamcol1, teamcol2, teamcol3 = st.columns([1.6,0.6,1])

with teamcol1:
    team_content = """
I'm a huge fan of Liverpool F.C. & the Indian Cricket Team and have been to following them across all formats and tournaments.\n
Supporting these teams isn’t just about the wins; it's about the emotions, the community, and the life lessons they bring — like staying focused, bouncing back from setbacks, and always playing as a team.\n
At the time of writing, both are reigning champions — good times!! 🏆🏆  
"""
    st.warning(team_content)

with teamcol2:
    st.image("LFC_Champions.jpg", caption = "Premier League Champions 2024-2025", width=200)

with teamcol3:
    st.image("IndianCricketTeam_Champions.jpg", caption = "Champions Trophy Winners 2025", width =190)




st.markdown("---")

########################## End of Family and Personal Details ##############################################





# Second row (new content)
row2_col1, line_col2, row2_col3  = st.columns([3,0.5,3])

with row2_col1:
    st.subheader("Skills and Tools 🛠️")
    skills = """
•	Cloud Computing and Virtualization: GCP, AWS, Azure, Vmware\n
•	Containerization & Orchestration: Kubernetes & Docker \n
•	Infrastructure as Code: Terraform, Helm, Kustomize\n
•	DevOps & GitOps Tools: FluxCD, ArgoCD, Argo Workflows, GitHub Actions, Jenkins (basic)\n
•	Scripting & Automation: Python, Bash, Kafka Pub/Sub Automation\n
•	Configuration Management: YAML, JSON, Secret Management (Vault, Secret Manager)\n
•	Networking & Security: VPC Networking, Load Balancers, Cloud Armor, SSL/TLS Certificate Management, DNS (Cloud DNS, External DNS)\n
•	Monitoring & Troubleshooting: Google Cloud Operations, Datadog, Prometheus, Grafana, ServiceNow\n
•	Process & Management: Agile/Scrum, Sprint Planning, Daily Standups, Team Leadership\n
•	Disaster Recovery & Platform Resilience: DR Drills, Platform Scaling and High Availability Practices\n
•	Collaboration & Documentation: Jira, Confluence, Microsoft Teams, Slack\n
•   AI: Content creation, documentation - Chatgpt, MS Copilot; AI-assisted coding / scripting - Copilot\n
    """
    st.write(skills)

with line_col2:
    st.markdown(
        """
        <div style='width:2px; height: 700px; background-color: gray; margin: auto;'></div>
        """,
        unsafe_allow_html=True
    )


with row2_col3:
    st.subheader("Certifications and Trainings 📜")
    st.markdown("[Google Cloud Professional Architect](https://www.credly.com/badges/67c61d2a-2b56-4244-8c4d-90e67419b6c6/linked_in?t=swjm5z)")
    st.markdown("[Certified Kubernetes Administrator](https://www.credly.com/badges/0002e151-03ba-4376-a9a6-84a7298c082d/public_url)")
    st.markdown("[Post Graduate Certificate in DevOps - IIIT Bengaluru](https://www.credential.net/6890ecc2-3af4-4df9-869a-ba70d7fda2a6#acc.u7stqgnQ)")
    st.markdown("[Advance Management Training - EAZL.ai](https://drive.google.com/file/d/1dxyZlAP2gC6FId7AmTxcItJP-dCDvjRk/view)")
st.markdown("---")


# with row2_col3:
#     st.subheader("Hobbies")
#     st.markdown("""
#     - Watching football
#     - Playing video games
#     - Exploring tech blogs
#     """)


# st.header("Recent Projects")
#
# df = pd.read_csv("data.csv", sep=",")
#
# for index, row in df.iterrows():
#     st.subheader(row["title"])
#     st.write(row["description"])
#     st.image("projectimages/" + row["image"], width=100)
