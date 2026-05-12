# Skill Taxonomies – Career Intelligence Platform

This document defines the skill taxonomies for the three target domains in v1. Each skill list is organized by category and serves as the foundation for skill extraction and recommendations.

**How to use this document:**
1. Review each domain carefully
2. Get feedback from domain experts (ask classmates/professionals in each field)
3. Refine and expand based on feedback
4. Convert to Python code (`data/taxonomies.py`) once finalized

---

## **Management Domain**

### **Leadership & People Management**
- Leadership
- Team Management
- Delegation
- Mentoring
- Coaching
- Conflict Resolution
- Change Management
- Organizational Development

### **Communication & Stakeholder Management**
- Presentation Skills
- Stakeholder Management
- Written Communication
- Active Listening
- Interpersonal Skills
- Public Speaking
- Executive Communication
- Cross-functional Communication

### **Project & Process Management**
- Project Management
- Planning & Scheduling
- Organization & Prioritization
- Process Improvement
- Agile/Scrum
- Risk Management
- Resource Allocation
- Timeline Management

### **Soft Skills & Mindsets**
- Problem Solving
- Decision Making
- Critical Thinking
- Emotional Intelligence
- Adaptability
- Creativity
- Initiative
- Accountability

### **Tools & Platforms**
- Microsoft Office (Word, PowerPoint, Outlook)
- Excel (Dashboards, Reporting)
- Asana
- Monday.com
- Jira
- Slack
- Microsoft Teams
- Google Workspace
- Confluence

### **Domain-Specific Skills**
- Business Acumen
- Strategic Thinking
- Financial Literacy
- Customer Focus
- Sales Management
- Quality Management

---

## **Finance Domain**

### **Excel & Spreadsheets**
- Excel (General)
- Pivot Tables
- VLOOKUP / INDEX-MATCH
- Advanced Formulas
- Macros & VBA
- Data Cleaning & Validation
- Excel Dashboards & Visualization

### **Accounting & Financial Fundamentals**
- Financial Accounting
- Managerial Accounting
- Bookkeeping
- General Ledger
- Accounts Payable/Receivable
- GAAP (Generally Accepted Accounting Principles)
- Reconciliation

### **Financial Analysis & Modeling**
- Financial Analysis
- Financial Modeling
- Forecasting & Projections
- Budgeting & Budget Analysis
- Valuation Models
- Scenario Analysis
- Variance Analysis

### **Financial Reporting & Interpretation**
- Financial Reporting
- Income Statement Analysis
- Balance Sheet Analysis
- Cash Flow Analysis
- Ratio Analysis
- Trend Analysis
- Financial Statement Interpretation

### **Data Tools & Platforms**
- Power BI
- Tableau
- SQL
- Python (Data Analysis)
- SAP
- QuickBooks
- Xero
- Tableau Public
- Google Analytics

### **Domain Knowledge & Business Acumen**
- Business Acumen
- ROI Analysis
- Profitability Analysis
- Cost-Benefit Analysis
- Risk Assessment & Mitigation
- Compliance & Regulatory Knowledge
- Internal Controls
- Audit Basics

---

## **Business Analytics Domain**

### **SQL & Databases**
- SQL (General)
- SELECT & WHERE Clauses
- Joins (INNER, LEFT, RIGHT, FULL)
- Aggregations & GROUP BY
- Subqueries & CTEs (Common Table Expressions)
- Database Design & Normalization
- Query Optimization
- Data Modeling

### **Python & Data Manipulation**
- Python (General)
- Pandas
- NumPy
- Data Cleaning & Preprocessing
- Data Transformation
- Data Structures (lists, dicts, sets)
- File I/O (CSV, JSON, Excel)
- Jupyter Notebooks

### **Data Visualization & Storytelling**
- Tableau
- Power BI
- Data Visualization Best Practices
- Dashboard Design
- Data Storytelling
- Presenting Insights
- Visual Design Principles
- matplotlib / Plotly (Python visualization libraries)

### **Statistics & Hypothesis Testing**
- Statistical Analysis
- Hypothesis Testing
- A/B Testing & Experimentation
- Probability & Distribution Theory
- Regression Analysis (Linear, Logistic)
- Correlation & Causation
- Statistical Significance
- Descriptive Statistics

### **Excel & Analytical Tools**
- Excel (Advanced)
- Pivot Tables (Advanced)
- Statistical Functions
- Data Analysis Toolpak
- Scenario Analysis
- What-If Analysis
- Data Visualization in Excel

### **Domain Knowledge & Business Acumen**
- Business Acumen
- KPI Definition & Tracking
- Metrics Definition
- Customer Insights & Analytics
- Product Analytics
- User Behavior Analysis
- Data-Driven Decision Making
- Business Problem Solving

---

## **Template for Python Implementation**

Once you've refined these taxonomies, convert them to Python code like this:

```python
# data/taxonomies.py

SKILL_TAXONOMIES = {
    "management": {
        "leadership": [
            "Leadership",
            "Team Management",
            "Delegation",
            "Mentoring",
            "Coaching",
            "Conflict Resolution",
            "Change Management",
            "Organizational Development",
        ],
        "communication": [
            "Presentation Skills",
            "Stakeholder Management",
            "Written Communication",
            "Active Listening",
            "Interpersonal Skills",
            "Public Speaking",
            "Executive Communication",
            "Cross-functional Communication",
        ],
        # ... other categories
    },
    "finance": {
        "excel": [
            "Excel",
            "Pivot Tables",
            "VLOOKUP",
            # ...
        ],
        # ... other categories
    },
    "business_analytics": {
        "sql": [
            "SQL",
            "SELECT",
            # ...
        ],
        # ... other categories
    },
}
```

---

## **Feedback Form** (For Domain Experts)

Share this with 1-2 people in each field and ask:

**Management:** "If you were hiring for a management role, what skills would you look for that I'm missing from this list?"

**Finance:** "If you were hiring for a finance/accounting role, what skills would you look for that I'm missing from this list?"

**Business Analytics:** "If you were hiring for a data/analytics role, what skills would you look for that I'm missing from this list?"

**Template:**
```
Domain: [Management/Finance/BA]
Feedback:
- Missing skills: [list]
- Skills to remove: [list]
- Skills to clarify: [list]
- Other suggestions: [list]
```

---

## **Refinement Checklist**

- [ ] Management taxonomy reviewed by a manager or team lead
- [ ] Finance taxonomy reviewed by a finance professional/accountant
- [ ] Business Analytics taxonomy reviewed by a data analyst
- [ ] No duplicates across categories
- [ ] All skills are "extractable" (detectable in a CV or job description)
- [ ] Skills are specific enough (not too vague like "Technical Skills")
- [ ] Expanded to 40-60+ skills per domain
- [ ] Converted to Python code (`data/taxonomies.py`)
- [ ] Ready for backend development

---

**Version:** 1.0  
**Status:** Ready for feedback and refinement
