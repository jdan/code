import pygtk
import gtk

class HelloWorld:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(800,600)
        self.window.connect("destroy", self.destroy)

        self.wv = WebView()
        self.wv.load_uri('http://google.com')
        self.wv.show()
        self.window.add(wv)

        self.button = gtk.Button("Close")
        self.button.connect("clicked", self.destroy, None)

        self.window.add(self.button)
        self.button.show()
        self.window.show()

    def main(self):
        gtk.main()

    def destroy(self, widget, data=None):
        gtk.main_quit()

hello = HelloWorld()
hello.main()
