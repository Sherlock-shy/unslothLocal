<h1>unslothLocal</h1>
Modified code to run unsloth finetuning locally.
This is the code let me run the unsloth locally for finetuning.
Why don't you use google collab they provided you ask?
Cause when i tried to trian it with small training rate, google collab say I need to pay to run long term and it stop me in the middle of training and I don't wanna pay it, I have an 4070 super, why don't I use it instead?

<h2>Original project and soucre code</h2>

<a href="https://docs.unsloth.ai/get-started/unsloth-notebooks"> Unsloth notebook</a>
<a href="https://github.com/unslothai/unsloth">Unsloth source code</a>
<a href="https://unsloth.ai/">Unsloth website</a>

<h3>What you needed</h3>

If on windows, install wsl2 and ubuntu
Windows cannot run it direcly as the <a href="https://github.com/triton-lang/triton">Triton</a> is not supporting windows

linux should be able to run the code without problems

I don't use mac so I have no idea how to do that, you have to figure it out yourself

Install miniconda/conda if you want to use that, or not use pip

```bash
conda create --name unsloth_env \
    python=3.11 \
    pytorch-cuda=12.1 \
    pytorch cudatoolkit xformers -c pytorch -c nvidia -c xformers \
    -y
conda activate unsloth_env

pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install --no-deps trl peft accelerate bitsandbytes
```

pip install

```bash
pip install --upgrade pip
pip install "unsloth[cu121-torch240] @ git+https://github.com/unslothai/unsloth.git"
```

After creation of environment, you can install the requirements

```bash
pip install -r requirements.txt
```

I recommend really the <a href="https://github.com/unslothai/unsloth/blob/main/README.md">read me</a> from the unsloth first before using this code if you really want to use my crippled code lol

<h3>datasets structure for the code</h3>
So for the dtaasets, I am using a structure where it have an conversation_id, role, either the input role or output role and the content.

This is a multi turn conversation datastructure, if you want to use any other structure,  you can, but you will have to modify the trainer, testing validations code as well.





