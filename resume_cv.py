import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Mohammed Furkhan - DevOps Engineer",
    layout="wide",
    initial_sidebar_state="collapsed",
     page_icon ="📑"
    
)

# Custom CSS for Word-like styling
st.markdown("""
<style>
body {
    font-family: 'Calibri', sans-serif;
    line-height: 1.6;
}
.resume-header {
    text-align: center;
    margin-bottom: 20px;
}
.section-title {
    color: #2F5496;
    font-size: 16px;
    font-weight: bold;
    border-bottom: 1px solid #2F5496;
    margin-top: 15px;
    margin-bottom: 10px;
}
.content {
    margin-left: 20px;
}
</style>
""", unsafe_allow_html=True)

# Header

st.markdown("""
<div class='resume-header'>
    <h1 style='margin-bottom: 5px;'>Mohammed Furkhan</h1>
     <h3 style='margin: 5px;'>DevOps Engineer</h3>
    
</div>
""", unsafe_allow_html=True)

# Professional Summary
st.markdown("<div class='section-title'>SUMMARY</div>", unsafe_allow_html=True)
st.write("""
DevOps Engineer with experience in implementing and maintaining CI/CD pipelines, cloud infrastructure, 
and automation solutions. Skilled in AWS, Docker, Kubernetes, and Infrastructure as Code. 
Currently working with Citi Bank client through TCS, focusing on streamlining deployment processes 
and improving infrastructure efficiency.
""")

# Technical Skills
st.markdown("<div class='section-title'>TECHNICAL SKILLS</div>", unsafe_allow_html=True)
st.markdown("""
- **Cloud Platforms:** AWS, Azure
- **Infrastructure as Code:** Terraform, CloudFormation
- **Containerization:** Docker, Kubernetes
- **CI/CD:** Jenkins, GitLab CI, GitHub Actions
- **Configuration Management:** Ansible, Chef
- **Monitoring:** Prometheus, Grafana, ELK Stack
- **Version Control:** Git, GitHub
- **Scripting:** Python, Bash, Shell
- **Operating Systems:** Linux, Ubuntu, CentOS
- **Security:** DevSecOps, AWS Security
""")

# Professional Experience
st.markdown("<div class='section-title'>WORKING EXPERIENCE</div>", unsafe_allow_html=True)
st.markdown("""
**DevOps Engineer | TCS (Citi Bank Client)**  
*June 2022 - Present*
- Implementing and maintaining CI/CD pipelines using Jenkins for Citi Bank's financial applications
- Managing AWS infrastructure using Terraform and CloudFormation
- Collaborating with development teams to automate deployment processes
- Implementing monitoring solutions using Prometheus and Grafana
""")

# Projects
st.markdown("<div class='section-title'>KEY PROJECTS</div>", unsafe_allow_html=True)
st.markdown("""
**1. Financial Application Deployment Automation**
- Developed and implemented automated deployment pipelines for critical financial applications
- Reduced deployment time from 4 hours to 45 minutes
- Implemented blue-green deployment strategy for zero-downtime updates
- Technologies: Jenkins, Docker, Kubernetes, AWS EKS

**2. Infrastructure Monitoring System**
- Designed and implemented comprehensive monitoring solution for cloud infrastructure
- Set up Prometheus and Grafana dashboards for real-time monitoring
- Created automated alerting system for critical metrics
- Achieved 99.9% system visibility and reduced incident response time by 60%
- Technologies: Prometheus, Grafana, AlertManager, AWS CloudWatch

**3. Disaster Recovery Automation**
- Implemented automated DR solution for critical banking applications
- Developed infrastructure as code using Terraform for DR environment
- Reduced Recovery Time Objective (RTO) from 4 hours to 1 hour
- Automated regular DR testing procedures
- Technologies: Terraform, AWS, Python, Shell Scripting
""")

# Education
st.markdown("<div class='section-title'>EDUCATION</div>", unsafe_allow_html=True)
st.markdown("""
**Bachelor of Technology in Computer Science**  
PDA Engineering College (2018 - 2022)
""")

# Certifications
st.markdown("<div class='section-title'>CERTIFICATIONS</div>", unsafe_allow_html=True)
st.markdown("""
- GCP Certified Cloud Engineer

""")


# Languages
st.markdown("<div class='section-title'>LANGUAGES</div>", unsafe_allow_html=True)
st.markdown("""
- English (Professional)
- Hindi (Professional)
- Kannada (Native)
""" )


#contact
st.markdown("""
<div class='section-title'>CONTACT</div>
<strong> Mail :  </strong> mohammedfurkhan073@gmail.com | Mobile : +91 8217405450 | Location : Hyderabad ,India
""", unsafe_allow_html=True)
