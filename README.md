<h1>unslothLocal</h1>
Modified code to run unsloth finetuning locally.
Q: Why don't you use google collab they provided you ask?
A: I am bored

<h2>Original project and soucre code</h2>

<a href="https://docs.unsloth.ai/get-started/unsloth-notebooks"> Unsloth notebook</a>
<a href="https://github.com/unslothai/unsloth">Unsloth source code</a>
<a href="https://unsloth.ai/">Unsloth website</a>

<h3>What you needed</h3>

If you are using windows, please install wsl2 to run the code as <a href="https://github.com/triton-lang/triton">Triton</a> are not supporting on windows

linux should be able to run the code without problems

I don't have a mac so I have no idea how to run on it, you may have to figure it out yourself.

<h2>Environment setup</h2>

I am using conda, simply run:
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

Please read <a href="https://github.com/unslothai/unsloth/blob/main/README.md">read me</a> from unsloth first before using this code.
This code are not suppose to be used.

<h3>datasets structure for the code</h3>
- conversation_id
- role 
- the input role, output role and the content.

This is a multi turn conversation datastructure, if you want to use any other structure,  please modify the trainer and testing validations code as well.





