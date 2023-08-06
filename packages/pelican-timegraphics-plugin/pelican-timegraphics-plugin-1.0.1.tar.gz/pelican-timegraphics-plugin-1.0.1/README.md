# Time.Graphics plugin for Pelican: A Plugin for Pelican

Easily embed Time.Graphics timelines in your Pelican articles

## Installation

This plugin can be installed via:

    pip install pelican-timegraphics-plugin
    
Next add it to the `PLUGINS` section of `pelicanconf.py`.

```python
PLUGINS = [
    '...',
    'pelican.plugins.timegraphics'
    '...',
]
```
    
## Usage

In your articles, just add lines to your posts that look like:

```markdown
[timegraphics:id=123456,width=100%,height=400,allowfullscreen=1,frameborder=0]
```

The resulting html will look like

```html
<iframe src="https://time.graphics/embed?v=1&id=123456" width="100%" height="400" frameborder="0" allowfullscreen></iframe>
<a style="font-size: 12px; text-decoration: none;" title="Powered by Time.Graphics" href="https://time.graphics">Powered by Time.Graphics</a></div>
```

### Settings

#### `TIMEGRAPHICS_DEFAULT_WIDTH`

The default with of a timeline. Default is `'100%'`
- Can be overruled on each timeline with the `width` parameter

#### `TIMEGRAPHICS_DEFAULT_HEIGHT`

- The default height of a timeline. Default is `'400'`
- Can be overruled on each timeline with the `height` parameter

#### `TIMEGRAPHICS_ALLOW_FULLSCREEN`

- Sets the default on whether users of your site can view timelines in fullscreen.
- Allowed values are `'0'` and `'1'`
- Default is `'1'`
- Can be overruled on each timeline with the `allowfullscreen` parameter

#### `TIMEGRAPHICS_SHOW_FRAMEBORDER`

- Whether to show a border around each timeline
- Allowed values are `'0'` and `'1'`
- Default is `'0'`
- Can be overruled on each timeline with the `frameborder` parameter

#### `TIMEGRAPHICS_SHOW_POWERED_BY`

- Whether to show "Powered by Time.Graphics" under the timeline
- Allowed values are `True` and `False`
- Default is `True` 

## Contributing

Contributions are welcome and much appreciated. Every little bit helps. 
You can contribute by improving the documentation, adding missing features, and fixing bugs.
You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, 
beginning with the **Contributing Code** section.

[existing issues]: https://github.com/johanvergeer/pelican-timegraphics-plugin/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html
