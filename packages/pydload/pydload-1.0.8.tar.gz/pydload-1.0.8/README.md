# PyDload

# Installation
```
pip install pydload
```

Documentation at http://bpraneeth.com/docs/pydload/

# Usage
```python
# As a python module
import pydload
pydload.dload('url')
```

```bash
# As a cli tool
pydload url_to_download
```

# Optional Params

max_time - default:30sec. If download takes more than max_time stop download.

timeout - default:10sec. Requests timeout. Max time allowed for establishing connection.
