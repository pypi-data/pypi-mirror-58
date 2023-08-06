# udict.py

A simple module to get pages from Urban Dictionary


## Installing

Python 3.5 or higher is required

    # Linux/macOS
    python3 -m pip install -U udict.py

    # Windows
    py -3 -m pip install -U udict.py

## Example Usage

```python
import udict

myPage = udict.get_page("Python")
topDef = myPage.definitions[0]
print(topDef.meaning) #Prints top definition of a term.
```