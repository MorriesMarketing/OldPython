class my_class(object):
    
    def __init__(self, driver, text, element_path):
    
        self.driver = driver
        self.text = text
        self.element_path = element_path
    
    def fix_text_box(self):
        special_symbols = ['"', '/', '<', '>', ';', ':', '=', '-', '\n', '\t']

        for x in special_symbols:
            self.text = self.text.replace(x,f'\{x}')
        print(self.text)
        self.driver.execute_script('arguments[0].value = "' + self.text + '";', self.element_path)




