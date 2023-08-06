class dynamic(dict):
    
    def __getattr__(self, item):
        if not item in self.keys(): return None
        return self[item]

    def __dir__(self):
        return super().__dir__() + [str(k) for k in self.keys()]