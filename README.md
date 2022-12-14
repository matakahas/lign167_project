## Final project for LIGN 167: Probing syntactic knowledge of neural language models with psycholinguistic methods
This is a repository for my final project where I tested whether neural LMs have learned a syntactic constraint in Japanese. The repository includes the following:

* `LSTM.ipynb`: Colab notebook walking through the process of conducting finetuning and calculating token-by-token surprisals for Japanese LSTM LMs.
* `GPT-2.ipynb`: Colab notebook doing the same for Japanese GPT-2.
* `GPT-3.ipynb`: Jupyter notebook (that I ran locally) doing the same + getting acceptability judgments from GPT-3.
* `get_surprisal_data.py`: Python code to get surprisal data from GPT-3 using `surprisal` [package](https://pypi.org/project/surprisal/) (run on the notebook above)
* `surprisal`: Folder containing code from the surprisal package. I needed to modify the code in the file `model.py` in order to get surprisal values for Japanese sentences.
* `data`: Folder containing (i) sentences used for finetuning, (ii) test sentences used to evaluate LM's performance, and (iii) results of the evaluation. For this project, I put all the data under a personal folder for this class on Google Drive so make sure to change paths accordingly if you want to use them.   

I used Google Colab to finetune and get surprisal data for LSTM and GPT-2 models. For GPT-3, because the `surprisal` package required Python 3.9 or above, and upgrading Python version on Colab causes some dependency issues, I created a virtual env in my machine from which I ran all the code.
