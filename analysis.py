import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# setting chart style
sns.set_style("whitegrid")

# reading dataset
df = pd.read_excel(
    "Financial Dataset Task.xlsx",
    sheet_name="Financial Dataset Task"
)

# checking dataset
print(df.head())
print(df.info())

# basic KPI calculations
total_respondents = len(df)

bank_holders = (
    df['Has a Bank account'] == 'Yes'
).sum()

non_holders = (
    df['Has a Bank account'] == 'No'
).sum()

countries = df['country'].nunique()

# bank account analysis
bank_counts = df['Has a Bank account'].value_counts()

print(bank_counts)

plt.figure(figsize=(8,5))

bank_counts.plot(
    kind='bar',
    color=['steelblue', 'orange']
)

plt.title("Bank Account Distribution")
plt.xlabel("Bank Account")
plt.ylabel("Count")

plt.savefig("bank_distribution.png", dpi=300)

plt.show()

# percentage chart
plt.figure(figsize=(6,6))

bank_counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=['steelblue', 'orange']
)

plt.title("Bank Account Percentage")
plt.ylabel("")

plt.savefig("bank_account_percentage.png", dpi=300)

plt.show()

# country analysis
country_data = df.groupby('country')[
    'Has a Bank account'
].count()

print(country_data)

plt.figure(figsize=(8,5))

country_data.plot(
    kind='bar',
    color='green'
)

plt.title("Country-wise Analysis")
plt.xlabel("Country")
plt.ylabel("Count")

plt.savefig("country_analysis.png", dpi=300)

plt.show()

# gender analysis
gender_data = df.groupby(
    'gender_of_respondent'
)['Has a Bank account'].count()

print(gender_data)

plt.figure(figsize=(8,5))

gender_data.plot(
    kind='bar',
    color=['purple', 'orange']
)

plt.title("Gender Analysis")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.savefig("gender_analysis.png", dpi=300)

plt.show()

# age group analysis
age_data = df.groupby(
    'Age_Group'
)['Has a Bank account'].count()

print(age_data)

plt.figure(figsize=(8,5))

age_data.plot(
    kind='bar',
    color=['blue', 'green', 'orange', 'red']
)

plt.title("Age Group Analysis")
plt.xlabel("Age Group")
plt.ylabel("Count")

plt.xticks(rotation=0)

plt.savefig("age_group_analysis.png", dpi=300)

plt.show()

# rural and urban analysis
location_data = df.groupby(
    'Type of Location'
)['Has a Bank account'].count()

print(location_data)

plt.figure(figsize=(8,5))

location_data.plot(
    kind='bar',
    color=['teal', 'darkblue']
)

plt.title("Rural vs Urban Analysis")
plt.xlabel("Location")
plt.ylabel("Count")

plt.xticks(rotation=0)

plt.savefig("location_analysis.png", dpi=300)

plt.show()

# seaborn country chart
plt.figure(figsize=(10,6))

sns.countplot(
    x='country',
    hue='Has a Bank account',
    data=df,
    palette='Set2'
)

plt.title("Country-wise Financial Inclusion")
plt.xlabel("Country")
plt.ylabel("Count")

plt.savefig(
    "seaborn_country_analysis.png",
    dpi=300
)

plt.show()

# seaborn gender chart
plt.figure(figsize=(8,5))

sns.countplot(
    x='gender_of_respondent',
    hue='Has a Bank account',
    data=df,
    palette='Set1'
)

plt.title("Gender-wise Financial Inclusion")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.savefig(
    "seaborn_gender_analysis.png",
    dpi=300
)

plt.show()

# dashboard creation
fig, axes = plt.subplots(
    2,
    2,
    figsize=(16,10)
)

fig.suptitle(
    "Financial Inclusion Dashboard",
    fontsize=20,
    fontweight='bold'
)

# KPI boxes
fig.text(
    0.10,
    0.90,
    f"Total Respondents\n{total_respondents}",
    bbox=dict(facecolor='skyblue')
)

fig.text(
    0.33,
    0.90,
    f"Bank Holders\n{bank_holders}",
    bbox=dict(facecolor='lightgreen')
)

fig.text(
    0.56,
    0.90,
    f"Non Holders\n{non_holders}",
    bbox=dict(facecolor='salmon')
)

fig.text(
    0.79,
    0.90,
    f"Countries\n{countries}",
    bbox=dict(facecolor='orange')
)

# charts inside dashboard
bank_counts.plot(
    kind='bar',
    ax=axes[0,0],
    color=['steelblue', 'orange']
)

axes[0,0].set_title(
    "Bank Account Distribution"
)

country_data.plot(
    kind='bar',
    ax=axes[0,1],
    color='green'
)

axes[0,1].set_title(
    "Country Analysis"
)

gender_data.plot(
    kind='bar',
    ax=axes[1,0],
    color=['purple', 'orange']
)

axes[1,0].set_title(
    "Gender Analysis"
)

age_data.plot(
    kind='bar',
    ax=axes[1,1],
    color=['blue', 'green', 'orange', 'red']
)

axes[1,1].set_title(
    "Age Group Analysis"
)

plt.tight_layout(rect=[0,0,1,0.82])

plt.savefig(
    "financial_dashboard.png",
    dpi=300
)

plt.savefig(
    "financial_dashboard.pdf"
)

plt.show()

# final insights
print("\nKey Insights")
print("Total Respondents:", total_respondents)
print("Bank Holders:", bank_holders)
print("Non Holders:", non_holders)
print("Countries Covered:", countries)
print("Adults have the highest financial inclusion")
print("Rural areas show lower banking access")
print("Financial inclusion differs across countries")