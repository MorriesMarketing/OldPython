import dominate
from dominate.tags import *
from dominate.util import raw

class Page(object):
    def __init__(self):
        self.Email_Body = dominate.document(title=f'Walser Ignite Specials')

    def doc(self):
        with self.Email_Body.head:
            style("""

            """)
        with self.Email_Body:
            with div(cls="greeting", style=f'margin: 0px 0px 20px 0px;'):
                div('Good Morning Walser Management Team,')
            with div(cls='intro'):
                div('This explains what the email is for')
            with div(cls='navigation'):
                div('This is to explain how to operate the Excel Sheet')
            with div(cls='closing'):
                div('say goodbye')
            with div(cls='Signtature', style=f'margin: 20px 0px 0px 0px;'):
                div('Have a great day!')
                div('Matt Muhlenkort')
                div('SEO/SEM Analyst')
                div('612-275-3644')

        return self.Email_Body