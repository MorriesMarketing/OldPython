class JsTextBox():
        
    def fix_text_box(driver, text, element_path):
        special_symbols = ['"', '/', '<', '>', ';', ':', '=', '-', '\n', '\t','®']

        for x in special_symbols:
            text = text.replace(x,f'\{x}')
        print(text)
        driver.execute_script('arguments[0].value = "' + text + '";', element_path)