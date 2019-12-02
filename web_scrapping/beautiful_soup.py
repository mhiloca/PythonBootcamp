from bs4 import BeautifulSoup



html = """
<!DCOCTYPE htmal>
''html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also specail.</li>
    <li>This list item is not special.</li>
  </ol>
  <div>bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
# data = soup.select('.special')
# for element in data:
#     print(element.get_text())
data = soup.find(class_='special').find_next_sibling().get_text()
print(data)
