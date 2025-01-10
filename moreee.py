# #!/usr/bin/env python
# # coding: utf-8

# import pandas as pd
# import numpy as np
# import streamlit as st
# import plotly.express as px


# import os
# #print(os.getcwd())

# df = pd.read_csv("/Users/mofeogunsola/Documents/dental.csv", sep=";") 

# #from IPython.display import display

# #df.head(10)

# # In[4]:


# df.rename(columns={"EXAM_USER_CNT": "Benefits Spent", "EXAM_SVC_CNT": "Benefits Allocated"}, inplace=True)

# #df.columns
# # In[5]

# df.isna().sum()

# # In[6]:

# columns_keep = ['Benefits Spent', 'Benefits Allocated', 'CALENDAR_YEAR', 'PROVIDER_TYPE']
# df=df[columns_keep]

# #df.head()


# # In[7]:


# #print('PROVIDER_TYPE' in df.columns)  # Should return True if it exists


# # In[8]:


# # Apply the transformation to capitalize only the first letter of each value in PROVIDERTYPE
# df['PROVIDER_TYPE'] = df['PROVIDER_TYPE'].apply(lambda x: x.lower().capitalize())

# # Check the updated column
# #print(df['PROVIDER_TYPE'].head())



# # In[9]:


# #removing the _ 

# df.columns = df.columns.str.replace('_', ' ')

# #print(df.columns)


# # In[10]:


# df


# # In[11]:


# # Add utilization rate for quarterly data
# df["Utilization Rate%"] = (df["Benefits Spent"] / df["Benefits Allocated"]) * 100
# df["Utilization Rate%"] = df["Utilization Rate%"].round(1)

#  # Preview the first few rows
# #print(df[["Benefits Spent", "Benefits Allocated", "Utilization Rate%"]].head(30))
# #print(df)


# # In[12]:


# #dropping na values from the columns 

# df.dropna(subset=['Utilization Rate%', 'Benefits Allocated', 'Benefits Spent' ], inplace=True)
# #print(df.head(20))


# # In[18]:


# # Add Benefit ID column with random numbers (for example between 100000 and 999999)

# df['Benefit ID'] = np.random.randint(100000, 999999, size=len(df))

# # Print the updated dataframe
# #print(df)


# # In[ ]:




# #-----------------------------------------------------------------------------------------------
# # In[13]:


# import streamlit as st
# import pandas as pd
# import plotly.express as px


# # In[24]:


# # Display company logo in sidebar
# #st.sidebar.image("soda.png")

# st.sidebar.image("/Users/mofeogunsola/Documents/soda.png")
                 
# #use_container_width=True)

# # Sidebar Navigation for Graph Selection
# st.sidebar.title("Dashboard Navigation")

# option = st.sidebar.radio(
#    "Select a graph:", 
#     ["Utilization Rate by Person", 
#     "100% Stacked Bar Chart"])

# # Page Title
# st.title("Benefits Utilization")
# st.subheader("Comparison of Amount Spent and Allocated")
# #-------------------------------------------------------------------------------------------


# if option == "Utilization Rate by Person":
#     st.header("Utilization Rate by Person")

#     fig1 = px.bar(
#         df,
#         x=df.index.astype(str),  # Subscriber index on X-Axis
#         y="Utilization Rate%",
#         text="Utilization Rate%",
#         animation_frame="CALENDAR YEAR",
#         title="Utilization Rate by Person, per Year",
#         labels={"x": "BenefitID", "Utilization Rate%": "Utilization Rate (%)"},
#         orientation="v",  # Vertical bar chart
#         color="Utilization Rate%",  # Add color gradient
#         color_continuous_scale="Viridis",  # Use a color scheme
#         height=400,
#     )

#     # Update layout for cleaner display
#     fig1.update_traces(texttemplate='%{text}%', textposition="outside")
#     fig1.update_layout(
#         xaxis=dict(title="BenefitID"),
#         yaxis=dict(title="Utilization Rate (%)")
#     )
#     st.plotly_chart(fig1)

# st.write(df.head(10))



# # In[ ]:


# elif option == "100% Stacked Bar Chart":
#     st.header("100% Stacked Bar Chart")

#     # Calculate "Amount Remaining" column
#     df["Amount Remaining"] = df["Benefits Allocated"] - df["Benefits Spent"]
    
