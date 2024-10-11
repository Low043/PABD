from src.services.builder import *
from src.views import *
import webview

class NFTStore:
    def __init__(self):
        self.database = Builder().connect()#Connect to database (create if not exists)
        self.user = None#Connected User

        #View classes
        self.login = LoginView(self)
        self.register = RegisterView()
        self.feed = FeedView()
        self.cart = CartView()

#Init Login View
window = webview.create_window("NFTStore", "src/views/login/index.html",js_api=NFTStore(),width=600,height=600,min_size=(600,600))
webview.start()