# LangChainTemplate

<img src="https://github.com/amwaters/LangChainTemplate/blob/5394848d6f0bbb3a7824eb9aebc41ec6c7ac81b3/LangChainTemplate.jpg?raw=true"
  style="width: 24em;"
/>

A template for LangChain apps!


## Features

+ Docker containment
+ Debugging in Visual Studio Code
+ NVIDIA driver support
+ [Streamlit](https://streamlit.io/) UI support


## Quick Start

1. Install:
    + [Docker](https://docs.docker.com/get-docker/)
    + [Docker Compose](https://docs.docker.com/compose/install/)
      (if it's not included with your Docker distribution)
    + [Visual Studio Code](https://code.visualstudio.com/download)
    + The [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
      for Visual Studio Code
    + For NVIDIA driver support, set up the
      [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)
      for Docker.
<p>

2. Clone this repo:

   ```bash
   git clone https://whatever-the-url/of-this-repo-is.git
   ```

3. Open the repo folder in Visual Studio Code.

4. Create a file named `.env` for your API keys
   and other secrets (it should be ignored by GIT and Docker).
   To run the demo app, you should at least provide an
   [OpenAI key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key).
   For example:

   ```bash
   OPENAI_API_KEY=my-openai-key
   ```

5. Configure options in `.vscode/settings.json`

6. Hit F5 to say hello to an AI!

7. Start developing your app in the `Source` folder.


## Directory

+ `.vscode` &ndash; configuration for VS Code
    + `settings.json` &ndash; Includes **LangChainTemplate feature settings**
+ `Data/Home` &ndash; the container's home directory
  (mounted to `/home/user` as read/write)
+ `Data/Models` &ndash; a place to put big files
  (mounted to `/data/models` as read-only)
+ `Source`
    + `packages` &ndash; a place to organise custom packages for your app
    + `main.py` &ndash; your app's main entrypoint
    + `requirements.txt` &ndash; a PIP requirements file
      for your app's package dependencies
    + `Home.py` &ndash; the home page for streamlit apps
    + `pages/*.py` &ndash; additional pages for streamlit apps


## Planned Features

+ Streamlit CSS template
+ Offline model installer
+ GPU demo
+ HTTPS
+ Testing framework
+ UI authentication (e.g. [Streamlit-Authenticator](https://github.com/mkhorasani/Streamlit-Authenticator))
+ Update guide
+ Improve feature selection (more features and less spaghetti!)
