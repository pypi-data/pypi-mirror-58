# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['textify']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'textify',
    'version': '0.0.1',
    'description': 'A Simple Text Cleaning Package  For cleaning text during NLP',
    'long_description': '# textify\nA Simple Text Cleaning and Normalization Package For NLP\n\n\n#### Installation\n```bash\npip install textify\n```\n\n### Usage\n#### Clean Text\n+ Clean text by removing emails,numbers,etc\n```python\n>>> from textify import TextCleaner\n>>> docx = TextCleaner()\n>>> docx.text = "your text goes here"\n>>> docx.clean_text()\n```\n\n#### Remove Emails,Numbers,Phone Numbers \n```python\n>>> docx.remove_emails()\n>>> docx.remove_numbers()\n>>> docx.remove_phone_numbers()\n```\n\n\n#### Remove Special Characters\n```python\n>>> docx.remove_special_characters()\n```\n\n#### Replace Emails,Numbers,Phone Numbers\n```python\n>>> docx.replace_emails()\n>>> docx.replace_numbers()\n>>> docx.replace_phone_numbers()\n```\n\n### Using TextExtractor\n+ To Extract emails,phone numbers,numbers from text\n```python\n>>> from textify import TextExtractor\n>>> docx = TextExtractor()\n>>> docx.text = "your text with example@gmail.com goes here"\n>>> docx.extract_emails()\n```\n\n#### By \n+ Jesse E.Agbe(JCharis)\n+ Jesus Saves @JCharisTech\n\n\n#### NB\n+ Contributions Are Welcomed\n+ Notice a bug, please let us know.\n+ Thanks A lot\n',
    'author': 'Jesse E.Agbe(JCharis)',
    'author_email': 'jcharistech@gmail.com',
    'url': 'https://github.com/Jcharis/textify',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
