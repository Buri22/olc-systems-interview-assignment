class HTMLElement:
    def __init__(self, tag, **kwargs):
        self.tag = tag
        self.attributes = kwargs
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        indent = '  '
        attributes = []
        for k, v in self.attributes.items():
            # Use 'classname' as a keyword argument for 'class'
            if k == 'classname': k = 'class'
            attributes.append(f'{k}="{v}"')
        attributes_str = ' ' + ' '.join(attributes) if attributes else ''
        lines = [f'<{self.tag}{attributes_str}>']
        for child in self.children:
            lines.extend([indent + line for line in str(child).splitlines()])
        lines.append(f'</{self.tag}>')

        if len(self.children) == 0: return ''.join(lines)
        else: return '\n'.join(lines)

class Input(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('input', **kwargs)

class Select(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('select', **kwargs)

class Option(HTMLElement):
    def __init__(self, text, value):
        super().__init__('option', value=value)
        self.text = text

    def __str__(self):
        return f'<{self.tag} value="{self.attributes["value"]}">{self.text}</{self.tag}>'

class A(HTMLElement):
  def __init__(self, href, **kwargs):
    super().__init__('a', href=href, **kwargs)

class Img(HTMLElement):
    def __init__(self, src, **kwargs):
        super().__init__('img', src=src, **kwargs)

class Div(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('div', **kwargs)

class Form(HTMLElement):
    def __init__(self, **kwargs):
        super().__init__('form', **kwargs)

# Example usage
form = Form(action='submit.php', classname='contact-form')

contact_div = Div(classname='contact-info', style='background-color: #f0f0f0; padding: 20px;')
contact_div.add_child(Input(type='text', name='username', placeholder='Username', value='Martin Burza'))
contact_div.add_child(Input(type='email', name='email', placeholder='Email', value='martin@burza.com'))
form.add_child(contact_div)

select = Select(name='gender')
select.add_child(Option('Male', 'male'))
select.add_child(Option('Female', 'female'))
select.add_child(Option('Other', 'other'))
select.add_child(Option('Undefined', 'undefined'))
form.add_child(select)

anchor = A('https://example.com', target='_blank')
anchor.add_child('Visit example.com')
form.add_child(anchor)

form.add_child(Img('image.jpg', alt='Image'))

print(form)