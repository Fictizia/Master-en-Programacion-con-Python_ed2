class Name():

    def parse(self, response):
        self._extract_data(response)
    
    def _extract_data(self, response, page=0):
        response.lalalala()
        response.lalalal(2)
        self._next_page(page)
    
    def _next_page(self, page):
        if page < 38:
            new_response = self._extract_the_url_response()
            new_page = page + 1
            self._extract_data(new_response, new_page)
    
    def _extract_the_url_response(self):
        # scrappy things
        return 'scarppy things'
    