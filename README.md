## Final project for LIGN 167: Probing syntactic knowledge of neural language models with psycholinguistic methods
This is a repository for my final project where I tested whether neural LMs have learned a syntactic constraint in Japanese. The repository includes the following:

* `LSTM.ipynb`: Colab notebook walking through the process of conducting finetuning and calculating token-by-token surprisals for Japanese LSTM LMs.
* `GPT-2.ipynb`: Colab notebook doing the same for Japanese GPT-2.
* `GPT-3.ipynb`: Jupyter notebook (that I ran locally) doing the same + getting acceptability judgments from GPT-3.

I used Google Colab to finetune and get surprisal data for LSTM and GPT-2 models. For GPT-3, because the `surprisal` package required Python 3.9 or above, and upgrading Python version on Colab causes some dependency issues, I created a local virtual env from which I ran all the code.