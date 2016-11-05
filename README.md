# Setup

- Create Etherpad
- Start `screen`
- Split `screen`
- Resize `screen`'s top panel to 10 lines or so high
- Run command to output history and tail it

```bash
export PROMPT_COMMAND="history 1 >> /tmp/history.txt"
```

- Start watching for changes outside of screen
- Start Python server

