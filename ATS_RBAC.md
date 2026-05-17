# ATS Role-Based Access Control Design
 
---
 
## 1. Roles
 
| Role | Description |
|---|---|
| **Admin** | The system owner. Manages users and the platform. Does not participate in the hiring process. |
| **Recruiter** | In charge of the hiring process. Manages job postings, candidate communications, and moves candidates through the hiring process. |
| **Hiring Manager** | Looks over the process. Focuses on evaluating candidates, submitting feedback, and approving job requisitions. |
| **Candidate** | One who applies for a job. An external user. Access is limited to their own application, profile, and any offers. |
 
---
 
## 2. Permissions
 
| Permission | Description |
|---|---|
| `ROLE_MANAGE` | Add or remove employees from the ATS and assign their roles. |
| `AUDIT_LOG_VIEW` | View a history of who accessed or changed data in the system. |
| `JOB_CREATE` | Draft a new job opening. |
| `JOB_APPROVE` | Approve the job opening to be published. |
| `JOB_PUBLISH` | Push a job to the company career site or job boards. |
| `JOB_EDIT_DESC` | Modify the info or text of a job posting. |
| `CAND_VIEW_CONTACT` | View a candidate's personal contact information such as phone number and email address. |
| `CAND_VIEW_ALL` | Search and view all candidates across every job posting in the system. |
| `CAND_MOVE_STAGE` | Change a candidate's status through hiring stages. |
| `CAND_REJECT` | Send a rejection notice to the candidate. |
| `NOTE_ADD` | Post notes about a candidate linked to their profile. |
| `FEEDBACK_SUBMIT` | Some form of feedback that can be given to any user. |
| `SCHED_INTERVIEW` | Access calendars to book interviews between candidates and interviewers. |
| `MSG_SEND` | Send emails to candidates directly through the ATS platform. |
| `OFFER_CREATE` | Generate a formal offer letter. |
| `APP_STATUS_READ` | View the current status of your own application. |
| `APP_WITHDRAW` | Remove oneself from consideration for a role. |
| `PROFILE_EDIT` | Update your own personal details, contact information, and preferences. |
| `DOCUMENT_MANAGE` | Upload, replace, or remove your own resumes, cover letters, and portfolios. |
| `OFFER_VIEW` | Access to view candidate offers. |
 
---
 
## 3. Role-Permission Matrix
 
| Permission | Admin | Recruiter | Hiring Manager | Candidate |
|---|:---:|:---:|:---:|:---:|
| `ROLE_MANAGE` | ✅ | | | |
| `AUDIT_LOG_VIEW` | ✅ | | | |
| `JOB_CREATE` | ✅ | ✅ | ✅ | |
| `JOB_APPROVE` | ✅ | | ✅ | |
| `JOB_PUBLISH` | ✅ | ✅ | | |
| `JOB_EDIT_DESC` | ✅ | ✅ | ✅ | |
| `CAND_VIEW_CONTACT` | ✅ | ✅ | ✅ | |
| `CAND_VIEW_ALL` | ✅ | ✅ | ✅ | |
| `CAND_MOVE_STAGE` | ✅ | ✅ | | |
| `CAND_REJECT` | ✅ | ✅ | | |
| `NOTE_ADD` | ✅ | ✅ | ✅ | |
| `FEEDBACK_SUBMIT` | ✅ | ✅ | ✅ | |
| `SCHED_INTERVIEW` | ✅ | ✅ | | |
| `MSG_SEND` | ✅ | ✅ | | |
| `OFFER_CREATE` | ✅ | ✅ | | |
| `APP_STATUS_READ` | | | | ✅ |
| `APP_WITHDRAW` | | | | ✅ |
| `PROFILE_EDIT` | | | | ✅ |
| `DOCUMENT_MANAGE` | | | | ✅ |
| `OFFER_VIEW` | | | | ✅ |
 
---
 
## 4. Rationale
 
- Stayed with 4 roles for simplicity. Recruiter, Hiring Manager, and Candidate are the most important roles in an ATS. Added admin so someone had deeper access to the system.
- The hiring manager does not control candidate pipeline stages. The recruiter is there to handle the process of hiring, while the hiring manager is there to observe it and make decisions. This ensures separation of duties.
- The recruiter does not have access to `JOB_APPROVE` because it is not their role to authorize a job on a company's behalf. More separation of duties. The person doing the work shouldn't also be the one approving the budget for it.
---
 
## 5. Decided Not Necessary
 
- Outside/contract recruiters. For simplicity, just assume all recruiters are internal.
- Permissions that change based on the status or completion of other permissions. Needlessly complex.
- A separate interviewer role. The hiring manager is the interviewer.
- No login system. That is a part of a different system, not ATS.
---
 
## 6. Would Add With More Time
 
- More roles, like a Budget Approver role. Separates budget approval from the Hiring Manager.
- Notification system. Alerting the right people when a candidate moves stages or accepts an offer, etc.
- Somehow to show that each role has a different dashboard view upon login.
---
 
## 7. Weak Areas
 
- Admin is very powerful. A real system would likely have different Admins, like IT Admin or HR Admin, to prevent one person from having access to the entire system.
- No read-only role.
- The model doesn't account for internal hires. What if a recruiter or a hiring manager is also a candidate for a job?
