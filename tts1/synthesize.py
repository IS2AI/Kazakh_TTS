import time, argparse, sys
import torch
from espnet2.bin.tts_inference import Text2Speech
from parallel_wavegan.utils import download_pretrained_model
from parallel_wavegan.utils import load_model, read_hdf5
from scipy.io.wavfile import write
from pathlib import Path

fs = 22050

def get_args():
    parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--text", help="your text", required=True)
    print(' '.join(sys.argv))
    args = parser.parse_args()
    return args

## specify the path to vocoder's checkpoint
vocoder_checkpoint="exp/vocoder/checkpoint-400000steps.pkl"
vocoder = load_model(vocoder_checkpoint).to("cuda").eval()
vocoder.remove_weight_norm()

## specify path to the main model(transformer/tacotron2/fastspeech) and its config file
config_file = "exp/tts_train_raw_char/config.yaml"
model_path = "exp/tts_train_raw_char/train.loss.ave_5best.pth"

text2speech = Text2Speech(
    config_file,
    model_path,
    device="cuda",
    # Only for Tacotron 2
    threshold=0.5,
    minlenratio=0.0,
    maxlenratio=10.0,
    use_att_constraint=True,
    backward_window=1,
    forward_window=3,
    # Only for FastSpeech & FastSpeech2
    speed_control_alpha=1.0,
)
text2speech.spc2wav = None  # Disable griffin-lim

args = get_args()
sample_text = args.text
with torch.no_grad():
    output_dict = text2speech(sample_text.lower())
    feat_gen = output_dict['feat_gen']
    wav = vocoder.inference(feat_gen)
    
## here all of your synthesized audios will be saved
folder_to_save, wav_name = "synthesized_wavs", "example.wav"

Path(folder_to_save).mkdir(parents=True, exist_ok=True)

write(folder_to_save + "/" + wav_name, fs, wav.view(-1).cpu().numpy())
    

