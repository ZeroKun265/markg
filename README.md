![](assets/Mark_banner.svg)
# Markg

<table>
  <tr>
    <td>
      <img src="assets/Mark_icon.svg" alt="Mark Icon" width="300" height="300">
    </td>
    <td>
      Markg (The g is silent) stands for: Make A Really Kool (Graph) --it's a reference to a dear friend of mine-- and aims to be a way to generate custom graphs (with theming!) through web requests, useful for iframes in READMEs.<br><br>
      Markg uses Chart.js for graph generation
    </td>
  </tr>
</table>

# Warnings about dev time and quality
I'd like to point out that this project is not only still just empty, but is also being coded on the very low free time university leaves me to do what i like (not that i don't like what i study, ofc.. you get the idea).

I am glad if people contribute and all, and i'll try to actually finish this side project for once, but no garantees

That being said..

# 

### Availability
Markg is now in version alpha 0.1, the support is extremely basic so deal with it
Not yet available as a website, please wait a little longer for that

### How to use
> [!NOTE]
> Given the fact that, as of writing this, no domain has been acquired for the project, `<marg-url>` will be used as a placeholder for it

Markg uses [Chart.js](https://www.chartjs.org/) to render data, it's basically a glorified iframe.

It can be used both in an iframe or in a markdown embed:
```html
<iframe src="http://<markg-url>/embed", widht="400", height="200"></iframe>
```
```md
![](http://<markg-url>/embed)
```

In order not to render a default Hello World message, markg needs some data, which can be provided either as query args either in json, or in base64(json converted to base64 to help with the url limit of 2000 charachters)
The syntax is this: `https://<matkg-url>/embed?t=<type>&d=<data>`
- Type can either be `json` (which it defaults to if not specified) or `base64`
- Data will either be a json string or the same json converted into a base64 string (There is a plan for some online tools to make it easier to generate the data)

#### Data
The data is the same as it would be with [Chart.js](https://www.chartjs.org/docs/latest/general/data-structures.html), example:
```json
{
  "test": 0,
  "type": "line",
  "data": {
    "labels": [],
    "datasets": [{
      "label": "My data",
      "data": [{"x": "2016-12-25", "y": 20}, {"x": "2016-12-26", "y": 10}]
    }]
  }
}
```

> [!CAUTION]
> Note that the only difference is the `"test": 0` line, which is specific to markg and is used to access various test cases, and 0 disables testing. It is necessary as without it it will default to `test: 1`

If we were for example to convert this into base64 and then use it in a link it would like like this: `http://<marg-url>/embed?t=base64&d=eyJ0ZXN0IjogMCwgInR5cGUiOiAibGluZSIsICJkYXRhIjogeyJsYWJlbHMiOiBbXSwiZGF0YXNldHMiOiBbeyJsYWJlbCI6ICJNeSBkYXRhIiwiZGF0YSI6IFt7IngiOiAiMjAxNi0xMi0yNSIsICJ5IjogMjB9LCB7IngiOiAiMjAxNi0xMi0yNiIsICJ5IjogMTB9XX1dfX0=`

Using recular json it would look like this(Remembering to reformat it to be url compatible): `http://<marlg-url>/embed?d=%7B%22test%22%3A%200%2C%20%22type%22%3A%20%22line%22%2C%20%22data%22%3A%20%7B%22labels%22%3A%20%5B%5D%2C%20%22datasets%22%3A%20%5B%7B%22data%22%3A%20%5B%7B%22x%22%3A%20%222016-12-25%22%2C%20%22y%22%3A%2020%7D%2C%20%7B%22x%22%3A%20%222016-12-26%22%2C%20%22y%22%3A%2010%7D%5D%2C%20%22label%22%3A%20%22My%20Data%22%7D%5D%7D%7D`


### Goals for future development
- The ability to do POST requests and use a lot more data than currently possible due to the url 2000 character limit (Graphs made with this will not be embeddable, but the html can be copied/downloaded)
- A frontpage website with some "docs"
- An online editor that allows to generate graphs with visual feedback, with the ability to copy urls with base64/json
- The ability to store graphs with a lot of data/settings on a database and be able to embed them everywhere with the use of a UID (this will come with some small server cost tho, so we'll see in the future)

### How to contribute
I know my dev structure sucks but i have never actually done something serious, so if you have suggestions on how to change it, please open an issue!

1. Have the correct version of python installed, see below
2. Clone the repo and enter the project's folder
3. Create a python virtual environment and install the necessary packages with `pip install -r dev/requirements.txt` (or `pip install -r dev\requirements.txt` on Windows)
4. Create a `config.ini` file inside the `dev` folder (See below for config template)
5. Test if everything works by running the `launch.sh` script or the `launch.bat` depending on your OS
  - You can check if the server works by quering `http://localhost:<port>/embed?` which will default to a hello world message if everything works
6. Get to coding, there isn't much code to begin with since it's mostly just data retrieval and formatting in an html page

### System Requirements
- Python: as of now the project is being developed with Python 3.12.4(latest as of writing), altough no testing for previous versions was done, be advised

