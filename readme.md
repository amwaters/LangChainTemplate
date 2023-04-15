# LangChainTemplate

A template for LangChain apps!


## Features

+ Docker containment
+ Debugging in Visual Studio Code


## Quick Start

1. Install:
    + [Docker](https://docs.docker.com/get-docker/)
    + [Docker Compose](https://docs.docker.com/compose/install/)
      (if it's not included with your Docker distribution)
    + [Visual Studio Code](https://code.visualstudio.com/download)
    + The [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
      for Visual Studio Code
<p/>

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

5. Hit F5 to say hello to an AI!

6. Start developing your app in the `Source` folder.


## Directory

+ `.vscode` &ndash; configuration for VS Code,
  including launchers, debuggers, and intellisense
+ `Data` &ndash; several folders which will be mounted in the container
  for I/O
    + `Persistent/Home` &ndash; the container's home directory
      (mounted as read/write)
    + `Static/Models` &ndash; a place to put big files
      (mounted as read-only)
+ `Source`
    + `packages` &ndash; a place to organise packages for your app
    + `main.py` &ndash; your app's main entrypoint
    + `requirements.txt` &ndash; a PIP requirements file
      for your app's dependencies.


## Planned Features

+ GPU support
+ Offline model installer
+ Testing framework
+ Update guide
+ UI support (maybe [langflow](https://github.com/logspace-ai/langflow))
