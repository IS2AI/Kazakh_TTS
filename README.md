# KazakhTTS RECIPE

This is the recipe of Kazakh text-to-speech model based on KazakhTTS corpus.

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
 
Download [KazakhTTS dataset](https://issai.nu.edu.kz/tts-eng/) and untar in the directory of your choice. Specify the path to the dataset inside `KazakhTTS/tts1/local/data.sh` script:
```
db_root=/path-to-speaker-folder
```
For example `db_root=/home/datasets/ISSAI_KazakhTTS/M1_Iseke/`

## Training

To train the models, run the script `./run.sh` inside `KazakhTTS/tts1/` folder. GPU and RAM specifications can be found in the configuration (`conf/`) folder.

```
./run.sh --stage 1 --stop_stage 6 --train_config conf/train.yaml 
```
If you would like to train fastspeech/transformer models, change `train_config=conf/train.yaml` accordingly. The detailed description of each stage are documented in ESPNet's repository. 

## Pretrained Models

If you want to use pretrained models, download them from the links below and unzip inside `KazakhTTS/tts1/` folder.

### kaztts_male1_tacotron2_train.loss.ave
- https://issai.nu.edu.kz/wp-content/uploads/2021/04/kaztts_male1_tacotron2_train.loss.ave.zip

### kaztts_female1_tacotron2_train.loss.ave
- https://issai.nu.edu.kz/wp-content/uploads/2021/04/kaztts_female1_tacotron2_train.loss.ave.zip

You would also need the pre-trained vocoder to convert generated mel-spectrogram to wav. This repository used [ParallelWaveGAN](https://github.com/kan-bayashi/ParallelWaveGAN) to train the vocoders on the same KazakhTTS corpus.

### parallelwavegan_male1_checkpoint
- https://issai.nu.edu.kz/wp-content/uploads/2021/04/parallelwavegan_male1_checkpoint.zip

### parallelwavegan_female1_checkpoint
- https://issai.nu.edu.kz/wp-content/uploads/2021/04/parallelwavegan_female1_checkpoint.zip

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

