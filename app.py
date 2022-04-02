#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


from textblob import TextBlob


# In[3]:


app = Flask(__name__)


# In[4]:


from flask import request, render_template

@app.route("/", methods=["GET","POST"])
def index():
        if request.method == "POST":
            text = request.form.get("text")
            print(text)
            s = TextBlob(text).sentiment
            return(render_template("index.html", result = s))
        else:
            return(render_template("index.html", result = "2"))


# In[ ]:


if __name__ =="__main__":
    app.run()


# In[ ]:




