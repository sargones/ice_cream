import streamlit as st
import pandas as pd
# from main import artist_df

st.set_page_config(
    page_title='Sweet talks over ice cream', page_icon='🍦')  # 🍦 👋

st.title("🎙️'Sweet talks over ice cream'🎙️")
st.subheader('with Tam and Plam')
spaces = ("""





        """)


st.text(spaces)

st.image('ice_cream.png')
st.text(spaces)

st.text(""" 
        Welcome to "Sweet talks over ice cream" a podcast where we dive deep into the multifaceted aspects of our lives, from the professional to the personal, and everything in between. 
        where we dive into one of humanity’s sweetest companions—ice cream. From ancient chilled desserts to todays colorful scoops, ice cream has been with us through celebrations, heartbreaks, and lazy Sunday afternoons. 
        It’s more than just a treat; it’s a conversation starter, a comfort, and often the excuse we need to gather with friends. In this episode, we explore how ice cream became a cultural symbol of joy and connection around the world. 
        So grab your favorite flavor and let us melt into the story.         
        Join us as we embark on this journey of discovery and connection, and perhaps, find a little bit of ourselves along the way.
        """)

st.text(spaces)
st.divider()
st.text(spaces)
st.text(""" 
        Of course we cannot start with out topic but the Ice Cream itself.
        Ice cream has been such a great companion in human interaction and social bonding:
         - Universal Appeal – Ice cream transcends age, culture, and language. Almost everyone has a favorite flavor, making it an easy, inclusive way to connect with others.
         - Built for Sharing – Whether it’s scooping from the same tub, trying each other’s cones, or ordering a sundae for two, ice cream invites sharing and conversation.
         - Breaks the Ice – Offering someone ice cream is a low-pressure, friendly gesture that naturally leads to small talk, laughter, and deeper conversations.
         - Celebratory Symbol – From birthdays and graduations to first dates and reunions, ice cream often marks special moments and creates positive shared memories.
         - Comfort in a Cone – In tough times, ice cream becomes a silent companion—its nostalgic and soothing nature helps people open up emotionally or just feel a little better.
         - Playful and Nostalgic – Ice cream brings back memories of childhood, fun, and freedom, which often lightens the mood and makes people feel more relaxed and open.
         - Cultural Connector – Across the world, different cultures have unique ice cream traditions. Trying or talking about them is a delicious gateway to learning about others.
        """)
st.divider()
st.text(spaces)
# st.image('Evolution.png')
# st.divider()
# st.text(spaces)

##############
# Popularity

st.subheader("Best Ice Cream rating:")

url_details = 'https://raw.githubusercontent.com/sargones/ice_cream/refs/heads/main/products.csv?token=GHSAT0AAAAAADIDTRB4RYYGR4UYTVJGAMLC2EGR6PQ'
icecream_df = pd.read_csv(url_details)
popularity_df = icecream_df[['name', 'rating', 'ingredients']]
min_pop = icecream_df['rating'].min()
max_pop = icecream_df['rating'].max()


low_pop, high_pop = st.slider("Select a range", min_pop, max_pop, (3, 4))

# st.dataframe(popularity_df[(popularity_df['rating'] >= low_pop) & (popularity_df['rating'] <= high_pop)],
#              hide_index=True, width=400)

st.divider()
##############

st.divider()
st.text(spaces)


# st.audio('ice_cream.wav', format="audio/wav", start_time=0, sample_rate=None,
# end_time=None, loop=False, autoplay=False)

st.divider()
st.text(spaces)

st.write("Thanks for stopping by, hope you'll enjoy it! 🤖 ")
st.write("In case you liked it or the long calls - feel free to subscibe to ")
st.write("🎙️'Sweet talks over ice creamt'🎙️")
st.write("🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦🍦")
# st.write("hosted by Tam and Plam.")
