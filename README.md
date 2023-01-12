<!-- #region -->
# KazakhTTS RECIPE

This is the recipe of Kazakh text-to-speech model based on KazakhTTS and KazakhTTS2 corpora.

## Setup and Requirements 

Our code builds upon [ESPnet](https://github.com/espnet/espnet), and requires prior installation of the framework. Please follow the [installation guide](https://espnet.github.io/espnet/installation.html) and put the KazakhTTS folder inside `espnet/egs2/` directory:
```
cd espnet/egs2
git clone https://github.com/IS2AI/Kazakh_TTS.git
```
Go to Kazakh_TTS/tts1 folder and create links to the dependencies:
```
ln -s ../../TEMPLATE/tts1/path.sh .
ln -s ../../TEMPLATE/asr1/pyscripts .
ln -s ../../TEMPLATE/asr1/scripts .
ln -s ../../../tools/kaldi/egs/wsj/s5/steps .
ln -s ../../TEMPLATE/tts1/tts.sh .
ln -s ../../../tools/kaldi/egs/wsj/s5/utils .
```

## Downloading the dataset
 
Download [KazakhTTS dataset](https://docs.google.com/forms/d/e/1FAIpQLSf4vlv2NAV2dA8QL2V_uQZHOUENY6SR87n_9xToSEHX5oylVA/viewform) and untar in the directory of your choice. Specify the path to the dataset directory (where Audio/Transcripts dirs are located) inside `KazakhTTS/tts1/local/data.sh` script:
```
db_root=/path-to-speaker-folder
```
For example `db_root=/home/datasets/ISSAI_KazakhTTS/M1/Books`

## Training

To train the models, run the script `./run.sh` inside `KazakhTTS/tts1/` folder. GPU and RAM specifications can be found in the configuration (`conf/`) folder.

```
./run.sh --stage 1 --stop_stage 6 --train_config conf/train.yaml 
```
If you would like to train fastspeech/transformer models, change `train_config=conf/train.yaml` accordingly. The detailed description of each stage are documented in ESPNet's repository. 

## Pretrained models

The model was developed by the Institute of Smart Systems and Artificial Intelligence, Nazarbayev University Kazakhstan (henceforth ISSAI).

Please use the model only for a good cause and in a wise manner. You must not use the model to generate data that are obscene, offensive, or contain any discrimination with regard to religion, sex, race, language or territory of origin.

ISSAI appreciates and requires attribution. An attribution should include the title of the original paper, the author, and the name of the organization under which the development of the model took place. For example:


  *Mussakhojayeva, S., Janaliyeva, A., Mirzakhmetov, A., Khassanov, Y., Varol, H.A. (2021) KazakhTTS: An Open-Source Kazakh Text-to-Speech Synthesis Dataset. Proc. Interspeech 2021, 2786-2790, doi: 10.21437/Interspeech.2021-2124. The Institute of Smart Systems and Artificial Intelligence (issai.nu.edu.kz), Nazarbayev University, Kazakhstan*

### kaztts_female1_tacotron2_train.loss.ave
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/kaztts_female1_tacotron2_train.loss.ave.zip

### kaztts_female2_tacotron2_train.loss.ave
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/kaztts_female2_tacotron2_train.loss.ave.zip

### kaztts_female3_tacotron2_train.loss.ave
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/kaztts_female3_tacotron2_train.loss.ave.zip

### kaztts_male1_tacotron2_train.loss.ave
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/kaztts_male1_tacotron2_train.loss.ave.zip

### kaztts_male2_tacotron2_train.loss.ave
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/kaztts_male2_tacotron2_train.loss.ave.zip


## Pretrained vocoders

### parallelwavegan_female1_checkpoint
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/parallelwavegan_female1_checkpoint.zip

### parallelwavegan_female2_checkpoint
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/parallelwavegan_female2_checkpoint.zip

### parallelwavegan_female3_checkpoint
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/parallelwavegan_female3_checkpoint.zip

### parallelwavegan_male1_checkpoint
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/parallelwavegan_male1_checkpoint.zip

### parallelwavegan_male2_checkpoint
- https://issai.nu.edu.kz/wp-content/uploads/2022/03/parallelwavegan_male2_checkpoint.zip



## Speech synthesis

You can synthesize an arbitrary text using `synthesize.py` script. Modify the following lines in the script:
```
## specify the path to vocoder's checkpoint, i.e
vocoder_checkpoint="exp/vocoder/checkpoint-400000steps.pkl"

## specify path to the main model(transformer/tacotron2/fastspeech) and its config file
config_file = "exp/tts_train_raw_char/config.yaml"
model_path = "exp/tts_train_raw_char/train.loss.ave_5best.pth"
```

Now you can run the script using an arbitrary text, for example:
```
python synthesize.py --text "бүгінде өңірде тағы бес жобаның құрылысы жүргізілуде."
```
The generated file will be saved in `tts1/synthesized_wavs` folder.

## Citation
```
@inproceedings{mussakhojayeva21_interspeech,
  author={Saida Mussakhojayeva and Aigerim Janaliyeva and Almas Mirzakhmetov and Yerbolat Khassanov and Huseyin Atakan Varol},
  title={{KazakhTTS: An Open-Source Kazakh Text-to-Speech Synthesis Dataset}},
  year=2021,
  booktitle={Proc. Interspeech 2021},
  pages={2786--2790},
  doi={10.21437/Interspeech.2021-2124}
}
```
<!-- #endregion -->
