# TextAnalyticsLab/TextLab (Text Analytics Toolkit for Python)
## Current release: TextLab [v0.1.5]

<img src="" height="200">

## TextAnalyticsLab (TextLab) - a collection of Text Analytics tools for Python.

<img src="" height="200">

## Introduction
'TextAnalyticsLab'/'TextLab' is a Python package providing a set of text analytics tools 
for data mining and machine learning projects and end-to-end text analytics 
application development. It is compatible with and interoperate with data 
analysis and manipulation library Pandas,  natural language processing library 
nltk, Machine Lerning TookKit (pymltoolkit|mltk), and many other AI and machine 
learning platforms. 

## Installation
```
pip install TextLab
```
If the installation failed with dependancy issues, execute the above command with --no-dependencies

```
pip install TextLab --no-dependencies
```

## Functions
- Text Similarity
- OCR (A wrapper to convert image documents to text using Tesseract-OCR and Ghostscript)
- Text Mining and Information Extraction (in v0.2.0)
- Cleaning Text content
- Web Scraping (in v0.1.6)
- Email Data Extraction
- Classification of Text Conent (in v0.2.0)


## Usage
```python
import textlab
```

### Warning: Python Variable, Function or Class names 
The Python interpreter has a number of built-in functions. It is possible to overwrite thier definitions when coding without any rasing a warning from the Python interpriter. (https://docs.python.org/3/library/functions.html)
Therfore, AVOID THESE NAMES as your variable, function or class names.
<table border="1">
<tr><td>abs</td><td>all</td><td>any</td><td>ascii</td><td>bin</td><td>bool</td><td>bytearray</td><td>bytes</td></tr>
<tr><td>callable</td><td>chr</td><td>classmethod</td><td>compile</td><td>complex</td><td>delattr</td><td>dict</td><td>dir</td></tr>
<tr><td>divmod</td><td>enumerate</td><td>eval</td><td>exec</td><td>filter</td><td>float</td><td>format</td><td>frozenset</td></tr>
<tr><td>getattr</td><td>globals</td><td>hasattr</td><td>hash</td><td>help</td><td>hex</td><td>id</td><td>input</td></tr>
<tr><td>int</td><td>isinstance</td><td>issubclass</td><td>iter</td><td>len</td><td>list</td><td>locals</td><td>map</td></tr>
<tr><td>max</td><td>memoryview</td><td>min</td><td>next</td><td>object</td><td>oct</td><td>open</td><td>ord</td></tr>
<tr><td>pow</td><td>print</td><td>property</td><td>range</td><td>repr</td><td>reversed</td><td>round</td><td>set</td></tr>
<tr><td>setattr</td><td>slice</td><td>sorted</td><td>staticmethod</td><td>str</td><td>sum</td><td>super</td><td>tuple</td></tr>
<tr><td>type</td><td>vars</td><td>zip</td><td>__import__</td></tr>
</table>

If you accedently overwrite any of the built-in function (e.g. list), execute the following to bring built-in defition.
```python
del(list)
```

## Text Analytics Example

### Text Similarity
```python
import textlab

str1 = 'Hello'
str2 = 'Hola'

dl_distance = textlab.damerau_levenshtein_distance(str1, str2, case_sensitive=True, normalized=False)
print('damerau_levenshtein_distance: ', dl_distance)

dl_distance_normalized = textlab.damerau_levenshtein_distance(str1, str2, case_sensitive=True, normalized=True)
print('damerau_levenshtein_distance (normalized): ', dl_distance_normalized)

substrings = textlab.get_substrings(string=str1, case_sensitive=True, min_length=2, max_length=512)
print('substrings: ', substrings)

j_index = textlab.jaccard_index(str1, str2, method='substring', case_sensitive=True, min_length=1, max_length=512) #method='words'
print('jaccard_index: ', round(j_index,3))
```

```
damerau_levenshtein_distance:  3
damerau_levenshtein_distance (normalized):  0.6
substrings:  ['He', 'll', 'Hel', 'el', 'llo', 'lo', 'ello', 'Hell', 'Hello', 'ell']
jaccard_index:  0.143
```

```python
# A paragraph from Wikipedia: https://en.wikipedia.org/wiki/Albert_Einstein
text = """
Albert Einstein; 14 March 1879 – 18 April 1955) was a German-born theoretical physicist[5] who developed the theory of relativity, one of the two pillars of modern physics (alongside quantum mechanics).[3][6]:274 His work is also known for its influence on the philosophy of science.[7][8] He is best known to the general public for his mass–energy equivalence formula {\displaystyle E=mc^{2}} E = mc^2, which has been dubbed "the world's most famous equation".[9] He received the 1921 Nobel Prize in Physics "for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect",[10] a pivotal step in the development of quantum theory.
"""

text1 = textlab.normalize_text(text, method='str')
text2 = textlab.normalize_text(text, method='regex')
```
text1
```
'albert einstein march – april was a germanborn theoretical physicist who developed the theory of relativity one of the two pillars of modern physics alongside quantum mechanics his work is also known for its influence on the philosophy of science he is best known to the general public for his mass–energy equivalence formula displaystyle emc e mc which has been dubbed the worlds most famous equation he received the nobel prize in physics for his services to theoretical physics and especially for his discovery of the law of the photoelectric effect a pivotal step in the development of quantum theory'
```
text2
```
'albert einstein march april was a germanborn theoretical physicist who developed the theory of relativity one of the two pillars of modern physics alongside quantum mechanics his work is also known for its influence on the philosophy of science he is best known to the general public for his mass energy equivalence formula displaystyle emc e mc which has been dubbed the worlds most famous equation he received the nobel prize in physics for his services to theoretical physics and especially for his discovery of the law of the photoelectric effect a pivotal step in the development of quantum theory'
```

```python
#Text from Wikipedia page: https://en.wikipedia.org/wiki/Email_address
text = """
An email address identifies an email box to which email messages are delivered. A wide variety of formats were used in early email systems, but only a single format is used today, following the standards developed for Internet mail systems since the 1980s. This article uses the term email address to refer to the addr-spec defined in RFC 5322, not to the address that is commonly used; the difference is that an address may contain a display name, a comment, or both.

Valid email addresses
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com (may go to user.name@example.com inbox depending on mail server)
x@example.com (one-letter local-part)
example-indeed@strange-example.com
admin@mailserver1 (local domain name with no TLD, although ICANN highly discourages dotless email addresses)
example@s.example (see the List of Internet top-level domains)
" "@example.org (space between the quotes)
"john..doe"@example.org (quoted double dot)
Invalid email addresses
Abc.example.com (no @ character)
A@b@c@example.com (only one @ is allowed outside quotation marks)
a"b(c)d,e:f;g<h>i[j\k]l@example.com (none of the special characters in this local-part are allowed outside quotation marks)
just"not"right@example.com (quoted strings must be dot separated or the only element making up the local-part)
this is"not\allowed@example.com (spaces, quotes, and backslashes may only exist when within quoted strings and preceded by a backslash)
this\ still\"not\\allowed@example.com (even if escaped (preceded by a backslash), spaces, quotes, and backslashes must still be contained by quotes)
"""

email_addresses = textlab.extract_email_addresses(text)
```

Output:
```
['simple@example.com',
 'very.common@example.com',
 'disposable.style.email.with+symbol@example.com',
 'other.email-with-hyphen@example.com',
 'fully-qualified-domain@example.com',
 'user.name+tag+sorting@example.com',
 'user.name@example.com',
 'example-indeed@strange-example.com',
 'example@s.example',
 'right@example.com',
 'llowed@example.com',
 'allowed@example.com']
 ```
 
```python
# Scrape Wikipedia page to get a list of countries and Codes for the representation of names of countries and their subdivisions.
 
tablle = textlab.extract_tables_webpage(r'https://en.wikipedia.org/wiki/ISO_3166-1')[1] # Required information in the 2nd table extracted
tablle.sample(6)
```

```
    English short name (using title case) Alpha-2 code Alpha-3 code  Numeric code Link to ISO 3166-2 subdivision codes Independent
143                                Mexico           MX          MEX           484                        ISO 3166-2:MX         Yes
220                              Thailand           TH          THA           764                        ISO 3166-2:TH         Yes
233                  United Arab Emirates           AE          ARE           784                        ISO 3166-2:AE         Yes
81                                 Gambia           GM          GMB           270                        ISO 3166-2:GM         Yes
148                            Montenegro           ME          MNE           499                        ISO 3166-2:ME         Yes
21                                Belgium           BE          BEL            56                        ISO 3166-2:BE         Yes
```

## Processing Documents
```python
test_image_file = 'test.jpg'
test_pdf_file = 'test.pdf'
```

```python
# Set Tesseract environment variables
textlab.set_tesseract_path(tesseract_path=r'C:\Projects\Tesseract', temp_folder=None)

# Set Ghostscript environment variables
textlab.set_ghostscript_path(ghostscript_path=r'C:\Projects\GhostScript\bin', temp_folder=r'C:\Projects\GhostScript\temp', ghostscript_exe='gswin64c.exe')

```python
# Trimming Image Borders
image = textlab.read_image_file(file_path=test_image_file, show_image=False)
boundbox = textlab.get_active_image_area(image, background='white')
image = textlab.draw_image_box(image, boundbox=[(0, 0), image.size], color=(0,0,255), width=5)
image = textlab.draw_image_box(image, boundbox=boundbox, color=(255,0,0), width=5)
image.show()
```

### OCR Test
```python

image = textlab.read_image_file(file_path=test_image_file, show_image=False)

output = textlab.image_to_osd(image, lang='eng', oem='0', dpi='90', tessdata_dir=None, os_temp=False)
print(output)

output = textlab.image_to_text(image, osd=True, aps=True, lang='eng', dpi='90', tessdata_dir=None, os_temp=False)
print(output['text'])

output = textlab.image_to_text_map(image, lang='eng', oem='0', dpi='90', tessdata_dir=None, os_temp=False)
print(output)

output = textlab.image_to_html(image, osd=True, aps=True, oem='3', lang='eng', dpi='90')
print(output['html'])

output = textlab.image_to_searchable_pdf(image, osd=False, aps=False, sparse=True, oem='0', lang='eng', dpi='90')
print(output['pdf'])
```

### PDF To Image
```python
images = textlab.pdf_to_images(pdf_file=test_pdf_file, image_format='png', dpi=300, out_file_prefix='out_', start_page=1, end_page=None, temp_folder=None)
```

### Process PDF file and store results in Pandas DataFrame
```python
set_ghostscript_path(ghostscript_path=r'C:\Projects\GhostScript\bin', temp_folder=r'C:\Projects\GhostScript\temp', ghostscript_exe='gswin64c.exe')
set_tesseract_path(tesseract_path=r'C:\Projects\Tesseract', temp_folder=r'C:\Projects\Tesseract\temp')
ImagesTable = create_document_image_table(r'C:\Projects\test\test.pdf', start_page=1, end_page=None)
ImagesTable = process_docuement_image_table(ImagesTable)
```

Convert PDF or Image file to text
```python
ImagesTextTable = convert_document_file_to_text(file_path, osd=True, aps=True, lang='eng', dpi=90, oem='3')
```
Convert PDF to Image DataFrame
```python
ImagesTable = create_document_image_table(file_path, start_page=1, end_page=None)
```

Appy OCR on Images DataFrame 
```python
ImagesTextTable = convert_document_image_table_to_text(ImagesTable, osd=True, aps=True, lang='eng', oem='3', dpi=90, tessdata_dir=None, os_temp=False)
```
## Email Data Extraction
EML file
```python
import email
eml_file_path = r'C:\MailBox\test.eml'
email_object =  textlab.read_eml(eml_file_path)
email_data = textlab.read_email_eml(email_object, return_type='dict')
# Create Pandas dataset
email_data_df = textlab.email_to_dataframe(email_data)
```
Read from Exchange Web Services (using exchangelib)
```python
# Fetch email
username = 'username@emailserver.com'
password = 'secretpasscode'
server = 'mail.emailserver.com'
primary_smtp_address = 'username@emailserver.com'
account = textlab.connect_ews_user_account(username, password, server, primary_smtp_address)

filters ={'datetime_received__range':{'start':'Sun, 20 May 2018 06:00:00 -0500', 'end':'Sun, 20 May 2018 18:00:00 -0500'}
ews_objects = textlab.fetch_emails_ews(account, folder='INBOX', filters=filters, print_tree=False)

# Read
ews_object = ews_objects[0]
email_data = textlab.read_email_ews(ews_object, return_type='dict') #use return_type='frame' to return dataframe

# Convert to Python native email object
email_object = textlab.ews_to_email_object(ews_object)

```
## License
```
Copyright 2019 Sumudu Tennakoon

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## Text Analytics Project Timeline
- 2018-07-10 [v0.0.1]: Initial set of functions for text data analysis was published to Github. (https://github.com/sptennak/TextAnalytics).
- 2019-01-03 [v0.0.2]: Created more functions for data exploration including web scraping and geo spacial data analysis for for IBM Coursera Data Science Capstone Project was published to Github. (https://github.com/sptennak/Coursera_Capstone).
- 2019-07-20 [v0.1.2]: First release of the "TextLab" Text Analytics Python package to PyPI.
- 2019-11-10 [v0.1.3]: Enhancments and bug fixes. Integrated a wrapper to convert image documents to text using Tesseract-OCR and Ghostscript. This module was developed as a part of IBM Coursera Advanced Data Science Professional Certificate Capstone Project. (https://github.com/sptennak/IBM-Coursera-Advanced-Data-Science-Capstone) in the initial stage, but was not used in the final version due to text analytics was omitted in the final deliverable.
- 2019-11-16 [v0.1.4]: Bug Fixes, Enhanced Document Processing functions. Integrated Document Server API with OCR function.
- 2019-12-21 [v0.1.5]: Integrated email data extraction functions and cleaning text content.

## Future Release Plan
 
- TBD [v0.1.6]: Integreate Web scraping functions. Comprehensive documentation, Major bug-fix version of the initial release with some enhancements.
- TBD [v0.1.6]: Enhance Information extraction functionality. Adding support to more opersource tools (OCR, Image Converters, etc.) avaiable. 
- TBD [v0.2.0]: Integrate Text Mining, Information Extraction, and Classification.
- TBD [v0.3.0]: End-to-end Text Analytics Application Development

## References
- https://pandas.pydata.org/
- https://www.numpy.org/
- https://docs.python.org/3.6/library/re.html
- https://matplotlib.org/
- https://github.com/tesseract-ocr/tesseract
- https://github.com/tesseract-ocr/tesseract/wiki/APIExample
- https://github.com/tesseract-ocr/tesseract/wiki/Command-Line-Usage
- https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality
- https://github.com/madmaze/pytesseract
- https://www.ghostscript.com/
- https://pillow.readthedocs.io/en/5.1.x/handbook
- https://github.com/ecederstrand/exchangelib
- https://docs.python.org/3/library/email.html

## Other helpful text Anlytics and Natural Language Processing Python libraries
- https://www.nltk.org/
- https://textblob.readthedocs.io
- https://radimrehurek.com/gensim/
- https://spacy.io/
