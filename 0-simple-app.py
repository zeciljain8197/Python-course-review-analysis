import justpy as jp

# Every justpy app will have a main object
# It is known as the quasar page. 
# This is because justpy uses the quasar framework.

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis Of Course Reviews", classes="text-h3 text-weight-bold text-center q-pa-md inset-shadow-down shadow-1 bg-positive")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis!!!", classes="text-h3")
    return wp

jp.justpy(app)
