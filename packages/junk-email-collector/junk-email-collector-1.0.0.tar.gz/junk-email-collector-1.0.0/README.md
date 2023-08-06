# Junk Email Collector
Download raw Junk/Spam emails using IMAP.

## Requirements

[Imbox](https://github.com/martinrusev/imbox) (Python 3)

## Usage
```python3
#!/usr/bin/env python3
from junk_email_collector import JunkEmailCollector

example_junk = JunkEmailCollector("imap.example.com", "email@example.com", "password", "Junk")
example_junk.get_junk()

```

Will download all unread emails from "Junk" folder of `email@example.com`, saving the raw emails to the folder `email_example.com/`
