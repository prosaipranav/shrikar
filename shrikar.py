import streamlit as st 

st.set_page_config(page_title="shrikar", page_icon=":tada:", layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



st.title("Hi Everyone :wave:")
st.write("##")
st.header("This website is dedicated to  Shrikar")

with st.container():
    st.write(" --- ")
    st.header("About :rainbow[Shrikar] 🧐")
    st.write("##")
    text_column, image_column = st.columns((2,1))
    with image_column:
        st.image('shrikar_face.jpg', width=300)
    with text_column:
        st.write("Shrikar has this :red[incredible ambition to become a pilot], which speaks volumes about his drive and vision for the future. Despite the playful jabs we share, it’s clear that he’s got a unique spirit.")
                 
                 
        st.write("His physique, with that distinctive look, only adds to his individuality—he stands out in a crowd, and that’s not something everyone can say. :green[His voice might be different, but it’s a reminder that we all have our quirks, and it’s those quirks that make us memorable.] Shrikar is one of those people who,no matter what, is unapologetically himself, and that’s truly admirable. I have no doubt that he’ll soar, :blue[both literally and figuratively, as he pursues his dream of becoming a pilot.]")
    st.write("---")

with st.container():
    st.write("##")
    st.write("##")
    st.write("##")
    st.header("Kundi🍑 Explosion:bomb: jokes")
    st.write("##")
    st.subheader(":blue-background[Mr. Kundilicious ❗]")
    st.write("##")
    st.success("Shrikar , with a backside like that, you don’t walk into rooms—you reverse park into them. No wonder your jeans scream for mercy every time you sit down!")
    st.success("Shrikar, I don't know what's wider your career ambitions or the back end you're dragging around like a parade float.")
    st.success("Shrikar, with that kundi so huge, I’m surprised you don’t need an extra boarding pass just for it! Forget the pilot's seat, they might as well give you cargo space because no cockpit's fitting all that.") 
    st.success("You look like an ostrich that skipped leg day but somehow focused all its energy on building the biggest kundi known to mankind. Honestly, your butt’s the only thing that could land a plane—just sit down and boom, runway secured!")
    st.success("Bro, when the doctor saw your kundi, he had to step back and go 'dayuuuuuum!' I bet he started looking for a second opinion just to make sure it wasn’t a medical phenomenon.")
    st.success(" Forget MRIs, they probably needed a full satellite image to capture that thing. Your kundi's got more presence than you do, man—it enters a room five minutes before the rest of you!")

with st.container():
    st.write("---")
    st.header(" Explosive :bomb: poem ")
    st.write("##")
    text_column, image_column = st.columns((2,1))
    with image_column:
        st.image('baby_shrikar.jpg',use_column_width=True)
        st.caption("Baby shrikar during online classes")
    with text_column:

        st.write("""
    Shrikar, with that bakery kundi so wide,  
    You could serve up buns on the side.  
    Forget flying high in the sky,  
    Your butt's too big to even try!  

    Every step you take, the earth shakes,  
    That dump truck of yours leaves nothing in its wake.  
    Your dream’s to fly and soar real far,  
    But with that kundi, you’re your own radar!

    They say dreams need wings to rise,  
    But yours is all bunda, no surprise.  
    So, keep strutting with that load you’ve got,  
    Just know your kundi’s the only thing you’
    Just know your kundi’s the only thing you’ve taught!""")
        
    st.write("---")


with st.container():
    st.header("CLASSIC SHRIKAR BEHAVIOR ")
    image_column1, image_column2= st.columns((1,1))
    with image_column1:
        st.subheader("SHRIKAR :red[BEFORE] MORAL SCIENCE PERIOD")
        st.image('s8.jpg',use_column_width=True)
    with image_column2:
        st.subheader("SHRIKAR :red[DURING] MORAL SCIENCE PERIOD")
        st.image('s1.jpg',use_column_width=True)