#     # Create stacked dataframe with "Benefits Spent" and "Amount Remaining"
#     stacked_df = df[["Benefits Spent", "Amount Remaining"]]  # No subtraction operator needed here

#     # Create a bar plot
#     fig2 = px.bar(
#         stacked_df,
#         barmode="relative",
#         orientation="v",
#         height=400,
#         labels={"value": "Benefits Allocated", "variable": ""},
#         title="100% Stacked Bar Chart",
#     )

#     fig2.update_layout(
#         xaxis=dict(title="BenefitID"),
#         yaxis=dict(title="Benefit Amount Allocated (%)"),
#     )

#     st.plotly_chart(fig2)


#     st.write(df.head(10))

# In[ ]:


#get_ipython().system('jupyter nbconvert --to script moreee.ipynb')


# In[ ]:

#-----------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df = pd.read_csv("/Users/mofeogunsola/Documents/dental.csv", sep=";") 

# Rename columns
df.rename(columns={"EXAM_USER_CNT": "Benefits Spent", "EXAM_SVC_CNT": "Benefits Allocated"}, inplace=True)
#df.columns

#df.isna().sum()

columns_keep = ['Benefits Spent', 'Benefits Allocated', 'CALENDAR_YEAR', 'PROVIDER_TYPE']
df = df[columns_keep]

# Process PROVIDER_TYPE
df['PROVIDER_TYPE'] = df['PROVIDER_TYPE'].apply(lambda x: x.lower().capitalize())

# Remove underscores from columns
df.columns = df.columns.str.replace('_', ' ')

# Add Utilization Rate
df["Utilization Rate%"] = (df["Benefits Spent"] / df["Benefits Allocated"]) * 100
df["Utilization Rate%"] = df["Utilization Rate%"].round(1)

# Dropping Na values from selected columns
df.dropna(subset=['Utilization Rate%', 'Benefits Allocated', 'Benefits Spent'], inplace=True)

# Add random Benefit ID
df['Benefit ID'] = np.random.randint(100000, 999999, size=len(df))

#---------------------------------------------------------------------------------------
# Now, use Streamlit to show the dashboard instead of printing the data directly

# Sidebar
st.sidebar.image("/Users/mofeogunsola/Documents/soda.png")

st.sidebar.title("Dashboard Navigation")
option = st.sidebar.radio(
   "Select option:", 
    ["Utilization Rate by Person", "100% Stacked Bar Chart", "Top 20 Rows"])

st.title("Benefits Utilization")
st.subheader("Comparison of Amount Spent and Allocated")

if option == "Utilization Rate by Person":
    st.header("Utilization Rate by Person - Bar Chart")

    fig1 = px.bar(
        df,
        x=df.index.astype(str),
        y="Utilization Rate%",
        text="Utilization Rate%",
        animation_frame= "CALENDAR YEAR",
        #title="Utilization Rate by Person, per Year",
        labels={"x": "BenefitID", "Utilization Rate%": "Utilization Rate (%)"},
        orientation="v",
        color="Utilization Rate%",
        color_continuous_scale="Viridis",
        height=400,
    )

    fig1.update_traces(texttemplate='%{text}%', textposition="outside")
    fig1.update_layout(
        xaxis=dict(title="BenefitID"),
        yaxis=dict(title="Utilization Rate (%)")
    )
    st.plotly_chart(fig1)

elif option == "100% Stacked Bar Chart":
    st.header("100% Stacked Bar Chart")

    df["Amount Remaining"] = df["Benefits Allocated"] - df["Benefits Spent"]
    stacked_df = df[["Benefits Spent", "Amount Remaining"]]

    fig2 = px.bar(
        stacked_df,
        barmode="relative",
        orientation="v",
        height=400,
        labels={"value": "Benefits Allocated", "variable": ""},
        #title="100% Stacked Bar Chart",
    )

    fig2.update_layout(
        xaxis=dict(title="BenefitID"),
        yaxis=dict(title="Benefit Amount Allocated (%)"),
    )

    st.plotly_chart(fig2)

# 3. Third page (Top 20 Rows)
elif option == "Top 20 Rows":
    st.header("Data Table")

    # Displaying the top 20 rows of the DataFrame
    st.write(df.head(20))


