import streamlit as st

import pandas as pd



st.set_page_config(layout="wide", page_title="Work Experience", page_icon="🧑‍💻")

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


st.header("Professional Experience 🌐")

########################  Snapshot  ###################################################

st.subheader("My Journey, So Far...")

st.image("pages/careersnapshot.png", caption="Technological partners / vendors worked with", width=600)

################################ End of Career Snapshot ################################################


############################## GM Job Role ##############################################

st.header("Job Responsibilities")

st.subheader("General Mills India")

genmills_job_role ="""
* Operate and secure enterprise-grade GKE clusters and IIS platforms, ensuring seamless hosting of internal and external web applications with a strong focus on availability, security, and performance.\n
* Design and manage scalable infrastructure using Terraform, enabling consistent provisioning of GCP resources including GKE clusters, VPCs, compute instances, and Cloud Armor through infrastructure-as-code practices.\n
* Implement GitOps-based application deployments with Flux, ArgoCD, and Kustomize, facilitating automated, secure, and version-controlled CI/CD pipelines on Kubernetes.\n
* Administer Kubernetes clusters, perform upgrades, and integrate critical add-ons like cert-manager, external-dns, and vault-secret-operator to enhance operational reliability and security.\n
* Modernize legacy applications by containerizing them with Docker, collaborating closely with development teams to drive cloud-native adoption and streamline deployments.\n
* Automate Kubernetes operations using Kafka pub/sub, Argo Workflows, and Python scripting to improve operational efficiency, reduce manual effort, and ensure consistency in resource provisioning.\n
* Lead incident response and platform troubleshooting, serving as a primary escalation point while working cross-functionally with developers, PMs, and analysts to minimize downtime and resolve complex issues.\n
"""

st.write(genmills_job_role)

st.subheader("Projects:")

genmills_projects ="""
* Migration to Infrastructure as Code (IaC) for DNS Management: Transition DNS record management from manual (ClickOps) operations to Infrastructure as Code using Terraform with Infoblox as the DNS provider adding auditability of the records along effiecient and quick management.\n

* Automated Decommissioning of Applications from GKE Clusters:  Implemented an automation using Kafka Pub/Sub and Argowork flows integrated with Backstage to auto-decommission applications as requested via Backstage by their respective owners.
 
"""

st.write(genmills_projects)

######################### End of GM Job roles ###################################



############################## Allot Job Role ##################################

st.subheader("Allot Communications India")

allot_job_role = """
* Managed deployment, monitoring, and troubleshooting of Allot Solutions on Azure, AWS, and VMware platforms, utilizing services like AKS, EKS, EC2, IAM, and vCenter.\n
* Handled Kubernetes cluster administration, including Ansible-based provisioning and certificate automation.\n
* Provided L3 product support for platform and cloud operations, and served as system administrator for demo center setups.\n 
* Built and maintained CI/CD pipelines for lab and POC environments using Jenkins, Terraform, and container technologies.\n
* Automated infrastructure provisioning and routine operations using shell scripts and Ansible playbooks.\n
* Developed and integrated monitoring solutions using Prometheus, Grafana, and Jenkins for system-level insights.\n 
* Created custom alerts and dashboards for proactive issue resolution and performance monitoring.\n
* Ensured product security through vulnerability assessments, SSL management, and CIS-standard configuration.\n
* Delivered end-to-end deployment and support for DPI and network security products like Netxplorer, ASM, and Clearsee.\n 
* Acted as queue manager, resolving over 580 technical cases with SLA breach under 5%, and provided 100% RCA documentation for critical issues.\n 
* Recognized for leading L1 support operations and mentoring teams at Rakuten Mobile and Reliance Jio.\n
* Conducted technical training sessions for partners, customers, and internal teams.\n
* Offered on-site and remote L2 support for key clients, maintaining strong customer engagement.\n
"""

st.write(allot_job_role)

st.subheader("Projects:")
allot_projects ="""
* Implementation of a custom monitoring system via use of Jenkins and shell scripting for Legacy Monolithic applications on linux systems.\n
* UAT for different Allot smart solution applications post installation via Jenkins pipeline.\n
* India Lab Server setup with Vmware vsphere and vcenter on baremetal servers.\n
* Real time Alerts from Allot Smart solutions using Prometheus to Slack channel with AI bot integration - AI Hackathon.
"""
st.write(allot_projects)


































# df = pd.read_csv("pages/data.csv", sep=",")
#
# for index, row in df.iterrows():
#     st.subheader(row["title"])
#     st.write(row["description"])
#     # st.image("pages/projectimages/" + row["image"], width=100)
