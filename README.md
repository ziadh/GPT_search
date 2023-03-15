# Run ChatGPT right from your terminal
### This is a simple python script that enables you to run ChatGPT from your terminal

## Set-up

From your terminal, run the following command to clone this repo:

```
git clone https://github.com/ziadh/GPT_search.git
```
Get the path for the main.py file

![image](https://user-images.githubusercontent.com/15097797/224567612-b5e30aec-9547-4411-a30f-2bf77d1a06c9.png)

Install the script requirements 



```
pip install -r requirements.txt 
```


On your ```bash``` terminal run the following command

```
cd ~
```

Edit the ```.bashrc``` file using vim, neon, or your any text editor and add this alias replacing the PATH-TO-main with the path you got from step 2
```
alias gpt='python PATH-TO-main.py'
```

Save the file and restart terminal and you're all set!

# Q&A

## Does this monitor my GPT requests?

Nope, this was simply made to make my life easier. You are more than welcome to take a look at the code yourself and verify that no info is being shared

## Will you update this more often?

I'll update and send out releases if I came across ways to improve it or if I get requested features
