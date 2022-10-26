create env

``` bash
conda create -n winequality python=3.9.12 -y
```

activate env
```bash
conda activate winequality
```

create requirements.txt file
```bash
pip install -r requirements.txt
```

download the dataset

https://drive.google.com/drive/u/3/folders/1GIPiKiNJs1UCuh7Tn7yARYLAtIBGS88Q

initialize git
```bash
git init
```

initialize dvc
```bash
dvc init
```

add dataset tracking to dvc
```bash
dvc init
```

add commit to git
```bash
git add . && git commit -m "first commit"
```