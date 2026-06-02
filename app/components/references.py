import streamlit as st


def show_references(topic):

    st.markdown("## Trusted References")

    topic_query = topic.replace(" ", "+")

    references = {

        "Wikipedia":
        f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}",

        "GeeksforGeeks":
        f"https://www.google.com/search?q=GeeksforGeeks+{topic_query}",

        "Khan Academy":
        f"https://www.google.com/search?q=Khan+Academy+{topic_query}",

        "TutorialsPoint":
        f"https://www.google.com/search?q=TutorialsPoint+{topic_query}",

        "IBM Documentation":
        f"https://www.google.com/search?q=IBM+{topic_query}"
    }

    for name, link in references.items():

        st.markdown(f"- [{name}]({link})")