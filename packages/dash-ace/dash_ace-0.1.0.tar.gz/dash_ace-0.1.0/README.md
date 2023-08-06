# Dash Ace

Dash Ace is a [Plotly Dash](https://dash.plot.ly) component of Ace editor that wraps up a [react ace editor](https://github.com/securingsincity/react-ace)

It supports the following four modes: Python, SQL, Text, Norm and several themes: github, monokai, tomorrow, twilight, textmate.
If you want other languages and themes, you can fork the repo and modify the code. Dynamic loading of modes and themes are not supported yet.

## Installation
```
pip install dash-ace
```

## Example
The following is a simple example using this component.
```python
import dash
import dash_ace
import dash_html_components as html
import flask
from flask import jsonify
from flask_cors import CORS

server = flask.Flask(__name__)
CORS(server)

app = dash.Dash(__name__,
                server=server,
                routes_pathname_prefix='/dash/'
                )

app.layout = html.Div([
    dash_ace.DashAceEditor(
        id='input',
        value='def test(a: int) -> str : \n'
              '    return f"value is {a}"',
        theme='github',
        mode='python',
        tabSize=2,
        enableBasicAutocompletion=True,
        enableLiveAutocompletion=True,
        autocompleter='/autocompleter?prefix=',
        placeholder='Python code ...'
    )
])


@server.route('/autocompleter', methods=['GET'])
def autocompleter():
    return jsonify([{"name": "Completed", "value": "Completed", "score": 100, "meta": "test"}])


if __name__ == '__main__':
    app.run_server(debug=True)
```

## Properties

| Prop                      | Default      | Type     | Description                                                                                                                                                                                                                                                                         |
| ------------------------- | ------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                        | 'ace-editor' | str   | Unique Id to be used for the editor                                                                                                                                                                                                                                                 |
| placeholder               | 'Type code here ...'| str   | Placeholder text to be displayed when editor is empty                                                                                                                                                                                                                               |
| mode                      | 'python'     | str   | Language for parsing and code highlighting                                                                                                                                                                                                                                          |
| theme                     | 'github'     | str   | theme to use                                                                                                                                                                                                                                                                        |
| value                     | ''           | str   | value you want to populate in the code highlighter                                                                                                                                                                                                                                  |
| className                 | None         | str   | custom className                                                                                                                                                                                                                                                                    |
| fontSize                  | 14           | int   | pixel value for font-size                                                                                                                                                                                                                                                           |
| showGutter                | True         | bool  | show gutter                                                                                                                                                                                                                                                                         |
| showPrintMargin           | True         | bool  | show print margin                                                                                                                                                                                                                                                                   |
| highlightActiveLine       | True         | bool  | highlight active line                                                                                                                                                                                                                                                               |
| focus                     | False        | bool  | whether to focus                                                                                                                                                                                                                                                                    |
| cursorStart               | 1            | int   | the location of the cursor                                                                                                                                                                                                                                                          |
| wrapEnabled               | False        | bool  | Wrapping lines                                                                                                                                                                                                                                                                      |
| readOnly                  | False        | bool  | make the editor read only                                                                                                                                                                                                                                                           |
| minLines                  | None         | int   | Minimum number of lines to be displayed                                                                                                                                                                                                                                             |
| maxLines                  | None         | int   | Maximum number of lines to be displayed                                                                                                                                                                                                                                             |
| enableBasicAutocompletion | False        | bool  | Enable basic autocompletion                                                                                                                                                                                                                                                         |
| enableLiveAutocompletion  | False        | bool  | Enable live autocompletion     
| autocompleter             | None         | str   | Custom auto completer from a language server
| prefixLine                | False        | bool  | Custom auto completer takes the current line as the prefix (False to take the current word)
| triggerWords              | None         | list    | The list of possible words before the cursor can trigger the custom auto completer (default to any words) 
| enableSnippets            | False        | bool  | Enable snippets                                                                                                                                                                                                                                                                     |
| tabSize                   | 4            | int   | tabSize                                                                                                                                                                                                                                                                             |
| debounceChangePeriod      | None         | int   | A debounce delay period for the onChange event                                                                                                                                                                                                                                      |
| editorProps               | None         | dict   | properties to apply directly to the Ace editor instance                                                                                                                                                                                                                             |
| setOptions                | None         | dict   | [options](https://github.com/ajaxorg/ace/wiki/Configuring-Ace) to apply directly to the Ace editor instance                                                                                                                                                                         |
| commands                  | None         | list    | new commands to add to the editor                                                                                                                                                                                                                                                   |
| annotations               | None         | list    | annotations to show in the editor i.e. `[{ row: 0, column: 2, type: 'error', text: 'Some error.'}]`, displayed in the gutter                                                                                                                                                        |
| markers                   | None         | list    | [markers](https://ace.c9.io/#nav=api&api=edit_session) to show in the editor, i.e. `[{ startRow: 0, startCol: 2, endRow: 1, endCol: 20, className: 'error-marker', type: 'background' }]`. Make sure to define the class (eg. ".error-marker") and set `position: absolute` for it. |
| style                     | None         | dict   | camelCased properties                                                                                                                            Get started with:


## Custom Auto Completer
A language server can provide a better intellisense service to recommend the most relevant keywords, types and variables.
`autocompleter='/autocompleter?prefix='` configures the editor to consult the API with prefix. The returned list of recommended words
have the schema of `name: str, value: str, score: int, meta: str`. The popup menu in UI shows `value` and `meta` and order the 
recommended words by the `score`. The one with the highest `score` lists at the top.


Ace editor autocompletion by default takes the current word as the prefix, set `prefixLine=True` allows the custom auto completer
to receive the whole line before the cursor as the prefix. Note that ace editor does not invoke live auto completion for anything
other than words. Press `Ctrl+Space` to show the recommended completions to access members like `test.` or to define types like `test:`.

Hitting the language server for every key press can overload the server. Setting `triggerWords` to explicitly invoking custom auto completion
is highly recommended. Note that symbols need to be escaped, e.g., `\\.`, because these words will be used to compose a regex directly. 
See javascript regex for more details.

The following is a complete example:

```python
    dash_ace.DashAceEditor(
        id='input',
        value='test(a: Integer) -> String := \n'
              '    return f"value is {a}"',
        theme='github',
        mode='norm',
        tabSize=2,
        enableBasicAutocompletion=True,
        enableLiveAutocompletion=True,
        autocompleter='/autocompleter?prefix=',
        prefixLine=True,
        triggerWords=[':', '\\.', '::'], # consult the completer for types, members and inheritances
        placeholder='Norm code ...'
    ),
``` 

## Custom Mode
Ace editor has a simple mechanism to create a custom mode. This component ships with a [Norm language](https://github.com/reasoned-ai/norm) 
that is designed for interactive probabilistic logic programming. If you want to create your own custom mode, it is recommended to modify
the [code](https://github.com/reasoned-ai/dash-ace/blob/master/src/lib/components/NormMode.js) directly. 

The syntax rules can be created and tested on [Mode Creator](https://ace.c9.io/tool/mode_creator.html). Remember to modify the folding 
patterns to reflect the correct folding.
    
## TODO
1. Support a general custom mode that allow rules to pass in as a json dictionary
2. Support dynamic loading of modes and themes
3. Support code analysis customizations to indicate errors and suggest changes

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)


## Developments
Follow these instructions to develop dash ace

### Install dependencies

If you have selected install_dependencies during the prompt, you can skip this part.

1. Install npm packages
    ```
    $ npm install
    ```
2. Create a virtual env and activate.
    ```
    $ virtualenv venv
    $ . venv/bin/activate
    ```
    _Note: venv\Scripts\activate for windows_

3. Install python packages required to build components.
    ```
    $ pip install -r requirements.txt
    ```
4. Install the python packages for testing (optional)
    ```
    $ pip install -r tests/requirements.txt
    ```

### Modify `src/lib/components/DashAceEditor.react.js`.

- The demo app is in `src/demo` and you will import your example component code into your demo app.
- Test your code in a Python environment:
    1. Build your code
        ```
        $ npm run build
        ```
    2. Run javascript demo
       ```
       $ npm start
       ```
    2. Run and modify the `usage.py` sample dash app:
        ```
        $ python usage.py
        ```
- Write tests for your component.
    - A sample test is available in `tests/test_usage.py`, it will load `usage.py` and you can then automate interactions with selenium.
    - Run the tests with `$ pytest tests`.
    - The Dash team uses these types of integration tests extensively. Browse the Dash component code on GitHub for more examples of testing (e.g. https://github.com/plotly/dash-core-components)
- Add custom styles to your component by putting your custom CSS files into your distribution folder (`dash_ace`).
    - Make sure that they are referenced in `MANIFEST.in` so that they get properly included when you're ready to publish your component.
    - Make sure the stylesheets are added to the `_css_dist` dict in `dash_ace/__init__.py` so dash will serve them automatically when the component suite is requested.
- [Review your code](./review_checklist.md)

