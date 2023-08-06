import uuid
from flask import Flask, jsonify, request
from werkzeug.routing import BaseConverter
from .page import Page
from .element import Element

class CallbackRegistryType:
    uuid_callback_map = {}
    callback_uuid_map = {}
    def uuid_for_callback(self, callback):
        if callback in self.callback_uuid_map:
            return self.callback_uuid_map[callback]
        else:
            cb_uuid = str(uuid.uuid1())
            self.uuid_callback_map[cb_uuid] = callback
            self.callback_uuid_map[callback] = cb_uuid
            return cb_uuid
    def make_callback(self, uuid, args):
        if uuid in self.uuid_callback_map:
            return self.uuid_callback_map[uuid](*args)
        else:
            # TODO: Return an error to the frontend
            return None

callbackRegistry = CallbackRegistryType()

class PurePathConverter(BaseConverter):
    regex = r'[a-zA-Z0-9\/]+'

class MenuItem(Element):
    """Represents a menu item
    
        Args:
            name (str): the title of the menu
            url (str, optional): the url the menu will navigate to. Defaults to ''.
            icon (str, optional): the icon of the menu. See https://ant.design/components/icon/. Defaults to None.
            children (list, optional): set this if the menu has a sub-menu. Defaults to [].
    """
    def __init__(self, name, url='', icon=None, children=[]):
        super().__init__('MenuItem', name=name, path=url, icon=icon, component='./index', children=children)
        self.components_fields = ['children']


class AdminApp:
    """Create an AdminUI App"""
    def __init__(self):
        self.app = Flask(__name__, static_url_path='/')
        self.app.url_map.converters['purePath'] = PurePathConverter 
        self.pages = {}
        self.menu = []

    def page(self, url, name):
        """Register a AdminUI Page
        
        Args:
            url (str): the url of the page. e.g. '/', '/detail', '/user/new'.
                You may have at most 2 levels. 
            name (str): the title of the page
        
        Example: 
            @app.page('/detail', 'Detail Page')
            def detail_page(arg): 
                # additional url parameters will be passed here
                # if you declare '/details' and user visits '/details/2', 2 will be passed here
                return [ ...Elements of the page... ]
        """
        def decorator(func):
            self.pages[url] = Page(url, name, builder=func)
        return decorator
    
    def set_menu(self, menu):
        """Setup the menu of the website. If not called, no menu will be shown
        
        Args:
            menu (MenuItem[]): A list of MenuItem objects.
        """
        self.menu = menu
    
    def serve_page(self, url=''):
        """!!! Private method, don't call. Serve the page specifications
        
        Args:
            url (str, optional): The url pattern of the page.
        """
        url_parts = url.split('/')
        full_url = '/'+url
        base_url = '/'+url_parts[0]
        if full_url in self.pages:
            return jsonify(self.pages[full_url].as_list())
        elif base_url in self.pages and len(url_parts)>1:
            return jsonify(self.pages[base_url].as_list(url_parts[1]))
        else:
            return 'page not registered'

    def handle_page_action(self):
        """!!! Private method, don't call. Manage user actions like button clicks"""
        msg = request.get_json()
        if 'args' not in msg:
            msg['args'] = []
        response = callbackRegistry.make_callback(msg['cb_uuid'], msg['args'])
        if response is not None:
            return response.as_dict()
        else:
            return 'error'

    def serve_menu(self):
        """!!! Private method, don't call. Serve the menu to the frontend"""
        return jsonify({
            'menu': [x.as_dict() for x in self.menu]
        })

    def serve_root(self, path=''):
        """!!! Private method, don't call. Serve the index.html"""
        return self.app.send_static_file('index.html')
    
    def mock_current_user(self):
        """!!! Private method, don't call. Will be removed after implementing the login system"""
        return jsonify({
            'name': 'Serati Ma'
        })

    def run(self):
        """run the AdminUI App"""
        # self.app.route('/api/page_layout/<url>')(self.serve_page)
        self.app.route('/api/page_layout/<purePath:url>/')(self.serve_page)
        self.app.route('/api/page_layout/')(self.serve_page)
        self.app.route('/api/currentUser')(self.mock_current_user)
        self.app.route('/api/main_menu')(self.serve_menu)
        self.app.route('/api/page_action', methods=['POST'])(self.handle_page_action)
        self.app.route('/')(self.serve_root)
        self.app.route('/<purePath:path>/')(self.serve_root)
        self.app.run()