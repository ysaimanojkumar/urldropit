import logging
import handler


class URLDropit(handler.Handler):
    def get(self):
        error = self.request.get('error')
        if error is not None:
            self.render('sb_form.jinja2', active='home', error=error)
        else:
            self.render('sb_form.jinja2', active='home')

    def post(self):
        url = self.request.get('url')
        filename = self.request.get('filename')
        if url is not None and url != '':
            logging.debug('URL is %s' % url)
            if url.find('http://') != 0 and url.find('https://') != 0:
                url = 'http://' + url
                logging.debug('Modified URL is %s' % url)
            self.render('sb_download.jinja2', url=url, filename=filename)
        else:
            self.redirect('/?error=URL field should not be blank')