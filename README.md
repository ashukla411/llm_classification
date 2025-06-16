# llm_classification
This repo is an example of how to use LLM for classification projects
## Local Setup
Following dependencies are pre-requisites for this repo
- python3.12: For code execution locally
- conda/minicoda/virtualenv: For python virtual environment management
- jupyter notebooks or anaconda navigator with notebooks
- docker for containerization

Please make sure all of the above tools are setup before running anything locally.

Run following commands for installing all the python-pip dependencies. Make sure you have activated your virtual environment first

- `pip install fastapi[standard]`
- `pip install transformers evaluate torch peft pandas numpy matplotlib scikit-learn seaborn`

## Docker setup
Make sure `docker ps` or `sudo docker ps` executes successfully in your terminal.
- `docker build -t APPNAME .`
```
Sending build context to Docker daemon  12.65MB
Step 1/6 : FROM python:3.12
 ---> 8c5092866cc6
Step 2/6 : WORKDIR /usr/app
 ---> Using cache
 ---> d1d990b39e7d
Step 3/6 : COPY . ./
 ---> a867a959bead
.
.
.
Installing collected packages: webencodings, wcwidth, pytz, pure_eval, ptyprocess, nvidia-cusparselt-cu12, mpmath, fastjsonschema, xxhash, websockets, websocket-client, webcolors, uvloop, urllib3, uri-template, tzdata, typing_extensions, types-python-dateutil, traitlets, tqdm, tornado, tinycss2, threadpoolctl, sympy, soupsieve, sniffio, six, shellingham, setuptools, Send2Trash, safetensors, rpds-py, rfc3986-validator, regex, pyzmq, PyYAML, python-multipart, python-json-logger, python-dotenv, pyparsing, Pygments, pycparser, pyarrow, psutil, propcache, prompt_toolkit, prometheus_client, platformdirs, pillow, pexpect, parso, pandocfilters, packaging, overrides, nvidia-nvtx-cu12, nvidia-nvjitlink-cu12, nvidia-nccl-cu12, nvidia-curand-cu12, nvidia-cufile-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, numpy, networkx, nest-asyncio, multidict, mistune, mdurl, MarkupSafe, kiwisolver, jupyterlab_pygments, jsonpointer, json5, joblib, idna, httptools, hf-xet, h11, fsspec, frozenlist, fqdn, fonttools, filelock, executing, dnspython, dill, defusedxml, decorator, debugpy, cycler, click, charset-normalizer, certifi, bleach, babel, attrs, async-lru, asttokens, annotated-types, aiohappyeyeballs, yarl, uvicorn, typing-inspection, triton, terminado, stack-data, scipy, rfc3339-validator, requests, referencing, python-dateutil, pydantic_core, nvidia-cusparse-cu12, nvidia-cufft-cu12, nvidia-cudnn-cu12, multiprocess, matplotlib-inline, markdown-it-py, jupyter_core, Jinja2, jedi, ipython_pygments_lexers, httpcore, email_validator, contourpy, comm, cffi, beautifulsoup4, anyio, aiosignal, watchfiles, starlette, scikit-learn, rich, pydantic, pandas, nvidia-cusolver-cu12, matplotlib, jupyter_server_terminals, jupyter_client, jsonschema-specifications, ipython, huggingface-hub, httpx, arrow, argon2-cffi-bindings, aiohttp, typer, torch, tokenizers, seaborn, rich-toolkit, jsonschema, isoduration, ipykernel, fastapi, argon2-cffi, transformers, nbformat, fastapi-cli, datasets, accelerate, peft, nbclient, jupyter-events, evaluate, nbconvert, jupyter_server, notebook_shim, jupyterlab_server, jupyter-lsp, jupyterlab, notebook
.
Step 6/6 : CMD [ "fastapi","dev", "app.py" ]
 ---> Running in facee7b5b1e1
 ---> Removed intermediate container facee7b5b1e1
 ---> f5481f7b054b
Successfully built f5481f7b054b
Successfully tagged velsera:latest
```
- `docker images`
```
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
APPNAME      latest    f5481f7b054b   36 seconds ago   XX.XXMB/GB
```
- `docker run -p 8000:8000 APPNAME`
```
      INFO   Will watch for changes in these directories: ['/usr/app']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [1] using WatchFiles
Some weights of DistilBertForSequenceClassification were not initialized from the model checkpoint at samsaara/medical_condition_classification and are newly initialized because the shapes did not match:
- classifier.bias: found shape torch.Size([751]) in the checkpoint and torch.Size([2]) in the model instantiated
- classifier.weight: found shape torch.Size([751, 768]) in the checkpoint and torch.Size([2, 768]) in the model instantiated
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
      INFO   Started server process [17]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
```

## Docker Improvements
If you store the models over cloud storage our host it over some cloud infrastrucutre you can save the default docker image size of this repository.
